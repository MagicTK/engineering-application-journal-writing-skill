# Contributing

Contributions should improve general engineering-application writing behavior rather than encode one manuscript, model, dataset, journal, or author's private workflow.

## Before A Change

1. Identify whether the change concerns a universal invariant, a manuscript archetype, a workflow stage, or a conditional topic playbook.
2. Keep engineering challenges, method families, tasks, object scales, and non-ordinal evidence profiles separate.
3. Add detailed domain material to `references/`, not to the core orchestrator.
4. Do not commit copyrighted papers, confidential manuscripts, proprietary data, private absolute paths, or generated result figures.

## Skill Changes

- Keep `SKILL.md` focused on decisions and procedure.
- Use clear trigger descriptions with positive and negative scope.
- Update the English canonical skill and Chinese operational mirror together.
- Preserve the same `<!-- invariant: ... -->` set in both files.
- Add or update `agents/openai.yaml` when a trigger or skill purpose changes.
- Add a routing or behavior eval for a new capability or failure mode.

## Terminology Contributions

General mechanism/module/method names need at least two distinct relevant
published journal papers with matching operational meanings, preferably three
to five for ambiguous terms. Include full phrase, source IDs/DOIs, pages,
exact-versus-equivalent use, differences and scope. Deduplicate versions of the
same work; titles and bibliography hits alone are insufficient. Verify Chinese
separately with a reliable online scholarly or terminology source and a precise
locator. Record unresolved translation/access limits. Follow the [admission
procedure](references/engineering-application-terminology-bank.md#0-admit-names-not-search-counts).

Keep one-paper names attributed, author proposals project-specific and ordinary
functional descriptions descriptive. Do not promote fictional test names or
private draft wording to general terminology. Preserve raw executed test
requests/responses when improving guidance; add a new test rather than silently
rewriting past evidence. Do not publish extracted full-text source contexts.

## Validation

Run:

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

For substantive changes, also forward-test the affected skill on at least one manuscript or research brief that was not used to design the change.

## Pull Request Notes

State:

- the failure mode or use case;
- the selected abstraction level;
- changed skills/references/templates;
- added eval cases;
- validation performed;
- any bilingual or backward-compatibility impact.
