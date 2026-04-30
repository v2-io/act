#!/usr/bin/env python3
"""
Pass A processor: synthesize consolidated_rationale fields.

Design (pass-a-brief.md):
  - Journalistic stance, not summarization. Surface substantive arguments.
  - Preserve dissent verbatim where it's load-bearing.
  - No consensus-signaling. Numbers (vote distribution) are already in the
    card; the rationale text adds the WHY.
  - 1-3 sentences typically; match length to substance.
  - For low-engagement single-vote rows: a brief, accurate description is
    fine — "Single-architecture proposal without elaboration."

Auto-synthesis covers cases where the corpus material is non-contradictory
and limited in volume. High-stakes cases (load-bearing keeps with rich
defense, contested multi-arg cases, substantive dissent) are flagged for
manual synthesis.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

PATH = Path('msc/naming/master-list-curated.json')


# ---------------------------------------------------------------------------
# Note normalization

def clean_note(note):
    if not note:
        return ''
    n = note.strip()
    n = re.sub(r'\s*\[from [^\]]+\]', '', n)
    n = re.sub(r'\s*\[original phrasing:[^\]]+\]', '', n)
    n = re.sub(r'\s*\[one of \d+ alternatives[^\]]*\]', '', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n


def neutralize_voice(text):
    """Strip first-person voice that biases R2 voters."""
    if not text:
        return text
    n = text
    replacements = [
        (r"\bI'd\b", "the proposer would"),
        (r"\bI'm\b", "the proposer is"),
        (r"\bI've\b", "the proposer has"),
        (r"\bI had voted\b", "the proposer voted"),
        (r"\bI think\b", "the proposer notes"),
        (r"\bI argue\b", "the proposer argues"),
        (r"\bI propose\b", "the proposer proposes"),
        (r"\bI prefer\b", "the proposer prefers"),
        (r"\bI reject\b", "rejected"),
        (r"\bI note\b", "noted"),
        (r"\bI considered\b", "considered"),
        (r"\bMy reading\b", "the proposer's reading"),
        (r"\bMy preference\b", "the proposer's preference"),
        (r"\bMy view\b", "the proposer's view"),
        (r"\bIn my view\b", "the proposer reasons"),
        (r"\bI vote\b", "the proposer votes"),
        (r"\bI flag\b", "flagged"),
        (r"\bI suspect\b", "the proposer suspects"),
        (r"\bI agree\b", "the proposer agrees"),
        (r"\bI also\b", "also"),
    ]
    for pat, repl in replacements:
        n = re.sub(pat, repl, n)
    # collapse double spaces
    n = re.sub(r'\s+', ' ', n).strip()
    return n


def is_substantive(note):
    if not note:
        return False
    n = note.strip().lower()
    if len(n) < 12:
        return False
    bare = {
        'pair-partner.', 'keep.', 'confirm.', 'agree.', 'accept.',
        'see above.', 'core diagnostic.', 'standard.', 'established.',
        'as above.', 'load-bearing.', 'crisp.', 'standard pair.',
    }
    return n not in bare


# ---------------------------------------------------------------------------
# Per-candidate rationale builders

def build_rationale(cur, cand):
    """Return (rationale_or_None, flag_or_None)."""
    votes = cand.get('votes', [])
    if not votes:
        return (None, "no votes (data anomaly)")

    is_keep = cand.get('is_keep', False)
    n_votes = len(votes)
    has_substantive_dissent = any(
        v.get('weight', 0) < 0 and is_substantive(clean_note(v.get('notes')))
        for v in votes
    )

    # High-stakes flagging: heavy multi-vote candidates with substantive notes
    # need careful manual synthesis; the brief example for these is roughly
    # the first canonical example.
    if is_keep and n_votes >= 8:
        return (None, "load-bearing keep with rich defense — manual synthesis")
    if not is_keep and n_votes >= 8:
        return (None, "high-engagement rename candidate — manual synthesis")
    if has_substantive_dissent and n_votes >= 3:
        return (None, "substantive dissent across votes — manual synthesis")

    if n_votes == 1:
        return single_vote_rationale(cur, cand, votes[0])
    return multi_vote_rationale(cur, cand, votes)


# ---------------------------------------------------------------------------
# Single-vote case

def single_vote_rationale(cur, cand, vote):
    note = clean_note(vote.get('notes'))
    weight = vote.get('weight', 0)

    if not note:
        return ("Single-architecture proposal without elaboration in the source vote.", None)

    short = note.rstrip('.').strip()

    # Reject votes — frame the argument against without leaking the vote count
    if weight < 0:
        framed = neutralize_voice(short)
        framed = capitalize_first(framed)
        if not framed.endswith(('.', '!', '?')):
            framed = framed + '.'
        return (f"Rejection argument: {decapitalize_first(framed)}", None)

    # Substantive single-vote — present the argument neutrally
    framed = neutralize_voice(short)
    framed = capitalize_first(framed)
    if not framed.endswith(('.', '!', '?')):
        framed = framed + '.'
    return (framed, None)


def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:] if s[0].isalpha() else s


def decapitalize_first(s):
    if not s:
        return s
    if len(s) >= 2 and s[0].isupper() and s[1].islower():
        return s[0].lower() + s[1:]
    return s


# ---------------------------------------------------------------------------
# Multi-vote case (low-engagement: 2-7 votes, no substantive dissent)

def multi_vote_rationale(cur, cand, votes):
    cleaned = [(v, clean_note(v.get('notes'))) for v in votes]
    cleaned = [(v, n) for v, n in cleaned if n]

    if not cleaned:
        return ("Affirmed by multiple voters without substantive elaboration in the per-vote notes.", None)

    pos_notes = [n for v, n in cleaned if v.get('weight', 0) > 0 and is_substantive(n)]
    neg_notes = [n for v, n in cleaned if v.get('weight', 0) < 0 and is_substantive(n)]

    pos_args = distinctive_arguments(pos_notes, max_count=3)
    neg_args = distinctive_arguments(neg_notes, max_count=2)

    if not pos_args and not neg_args:
        # Multi-vote but all bare-confirmation
        return ("Multiple voters affirmed without substantive elaboration beyond brief endorsements.", None)

    parts = []
    if pos_args:
        if len(pos_args) == 1:
            arg = neutralize_voice(pos_args[0]).rstrip('.')
            parts.append(capitalize_first(arg) + '.')
        else:
            # Present each argument as its own sentence to read as substantive case,
            # not a list of opinions.
            sents = [capitalize_first(neutralize_voice(a).rstrip('.')) + '.' for a in pos_args]
            parts.extend(sents)

    if neg_args:
        if len(neg_args) == 1:
            arg = neutralize_voice(neg_args[0]).rstrip('.')
            parts.append(f"Objection: {decapitalize_first(arg)}.")
        else:
            sents = [f"Objection: {decapitalize_first(neutralize_voice(a).rstrip('.'))}." for a in neg_args]
            parts.extend(sents)

    return (' '.join(parts), None)


def distinctive_arguments(notes, max_count=3):
    seen = []
    for n in notes:
        if not n:
            continue
        found = False
        for i, existing in enumerate(seen):
            if jaccard(n, existing) > 0.55:
                if len(n) > len(existing):
                    seen[i] = n
                found = True
                break
        if not found:
            seen.append(n)
    return [first_sentence(s) for s in seen[:max_count]]


def first_sentence(note):
    n = note.strip()
    parts = re.split(r'(?<=[.!?])\s+', n, maxsplit=1)
    out = parts[0].strip() if parts else n
    if len(out) < 30 and len(parts) > 1:
        out = (out + ' ' + parts[1]).strip()
        parts2 = re.split(r'(?<=[.!?])\s+', out, maxsplit=1)
        out = parts2[0].strip() if parts2 else out
    return out


def jaccard(a, b):
    sa = set(re.findall(r'\w+', a.lower()))
    sb = set(re.findall(r'\w+', b.lower()))
    if not sa or not sb:
        return 0
    return len(sa & sb) / len(sa | sb)


# ---------------------------------------------------------------------------
# Main

def process(data):
    filled = 0
    flagged = 0
    skipped = 0
    flag_messages_by_current = defaultdict(list)

    for cur in data['currents']:
        for cand in cur['candidates']:
            if cand.get('consolidated_rationale') is not None:
                skipped += 1
                continue
            r, flag = build_rationale(cur, cand)
            if r is None:
                if flag:
                    flag_messages_by_current[cur['current']].append(
                        f"`{cand['candidate']}`: {flag}"
                    )
                    flagged += 1
                continue
            cand['consolidated_rationale'] = r
            filled += 1

    for cur in data['currents']:
        msgs = flag_messages_by_current.get(cur['current'])
        if not msgs:
            continue
        existing = cur.get('manual_curation_notes') or ''
        if 'Pass A flags:' in existing:
            continue
        flag_block = "Pass A flags:\n  - " + "\n  - ".join(msgs)
        cur['manual_curation_notes'] = (existing + ('\n\n' if existing else '') + flag_block).strip()

    return filled, flagged, skipped


def main():
    with PATH.open() as f:
        data = json.load(f)
    filled, flagged, skipped = process(data)
    print(f"Filled: {filled}", file=sys.stderr)
    print(f"Flagged for manual review: {flagged}", file=sys.stderr)
    print(f"Skipped (already filled): {skipped}", file=sys.stderr)
    with PATH.open('w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {PATH}", file=sys.stderr)


if __name__ == '__main__':
    main()
