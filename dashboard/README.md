# Dashboard

This is a small Next.js + Tailwind viewer for the experiment artifacts in the sibling `../results` directory, served at policyengine.org/ai-beliefs (base path `/ai-beliefs`).

## What It Shows

- quantity-by-quantity model comparisons with scope/lab filters
- interval swaps across pooled, REML, and Bayesian methods
- run-level response inspection, with each cell's parsed runs served as JSON at `/api/runs/<quantity-slug>/<model-slug>`
- the verbatim elicitation prompts, costs, and generation pipeline (`/process`)

The app reads:

- `../results/*/summary.csv`
- `../results/*/runs.jsonl`
- `../paper/tables/*.csv` (benchmark bands, top-rate mapping)

and picks the preferred experiment for each `(model, quantity)` pair by:

1. highest `n_successful_runs`
2. highest logged token usage
3. experiment directory name (deterministic tiebreak — file mtimes are
   checkout-time on a fresh clone, so they are deliberately not consulted)

## Run

```bash
bun run dev
```

Then open [http://localhost:3000/ai-beliefs](http://localhost:3000/ai-beliefs) (the global launch config serves it on port 3179).

## Test and build

```bash
bun run lint
bun run test
bun run build
```

CI runs all three on every push. Every page and `/api/runs` payload is statically generated at build time; there is no runtime data access.

## Deploy

Pushes to `main` deploy automatically via `.github/workflows/deploy.yml`, which stages `results/`, `paper/tables/`, and `paper/paper.pdf` into this directory (they are gitignored here) and ships to the Vercel production project with the `VERCEL_TOKEN` repository secret. The manual equivalent, from this directory:

```bash
rm -rf results tables && cp -R ../results results && cp -R ../paper/tables tables && cp ../paper/paper.pdf public/paper.pdf && vercel deploy --prod --yes --scope policy-engine
```

## Notes

- The app is dependency-light on purpose. It uses `csv-parse` to read summary files and Node file-system access for the run artifacts.
- `/api/runs/[slug]/[model]` routes are prerendered (`force-static`) for every gated cell; they exist because the raw `runs.jsonl` files are too large for GitHub's inline blob view to anchor into.
