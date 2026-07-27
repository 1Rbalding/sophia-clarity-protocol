# Sophia Testing & Security Plan (Draft)

**Version:** 0.1
**Date:** July 26, 2026
**Status:** In progress (supports Task 7)

## Goals
- Verify core mechanics match the requirements spec (one-home-one-vote, 10% non-profit, rate buy-down, sequential notes, protection, timelocks, recall).
- Ensure no over-allocation, negative balances, or governance capture.
- Hybrid (off-chain rules + optional on-chain) keeps costs low and avoids fee degradation patterns.

## Core Test Areas

### 1. Financial Mechanics
- Capital raise: exactly 10% to non-profit (guarded with min()).
- Non-profit allocation: only allowed purposes, never negative.
- Rate buy-down: participation score reduces rate from 6% toward 0%.
- Sequential notes: first + second, independent paydowns, 1:1 equity.

### 2. Insurance & Protection
- Mandatory fund contributions.
- Claims reduce fund.
- Protection flag activates on sufficient participation/fund.
- Never defaults to foreclosure.

### 3. Governance
- One home = one vote (physical verification assumed off-chain).
- Timelocks on actions.
- Founder recall: proactive call + majority vote removes founder.
- Term-limited roles (from GrantRoles.s.sol).

### 4. Timelock & Hybrid
- Simple delay simulation for proposals.
- Future: anchor key events on-chain (roles, tallies).

## Current Ad-Hoc Tests (in tests/test_pilot.py)

**Expanded to 14 focused tests** (original 6 + 8 new):
- EnhancedHome: rate relief, notes, protection.
- Timelock: propose/execute.
- Protocol: 10% split.
- Governance: recall.
- All passing in ad-hoc runs.

New tests added:
- Full paydown to zero + reverse eligibility
- Max participation rate reduction (3%)
- Non-profit allocation guard (capped)
- Multiple timelocks + status
- Recall edges (2/5 fail vs 3/5 pass)
- Insurance claim denial
- Protocol metrics
- End-to-end integration flow

## Security Checklist (KISS)
- [ ] Guard every allocation (done for non-profit).
- [ ] No tradable speculative token at core.
- [ ] Physical + timelock for vote activation.
- [ ] Founder starts "on the coin" but fully recallable.
- [ ] Separate non-profit legal entity.
- [ ] Transparent reporting (homes protected, funds used).

## Roadmap to More Tests
1. Add pytest-style tests/ directory with multiple files.
2. Simulation with 20+ homes + multi-raise scenarios.
3. Mock physical verification.
4. On-chain simulation for GrantRoles.
5. Edge cases: zero fund, full paydown, reverse eligibility.

## How to Run
- python tests/test_pilot.py (current ad-hoc)
- Extend with: python -m pytest tests/ (when implemented)

Keep it elegant, concise, and participation-driven.
