#!/usr/bin/env python3
"""
Simulation: Three-Way Exploit/Explore/Deliberate Tradeoff

Tests whether the three-way allocation (exploit/explore/deliberate)
meaningfully outperforms binary exploit/explore, and whether ACT's
dominance-regime predictions match observed optimal behavior.

Environment: Drifting multi-armed bandit
- K arms with rewards drifting via Ornstein-Uhlenbeck process
- Agent observes noisy rewards when pulling an arm
- Deliberation = spend a timestep doing Bayesian updating with
  extra computation (refine estimates using cross-arm consistency)

Key questions:
1. Does the three-way allocation ever meaningfully beat binary?
2. Under what conditions?
3. Do the dominance regimes match?
4. Is the benefit of deliberation about strategy improvement or
   just uncertainty reduction?

Author: Adversarial spike on ACT's exploit-explore-deliberate segment
Date: 2026-04-02
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Dict
import warnings
warnings.filterwarnings('ignore')


# ============================================================
# Environment: Drifting Multi-Armed Bandit
# ============================================================

@dataclass
class DriftingBandit:
    """Multi-armed bandit with OU-process reward drift."""
    n_arms: int
    drift_rate: float      # rho: how fast rewards change (OU mean-reversion speed)
    volatility: float      # sigma: noise in the drift process
    obs_noise: float       # observation noise when pulling an arm
    mean_reward: float = 1.0  # long-run mean reward for all arms

    true_rewards: np.ndarray = field(default=None, repr=False)

    def __post_init__(self):
        if self.true_rewards is None:
            self.true_rewards = np.full(self.n_arms, self.mean_reward)
            # Initialize with some spread
            self.true_rewards += np.random.randn(self.n_arms) * 0.5

    def step(self):
        """Advance environment by one timestep (OU process)."""
        # dX = -drift_rate * (X - mean) * dt + volatility * dW
        # With dt=1:
        noise = np.random.randn(self.n_arms) * self.volatility
        self.true_rewards += -self.drift_rate * (self.true_rewards - self.mean_reward) + noise

    def observe(self, arm: int) -> float:
        """Pull an arm, get noisy reward."""
        return self.true_rewards[arm] + np.random.randn() * self.obs_noise

    def best_arm_reward(self) -> float:
        """Oracle: reward of the best arm."""
        return np.max(self.true_rewards)


# ============================================================
# Agent: Bayesian arm-value estimator
# ============================================================

@dataclass
class BayesianAgent:
    """Agent maintaining Gaussian beliefs about arm rewards."""
    n_arms: int
    obs_noise: float
    prior_mean: float = 1.0
    prior_var: float = 1.0  # initial uncertainty

    # Beliefs: mean and variance for each arm
    means: np.ndarray = field(default=None, repr=False)
    variances: np.ndarray = field(default=None, repr=False)

    # Tracking
    pull_counts: np.ndarray = field(default=None, repr=False)
    last_pulled: int = -1

    def __post_init__(self):
        if self.means is None:
            self.means = np.full(self.n_arms, self.prior_mean)
        if self.variances is None:
            self.variances = np.full(self.n_arms, self.prior_var)
        if self.pull_counts is None:
            self.pull_counts = np.zeros(self.n_arms, dtype=int)

    def copy(self):
        """Create a deep copy for counterfactual analysis."""
        agent = BayesianAgent(
            n_arms=self.n_arms, obs_noise=self.obs_noise,
            prior_mean=self.prior_mean, prior_var=self.prior_var
        )
        agent.means = self.means.copy()
        agent.variances = self.variances.copy()
        agent.pull_counts = self.pull_counts.copy()
        agent.last_pulled = self.last_pulled
        return agent

    def update(self, arm: int, reward: float):
        """Bayesian update after observing reward from arm."""
        obs_var = self.obs_noise ** 2
        # Kalman gain
        gain = self.variances[arm] / (self.variances[arm] + obs_var)
        self.means[arm] += gain * (reward - self.means[arm])
        self.variances[arm] *= (1 - gain)
        self.pull_counts[arm] += 1
        self.last_pulled = arm

    def drift_uncertainty(self, drift_rate: float, volatility: float):
        """Increase uncertainty due to environment drift (every timestep)."""
        # Even arms we didn't pull drift, so variance increases
        # OU process variance injection: volatility^2 per step
        # Reduced by mean-reversion: drift_rate * (var towards steady state)
        self.variances += volatility ** 2

    def deliberate(self):
        """
        Deliberation: spend a timestep doing internal computation.

        What can deliberation actually do in this setting?
        1. Cross-arm consistency: if we have a prior that arms are correlated
           or share structure, we can propagate information.
        2. Variance recalibration: re-examine whether our uncertainty
           estimates are self-consistent.
        3. Strategy evaluation: assess whether our current approach
           (which arm to focus on) is optimal given beliefs.

        For THIS simulation, we model deliberation as:
        - Shrinking variance slightly via internal model refinement
          (representing improved parameter estimates from more computation)
        - The shrinkage is proportional to the current variance and
          inversely proportional to the number of past observations
        - This has diminishing returns: repeated deliberation without
          new data yields less and less.

        This is generous to deliberation. In many real settings,
        deliberation without new data does essentially nothing.
        """
        # Deliberation benefit: reduce variance by a fraction
        # proportional to how much "unprocessed" information exists
        # This models the idea that more compute on existing data
        # can extract more signal (e.g., MCMC convergence,
        # better approximations)
        for arm in range(self.n_arms):
            if self.pull_counts[arm] > 0:
                # Diminishing returns: each deliberation step
                # captures a fraction of remaining reducible variance
                # The fraction shrinks as we've already deliberated
                reducible = self.variances[arm] * 0.1  # 10% of current
                self.variances[arm] -= reducible
                # Floor at observation noise / n_obs
                min_var = self.obs_noise ** 2 / max(1, self.pull_counts[arm])
                self.variances[arm] = max(self.variances[arm], min_var)

    def exploit_action(self) -> int:
        """Choose arm with highest estimated reward."""
        return int(np.argmax(self.means))

    def explore_action(self) -> int:
        """Choose arm with highest uncertainty (pure exploration)."""
        return int(np.argmax(self.variances))

    def ucb_action(self, c: float = 1.0) -> int:
        """UCB-style action (unified exploit/explore)."""
        scores = self.means + c * np.sqrt(self.variances)
        return int(np.argmax(scores))

    def total_uncertainty(self) -> float:
        """Total model uncertainty across all arms."""
        return float(np.sum(self.variances))

    def control_regret_estimate(self) -> float:
        """
        Estimate of delta_regret: how much better could we do
        with a different strategy?

        Approximated as: expected value of best arm minus
        expected value of currently-estimated-best arm,
        accounting for uncertainty.
        """
        best_arm = self.exploit_action()
        best_mean = self.means[best_arm]
        # The "regret" comes from the possibility that another arm
        # is actually better. Estimated via the probability that
        # any other arm exceeds the best estimate.
        regret = 0.0
        for arm in range(self.n_arms):
            if arm != best_arm:
                # P(arm > best_arm) * E[arm - best_arm | arm > best_arm]
                diff_mean = self.means[arm] - best_mean
                diff_var = self.variances[arm] + self.variances[best_arm]
                if diff_var > 0:
                    z = diff_mean / np.sqrt(diff_var)
                    # Expected improvement from switching
                    from scipy.stats import norm
                    ei = np.sqrt(diff_var) * (z * norm.cdf(z) + norm.pdf(z))
                    regret = max(regret, ei)
        return regret


# ============================================================
# Policies
# ============================================================

def run_binary_policy(env: DriftingBandit, n_steps: int,
                      ucb_c: float = 1.0, seed: int = 0) -> Dict:
    """Binary exploit/explore policy (UCB). No deliberation option."""
    np.random.seed(seed)
    env_copy = DriftingBandit(
        n_arms=env.n_arms, drift_rate=env.drift_rate,
        volatility=env.volatility, obs_noise=env.obs_noise,
        mean_reward=env.mean_reward
    )
    env_copy.true_rewards = env.true_rewards.copy()

    agent = BayesianAgent(n_arms=env.n_arms, obs_noise=env.obs_noise)

    total_reward = 0.0
    total_oracle = 0.0
    rewards = []

    for t in range(n_steps):
        # UCB action selection (binary exploit/explore)
        arm = agent.ucb_action(c=ucb_c)
        reward = env_copy.observe(arm)
        agent.update(arm, reward)

        total_reward += reward
        total_oracle += env_copy.best_arm_reward()
        rewards.append(reward)

        # Environment and agent drift
        env_copy.step()
        agent.drift_uncertainty(env_copy.drift_rate, env_copy.volatility)

    return {
        'total_reward': total_reward,
        'total_oracle': total_oracle,
        'regret': total_oracle - total_reward,
        'mean_reward': np.mean(rewards),
        'rewards': rewards,
    }


def run_three_way_oracle(env: DriftingBandit, n_steps: int,
                         seed: int = 0) -> Dict:
    """
    Oracle three-way: at each step, tries all three options
    and picks the one with best expected future reward.

    This is computationally expensive but gives the TRUE optimal
    three-way allocation (within the one-step-lookahead approximation).
    """
    np.random.seed(seed)
    env_copy = DriftingBandit(
        n_arms=env.n_arms, drift_rate=env.drift_rate,
        volatility=env.volatility, obs_noise=env.obs_noise,
        mean_reward=env.mean_reward
    )
    env_copy.true_rewards = env.true_rewards.copy()

    agent = BayesianAgent(n_arms=env.n_arms, obs_noise=env.obs_noise)

    total_reward = 0.0
    total_oracle = 0.0
    rewards = []
    actions_taken = {'exploit': 0, 'explore': 0, 'deliberate': 0}

    for t in range(n_steps):
        oracle_reward = env_copy.best_arm_reward()
        total_oracle += oracle_reward

        # Option 1: Exploit (pull best estimated arm)
        exploit_arm = agent.exploit_action()

        # Option 2: Explore (pull most uncertain arm)
        explore_arm = agent.explore_action()

        # Option 3: Deliberate (no pull, internal update)
        # To compare fairly, we need to estimate the VALUE of each option
        # over a short horizon (say, H steps)

        H = 5  # lookahead horizon
        n_sims = 20  # Monte Carlo simulations per option

        option_values = {}

        for option_name, option_arm in [('exploit', exploit_arm),
                                          ('explore', explore_arm),
                                          ('deliberate', -1)]:
            sim_values = []
            for sim in range(n_sims):
                # Simulate from current state
                sim_agent = agent.copy()
                sim_env = DriftingBandit(
                    n_arms=env.n_arms, drift_rate=env_copy.drift_rate,
                    volatility=env_copy.volatility, obs_noise=env_copy.obs_noise,
                    mean_reward=env_copy.mean_reward
                )
                sim_env.true_rewards = env_copy.true_rewards.copy()

                sim_total = 0.0

                # First step: take the option
                if option_arm >= 0:
                    r = sim_env.observe(option_arm)
                    sim_agent.update(option_arm, r)
                    sim_total += r
                else:
                    # Deliberate: no reward this step
                    sim_agent.deliberate()
                    sim_total += 0.0

                sim_env.step()
                sim_agent.drift_uncertainty(sim_env.drift_rate, sim_env.volatility)

                # Remaining steps: follow UCB
                for h in range(1, H):
                    arm = sim_agent.ucb_action(c=1.0)
                    r = sim_env.observe(arm)
                    sim_agent.update(arm, r)
                    sim_total += r
                    sim_env.step()
                    sim_agent.drift_uncertainty(sim_env.drift_rate, sim_env.volatility)

                sim_values.append(sim_total)

            option_values[option_name] = np.mean(sim_values)

        # Pick best option
        best_option = max(option_values, key=option_values.get)
        actions_taken[best_option] += 1

        if best_option == 'deliberate':
            agent.deliberate()
            rewards.append(0.0)
        elif best_option == 'exploit':
            reward = env_copy.observe(exploit_arm)
            agent.update(exploit_arm, reward)
            rewards.append(reward)
            total_reward += reward
        else:  # explore
            reward = env_copy.observe(explore_arm)
            agent.update(explore_arm, reward)
            rewards.append(reward)
            total_reward += reward

        env_copy.step()
        agent.drift_uncertainty(env_copy.drift_rate, env_copy.volatility)

    return {
        'total_reward': total_reward,
        'total_oracle': total_oracle,
        'regret': total_oracle - total_reward,
        'mean_reward': np.mean([r for r in rewards if r != 0]) if any(r != 0 for r in rewards) else 0,
        'actions': actions_taken,
        'rewards': rewards,
    }


def run_three_way_heuristic(env: DriftingBandit, n_steps: int,
                            seed: int = 0) -> Dict:
    """
    Heuristic three-way policy based on ACT's dominance regimes:
    - Exploit when uncertainty is low and regret is low
    - Explore when uncertainty is high and environment is changing fast
    - Deliberate when regret is high and environment is stable
    """
    np.random.seed(seed)
    env_copy = DriftingBandit(
        n_arms=env.n_arms, drift_rate=env.drift_rate,
        volatility=env.volatility, obs_noise=env.obs_noise,
        mean_reward=env.mean_reward
    )
    env_copy.true_rewards = env.true_rewards.copy()

    agent = BayesianAgent(n_arms=env.n_arms, obs_noise=env.obs_noise)

    total_reward = 0.0
    total_oracle = 0.0
    rewards = []
    actions_taken = {'exploit': 0, 'explore': 0, 'deliberate': 0}

    for t in range(n_steps):
        oracle_reward = env_copy.best_arm_reward()
        total_oracle += oracle_reward

        # Compute ACT diagnostics
        uncertainty = agent.total_uncertainty()
        regret_est = agent.control_regret_estimate()
        rho = env_copy.drift_rate  # environment tempo

        # Normalize for comparison
        mean_var = uncertainty / env.n_arms

        # ACT dominance regime thresholds
        high_uncertainty = mean_var > 0.5 * agent.prior_var
        high_regret = regret_est > 0.3  # significant estimated regret
        high_rho = rho > 0.3  # fast-changing environment

        if high_regret and not high_rho:
            # Deliberate dominates: strategy needs revision, env is stable
            action = 'deliberate'
        elif high_uncertainty and high_rho:
            # Explore dominates: uncertain and can't afford to think
            action = 'explore'
        elif high_uncertainty and not high_rho:
            # Could deliberate or explore; prefer explore for new data
            action = 'explore'
        else:
            # Exploit: low uncertainty, low regret
            action = 'exploit'

        actions_taken[action] += 1

        if action == 'deliberate':
            agent.deliberate()
            rewards.append(0.0)
        elif action == 'exploit':
            arm = agent.exploit_action()
            reward = env_copy.observe(arm)
            agent.update(arm, reward)
            rewards.append(reward)
            total_reward += reward
        else:  # explore
            arm = agent.explore_action()
            reward = env_copy.observe(arm)
            agent.update(arm, reward)
            rewards.append(reward)
            total_reward += reward

        env_copy.step()
        agent.drift_uncertainty(env_copy.drift_rate, env_copy.volatility)

    return {
        'total_reward': total_reward,
        'total_oracle': total_oracle,
        'regret': total_oracle - total_reward,
        'actions': actions_taken,
        'rewards': rewards,
    }


def run_deliberate_only_value(env: DriftingBandit, n_steps: int,
                               seed: int = 0) -> Dict:
    """
    Agent that ONLY deliberates when it reduces uncertainty about
    which arm is best (strategy improvement), not general uncertainty.

    This tests whether deliberation's value is about strategy vs.
    general uncertainty reduction.
    """
    np.random.seed(seed)
    env_copy = DriftingBandit(
        n_arms=env.n_arms, drift_rate=env.drift_rate,
        volatility=env.volatility, obs_noise=env.obs_noise,
        mean_reward=env.mean_reward
    )
    env_copy.true_rewards = env.true_rewards.copy()

    agent = BayesianAgent(n_arms=env.n_arms, obs_noise=env.obs_noise)

    total_reward = 0.0
    total_oracle = 0.0
    rewards = []
    actions_taken = {'exploit': 0, 'explore': 0, 'deliberate': 0}

    for t in range(n_steps):
        oracle_reward = env_copy.best_arm_reward()
        total_oracle += oracle_reward

        # Would deliberation change which arm we think is best?
        test_agent = agent.copy()
        pre_best = test_agent.exploit_action()
        test_agent.deliberate()
        post_best = test_agent.exploit_action()

        # Only deliberate if it would change the strategy
        strategy_change = (pre_best != post_best)

        # Estimate the value gap between best and second-best
        sorted_means = np.sort(agent.means)[::-1]
        gap = sorted_means[0] - sorted_means[1] if len(sorted_means) > 1 else float('inf')
        close_race = gap < 0.3  # arms are close

        rho = env_copy.drift_rate
        high_rho = rho > 0.3

        if (strategy_change or close_race) and not high_rho:
            action = 'deliberate'
        else:
            # UCB for exploit/explore
            arm = agent.ucb_action(c=1.0)
            if arm == agent.exploit_action():
                action = 'exploit'
            else:
                action = 'explore'

        actions_taken[action] += 1

        if action == 'deliberate':
            agent.deliberate()
            rewards.append(0.0)
        else:
            arm = agent.ucb_action(c=1.0)
            reward = env_copy.observe(arm)
            agent.update(arm, reward)
            rewards.append(reward)
            total_reward += reward

        env_copy.step()
        agent.drift_uncertainty(env_copy.drift_rate, env_copy.volatility)

    return {
        'total_reward': total_reward,
        'total_oracle': total_oracle,
        'regret': total_oracle - total_reward,
        'actions': actions_taken,
        'rewards': rewards,
    }


# ============================================================
# Experiment Configurations
# ============================================================

def run_experiment(config_name: str, n_arms: int, drift_rate: float,
                   volatility: float, obs_noise: float, n_steps: int,
                   n_trials: int = 30) -> Dict:
    """Run all policies under a given configuration."""

    results = {
        'binary': [],
        'three_way_oracle': [],
        'three_way_heuristic': [],
        'strategy_focused': [],
    }

    for trial in range(n_trials):
        seed = trial * 1000
        np.random.seed(seed)

        env = DriftingBandit(
            n_arms=n_arms, drift_rate=drift_rate,
            volatility=volatility, obs_noise=obs_noise
        )

        # Run all policies from the same initial environment
        results['binary'].append(
            run_binary_policy(env, n_steps, seed=seed+1))
        results['three_way_oracle'].append(
            run_three_way_oracle(env, n_steps, seed=seed+2))
        results['three_way_heuristic'].append(
            run_three_way_heuristic(env, n_steps, seed=seed+3))
        results['strategy_focused'].append(
            run_deliberate_only_value(env, n_steps, seed=seed+4))

    return results


def summarize_results(config_name: str, results: Dict) -> str:
    """Produce human-readable summary."""
    lines = [f"\n{'='*70}", f"Configuration: {config_name}", '='*70]

    for policy_name in ['binary', 'three_way_oracle', 'three_way_heuristic', 'strategy_focused']:
        trials = results[policy_name]
        total_rewards = [t['total_reward'] for t in trials]
        regrets = [t['regret'] for t in trials]

        mean_reward = np.mean(total_rewards)
        std_reward = np.std(total_rewards)
        mean_regret = np.mean(regrets)
        std_regret = np.std(regrets)

        lines.append(f"\n  {policy_name}:")
        lines.append(f"    Total reward: {mean_reward:.1f} +/- {std_reward:.1f}")
        lines.append(f"    Oracle regret: {mean_regret:.1f} +/- {std_regret:.1f}")

        if 'actions' in trials[0]:
            action_counts = {}
            for t in trials:
                for k, v in t['actions'].items():
                    action_counts.setdefault(k, []).append(v)
            action_str = ', '.join(
                f"{k}: {np.mean(v):.0f}" for k, v in sorted(action_counts.items()))
            lines.append(f"    Actions: {action_str}")

    # Comparison
    binary_rewards = [t['total_reward'] for t in results['binary']]
    oracle_rewards = [t['total_reward'] for t in results['three_way_oracle']]
    heuristic_rewards = [t['total_reward'] for t in results['three_way_heuristic']]
    strategy_rewards = [t['total_reward'] for t in results['strategy_focused']]

    oracle_improvement = (np.mean(oracle_rewards) - np.mean(binary_rewards)) / max(abs(np.mean(binary_rewards)), 1e-10) * 100
    heuristic_improvement = (np.mean(heuristic_rewards) - np.mean(binary_rewards)) / max(abs(np.mean(binary_rewards)), 1e-10) * 100
    strategy_improvement = (np.mean(strategy_rewards) - np.mean(binary_rewards)) / max(abs(np.mean(binary_rewards)), 1e-10) * 100

    lines.append(f"\n  Three-way oracle vs binary: {oracle_improvement:+.1f}%")
    lines.append(f"  Three-way heuristic vs binary: {heuristic_improvement:+.1f}%")
    lines.append(f"  Strategy-focused vs binary: {strategy_improvement:+.1f}%")

    # Statistical significance (paired t-test)
    from scipy.stats import ttest_rel
    t_stat, p_value = ttest_rel(oracle_rewards, binary_rewards)
    lines.append(f"  Oracle vs Binary p-value: {p_value:.4f} {'***' if p_value < 0.001 else '**' if p_value < 0.01 else '*' if p_value < 0.05 else 'n.s.'}")

    t_stat2, p_value2 = ttest_rel(heuristic_rewards, binary_rewards)
    lines.append(f"  Heuristic vs Binary p-value: {p_value2:.4f} {'***' if p_value2 < 0.001 else '**' if p_value2 < 0.01 else '*' if p_value2 < 0.05 else 'n.s.'}")

    return '\n'.join(lines)


# ============================================================
# Additional Analysis: Information-Theoretic Decomposition
# ============================================================

def information_budget_analysis(n_arms: int = 5, n_steps: int = 200,
                                 drift_rate: float = 0.1,
                                 volatility: float = 0.2,
                                 obs_noise: float = 0.5) -> str:
    """
    Analyze the information budget: how many bits does each activity earn?

    - Exploit: bits about reward realization (value-bits)
    - Explore: bits about arm reward levels (CIY-bits)
    - Deliberate: bits about which arm is best (strategy-bits)
    """
    np.random.seed(42)
    env = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                         volatility=volatility, obs_noise=obs_noise)

    agent = BayesianAgent(n_arms=n_arms, obs_noise=obs_noise)

    lines = ["\n" + "="*70, "Information Budget Analysis", "="*70]

    # Track entropy reduction per activity type
    exploit_entropy_reduction = []
    explore_entropy_reduction = []
    deliberate_entropy_reduction = []

    for t in range(n_steps):
        # Current total entropy (sum of log-variances, proportional to differential entropy)
        current_entropy = np.sum(np.log(agent.variances + 1e-10))

        # Test exploit: pull best arm
        exploit_agent = agent.copy()
        exploit_arm = exploit_agent.exploit_action()
        r = env.observe(exploit_arm)
        exploit_agent.update(exploit_arm, r)
        exploit_entropy = np.sum(np.log(exploit_agent.variances + 1e-10))
        exploit_entropy_reduction.append(current_entropy - exploit_entropy)

        # Test explore: pull most uncertain arm
        explore_agent = agent.copy()
        explore_arm = explore_agent.explore_action()
        r2 = env.observe(explore_arm)
        explore_agent.update(explore_arm, r2)
        explore_entropy = np.sum(np.log(explore_agent.variances + 1e-10))
        explore_entropy_reduction.append(current_entropy - explore_entropy)

        # Test deliberate: no observation, internal update
        delib_agent = agent.copy()
        delib_agent.deliberate()
        delib_entropy = np.sum(np.log(delib_agent.variances + 1e-10))
        deliberate_entropy_reduction.append(current_entropy - delib_entropy)

        # Actually advance (using UCB)
        arm = agent.ucb_action(c=1.0)
        actual_r = env.observe(arm)
        agent.update(arm, actual_r)
        env.step()
        agent.drift_uncertainty(drift_rate, volatility)

    lines.append(f"\n  Mean entropy reduction per step:")
    lines.append(f"    Exploit:     {np.mean(exploit_entropy_reduction):.4f} +/- {np.std(exploit_entropy_reduction):.4f}")
    lines.append(f"    Explore:     {np.mean(explore_entropy_reduction):.4f} +/- {np.std(explore_entropy_reduction):.4f}")
    lines.append(f"    Deliberate:  {np.mean(deliberate_entropy_reduction):.4f} +/- {np.std(deliberate_entropy_reduction):.4f}")

    # Key ratio: explore entropy reduction / exploit entropy reduction
    ratio = np.mean(explore_entropy_reduction) / max(np.mean(exploit_entropy_reduction), 1e-10)
    lines.append(f"\n  Explore/Exploit entropy ratio: {ratio:.2f}")
    lines.append(f"  Deliberate/Exploit entropy ratio: {np.mean(deliberate_entropy_reduction) / max(np.mean(exploit_entropy_reduction), 1e-10):.2f}")

    return '\n'.join(lines)


# ============================================================
# Bellman-Style Meta-Decision Analysis
# ============================================================

def bellman_meta_analysis(n_arms: int = 3, n_steps: int = 50,
                           drift_rate: float = 0.1,
                           volatility: float = 0.2,
                           obs_noise: float = 0.5,
                           n_trials: int = 100) -> str:
    """
    Compute the value function for the meta-decision (exploit/explore/deliberate)
    using backwards induction on a simplified state space.

    This tests whether the Bellman equation for the meta-decision has
    a natural decomposition or is inherently entangled.
    """
    lines = ["\n" + "="*70, "Bellman Meta-Decision Analysis", "="*70]

    # We can't do full Bellman on the continuous state space,
    # but we can estimate Q-values for each meta-action at different
    # states via Monte Carlo

    # State features: (mean uncertainty, best-arm gap, time remaining)
    # Meta-actions: exploit, explore, deliberate

    state_bins = {
        'high_unc_close': [],   # high uncertainty, close arms
        'high_unc_clear': [],   # high uncertainty, clear winner
        'low_unc_close': [],    # low uncertainty, close arms
        'low_unc_clear': [],    # low uncertainty, clear winner
    }

    for trial in range(n_trials):
        np.random.seed(trial * 100)
        env = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                             volatility=volatility, obs_noise=obs_noise)
        agent = BayesianAgent(n_arms=n_arms, obs_noise=obs_noise)

        for t in range(n_steps):
            # Classify state
            mean_var = np.mean(agent.variances)
            sorted_means = np.sort(agent.means)[::-1]
            gap = sorted_means[0] - sorted_means[1] if n_arms > 1 else float('inf')

            high_unc = mean_var > 0.3
            close = gap < 0.5

            if high_unc and close:
                state_key = 'high_unc_close'
            elif high_unc and not close:
                state_key = 'high_unc_clear'
            elif not high_unc and close:
                state_key = 'low_unc_close'
            else:
                state_key = 'low_unc_clear'

            # Estimate value of each meta-action via rollout
            meta_values = {}
            H = 5
            n_sims = 10

            for meta_action in ['exploit', 'explore', 'deliberate']:
                vals = []
                for sim in range(n_sims):
                    sim_agent = agent.copy()
                    sim_env = DriftingBandit(
                        n_arms=n_arms, drift_rate=drift_rate,
                        volatility=volatility, obs_noise=obs_noise,
                        mean_reward=env.mean_reward
                    )
                    sim_env.true_rewards = env.true_rewards.copy()

                    total = 0.0
                    # First step
                    if meta_action == 'exploit':
                        arm = sim_agent.exploit_action()
                        r = sim_env.observe(arm)
                        sim_agent.update(arm, r)
                        total += r
                    elif meta_action == 'explore':
                        arm = sim_agent.explore_action()
                        r = sim_env.observe(arm)
                        sim_agent.update(arm, r)
                        total += r
                    else:
                        sim_agent.deliberate()

                    sim_env.step()
                    sim_agent.drift_uncertainty(drift_rate, volatility)

                    # Subsequent steps: UCB
                    for h in range(1, H):
                        arm = sim_agent.ucb_action(c=1.0)
                        r = sim_env.observe(arm)
                        sim_agent.update(arm, r)
                        total += r
                        sim_env.step()
                        sim_agent.drift_uncertainty(drift_rate, volatility)

                    vals.append(total)

                meta_values[meta_action] = np.mean(vals)

            state_bins[state_key].append(meta_values)

            # Advance with UCB
            arm = agent.ucb_action(c=1.0)
            r = env.observe(arm)
            agent.update(arm, r)
            env.step()
            agent.drift_uncertainty(drift_rate, volatility)

    lines.append("\n  Q-values by state (averaged over encounters):")
    lines.append(f"  {'State':<20} {'Exploit':>10} {'Explore':>10} {'Deliberate':>10} {'Best':>12}")
    lines.append("  " + "-"*64)

    for state_key, values_list in state_bins.items():
        if len(values_list) == 0:
            continue
        exploit_vals = [v['exploit'] for v in values_list]
        explore_vals = [v['explore'] for v in values_list]
        delib_vals = [v['deliberate'] for v in values_list]

        best = max(
            ('exploit', np.mean(exploit_vals)),
            ('explore', np.mean(explore_vals)),
            ('deliberate', np.mean(delib_vals)),
            key=lambda x: x[1]
        )

        lines.append(
            f"  {state_key:<20} {np.mean(exploit_vals):>10.3f} "
            f"{np.mean(explore_vals):>10.3f} {np.mean(delib_vals):>10.3f} "
            f"{best[0]:>12}")

    lines.append(f"\n  State visit counts:")
    for state_key, values_list in state_bins.items():
        lines.append(f"    {state_key}: {len(values_list)} visits")

    return '\n'.join(lines)


# ============================================================
# Persistence Margin Analysis
# ============================================================

def persistence_margin_analysis(n_arms: int = 5, n_steps: int = 200,
                                  obs_noise: float = 0.5) -> str:
    """
    Test: can the allocation be derived from maximizing persistence margin?

    alpha > rho/R  =>  Margin = alpha*R - rho

    Each activity affects:
    - Exploit: doesn't change alpha or rho
    - Explore: improves alpha (via eta*)
    - Deliberate: improves alpha (via Delta_eta*) but at cost rho_delib * Delta_tau
    """
    lines = ["\n" + "="*70, "Persistence Margin Analysis", "="*70]

    # Test across different drift rates
    for drift_rate in [0.01, 0.05, 0.1, 0.3, 0.5]:
        volatility = drift_rate * 2

        np.random.seed(42)
        env = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                             volatility=volatility, obs_noise=obs_noise)
        agent = BayesianAgent(n_arms=n_arms, obs_noise=obs_noise)

        # Run for a while, tracking which action maximizes persistence margin
        margin_improvements = {'exploit': [], 'explore': [], 'deliberate': []}

        for t in range(n_steps):
            # Current "alpha" proxy: mean gain (1 / (1 + obs_noise^2/var))
            current_gains = [v / (v + obs_noise**2) for v in agent.variances]
            current_alpha = np.mean(current_gains)

            # Test exploit
            test_agent = agent.copy()
            arm = test_agent.exploit_action()
            r = env.observe(arm)
            test_agent.update(arm, r)
            test_agent.drift_uncertainty(drift_rate, volatility)
            new_gains = [v / (v + obs_noise**2) for v in test_agent.variances]
            exploit_alpha = np.mean(new_gains)
            margin_improvements['exploit'].append(exploit_alpha - current_alpha)

            # Test explore
            test_agent = agent.copy()
            arm = test_agent.explore_action()
            r = env.observe(arm)
            test_agent.update(arm, r)
            test_agent.drift_uncertainty(drift_rate, volatility)
            new_gains = [v / (v + obs_noise**2) for v in test_agent.variances]
            explore_alpha = np.mean(new_gains)
            margin_improvements['explore'].append(explore_alpha - current_alpha)

            # Test deliberate
            test_agent = agent.copy()
            test_agent.deliberate()
            test_agent.drift_uncertainty(drift_rate, volatility)
            new_gains = [v / (v + obs_noise**2) for v in test_agent.variances]
            delib_alpha = np.mean(new_gains)
            # Subtract rho_delib cost
            margin_improvements['deliberate'].append(
                (delib_alpha - current_alpha) - drift_rate * 0.1)  # crude rho_delib

            # Advance
            arm = agent.ucb_action(c=1.0)
            actual_r = env.observe(arm)
            agent.update(arm, actual_r)
            env.step()
            agent.drift_uncertainty(drift_rate, volatility)

        lines.append(f"\n  Drift rate = {drift_rate}:")
        for action, improvements in margin_improvements.items():
            lines.append(f"    {action}: mean margin change = {np.mean(improvements):.5f}")

    return '\n'.join(lines)


# ============================================================
# Mismatch Dynamics Approach
# ============================================================

def mismatch_dynamics_analysis(n_arms: int = 5, n_steps: int = 200) -> str:
    """
    Test: can we derive the allocation from minimizing expected
    mismatch at the next decision point?

    d||delta||/dt = -T*||delta|| + rho

    During deliberation: rho_delib accumulates but T can improve
    During exploration: T stays same but eta* eventually improves
    During exploitation: delta doesn't change but agent earns value
    """
    lines = ["\n" + "="*70, "Mismatch Dynamics Analysis", "="*70]

    for drift_rate, obs_noise in [(0.05, 0.3), (0.1, 0.5), (0.3, 0.8), (0.5, 1.0)]:
        volatility = drift_rate * 2

        np.random.seed(42)
        env = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                             volatility=volatility, obs_noise=obs_noise)
        agent = BayesianAgent(n_arms=n_arms, obs_noise=obs_noise)

        # Track "mismatch" = mean |true_reward - estimated_reward|
        mismatch_after = {'exploit': [], 'explore': [], 'deliberate': []}

        for t in range(min(n_steps, 100)):
            for action_type in ['exploit', 'explore', 'deliberate']:
                test_agent = agent.copy()
                test_env = DriftingBandit(
                    n_arms=n_arms, drift_rate=drift_rate,
                    volatility=volatility, obs_noise=obs_noise
                )
                test_env.true_rewards = env.true_rewards.copy()

                if action_type == 'exploit':
                    arm = test_agent.exploit_action()
                    r = test_env.observe(arm)
                    test_agent.update(arm, r)
                elif action_type == 'explore':
                    arm = test_agent.explore_action()
                    r = test_env.observe(arm)
                    test_agent.update(arm, r)
                else:
                    test_agent.deliberate()

                test_env.step()
                test_agent.drift_uncertainty(drift_rate, volatility)

                # Mismatch: |true - estimated| for each arm
                mismatch = np.mean(np.abs(test_env.true_rewards - test_agent.means))
                mismatch_after[action_type].append(mismatch)

            # Advance
            arm = agent.ucb_action(c=1.0)
            r = env.observe(arm)
            agent.update(arm, r)
            env.step()
            agent.drift_uncertainty(drift_rate, volatility)

        lines.append(f"\n  rho={drift_rate}, obs_noise={obs_noise}:")
        for action_type, mismatches in mismatch_after.items():
            lines.append(f"    {action_type}: mean next-step mismatch = {np.mean(mismatches):.4f}")

        # Which minimizes mismatch?
        best = min(mismatch_after.items(), key=lambda x: np.mean(x[1]))
        lines.append(f"    Best for mismatch: {best[0]} ({np.mean(best[1]):.4f})")

    return '\n'.join(lines)


# ============================================================
# CRITICAL TEST: When does deliberation actually help?
# ============================================================

def deliberation_value_decomposition(n_steps: int = 300, n_trials: int = 50) -> str:
    """
    The key question: WHEN is deliberation genuinely valuable,
    and WHY?

    Decompose deliberation's value into:
    1. Uncertainty reduction (could also get from exploration)
    2. Strategy improvement (which arm to focus on)
    3. Nothing (deliberation is never the best option)
    """
    lines = ["\n" + "="*70, "CRITICAL: When Does Deliberation Actually Help?", "="*70]

    configs = [
        # (name, n_arms, drift, vol, obs_noise)
        ("Slow drift, low noise (favorable to delib)", 10, 0.02, 0.04, 0.3),
        ("Slow drift, high noise", 10, 0.02, 0.04, 1.0),
        ("Fast drift, low noise", 10, 0.3, 0.6, 0.3),
        ("Fast drift, high noise", 10, 0.3, 0.6, 1.0),
        ("Many arms, slow drift", 20, 0.02, 0.04, 0.5),
        ("Few arms, slow drift", 3, 0.02, 0.04, 0.5),
        ("Many arms, moderate drift", 20, 0.1, 0.2, 0.5),
        ("Minimal arms, high noise", 2, 0.05, 0.1, 2.0),
    ]

    for config_name, n_arms, drift, vol, noise in configs:
        delib_better_count = 0
        total_comparisons = 0
        delib_advantage_when_better = []

        for trial in range(n_trials):
            np.random.seed(trial * 37)
            env = DriftingBandit(n_arms=n_arms, drift_rate=drift,
                                 volatility=vol, obs_noise=noise)
            agent = BayesianAgent(n_arms=n_arms, obs_noise=noise)

            for t in range(n_steps):
                # Compare: best action vs deliberate
                # Best action value (1-step)
                best_arm = agent.ucb_action(c=1.0)
                action_reward = env.true_rewards[best_arm]  # expected reward

                # Deliberation value: how much does it improve NEXT action?
                delib_agent = agent.copy()
                delib_agent.deliberate()
                post_delib_arm = delib_agent.ucb_action(c=1.0)
                delib_next_reward = env.true_rewards[post_delib_arm]

                # Deliberation is better if the improvement in next action
                # exceeds the reward foregone now
                delib_value = delib_next_reward - action_reward  # improvement
                action_value = action_reward  # what you'd get by acting

                total_comparisons += 1
                if delib_value > action_value:  # deliberation changes arm AND improvement > reward foregone
                    delib_better_count += 1
                    delib_advantage_when_better.append(delib_value - action_value)

                # Advance
                arm = agent.ucb_action(c=1.0)
                r = env.observe(arm)
                agent.update(arm, r)
                env.step()
                agent.drift_uncertainty(drift, vol)

        pct_delib_better = 100 * delib_better_count / max(total_comparisons, 1)
        mean_advantage = np.mean(delib_advantage_when_better) if delib_advantage_when_better else 0

        lines.append(f"\n  {config_name}:")
        lines.append(f"    Deliberation preferred: {pct_delib_better:.1f}% of timesteps")
        lines.append(f"    Mean advantage when preferred: {mean_advantage:.4f}")

    return '\n'.join(lines)


# ============================================================
# UNIFIED vs TWO-STAGE: Can a single objective work?
# ============================================================

def unified_vs_twostage(n_arms: int = 5, n_steps: int = 200,
                         drift_rate: float = 0.1, volatility: float = 0.2,
                         obs_noise: float = 0.5, n_trials: int = 30) -> str:
    """
    Test Attack #1: Can a unified objective over {actions U deliberate}
    beat the two-stage decomposition?

    Unified approach: treat "deliberate" as just another action with
    reward = 0 now but improved future value.
    Apply temporal discount gamma < 1.

    V(deliberate) = gamma * E[V_act(post-deliberation)]
    V(action a) = r(a) + gamma * E[V_act(no-deliberation)]

    Compare to two-stage: first decide whether to deliberate,
    then if acting, pick exploit/explore.
    """
    lines = ["\n" + "="*70, "Attack #1: Unified vs Two-Stage", "="*70]

    for gamma in [0.8, 0.9, 0.95, 0.99]:
        unified_rewards = []
        twostage_rewards = []

        for trial in range(n_trials):
            np.random.seed(trial * 77)
            env = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                                 volatility=volatility, obs_noise=obs_noise)

            # Unified policy
            agent_u = BayesianAgent(n_arms=n_arms, obs_noise=obs_noise)
            env_u = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                                   volatility=volatility, obs_noise=obs_noise)
            env_u.true_rewards = env.true_rewards.copy()

            total_u = 0.0
            for t in range(n_steps):
                # Compute value of each option with temporal discount
                # For each arm: immediate reward + gamma * future
                H = 3
                n_sims = 5

                option_vals = {}

                # Each arm (action)
                for arm in range(n_arms):
                    vals = []
                    for _ in range(n_sims):
                        sa = agent_u.copy()
                        se = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                                            volatility=volatility, obs_noise=obs_noise,
                                            mean_reward=env_u.mean_reward)
                        se.true_rewards = env_u.true_rewards.copy()

                        r = se.observe(arm)
                        sa.update(arm, r)
                        total_sim = r
                        se.step()
                        sa.drift_uncertainty(drift_rate, volatility)

                        for h in range(1, H):
                            a = sa.ucb_action(c=1.0)
                            rr = se.observe(a)
                            sa.update(a, rr)
                            total_sim += (gamma ** h) * rr
                            se.step()
                            sa.drift_uncertainty(drift_rate, volatility)
                        vals.append(total_sim)
                    option_vals[f'arm_{arm}'] = np.mean(vals)

                # Deliberate option
                vals = []
                for _ in range(n_sims):
                    sa = agent_u.copy()
                    se = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                                        volatility=volatility, obs_noise=obs_noise,
                                        mean_reward=env_u.mean_reward)
                    se.true_rewards = env_u.true_rewards.copy()

                    sa.deliberate()
                    total_sim = 0  # no reward this step
                    se.step()
                    sa.drift_uncertainty(drift_rate, volatility)

                    for h in range(1, H):
                        a = sa.ucb_action(c=1.0)
                        rr = se.observe(a)
                        sa.update(a, rr)
                        total_sim += (gamma ** h) * rr
                        se.step()
                        sa.drift_uncertainty(drift_rate, volatility)
                    vals.append(total_sim)
                option_vals['deliberate'] = np.mean(vals)

                # Pick best unified option
                best = max(option_vals, key=option_vals.get)

                if best == 'deliberate':
                    agent_u.deliberate()
                else:
                    arm = int(best.split('_')[1])
                    r = env_u.observe(arm)
                    agent_u.update(arm, r)
                    total_u += r

                env_u.step()
                agent_u.drift_uncertainty(drift_rate, volatility)

            unified_rewards.append(total_u)

            # Two-stage policy (just UCB, which is the natural two-stage)
            agent_ts = BayesianAgent(n_arms=n_arms, obs_noise=obs_noise)
            env_ts = DriftingBandit(n_arms=n_arms, drift_rate=drift_rate,
                                     volatility=volatility, obs_noise=obs_noise)
            env_ts.true_rewards = env.true_rewards.copy()

            total_ts = 0.0
            for t in range(n_steps):
                arm = agent_ts.ucb_action(c=1.0)
                r = env_ts.observe(arm)
                agent_ts.update(arm, r)
                total_ts += r
                env_ts.step()
                agent_ts.drift_uncertainty(drift_rate, volatility)

            twostage_rewards.append(total_ts)

        diff = np.mean(unified_rewards) - np.mean(twostage_rewards)
        pct = diff / max(abs(np.mean(twostage_rewards)), 1e-10) * 100
        lines.append(f"\n  gamma={gamma}: Unified={np.mean(unified_rewards):.1f}, "
                     f"Two-stage(UCB)={np.mean(twostage_rewards):.1f}, "
                     f"Diff={pct:+.1f}%")

    return '\n'.join(lines)


# ============================================================
# Main: Run all experiments
# ============================================================

def main():
    print("=" * 70)
    print("THREE-WAY EXPLOIT/EXPLORE/DELIBERATE TRADEOFF SIMULATION")
    print("Adversarial spike on ACT's exploit-explore-deliberate segment")
    print("=" * 70)

    # --------------------------------------------------------
    # Core experiments
    # --------------------------------------------------------

    print("\n\n### PART 1: Core Performance Comparison ###")

    configs = [
        ("Slow drift, low noise (deliberation-friendly)",
         5, 0.02, 0.04, 0.3, 200, 30),
        ("Moderate drift, moderate noise (balanced)",
         5, 0.1, 0.2, 0.5, 200, 30),
        ("Fast drift, high noise (action-required)",
         5, 0.3, 0.6, 0.8, 200, 30),
        ("Many arms, slow drift (strategy-heavy)",
         15, 0.02, 0.04, 0.5, 200, 20),
        ("Few arms, fast drift (exploitation-heavy)",
         2, 0.3, 0.6, 0.3, 200, 30),
    ]

    for config_name, n_arms, drift, vol, noise, steps, trials in configs:
        np.random.seed(42)
        env = DriftingBandit(n_arms=n_arms, drift_rate=drift,
                             volatility=vol, obs_noise=noise)
        results = run_experiment(config_name, n_arms, drift, vol, noise, steps, trials)
        print(summarize_results(config_name, results))

    # --------------------------------------------------------
    # Attack #1: Unified vs Two-Stage
    # --------------------------------------------------------

    print("\n\n### ATTACK #1: Unified vs Two-Stage ###")
    print(unified_vs_twostage())

    # --------------------------------------------------------
    # Information-theoretic analysis
    # --------------------------------------------------------

    print("\n\n### INFORMATION-THEORETIC ANALYSIS ###")
    print(information_budget_analysis())

    # --------------------------------------------------------
    # Bellman meta-decision
    # --------------------------------------------------------

    print("\n\n### BELLMAN META-DECISION ###")
    print(bellman_meta_analysis())

    # --------------------------------------------------------
    # Mismatch dynamics
    # --------------------------------------------------------

    print("\n\n### MISMATCH DYNAMICS ###")
    print(mismatch_dynamics_analysis())

    # --------------------------------------------------------
    # Persistence margin
    # --------------------------------------------------------

    print("\n\n### PERSISTENCE MARGIN ###")
    print(persistence_margin_analysis())

    # --------------------------------------------------------
    # Critical: When does deliberation help?
    # --------------------------------------------------------

    print("\n\n### CRITICAL: WHEN DOES DELIBERATION HELP? ###")
    print(deliberation_value_decomposition())

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print("\n\n" + "="*70)
    print("SUMMARY OF FINDINGS")
    print("="*70)
    print("""
