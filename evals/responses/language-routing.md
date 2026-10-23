# Forward-Test Review Trace: Bilingual Trigger Routing

- Evaluator: `01a01093-7a78-73e1-ae1f-4935aa7aac9c` (`Confucius`)
- Model: inherited session model; exact identifier was not exposed by the subagent tool
- Context: fresh, read-only; frontmatter only
- Tested Skills: all English canonical and Chinese mirror frontmatter descriptions

## Prompt Set And Response

1. 中文端到端论文修改请求 -> `engineering-application-journal-writing-skill-zh`。请求覆盖实验、LaTeX 和交接，并使用中文提出。
2. English end-to-end revision request -> `engineering-application-journal-writing-skill`. The request covers evidence, LaTeX, and handoff and is written in English.
3. 中文请求润色英文稿 -> `engineering-terminology-polishing-zh`。路由取决于请求语言，稿件可以是英文。
4. English request to polish Chinese prose -> `engineering-terminology-polishing`. The canonical description explicitly routes English requests regardless of manuscript language.
5. 中文混合问题/方法分类请求 -> `industrial-ai-paper-router-zh`。
6. English five-axis classification request -> `industrial-ai-paper-router`.

The evaluator was required to copy exact frontmatter names and select exactly one Skill per prompt. No English/Chinese mirror pair was selected simultaneously.

