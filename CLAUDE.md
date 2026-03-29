# CLAUDE.md

This is a **Copier template** repository. The `template/` directory is the source of truth.
`my-project/` is generated output — never edit it directly.

## Workflow for any fix

1. Edit files under `template/`
2. Regenerate: `copier copy . ./my-project --data-file my-project-answers.yml --overwrite --trust`
3. Install deps and run tests: `cd my-project && just install && just test`

## Key commands (run from repo root)

```bash
copier copy . ./my-project --data-file my-project-answers.yml --overwrite --trust
cd my-project && just install && just test
cd my-project && just test-cov
```

## Template structure

- `template/` — Copier template source (Jinja2, rendered into `my-project/`)
- `copier.yml` — Template variables and tasks
- `my-project-answers.yml` — Test answers used to generate `my-project/`
- `my-project/` — Generated project (gitignored or treated as disposable)
