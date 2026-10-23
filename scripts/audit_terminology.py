#!/usr/bin/env python3
"""Read-only terminology candidates, not a grammar judge or a TeX compiler."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re


RULES = {
    "attribute": (r"\battributes?\b", "Distinguish measured variables, semantic/graph attributes and the verb attribute."),
    "record": (r"\brecords?\b", "Distinguish database/log records, learning samples and the verb record."),
    "state-condition": (r"\b(?:process|operating|operational|prototype)\s+(?:state|conditions?)s?\b", "Identify the physical, inferred or latent object; do not replace state with condition automatically."),
    "variable-feature": (r"\bvariable[- ](?:specific|wise)\s+(?:features?|behavio[u]?rs?)\b", "Distinguish distinctiveness from per-variable organization or independent encoding."),
    "stage-scope": (r"\b(?:intra|inter|cross)[- ]stage\b|\bstage[- ](?:level|structured)\b", "Check within/between/across scope and feature granularity against the actual operation."),
    "exchange": (r"\binformation\s+exchange\b", "Name the actual interaction, aggregation, fusion or communication; exchange is not universally wrong."),
    "offline": (r"\boffline\b", "Retain when evaluation timing matters; real-world data do not need this routine prefix."),
    "deployment": (r"\bdeploy(?:ment|ed)?\b|\breal[- ]time\b", "Verify operational or timing evidence; provenance alone does not establish deployment."),
    "causality": (r"\bcausal(?:ity)?\b|\broot[- ]cause\b", "Require matching task definition and causal/localization evidence, not just class labels."),
    "development-set": (r"\bdevelopment\s+(?:set|data|samples?)\b", "Confirm the real training/selection partition; do not invent a validation set."),
}
STOP = set("a an and are as at be been being but by can could do does for from has have in into is it its may of on or our that the their these they this those through to was were which will with within without we such each than then also".split())
TOKEN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
CONTROL = re.compile(r"\\(iffalse|iftrue|else|fi)\b")


def strip_comment(line: str) -> str:
    for index, char in enumerate(line):
        if char != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return line[:index]
    return line


def visible_lines(source: str, tex: bool = True) -> list[tuple[int, str]]:
    """Handle percent comments and literal iftrue/iffalse; no macro expansion."""
    rows = []
    stack: list[bool] = []
    comment_environment = False
    for number, raw in enumerate(source.splitlines(), 1):
        line = strip_comment(raw) if tex else raw
        if not tex:
            rows.append((number, line))
            continue
        if comment_environment:
            if r"\end{comment}" not in line:
                rows.append((number, ""))
                continue
            line = line.split(r"\end{comment}", 1)[1]
            comment_environment = False
        if r"\begin{comment}" in line:
            before, after = line.split(r"\begin{comment}", 1)
            if r"\end{comment}" in after:
                line = before + after.split(r"\end{comment}", 1)[1]
            else:
                line = before
                comment_environment = True
        pieces = []
        start = 0
        for match in CONTROL.finditer(line):
            if all(stack):
                pieces.append(line[start:match.start()])
            command = match.group(1)
            if command in {"iftrue", "iffalse"}:
                stack.append(command == "iftrue")
            elif command == "else" and stack:
                stack[-1] = not stack[-1]
            elif command == "fi" and stack:
                stack.pop()
            start = match.end()
        if all(stack):
            pieces.append(line[start:])
        rows.append((number, "".join(pieces)))
    return rows


def audit(source: str, *, tex: bool = True, min_count: int = 3, top: int = 60) -> dict:
    rows = visible_lines(source, tex)
    joined = "\n".join(line for _, line in rows)
    candidates = []
    for rule, (pattern, question) in RULES.items():
        regex = re.compile(pattern, re.I)
        occurrences = [
            {"line": number, "term": match.group(), "context": line[max(0, match.start()-70):match.end()+90].strip()}
            for number, line in rows for match in regex.finditer(line)
        ]
        if occurrences:
            candidates.append({"rule": rule, "count": len(occurrences), "question": question, "occurrences": occurrences})
    counts: Counter[str] = Counter()
    for _, line in rows:
        line = re.sub(r"\\(?:cite\w*|ref|label|eqref)\*?(?:\[[^]]*\])?\{[^}]*\}", " ", line)
        line = re.sub(r"\\[A-Za-z]+\*?", " ", line)
        for segment in re.split(r"[.!?;:{}]", line):
            tokens = [token.lower() for token in TOKEN.findall(segment)]
            for size in range(1, 5):
                for start in range(len(tokens)-size+1):
                    words = tokens[start:start+size]
                    if words[0] not in STOP and words[-1] not in STOP:
                        counts[" ".join(words)] += 1
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", joined, re.S) if tex else None
    return {
        "mode": "review_candidates_only",
        "limitations": ["Not a TeX compiler: custom macros, input files and arbitrary conditional branches require active-PDF verification.", "Candidate context is line-based; formulas, references and noun/verb ambiguity need manual screening.", "Frequency is not evidence that wording is right or wrong; no automatic replacements are proposed."],
        "abstract_whitespace_word_count": len(abstract.group(1).split()) if abstract else None,
        "candidates": candidates,
        "recurring_terms": [{"term": term, "count": count} for term, count in counts.most_common() if count >= min_count][:top],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--plain", action="store_true", help="Treat the input as plain text instead of TeX")
    parser.add_argument("--min-count", type=int, default=3)
    parser.add_argument("--top", type=int, default=60)
    args = parser.parse_args()
    if args.min_count < 1 or args.top < 1:
        parser.error("counts must be positive")
    if args.source.stat().st_size > 10_000_000:
        parser.error("input exceeds the 10 MB single-file review limit")
    result = audit(args.source.read_text(encoding="utf-8"), tex=not args.plain, min_count=args.min_count, top=args.top)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
