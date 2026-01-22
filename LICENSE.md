# Farm Daily Logic – Public Daily JSON Pipeline (Template)

## Purpose
Generate **global (UTC) daily puzzles** for Easy/Medium/Hard, **publicly** hosted as static JSON.

## Key decisions
- Fixed counts per difficulty: Easy (12 cells/6 cards), Medium (30/15), Hard (48/24)
- Shape and regions vary daily
- Fence color is **hint-only** (NOT used in rules)
- Rules evaluate **per CELL**; cards may cross regions
- UI: **snap-to-valid**; **check** only when all cards placed
- Publish only puzzles that are:
  1) uniquely solvable (Stop-at-2)
  2) within hardness target bands

## Public endpoints
- `/api/today.json`
- `/api/latest.json`
- `/api/daily/YYYY-MM-DD/meta.json` (public)
- `/api/daily/YYYY-MM-DD/easy.json` etc.

## Setup
1) Set GitHub Actions secret `GLOBAL_SALT`.
2) Connect Cloudflare Pages with output directory `public/`.

## IMPORTANT
`generator/solver_unique.py` and `generate_candidate()` are placeholders.
Replace with your real generator + CSP solver.
