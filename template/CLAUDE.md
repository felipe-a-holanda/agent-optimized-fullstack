# CLAUDE.md

This file provides context for Claude Code when working in this repository.

## Project Overview

AI-agent-optimized full-stack monorepo with contracts-first architecture.

## Key Commands

- `just install` — Install all dependencies (run once after cloning)
- `just dev` — Start database + backend + frontend
- `just test` — Run all tests
- `just lint` — Lint all code
- `just format` — Format all code
- `just generate-client` — Regenerate TypeScript types from OpenAPI spec
- `just db-migrate "message"` — Create a new Alembic migration
- `just db-upgrade` — Apply pending migrations
- `just seed` — Seed database with admin user and sample data
- `just reset` — Reset database and reapply migrations

## Architecture Rules

Read AGENTS.md for full rules. Key points:
- OpenAPI spec is the source of truth
- Backend: Router → Service → Repository (strict layers)
- Auth: JWT tokens in httpOnly cookies, `get_current_user` dependency for protected endpoints
- Frontend: Components → Hooks (features/*/api.ts) → API Client (lib/api-client.ts)
- Never use fetch() in components
- Never define duplicate types
- Always follow the `items` reference feature pattern
- Admin panel at `/admin` (superuser only, via SQLAdmin)

## When Adding a New Feature

Follow the checklist in AGENTS.md exactly. Copy the `items` feature as template.

## Tech Stack

- Backend: Python 3.12, FastAPI, SQLAlchemy 2.0 (async), Alembic, Pydantic v2, structlog
- Auth: passlib (bcrypt), python-jose (JWT), httpOnly cookies
- Admin: SQLAdmin at `/admin`
- Frontend: Next.js 14, TypeScript, Tailwind CSS, shadcn/ui, TanStack Query, React Hook Form, Zod, Zustand
- Infra: PostgreSQL 16 (Docker), pnpm workspaces, GitHub Actions CI
- Tools: Ruff (lint/format), pytest, Vitest, pre-commit
