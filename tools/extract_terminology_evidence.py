#!/usr/bin/env python3
"""Extract terminology frequencies and short source contexts from PDF corpora.

The script is intentionally read-only with respect to the source corpora. It
creates a JSON evidence file that keeps each term tied to the paper in which it
appears, so terminology guidance can be audited instead of inferred from memory.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from pypdf import PdfReader


def parse_corpus(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("corpus must be NAME=/absolute/path")
    name, path = value.split("=", 1)
    return name.strip(), Path(path).expanduser().resolve()


def read_terms(path: Path) -> list[str]:
    terms: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        term = line.strip()
        if term and not term.startswith("#"):
            terms.append(term)
    return terms


def extract_text(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = [(page.extract_text() or "") for page in reader.pages]
    text = "\n".join(pages)
    return re.sub(r"\s+", " ", text).strip()


def contexts(text: str, term: str, limit: int, radius: int) -> list[str]:
    pattern = re.compile(rf"(?i)(?<!\w){re.escape(term)}(?!\w)")
    snippets: list[str] = []
    for match in pattern.finditer(text):
        start = max(0, match.start() - radius)
        end = min(len(text), match.end() + radius)
        snippet = text[start:end].strip()
        if start:
            snippet = "..." + snippet
        if end < len(text):
            snippet += "..."
        snippets.append(snippet)
        if len(snippets) >= limit:
            break
    return snippets


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", action="append", required=True, type=parse_corpus)
    parser.add_argument("--terms", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--contexts-per-paper", type=int, default=2)
    parser.add_argument("--context-radius", type=int, default=150)
    args = parser.parse_args()

    terms = read_terms(args.terms.resolve())
    evidence: dict[str, list[dict[str, object]]] = defaultdict(list)
    corpus_totals: Counter[str] = Counter()
    failures: list[dict[str, str]] = []
    papers: list[dict[str, str]] = []
    duplicates: list[dict[str, str]] = []
    seen_titles: dict[str, str] = {}

    for corpus_name, corpus_dir in args.corpus:
        for pdf in sorted(corpus_dir.rglob("*.pdf")):
            title_key = re.sub(r"\s+", " ", pdf.stem).strip().casefold()
            if title_key in seen_titles:
                duplicates.append(
                    {
                        "corpus": corpus_name,
                        "paper": pdf.name,
                        "path": str(pdf),
                        "kept_path": seen_titles[title_key],
                    }
                )
                continue
            seen_titles[title_key] = str(pdf)
            papers.append({"corpus": corpus_name, "paper": pdf.name, "path": str(pdf)})
            try:
                text = extract_text(pdf)
            except Exception as exc:  # Keep the corpus audit running after one bad PDF.
                failures.append({"corpus": corpus_name, "paper": pdf.name, "error": str(exc)})
                continue

            lowered = text.lower()
            for term in terms:
                pattern = re.compile(rf"(?i)(?<!\w){re.escape(term)}(?!\w)")
                count = len(pattern.findall(lowered))
                if not count:
                    continue
                corpus_totals[f"{corpus_name}\t{term}"] += count
                evidence[term].append(
                    {
                        "corpus": corpus_name,
                        "paper": pdf.name,
                        "path": str(pdf),
                        "count": count,
                        "contexts": contexts(
                            text,
                            term,
                            args.contexts_per_paper,
                            args.context_radius,
                        ),
                    }
                )

    payload = {
        "corpora": [{"name": name, "path": str(path)} for name, path in args.corpus],
        "terms": terms,
        "paper_count": len(papers),
        "papers": papers,
        "corpus_term_totals": [
            {"corpus": key.split("\t", 1)[0], "term": key.split("\t", 1)[1], "count": count}
            for key, count in sorted(corpus_totals.items())
        ],
        "evidence": evidence,
        "failures": failures,
        "duplicates_skipped": duplicates,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"Extracted {len(papers)} unique PDFs; skipped {len(duplicates)} duplicate titles; "
        f"{len(failures)} failures; wrote {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
