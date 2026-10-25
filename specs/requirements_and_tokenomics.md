# Sophia Requirements & Tokenomics Specification

**Version:** 1.0  
**Date:** July 26, 2026  
**Status:** Completed (July 26, 2026)

## 1. High-Level Requirements

### 1.1 Functional Requirements (Core)
- **Governance**: One home = one vote. Physical verification of ownership/occupancy required to activate voting rights. All major actions subject to timelocks.
- **Credit Mechanics**:
  - Sequential First Note + Second Note structure.
  - 1:1 equity match on contributions.
  - Flexible paydown at homeowner's pace.
  - Hardship path + reverse option (at age 55 or when First Note paid off).
- **Insurance & Protection**:
  - Mandatory mutual/cooperative insurance fund participation.
  - Foreclosure is **never** the default outcome.
  - Protection via participation fund (insurance + rate relief).
- **Rate Relief**: Buy-down toward 0% tied directly to participation in the shared fund.
- **Non-Profit Protection Arm** (hard-coded):
  - Exactly 10% of **every** capital raise is automatically allocated to a separate Sophia non-profit entity.
  - Permitted uses only: acquisition of foreclosed/distressed homes for restoration, or sober living / safe withdrawal housing.
  - Prohibited: yield for participants, institutional control, political use.
  - Transparent reporting required (homes protected, funds used, people sheltered).
- **Founder Governance**:
  - Founder starts with governance participation ("on the governance coin" or equivalent role).
  - Fully subject to recall by homeowner vote at any time.
  - Founder commits to proactively calling for a vote upon entering retirement.

### 1.2 Non-Functional / Safeguards
- Institutional exclusion from core pool voting and control.
- No government ownership or control of the primary homeowner pool.
- Physical + timelock verification for governance actions.
- Transparent (auditable) tracking of all capital flows, including the 10% non-profit allocation.
- Low ongoing cost structure (avoid hidden gas/swap-style degradation).
- Hybrid design: real-world enforceable rules + optional on-chain elements for transparency (roles, timelocks, records).

### 1.3 Explicit Non-Goals (from Packet)
- Not a bank product.
- Not a GSE program.
- No institutional/government control of the core shelter pool.
- No trading of core pool interests in speculative fashion.
- No secrecy around the 10% non-profit rule.

## 2. Consensus Mechanism

