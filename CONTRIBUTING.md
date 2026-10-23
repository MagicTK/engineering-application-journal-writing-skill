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
