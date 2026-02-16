# TransitionOS

TransitionOS is a modular platform for running cities' workforce transition programs, climate investments, and civic oversight workflows from one stack. This repo is staged as a monorepo with space for a Next.js dashboard, FastAPI services, shared UI + data packages, and infrastructure glue. Nothing here is production-ready yet—it's the scaffold to start shipping.

## Monorepo layout

```
transitionOS/
├── apps/
│   ├── dashboard/        # Next.js client (actions, telemetry, viz)
│   └── api/              # FastAPI service for data + orchestration
├── packages/
│   ├── ui/               # (future) shared component library
│   └── schema/           # (future) pydantic/zod schema package
├── infra/                # IaC manifests (Terraform, Pulumi, etc.)
├── docker-compose.yml    # local dev orchestration
└── package.json          # workspace config
```

## Getting started (placeholder)

1. `npm install` (installs workspace tooling + dashboard deps)
2. `npm run dev --workspace @transitionos/dashboard`
3. `uvicorn apps.api.main:app --reload`

We'll document real steps once code lands.
