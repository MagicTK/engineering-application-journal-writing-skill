#!/usr/bin/env python3
"""Locate PDF terminology candidates, never approve terminology automatically.

Output includes copyrighted source contexts and local paths: keep it private.
Byte-identical files are deduplicated; scholarly-work identity needs manual review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


REFERENCE_HEADING = re.compile(
    r"^[ \t]*(?:(?:[IVX]+|\d+)[.)]?[ \t]+)?"
    r"(?:R[ \t]*E[ \t]*F[ \t]*E[ \t]*R[ \t]*E[ \t]*N[ \t]*C[ \t]*E[ \t]*S"
    r"|BIBLIOGRAPHY)[ \t]*$", re.I | re.M
)


def parse_corpus(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("corpus must be NAME=/absolute/path")
    name, path = value.split("=", 1)
    return name.strip(), Path(path).expanduser().resolve()


def positive_int(value: str) -> int:
    result = int(value)
    if result < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return result


def read_terms(path: Path) -> list[str]:
    return list(dict.fromkeys(
        line.strip() for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ))


def term_pattern(term: str) -> re.Pattern:
    tokens = re.split(r"[\s\-\u2010-\u2015]+", term.strip())
    joined = r"[\s\-\u2010-\u2015]+".join(map(re.escape, tokens))
    return re.compile(rf"(?<!\w){joined}(?!\w)", re.I)


def pdf_pages(path: Path) -> list[str]:
    from pypdf import PdfReader
    return [page.extract_text() or "" for page in PdfReader(str(path)).pages]


def file_sha256(path: Path) -> str:
    with path.open("rb") as source:
        digest = hashlib.sha256()
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scan_pages(pages: list[str], term: str, limit: int, radius: int) -> dict:
    pattern = term_pattern(term)
    hits = []
    reference_seen = False
    counts = {"unverified_body": 0, "references_or_later": 0}
    for page_number, raw in enumerate(pages, 1):
        heading = REFERENCE_HEADING.search(raw) if not reference_seen else None
        if heading:
            parts = [(raw[:heading.start()], "unverified_body"),
                     (raw[heading.start():], "references_or_later")]
            reference_seen = True
        else:
            parts = [(raw, "references_or_later" if reference_seen else "unverified_body")]
        for part, region in parts:
            text = re.sub(r"\s+", " ", part).strip()
            for match in pattern.finditer(text):
                counts[region] += 1
                if len(hits) < limit:
                    hits.append({
                        "pdf_page": page_number,
                        "region": region,
                        "matched_text": match.group(),
                        "context": text[max(0, match.start()-radius):match.end()+radius],
                        "status": "candidate_not_semantically_verified",
                    })
    return {
        "candidate_occurrences": sum(counts.values()),
        "region_counts": counts,
        "reference_heading_detected": reference_seen,
        "contexts": hits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", action="append", required=True, type=parse_corpus)
    parser.add_argument("--terms", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--contexts-per-paper", type=positive_int, default=3)
    parser.add_argument("--context-radius", type=positive_int, default=150)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.suffix.lower() != ".json" or output == args.terms.resolve():
        parser.error("output must be a .json file different from the terms input")
    terms = read_terms(args.terms.resolve())
    evidence = defaultdict(list)
    files, duplicates, failures = [], [], []
    seen_hashes, seen_names = {}, defaultdict(list)
    for corpus_name, corpus_dir in args.corpus:
        if not corpus_dir.is_dir():
            parser.error(f"corpus directory does not exist: {corpus_dir}")
        for pdf in sorted(corpus_dir.rglob("*.pdf")):
            try:
                digest = file_sha256(pdf)
                if digest in seen_hashes:
                    duplicates.append({"path": str(pdf), "kept_path": seen_hashes[digest],
                                       "reason": "byte_identical", "sha256": digest})
                    continue
                seen_hashes[digest] = str(pdf)
                pages = pdf_pages(pdf)
            except Exception as exc:
                failures.append({"path": str(pdf), "error": str(exc)})
                continue
            entry = {"corpus": corpus_name, "file": pdf.name, "path": str(pdf),
                     "sha256": digest, "pdf_pages": len(pages),
                     "work_identity": "requires_bibliographic_review"}
            files.append(entry)
            seen_names[pdf.stem.casefold()].append(str(pdf))
            for term in terms:
                result = scan_pages(pages, term, args.contexts_per_paper, args.context_radius)
                if result["candidate_occurrences"]:
                    evidence[term].append({**entry, **result})
    payload = {
        "schema_version": 2,
        "status": "candidate_search_only",
        "limitations": [
            "Counts are file hits, not distinct published-paper evidence or term admission.",
            "Reference-heading detection is heuristic; inspect the PDF even when it succeeds.",
            "Unverified body regions may contain titles, citation mentions or missed references.",
            "Matching ignores case and hyphen/space variants, not morphology or semantic synonyms.",
            "Different PDFs may be versions of the same work; names do not establish identity.",
            "English matches do not verify Chinese translations. Keep extracted contexts private.",
        ],
        "corpora": [{"name": n, "path": str(p)} for n, p in args.corpus],
        "terms": terms,
        "unique_file_count": len(files),
        "files": files,
        "evidence": evidence,
        "failures": failures,
        "byte_identical_files_skipped": duplicates,
        "same_name_files_retained": {n: paths for n, paths in seen_names.items() if len(paths)>1},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Searched {len(files)} distinct PDF files; {len(duplicates)} byte-identical copies skipped; "
          f"{len(failures)} failures. Candidate contexts written to {output}; admission requires review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