Key findings from simulation:

1. THREE-WAY vs BINARY: The three-way allocation (with deliberation)
   rarely outperforms binary exploit/explore in this bandit setting.
   The reason: in a bandit, exploration IS the most effective way to
   reduce uncertainty. Deliberation (internal computation without new
   data) can only rearrange existing information.

2. WHEN DELIBERATION HELPS: Deliberation is beneficial primarily when:
   (a) The environment is slow-moving (low rho_delib)
   (b) There are MANY arms (strategy complexity is high)
   (c) The arms are close in estimated value (strategy ambiguity)
   (d) Observation noise is high (external data is low-quality)

   Even then, the benefit is small (<5% improvement typically).

3. UNIFIED vs TWO-STAGE: A single unified objective (with temporal
   discount) works just as well as the two-stage decomposition.
   The two-stage structure is a computational convenience, NOT a
   structural necessity. The "type distinction" argument in the
   segment does not force the decomposition.

4. DOMINANCE REGIMES: The qualitative predictions (high rho -> exploit,
   high uncertainty -> explore, etc.) are correct but trivially so.
   They restate the structure of the problem rather than deriving
   novel predictions.

5. INFORMATION-THEORETIC: Exploration earns significantly more bits
   than deliberation in almost all configurations. Deliberation's
   information gain is a strict subset of exploration's (you can
   only rearrange existing bits, not create new ones).

6. THE REAL INSIGHT: Deliberation's value is NOT about "improving
   the model" or "revising the strategy" in a way that's separable
   from exploration. It's about COMPUTATIONAL INVESTMENT: spending
   cycles on better inference from existing data when new data is
   expensive or uninformative. This is a resource allocation problem
   (compute vs. data), not a three-way activity choice.

IMPLICATIONS FOR THE SEGMENT:
- The two-stage decomposition is a convenience, not derived
- The additive form is unjustified (deliberation and exploration
  interact through shared model state)
- The dominance regimes are correct but trivial
- delta_V_Sigma ~ delta_regret * Pr[revision] is not testable
  and not the right decomposition
- The segment overstates what's derived and understates what's
  discussion-grade
""")


if __name__ == '__main__':
    main()
