# Sophia Launch Roadmap & Testing/Security Plan

**Version:** 0.1 (Draft)
**Date:** July 26, 2026

## High-Level Phases

### Phase 1: Foundation (Current - July 2026)
- [x] Core requirements, tokenomics, governance spec
- [x] Basic prototype + pilot simulation (notes, rates, insurance, 10%, recall, timelocks)
- [x] Expanded testing plan (specs/testing_plan.md)
- [x] GitHub prep: community files (CONTRIBUTING, CODE_OF_CONDUCT), issue/PR templates, CI workflow, updated setup script
- [ ] Entity formation (LLC or equivalent in pilot state)
- [ ] Full code integration from source (D:/Sophia)
- [ ] Basic on-chain deployment tests (GrantRoles.s.sol on testnet)

### Phase 2: Testing & Hardening (Aug 2026)
- Unit and integration tests for:
  - Capital raise + exact 10% non-profit flow
  - Participation scoring and rate buy-down
  - Sequential notes and paydown
  - Timelocks and recall voting
  - Non-profit allocation restrictions
- Security review:
  - Review of term-limited roles (GrantRoles)
  - Physical verification process (off-chain + anchoring)
  - No single point of failure for founder recall
  - Protection against over-allocation or negative balances (now guarded in core)
- Pilot data simulation with real-world numbers from your CSVs

### Phase 3: Pilot Launch (Q3-Q4 2026)
- Select 5-20 pilot homes (voluntary participants)
- $1 seed + matching capital
- Legal operating agreement with:
  - Hard 10% non-profit rule
  - One home one vote + physical verification
  - Founder recall mechanism
- On-chain anchoring for transparency (capital flows, roles)
- Public dashboard (simple web view of metrics)

### Phase 4: Scale & Charter (2027+)
- Request charter of recognition (Presidential Packet goal)
- Expand to more states with licensing
- Full non-profit reporting
- Optional on-chain tokenized notes/equity (with heavy safeguards)
- Community governance transition (founder steps back via vote)

## Security Considerations (High Level)
- **Governance capture**: Prevented by one-home-one-vote, timelocks, term-limited roles, recall.
- **Financial leakage**: 10% hard-coded and guarded; non-profit is separate legal entity.
- **Verification**: Physical proof required for voting rights.
- **On-chain risks**: Use audited roles (your GrantRoles.s.sol); prefer hybrid model.
- **Founder risk**: Explicit retirement vote trigger built in.
- **Regulatory**: Hybrid design to stay out of pure "security" or bank definitions where possible.

## Testing Approach
- Python pytest-style tests for core classes (add to /tests)
- Simulation-driven tests (extend pilot_simulation)
- Manual walkthrough of recall and rate relief
- On-chain: Foundry tests for GrantRoles

## Key Deliverables
- Whitepaper v1.5 (with this roadmap)
- Pilot checklist
- Legal templates with exact rules
- Public metrics page (simple)

This is the people's document. Keep building. Participation is the path.

**Note (July 2026):** Initial GitHub issues have been seeded from this roadmap (see `.github/seed-issues/`). Run `./launch/seed-issues.sh` (requires `gh` CLI) after pushing the repository to GitHub.
