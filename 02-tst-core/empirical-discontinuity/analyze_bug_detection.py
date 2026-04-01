#!/usr/bin/env python3
"""Analyze what's being detected as bugs"""

import pickle
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional, List
import re

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
    file_transitions: int
    directory_transitions: int
    discontinuity_score: float
    is_bug_fix: bool
    is_refactor: bool
    time_since_last_commit: Optional[timedelta]
    commit_time_estimate: Optional[timedelta]

@dataclass
class FileMetrics:
    """Metrics for a single file"""
    filepath: str
    total_changes: int
    unique_authors: int
    bug_fix_frequency: float
    avg_discontinuity_per_change: float
    coupled_files: List[tuple]
    stability_score: float

# Load the data
with open('data/analysis.pkl', 'rb') as f:
    data = pickle.load(f)

commits = data['commits']

# Analyze bug detection
bug_fixes = [c for c in commits if c.is_bug_fix]
non_bugs = [c for c in commits if not c.is_bug_fix]

print(f"=== BUG DETECTION ANALYSIS ===")
print(f"Total commits: {len(commits)}")
print(f"Detected as bug fixes: {len(bug_fixes)} ({len(bug_fixes)/len(commits)*100:.1f}%)")
print(f"Not bug fixes: {len(non_bugs)} ({len(non_bugs)/len(commits)*100:.1f}%)")

# Show examples of what's being detected as bugs
print(f"\n=== SAMPLE 'BUG FIX' COMMITS ===")
for c in bug_fixes[:10]:
    print(f"\nMessage: {c.message[:80]}")
    print(f"  Discontinuity: {c.discontinuity_score:.0f}")
    print(f"  Files changed: {c.files_changed}")

# Show high-discontinuity non-bugs
print(f"\n=== HIGH-DISCONTINUITY NON-BUGS ===")
high_disc_non_bugs = sorted(non_bugs, key=lambda x: x.discontinuity_score, reverse=True)[:5]
for c in high_disc_non_bugs:
    print(f"\nMessage: {c.message[:80]}")
    print(f"  Discontinuity: {c.discontinuity_score:.0f}")
    print(f"  Files changed: {c.files_changed}")

# Check what words are triggering bug detection
bug_patterns = [
    r'\bfix\b', r'\bbug\b', r'\berror\b', r'\bissue\b',
    r'\bpatch\b', r'\brepair\b', r'\bcorrect\b', r'\bresolve\b'
]

print(f"\n=== TRIGGER WORD ANALYSIS ===")
trigger_counts = {pattern: 0 for pattern in bug_patterns}

for c in bug_fixes:
    message_lower = c.message.lower()
    for pattern in bug_patterns:
        if re.search(pattern, message_lower):
            trigger_counts[pattern] += 1

for pattern, count in sorted(trigger_counts.items(), key=lambda x: x[1], reverse=True):
    if count > 0:
        print(f"{pattern}: {count} occurrences")

# Analyze false positives
print(f"\n=== LIKELY FALSE POSITIVES ===")
print("(Commits with 'fix' but probably not bug fixes)")

for c in bug_fixes:
    msg_lower = c.message.lower()
    # Check for common false positive patterns
    if any(phrase in msg_lower for phrase in [
        'fix formatting', 'fix typo', 'fix comment', 'fix documentation',
        'fix style', 'fix lint', 'fix whitespace', 'fix indentation'
    ]):
        print(f"\n{c.message[:80]}")
        print(f"  Discontinuity: {c.discontinuity_score:.0f}")

# Better bug detection suggestion
print(f"\n=== IMPROVED BUG DETECTION ===")
print("Suggesting better patterns for this repository:")

# Count actual bug-like patterns
actual_bugs = 0
for c in commits:
    msg_lower = c.message.lower()
    # More specific bug patterns
    if any(phrase in msg_lower for phrase in [
        'fix bug', 'fixes bug', 'bugfix', 'bug fix',
        'fix error', 'fix crash', 'fix issue #',
        'fix broken', 'fix failing'
    ]):
        actual_bugs += 1

print(f"\nWith stricter patterns: {actual_bugs} likely real bugs ({actual_bugs/len(commits)*100:.1f}%)")
print("This would exclude commits that just 'fix' formatting, typos, or non-bug issues.")