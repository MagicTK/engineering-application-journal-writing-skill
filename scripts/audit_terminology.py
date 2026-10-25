#!/usr/bin/env python3
"""Read-only terminology candidates, not a grammar judge or a TeX compiler."""

from __future__ import annotations

import argparse
from bisect import bisect_right
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
    "offline": (r"\boffline\b", "Distinguish measurement procedures such as an offline assay from evaluation timing; real-world data do not need this routine prefix."),
    "deployment": (r"\bdeploy(?:ment|ed)?\b|\breal[- ]time\b", "Verify actual operational integration or the stated timing evidence; streaming computation and data provenance alone do not establish deployment."),
    "membership-probability": (r"\b(?:soft\s+(?:grouping|assignments?|clustering)|membership\s+(?:degrees?|values?)|calibrated\s+probabilit(?:y|ies))\b", "Distinguish graded weights, fuzzy memberships and probabilities; normalization alone does not establish calibration."),
    "physical-propagation": (r"\b(?:fault|feature|disturbance)\s+propagation\b|\bmessage\s+passing\b", "Distinguish physical disturbance spread from graph-feature updates; inspect the process evidence and actual operation."),
    "causality": (r"\bcausal(?:ity)?\b|\broot[- ]cause\b", "Distinguish past-only causal computation, predictive relations and physical causality; match diagnosis/localization claims to their actual evidence."),
    "development-set": (r"\bdevelopment\s+(?:set|data|samples?)\b", "Confirm the real training/selection partition; do not invent a validation set."),
}
STOP = set("a an and are as at be been being but by can could do does for from has have in into is it its may of on or our that the their these they this those through to was were which will with within without we such each than then also".split())
TOKEN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
CONTROL = re.compile(r"\\(iffalse|iftrue|else|fi)\b")
DIRECTIVE = re.compile(CONTROL.pattern + r"|\\(begin|end)\{comment\}")
PROSE_BOUNDARY = "\x00"
NONPROSE_ENVIRONMENT = re.compile(
    r"\\begin\s*\{thebibliography\}.*?\\end\s*\{thebibliography\}", re.S
)
NONPROSE_ARGUMENT = re.compile(
    r"\\(?:cite\w*|[Cc]ref|[Cc]pageref|autoref|pageref|eqref|ref|label|"
    r"parencite|textcite|autocite|footcite|nocite|url|path|href|bibliography|bibliographystyle)"
    r"\*?(?:\s*\[[^\[\]]*\]){0,2}\s*\{[^{}]*\}"
)


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
        pieces = []
        start = 0
        for match in DIRECTIVE.finditer(line):
            # Inactive branches do not execute comment environments; their bodies
            # still contain conditional tokens that TeX uses to find the branch end.
            if comment_environment:
                if match.group(2) == "end":
                    comment_environment = False
                start = match.end()
                continue
            if all(stack):
                pieces.append(line[start:match.start()])
            command = match.group(1)
            if command in {"iftrue", "iffalse"}:
                stack.append(command == "iftrue")
            elif command == "else" and stack:
                stack[-1] = not stack[-1]
            elif command == "fi" and stack:
                stack.pop()
            elif match.group(2) == "begin" and all(stack):
                comment_environment = True
            elif match.group(2) == "end" and all(stack):
                pieces.append(match.group())
            start = match.end()
        if all(stack) and not comment_environment:
            pieces.append(line[start:])
        rows.append((number, "".join(pieces)))
    return rows


def prose_lines(rows: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Mask reference metadata and mark exclusions without changing line numbers."""
    def blank(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group())

    def block_boundary(match: re.Match[str]) -> str:
        return PROSE_BOUNDARY + blank(match)[1:]

    text = "\n".join(line for _, line in rows)
    text = NONPROSE_ENVIRONMENT.sub(block_boundary, text)
    text = NONPROSE_ARGUMENT.sub(block_boundary, text)
    return [(number, line) for (number, _), line in zip(rows, text.split("\n"))]


def prose_blocks(source: str, rows: list[tuple[int, str]], tex: bool) -> list[tuple[str, list[int], list[int]]]:
    """Join ordinary wraps, retaining line spans and conservative TeX boundaries."""
    raw_lines = source.splitlines()
    blocks = []
    parts: list[str] = []
    starts: list[int] = []
    numbers: list[int] = []
    length = 0

    def flush() -> None:
        nonlocal length
        if starts:
            blocks.append(("".join(parts), starts[:], numbers[:]))
        parts.clear()
        starts.clear()
        numbers.clear()
        length = 0

    for number, line in rows:
        raw = raw_lines[number - 1]
        if not raw.strip():
            flush()
            continue
        stripped = strip_comment(raw) if tex else raw
        # Do not guess whitespace across conditional or comment-environment directives.
        directive = tex and bool(CONTROL.search(stripped) or r"\begin{comment}" in stripped or r"\end{comment}" in stripped)
        if directive:
            flush()
        line = line.lstrip(" \t") if tex else line
        segments = re.split(PROSE_BOUNDARY + r"|\\par\b", line) if tex else [line]
        for index, segment in enumerate(segments):
            if index:
                flush()
            if segment:
                starts.append(length)
                numbers.append(number)
                parts.append(segment)
                length += len(segment)
        if not tex or stripped == raw:
            parts.append(" ")
            length += 1
        if directive:
            flush()
    flush()
    return blocks


def audit(source: str, *, tex: bool = True, min_count: int = 3, top: int = 60) -> dict:
    rows = visible_lines(source, tex)
    if tex:
        rows = prose_lines(rows)
    joined = "\n".join(line for _, line in rows)
    blocks = prose_blocks(source, rows, tex)
    candidates = []
    for rule, (pattern, question) in RULES.items():
        regex = re.compile(pattern, re.I)
        occurrences = [
            {"line": numbers[bisect_right(starts, match.start()) - 1],
             "end_line": numbers[bisect_right(starts, match.end() - 1) - 1],
             "term": re.sub(r"\s+", " ", match.group()),
             "context": re.sub(r"\s+", " ", text[max(0, match.start()-70):match.end()+90]).strip()}
            for text, starts, numbers in blocks for match in regex.finditer(text)
        ]
        if occurrences:
            candidates.append({"rule": rule, "count": len(occurrences), "question": question, "occurrences": occurrences})
    counts: Counter[str] = Counter()
    for line, _, _ in blocks:
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
        "limitations": ["Not a TeX compiler: custom macros, input files, verbatim/catcode changes and arbitrary conditional branches require active-PDF verification.", "Known citation/reference keys, URL targets and literal thebibliography blocks are excluded and separate phrase spans in TeX mode; custom or nested forms need manual screening.", "Ordinary wraps are joined within paragraphs with source start/end lines retained; literal percent newline suppression is recognized. Conditional/comment-environment directive lines are conservative boundaries. Formulas, quoted titles and noun/verb ambiguity need manual screening.", "Frequency is not evidence that wording is right or wrong; no automatic replacements are proposed."],
        "abstract_whitespace_word_count": len(abstract.group(1).replace(PROSE_BOUNDARY, "").split()) if abstract else None,
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
