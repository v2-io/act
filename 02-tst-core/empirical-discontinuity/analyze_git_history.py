#!/usr/bin/env python3
"""
Git History Discontinuity Analyzer

Analyzes git repository history to measure the relationship between
code discontinuities and development time/bug rates.

Based on FP-012: Comprehension Continuity Principle
T_comprehend = T_base × (1 + α)^d
"""

import subprocess
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
import argparse
import sys
from collections import defaultdict, Counter
import numpy as np
from scipy import stats
import pickle


@dataclass
class CommitMetrics:
    """Metrics for a single commit"""
    hash: str
    timestamp: datetime
    author: str
    message: str
    files_changed: int
    unique_directories: int
    lines_added: int
    lines_deleted: int
    file_transitions: int  # Context switches between files
    directory_transitions: int  # Context switches between directories
    discontinuity_score: float
    is_bug_fix: bool
    is_refactor: bool
    time_since_last_commit: Optional[timedelta]
    commit_time_estimate: Optional[timedelta]  # Time to create this commit


@dataclass
class FileMetrics:
    """Metrics for a single file"""
    filepath: str
    total_changes: int
    unique_authors: int
    bug_fix_frequency: float
    avg_discontinuity_per_change: float
    coupled_files: List[Tuple[str, float]]  # (filepath, coupling_strength)
    stability_score: float  # Based on FP-003 (Lindy effect)


