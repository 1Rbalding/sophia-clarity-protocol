# Sophia Architecture (Clarity Protocol)

## Overview
Sophia is a hybrid homeowner-governed protocol for residential credit and mutual support. It combines traditional mortgage mechanics with protocol-level rules for transparency, participation, and value preservation. Designed to avoid the extraction patterns observed in 2025-2026 microcap pivots (e.g., VCIG and similar microcap pivots: pump-dumps via splits/warrants, hidden fee degradation, broken stock-to-coin correlation, 401k exposure).

**Core Principle:** One home, one vote. Participation, not capture. 10% of capital flows to non-profit protection.

**Not a bank/GSE product.** Separate non-profit arm. No institutional/government control of the core pool.

**Founder Governance Rule:** The founder starts with governance participation ("on the governance coin" or equivalent role/rights). This participation is subject to recall by homeowner vote at any time. The founder will proactively call for a vote upon entering retirement, ensuring a clean, democratic transition without entrenchment.

## High-Level Architecture
- **Off-Chain Core (Traditional Finance Layer)**
  - Sequential First/Second notes
  - Mutual/cooperative insurance fund
  - Rate buy-down engine tied to participation
  - Paydown at owner's pace + hardship/reverse options
  - Physical verification of homes/ownership

- **Governance Layer (Protocol Rules)**
  - One home, one vote (physical + timelocked)
  - Upgrade safeguards and timelocks
  - Institutional exclusion from core pool
  - Hard-coded 10% non-profit allocation (enforced in code and legal docs)
  - Founder starts on governance but remains fully recallable by vote; founder commits to triggering a retirement vote

- **Non-Profit Arm (Separate Legal Entity)**
  - 10% of every raise automatically allocated
  - Permitted: foreclosed/distressed home acquisition → restoration or sober living/safe withdrawal
  - Reporting: homes acquired, funds used, people sheltered
  - No voting rights in main protocol

- **Value Preservation Mechanisms**
  - Transparent participation scoring
  - No hidden gas/swap-style fee leakage (designed for low ongoing costs)
  - Direct correlation between contribution and benefit (unlike stock-to-coin decoupling)

- **On-Chain / Digitization Layer (Optional but Supported by "Protocol" Design)**
  - Timelock smart contracts for governance upgrades
  - On-chain voting or participation tracking tokens (if code implements)
  - Immutable record of capital allocations and non-profit flows
  - Potential for tokenized notes or equity shares with 1:1 match
  - Term-limited roles (e.g., via GrantRoles.s.sol) for founder and operators; founder role subject to vote-based recall

## Data & State
- Homes: ID, owner, notes balances, insurance fund contrib, participation score, status
- Capital: Total raised, non-profit balance (locked 10%)
- Governance: Votes per home, timelock queues, founder governance status (recallable)
- Reporting: Non-profit metrics (homes protected, people sheltered)

## Security & Safeguards
- Physical verification required for voting/onboarding
- Timelocks on protocol changes
- Hard separation of non-profit entity (no core pool control)
- Transparent on-chain (or auditable off-chain) records of 10% flows
- Founder governance explicitly recallable by vote; founder will call retirement vote

## On-Chain Role Management (from Integrated Code)
The on-chain layer uses term-limited roles to enforce bounded authority:
- Roles: ORIGINATOR_ROLE, CLAIMS_ROLE, PRICE_UPDATER_ROLE, VERIFIER_ROLE, GUARDIAN_ROLE, FUND_MANAGER_ROLE, PUBLIC_COMPUTER_ROLE, etc.
- Granting via `grantRoleWithTerm` (or fallback) with explicit end dates.
- Public computer for 2/3 upgrade unlocks.
- Founder initial participation maps to a governance/guardian-style role that remains subject to homeowner recall.

## Integration with User's Code
Your full code implements the above. The GrantRoles.s.sol script (integrated from your source) handles term-limited role assignment for MortgageController, InsurancePool, Oracles, Governance, and UpgradeUnlock. The off-chain stub in src/sophia_core.py demonstrates core classes (Home, SophiaProtocol).

## Next Architecture Details Needed
- Specific consensus (if on-chain): e.g., simple majority per home or quadratic?
- Tokenomics (if any token): participation credits, governance token (founder starts on it, recallable)?
- Data storage: off-chain DB + on-chain anchors?
- Compliance hooks: state licensing, KYC/AML for pilots.
- Exact mechanism for "governance coin" / founder recall vote (on-chain or hybrid?).

This architecture directly counters the problems in the analyzed tickers by prioritizing homeowner control, locked protections, transparent value flow, and founder governance that is explicitly temporary and people-recallable.