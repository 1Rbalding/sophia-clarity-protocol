# Sophia (Clarity Protocol)

**Project Name:** Sophia — Homeowner-Governed Residential Credit & Mutual Support System (with non-profit protection arm)  
**Also referred to as:** Clarity Protocol (transparent, value-preserving digitization framework)  
**Status:** Design complete; $1 initial funding committed; on-chain role scripts integrated; prototypes expanded; requirements & tokenomics defined. Ready for pilot/launch phase.  
**Date:** July 26, 2026 (Presidential Packet dated July 24, 2026)

## The Solution (from the Presidential Packet)

Sophia is the citizen-led answer to the failures we documented in the 2025-2026 microcap pivots (TIRXF as the first example, VCIG, and comparables).

It replaces the destructive patterns—pump-dump cycles, reverse splits for decoupling, hidden gas/swap fee degradation, broken stock-to-coin correlation, 401k/retail losses, and opaque Cayman-style structures—with a clean, participation-based system.

### Core Principles
- **One home, one vote** — homeowner self-governance.
- Sequential First/Second notes with mutual/cooperative insurance (foreclosure is **not** the default).
- Rate buy-down tied to participation in a shared fund (can go to 0% where supported).
- Paydown at a family’s own pace + hardship path.
- Equity with 1:1 match.
- Reverse option at age 55 or when First note is paid.
- Path from working years into retirement.
- Physical verification, timelock, upgrade safeguards; institutional exclusion from the core pool.

**Non-profit arm (locked 10% rule):** 10% of each capital raise is restricted to the separate Sophia non-profit entity for:
- Purchasing foreclosed/distressed homes for restoration, or
- Sober living / safe withdrawal housing.

The homeless and those in withdrawal deserve protection. Participation is the path.

**Founder Governance:** The founder begins with governance participation ("on the governance coin"). This is subject to recall by homeowner vote at any time. The founder will proactively call for a vote upon entering retirement, ensuring a democratic transition.

**Already begun:** $1 committed + full protocol design complete on paper and in technical specification (including on-chain Foundry scripts). Legal entity formation, licensing, and pilot-state compliance remain as prerequisites.

### What Sophia Explicitly Is Not
- Not a bank product.
- Not a GSE program.
- Not institutional or government control of the people’s shelter.
- Not a vehicle for trading the core pool.

This is the **people’s document**—once in motion, theirs to maintain.

## How This Addresses the 2022-2026 Digitization Problems
Our prior market analysis (VCIG ~$1.77B sampled turnover, $668M+ rough losses on spikes; TIRXF extreme drawdowns and splits; gas/swap fee erosion; stock-to-coin decoupling; broadening patterns; retirement money exposure) showed exactly what goes wrong when traditional assets pivot poorly.

Sophia provides the **Clarity** alternative:
- Transparent, homeowner-controlled correlation between participation and benefit (no hidden degradation).
- Built-in protections against the decoupling and extraction mechanics (splits, warrants, fee leakage).
- Direct focus on real shelter value preservation instead of narrative-driven pumps.
- Non-profit carve-out for the most vulnerable (foreclosure-to-protection).
- Term-limited and recallable governance (including founder role) to prevent capture.

## Current Phase & Progress (Active Tasks)

- [x] Problem definition & market research
- [x] Vision & solution definition (Presidential Packet + full design)
- [x] Whitepaper v1.0 (final polish, TIRXF references removed, public release version)
- [x] Architecture & governance spec
- [x] On-chain scripts integrated (GrantRoles.s.sol)
- [x] Requirements, high-level design, consensus & tokenomics (see specs/requirements_and_tokenomics.md)
- [x] Core prototype + pilot simulation (sequential notes, rate buy-down, insurance, 10% enforcement, recall)
- [x] Expanded ad-hoc testing (14 focused tests covering mechanics, edges, and integration)
- [x] GitHub setup complete (community files, CI, issue/PR templates, seed-issues script, remote configured)

See:
- `specs/testing_plan.md` for current test coverage and security checklist
- `launch/roadmap.md` for phased launch plan
- `CONTRIBUTING.md` for how to help
- [ ] Entity formation & legal structuring
- [ ] Full code integration from source + testing
- [ ] Pilot launch & first originations
- [ ] Presentation to the President / lawful charter of recognition

## Key Files & Structure
- `launch/roadmap.md` — Testing, security, and phased launch plan
- `specs/testing_plan.md` — Detailed test areas and security considerations
- `tests/test_pilot.py` — 14 ad-hoc tests (run with `python tests/test_pilot.py`)
- `CONTRIBUTING.md` — How to contribute
- `launch/github-setup.sh` — Helper script for initial GitHub repo creation
- `.github/` — Issue/PR templates + CI workflow

## GitHub & Community
- **Repo:** https://github.com/1Rbalding/sophia-clarity-protocol
- Use GitHub Issues for tasks (templates provided).
- All contributions must respect the 10% non-profit rule, one home one vote, and founder recall mechanics.
- Discussions and community building will be enabled once the repo is live.
- To seed initial issues from the roadmap: `./launch/seed-issues.sh` (requires `gh` CLI)
- `specs/requirements_and_tokenomics.md` — Explicit requirements, consensus (one-home-one-vote + timelocks), tokenomics (participation credits, rate buy-down, hard 10% non-profit lock)
- `specs/governance.md` — Founder recall mechanics
- `specs/sophia-core.md` — Core modules
- `docs/Sophia_Whitepaper.md` — v1.4 full document
- `docs/architecture.md` — Hybrid layers + on-chain roles
- `src/sophia_core.py` — Base protocol (capital raise 10%, governance)
- `src/governance_stub.py` — Founder recall implementation (RECALL PASSED demos)
- `prototypes/pilot_simulation.py` — Expanded sim: sequential notes, dynamic rates (6%→3%), insurance claims, multi-raise, non-profit usage, reverse eligibility
- `contracts/script/GrantRoles.s.sol` — Term-limited on-chain roles from your source
- `launch/` — launch-plan.md, checklist, integration scripts, github-setup.sh
- `data/examples/` — Your CSV data tables

## Prototype Demo Highlights
Run `python src/sophia_core.py` → capital raise + 10%, founder retirement vote (RECALL PASSED 3/5), metrics.

Run `python prototypes/pilot_simulation.py` → realistic 5-home pilot with rate relief, claims, non-profit allocations, recall.

## Next Immediate Actions
1. Copy full code from D:/Sophia into the workspace (use launch/code-integration.sh after copying).
2. Expand prototype further (full notes engine, timelock objects, oracle sim).
3. Run `./launch/github-setup.sh` (private repo).
4. Flesh out legal/charter language with 10% rule + founder recall.
5. Build pilot capital model + deck for Presidential meeting.

Reply with priorities:
- More code to integrate?
- Run specific simulations or on-chain scripts?
- GitHub / legal docs?
- Governance coin details or tokenomics refinements?

**Governance note (per your direction):** Founder stays on the governance coin initially but is subject to vote by the people at any time. You will ask for a vote as you go into retirement. This is now documented and executable across specs, whitepaper, architecture, and running code.

Participation is the path. Let's keep building.