**Primary Rule**: One home, one vote (physical verification required to register/activate a home's vote).

### Voting Mechanics (Current Design)
- Each verified home casts 1 vote (no quadratic or weighted voting at base layer to keep it simple and equal).
- Proposals include: rate changes, non-profit allocations, upgrades, founder recall, major policy.
- **Quorum**: Minimum participation (e.g., 50% of active homes) required for binding decisions.
- **Majority**: Simple majority (>50%) of votes cast for passage (adjustable via governance).
- **Timelock**: All passed votes have a mandatory delay (e.g., 7–30 days) before execution. Timelock can be on-chain or hybrid.
- **Physical Verification**: Homes must prove ownership/occupancy (off-chain process with on-chain anchoring where possible).
- **Upgrade Safeguards**: 2/3 "PUBLIC_COMPUTER_ROLE" or equivalent for certain changes (see GrantRoles.s.sol).

### On-Chain vs Hybrid
- Core voting can be off-chain (with on-chain execution hooks).
- On-chain elements (from your code): Term-limited roles, timelocks for upgrades, role-restricted actions.
- Recall votes trigger role revocation or equivalent on-chain action.

This model prevents capture seen in prior pivots while remaining practical for homeowners.

## 3. Tokenomics / Economics

### Core Principle
Participation is the path. Economics are designed around real shelter value preservation and mutual support — **not** speculative token trading or extraction.

### Down-Payment Assistance Allocation

#### Attachment
These rules are attached to the first minted Sophia coin and wrapped with the governance coin. Core homeowner rights (one-home-one-vote, participation credits, rate buy-down, mutual insurance, and the original 10% non-profit lock) remain independent. The wrap does not automatically confer additional voting power or claims on notes or reserves.

#### Source and Amount
Forty percent (40%) of net surplus is allocated to down-payment assistance.  
Net surplus equals protocol inflows minus:
- required mutual insurance reserve contributions,
- operating costs, and
- amounts required to maintain the rate buy-down at its target level.

The remaining sixty percent (60%) stays in the core protocol.

#### Permanent Reserve Floor
The protocol must always maintain mutual insurance reserves covering at least six (6) months of expected claims. This is a permanent floor. The 40% assistance allocation may only be taken from surplus above this floor. Any amount required to remain at or above the floor stays in the core protocol.

#### Assistance Pool
The 40% allocation is directed to a separate assistance pool. The original 10% non-profit lock remains completely independent and untouched.

#### Eligibility and Priority Order
Assistance is granted in the following priority order (highest to lowest):
1. Families who have never owned a home before
2. Families with no home ownership in the prior three (3) years
3. Individuals who have never owned a home before
4. Individuals with no home ownership in the prior three (3) years

#### Placement
These rules are recorded in this operating agreement / charter. Optional on-chain anchoring of the flows may be added later for transparency.

### Key Mechanisms
1. **Participation Score / Credits** (non-transferable at core)
   - Homes earn participation score through contributions to insurance fund and timely paydowns.
   - Higher score unlocks greater rate relief and protection benefits.
   - Example: Contribute > threshold → score increases → lower effective rate.

2. **Mutual Insurance Fund**
   - Mandatory contributions from participants.
   - Used to protect against default (no foreclosure as first resort).
   - Builds resilience for the community.

3. **Rate Buy-Down Engine**
   - Shared participation fund directly reduces rates for contributing homes.
   - Target: 0% effective rate where fund is sufficiently capitalized.
   - Transparent formula: rate reduction proportional to collective + individual participation.

4. **Capital Raise & 10% Non-Profit Lock (Hard Rule)**
   - On every raise: 90% to protocol pool (notes/equity), 10% strictly to separate non-profit.
   - Non-profit balance is tracked separately and auditable.
   - Uses restricted by charter/legal docs + code enforcement.

5. **Equity & Paydown**
   - 1:1 match on homeowner contributions.
   - Flexible principal reduction.
   - Hardship and reverse paths preserve dignity and optionality.

6. **Governance "Coin" / Rights**
   - Not a freely tradable speculative token.
   - Rights are tied to verified home ownership + participation.
   - Founder starts with participation rights but these are explicitly recallable by vote (as implemented in governance_stub.py and sophia_core.py).
   - Prevents the pump-dump, split, and decoupling patterns documented in VCIG/TIRXF analysis.

### Value Preservation Goals
- Direct, transparent correlation between participation and benefit (no hidden fee degradation or decoupling).
- Hard separation of non-profit (no leakage back to core pool for yield).
- Low-cost operations (hybrid model minimizes on-chain bloat where possible).
- Immutable record of 10% flows (on-chain anchoring supported).

### Risks & Mitigations (Explicit)
- **Speculation risk**: Mitigated by non-tradable core rights and focus on real housing economics.
- **Capture**: Timelocks + one-home-one-vote + founder recall + term-limited roles.
- **Liquidity/foreclosure**: Mutual insurance + non-profit safety net.
- **Regulatory**: Hybrid design + explicit licensing path for pilots.

## 4. Metrics & Success Criteria (for Prototype/Simulations)
- Capital raised vs. non-profit allocated (must maintain exact 10%).
- Homes protected via fund (vs. at-risk).
- Effective rate reduction achieved via participation.
- Recall vote execution and founder status transitions.
- Non-profit usage reporting (homes acquired, people sheltered).

## 5. Alignment with Existing Artifacts
- Presidential Packet: Letter + $1 seed + 10% rule + charter request.
- `src/sophia_core.py` + `governance_stub.py`: Demonstrates raise + 10%, recall mechanics, metrics.
- `contracts/script/GrantRoles.s.sol`: Term-limited on-chain roles.
- Whitepaper v1.4 and architecture.md: Full context.
- `specs/governance.md`: Dedicated founder recall spec.

## Next Steps (to complete this spec)
- Define exact rate buy-down formula.
- Add simulation parameters (target fund size for 0% rate, etc.).
- Integrate with the full user code from D:/Sophia when provided.
- Legal entity docs must codify the 10% lock and founder recall rule.

Participation is the path. This document + code = the foundation.

**Repository:** https://github.com/1Rbalding/sophia-clarity-protocol