class GitAnalyzer:
    """Analyzes git repository for discontinuity patterns"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.commits: List[CommitMetrics] = []
        self.file_metrics: Dict[str, FileMetrics] = {}
        self.coupling_matrix: Dict[Tuple[str, str], int] = defaultdict(int)
        
    def run_git_command(self, cmd: List[str]) -> str:
        """Execute git command and return output"""
        result = subprocess.run(
            ["git"] + cmd,
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Git command failed: {' '.join(cmd)}\n{result.stderr}")
        return result.stdout
    
    def analyze_repository(self, max_commits: int = 1000) -> None:
        """Main analysis entry point"""
        print(f"Analyzing repository at {self.repo_path}")
        
        # Get commit list
        commit_hashes = self.get_commit_hashes(max_commits)
        print(f"Found {len(commit_hashes)} commits to analyze")
        
        # Analyze each commit
        prev_timestamp = None
        for i, hash in enumerate(commit_hashes):
            if i % 100 == 0:
                print(f"Analyzing commit {i}/{len(commit_hashes)}")
            
            metrics = self.analyze_commit(hash, prev_timestamp)
            self.commits.append(metrics)
            prev_timestamp = metrics.timestamp
            
            # Update coupling matrix
            self.update_coupling_matrix(metrics)
        
        # Calculate file-level metrics
        self.calculate_file_metrics()
        
        # Calculate correlations
        self.calculate_correlations()
    
    def get_commit_hashes(self, max_commits: int) -> List[str]:
        """Get list of commit hashes"""
        output = self.run_git_command(["log", "--format=%H", f"-{max_commits}"])
        return output.strip().split('\n')
    
    def analyze_commit(self, hash: str, prev_timestamp: Optional[datetime]) -> CommitMetrics:
        """Analyze a single commit"""
        # Get commit details
        format_str = "%H%n%at%n%an%n%s"
        output = self.run_git_command(["show", "--format=" + format_str, "--name-only", hash])
        lines = output.strip().split('\n')
        
        # Parse basic info
        commit_hash = lines[0]
        timestamp = datetime.fromtimestamp(int(lines[1]))
        author = lines[2]
        message = lines[3]
        
        # Get changed files (skip empty lines and the commit message)
        changed_files = [f for f in lines[4:] if f.strip() and not f.startswith('diff')]
        
        # Get detailed stats
        stats_output = self.run_git_command(["show", "--stat", "--format=", hash])
        lines_added, lines_deleted = self.parse_diff_stats(stats_output)
        
        # Calculate discontinuity metrics
        files_changed = len(changed_files)
        unique_dirs = len(set(str(Path(f).parent) for f in changed_files))
        
        # Calculate transitions (simplified - would need more sophisticated analysis)
        file_transitions = self.calculate_transitions(changed_files)
        dir_transitions = self.calculate_directory_transitions(changed_files)
        
        # Calculate discontinuity score using FP-012 model
        # d = file_transitions + (dir_transitions * 2) + (cross_module * 4)
        discontinuity_score = file_transitions + (dir_transitions * 2)
        
        # Detect bug fixes and refactoring
        is_bug_fix = self.is_bug_fix_commit(message)
        is_refactor = self.is_refactor_commit(message)
        
        # Calculate time metrics
        time_since_last = None
        if prev_timestamp:
            time_since_last = timestamp - prev_timestamp
        
        # Estimate commit creation time (heuristic based on changes)
        commit_time = self.estimate_commit_time(files_changed, lines_added + lines_deleted)
        
        return CommitMetrics(
            hash=commit_hash,
            timestamp=timestamp,
            author=author,
            message=message,
            files_changed=files_changed,
            unique_directories=unique_dirs,
            lines_added=lines_added,
            lines_deleted=lines_deleted,
            file_transitions=file_transitions,
            directory_transitions=dir_transitions,
            discontinuity_score=discontinuity_score,
            is_bug_fix=is_bug_fix,
            is_refactor=is_refactor,
            time_since_last_commit=time_since_last,
            commit_time_estimate=commit_time
        )
    
    def parse_diff_stats(self, stats_output: str) -> Tuple[int, int]:
        """Parse diff statistics for lines added/deleted"""
        lines_added = 0
        lines_deleted = 0
        
        for line in stats_output.split('\n'):
            # Look for pattern like "10 insertions(+), 5 deletions(-)"
            match = re.search(r'(\d+) insertion', line)
            if match:
                lines_added = int(match.group(1))
            match = re.search(r'(\d+) deletion', line)
            if match:
                lines_deleted = int(match.group(1))
                
        return lines_added, lines_deleted
    
    def calculate_transitions(self, files: List[str]) -> int:
        """Calculate number of file transitions (context switches)"""
        if len(files) <= 1:
            return 0
        # Simplified: assume each file represents a context switch
        return len(files) - 1
    
    def calculate_directory_transitions(self, files: List[str]) -> int:
        """Calculate number of directory transitions"""
        if len(files) <= 1:
            return 0
        
        dirs = [str(Path(f).parent) for f in files]
        transitions = 0
        for i in range(1, len(dirs)):
            if dirs[i] != dirs[i-1]:
                transitions += 1
        return transitions
    
    def is_bug_fix_commit(self, message: str) -> bool:
        """Detect if commit is a bug fix"""
        bug_patterns = [
            r'\bfix\b', r'\bbug\b', r'\berror\b', r'\bissue\b',
            r'\bpatch\b', r'\brepair\b', r'\bcorrect\b', r'\bresolve\b'
        ]
        message_lower = message.lower()
        return any(re.search(pattern, message_lower) for pattern in bug_patterns)
    
    def is_refactor_commit(self, message: str) -> bool:
        """Detect if commit is a refactoring"""
        refactor_patterns = [
            r'\brefactor\b', r'\brestructure\b', r'\breorganize\b',
            r'\bclean\b', r'\bsimplify\b', r'\bextract\b', r'\bmove\b'
        ]
        message_lower = message.lower()
        return any(re.search(pattern, message_lower) for pattern in refactor_patterns)
    
    def estimate_commit_time(self, files_changed: int, lines_changed: int) -> timedelta:
        """Estimate time to create commit based on complexity"""
        # Heuristic: base time + time per file + time per line
        base_minutes = 10
        minutes_per_file = 5
        minutes_per_100_lines = 15
        
        total_minutes = (
            base_minutes +
            (files_changed * minutes_per_file) +
            (lines_changed / 100 * minutes_per_100_lines)
        )
        
        return timedelta(minutes=total_minutes)
    
    def update_coupling_matrix(self, metrics: CommitMetrics) -> None:
        """Update file coupling matrix based on commit"""
        # This would need actual file names from the commit
        pass  # Simplified for now
    
    def calculate_file_metrics(self) -> None:
        """Calculate metrics for each file in the repository"""
        file_changes = defaultdict(list)
        
        # Group commits by file
        for commit in self.commits:
            # Need to get actual files from commit
            # For now, this is simplified
            pass
        
        # Calculate metrics for each file
        # This would include coupling analysis, stability scores, etc.
    
    def calculate_correlations(self) -> None:
        """Calculate correlations between discontinuity and outcomes"""
        if not self.commits:
            return
        
        # Extract arrays for correlation
        discontinuities = [c.discontinuity_score for c in self.commits]
        is_bug_fix = [1 if c.is_bug_fix else 0 for c in self.commits]
        files_changed = [c.files_changed for c in self.commits]
        
        # Calculate correlations
        if len(set(discontinuities)) > 1:  # Need variance for correlation
            bug_correlation = stats.pearsonr(discontinuities, is_bug_fix)
            print(f"\nCorrelation between discontinuity and bugs: {bug_correlation[0]:.3f} (p={bug_correlation[1]:.3f})")
            
            files_correlation = stats.pearsonr(discontinuities, files_changed)
            print(f"Correlation between discontinuity and files changed: {files_correlation[0]:.3f} (p={files_correlation[1]:.3f})")
        
        # Test exponential model
        self.test_exponential_model()
    
    def test_exponential_model(self) -> None:
        """Test if comprehension time follows exponential model"""
        print("\nTesting Exponential Model: T = T_base × (1 + α)^d")
        
        # Group commits by discontinuity score
        discontinuity_groups = defaultdict(list)
        for commit in self.commits:
            d_score = int(commit.discontinuity_score)
            if commit.commit_time_estimate:
                discontinuity_groups[d_score].append(commit.commit_time_estimate.total_seconds() / 60)
        
        # Calculate average time for each discontinuity level
        x_values = []
        y_values = []
        for d_score, times in sorted(discontinuity_groups.items()):
            if times:
                x_values.append(d_score)
                y_values.append(np.mean(times))
        
        if len(x_values) > 2:
            # Fit exponential model: y = a * (1 + b)^x
            # Take log: log(y) = log(a) + x * log(1 + b)
            log_y = np.log(y_values)
            coeffs = np.polyfit(x_values, log_y, 1)
            
            alpha = np.exp(coeffs[0]) - 1
            t_base = np.exp(coeffs[1])
            
            print(f"Fitted model parameters:")
            print(f"  T_base = {t_base:.1f} minutes")
            print(f"  α = {alpha:.3f} ({alpha*100:.1f}% penalty per discontinuity)")
            
            # Calculate R-squared
            y_pred = [t_base * (1 + alpha)**x for x in x_values]
            ss_res = sum((y - y_pred[i])**2 for i, y in enumerate(y_values))
            ss_tot = sum((y - np.mean(y_values))**2 for y in y_values)
            r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
            
            print(f"  R² = {r_squared:.3f}")
            
            # Compare with linear model
            linear_coeffs = np.polyfit(x_values, y_values, 1)
            y_linear = [linear_coeffs[0] * x + linear_coeffs[1] for x in x_values]
            ss_res_linear = sum((y - y_linear[i])**2 for i, y in enumerate(y_values))
            r_squared_linear = 1 - (ss_res_linear / ss_tot) if ss_tot > 0 else 0
            
            print(f"\nLinear model R² = {r_squared_linear:.3f}")
            print(f"Exponential model fits {'better' if r_squared > r_squared_linear else 'worse'} than linear")
    
    def save_results(self, output_dir: str = "data") -> None:
        """Save analysis results"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Save commits data
        commits_data = [asdict(c) for c in self.commits]
        with open(output_path / "commits.json", 'w') as f:
            json.dump(commits_data, f, default=str, indent=2)
        
        # Save pickled data for later analysis
        with open(output_path / "analysis.pkl", 'wb') as f:
            pickle.dump({
                'commits': self.commits,
                'file_metrics': self.file_metrics,
                'coupling_matrix': self.coupling_matrix
            }, f)
        
        print(f"\nResults saved to {output_path}")
    
    def generate_report(self) -> str:
        """Generate analysis report"""
        report = []
        report.append("=" * 60)
        report.append("Git Repository Discontinuity Analysis Report")
        report.append("=" * 60)
        report.append(f"Repository: {self.repo_path}")
        report.append(f"Commits analyzed: {len(self.commits)}")
        
        if self.commits:
            avg_discontinuity = np.mean([c.discontinuity_score for c in self.commits])
            bug_fix_rate = sum(1 for c in self.commits if c.is_bug_fix) / len(self.commits)
            
            report.append(f"\nAverage discontinuity score: {avg_discontinuity:.2f}")
            report.append(f"Bug fix rate: {bug_fix_rate:.1%}")
            
            # Top discontinuous commits
            top_commits = sorted(self.commits, key=lambda c: c.discontinuity_score, reverse=True)[:5]
            report.append("\nTop 5 most discontinuous commits:")
            for c in top_commits:
                report.append(f"  {c.hash[:8]}: d={c.discontinuity_score:.1f}, files={c.files_changed}, {c.message[:50]}")
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Analyze git history for discontinuity patterns")
    parser.add_argument("--repo", default=".", help="Path to git repository")
    parser.add_argument("--max-commits", type=int, default=1000, help="Maximum commits to analyze")
    parser.add_argument("--output", default="empirical-discontinuity/data", help="Output directory")
    
    args = parser.parse_args()
    
    analyzer = GitAnalyzer(args.repo)
    
    try:
        analyzer.analyze_repository(args.max_commits)
        analyzer.save_results(args.output)
        print("\n" + analyzer.generate_report())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())