# Sophia Requirements & Tokenomics Specification

**Version:** 1.1  
**Date:** October 25, 2026  
**Status:** Updated with down-payment assistance allocation

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
  - Transparent reporting required.
- **Founder Governance**:
  - Founder starts with governance participation ("on the governance coin").
  - Fully subject to recall by homeowner vote at any time.
  - Founder commits to proactively calling for a vote upon entering retirement.

### 1.2 Non-Functional / Safeguards
- Institutional exclusion from core pool voting and control.
- No government ownership or control of the primary homeowner pool.
- Physical + timelock verification for governance actions.
- Transparent (auditable) tracking of all capital flows, including the 10% non-profit allocation.
- Low ongoing cost structure.
- Hybrid design: real-world enforceable rules + optional on-chain elements for transparency.

### 1.3 Explicit Non-Goals
- Not a bank product.
- Not a GSE program.
- No institutional/government control of the core shelter pool.
- No trading of core pool interests in speculative fashion.
- No secrecy around the 10% non-profit rule.

## 2. Consensus Mechanism
**Primary Rule**: One home, one vote (physical verification required).

- Each verified home casts 1 vote.
- Proposals: rate changes, non-profit allocations, upgrades, founder recall, major policy.
- Quorum and majority rules as defined; all passed votes subject to timelock.
- Recall votes can trigger role revocation (hybrid or on-chain).

## 3. Tokenomics / Economics

### Core Principle
Participation is the path. Economics are designed around real shelter value preservation and mutual support — not speculative token trading.

### Key Mechanisms
1. **Participation Score / Credits** (non-transferable at core)  
   Homes earn participation score through contributions and timely paydowns. Higher score unlocks greater rate relief.

2. **Mutual Insurance Fund**  
   Mandatory contributions. Used to protect against default.  
   **Permanent floor**: reserves must always cover at least 6 months of expected claims.

3. **Rate Buy-Down Engine**  
   Shared participation fund reduces rates. Transparent formula based on collective + individual participation.

4. **Capital Raise & 10% Non-Profit Lock**  
   On every raise: 90% to protocol pool, 10% strictly to separate non-profit. Non-profit balance tracked separately and auditable.

5. **Down-Payment Assistance Allocation**  
   (Attached to the first minted Sophia coin and wrapped with the governance coin. Core homeowner rights remain independent.)

   - 40% of net surplus is allocated to down-payment assistance.  
   - Net surplus = protocol inflows minus required mutual insurance reserve contributions, operating costs, and amounts required to maintain the rate buy-down at its target level.  
   - The remaining 60% stays in the core protocol.  
   - The 40% may only be taken from surplus **above** the permanent 6-month reserve floor.  
   - Directed to a **separate assistance pool**. The original 10% non-profit lock remains completely independent.  
   - Priority order (highest to lowest):  
     1. Families who have never owned a home before  
     2. Families with no home ownership in the prior 3 years  
     3. Individuals who have never owned a home before  
     4. Individuals with no home ownership in the prior 3 years  

6. **Equity & Paydown**  
   1:1 match on homeowner contributions. Flexible principal reduction. Hardship and reverse paths.

7. **Governance Coin / Rights**  
   Rights tied to verified home ownership + participation. Founder starts with participation rights but these are explicitly recallable. Not a freely tradable speculative token.

### Value Preservation Goals
- Direct correlation between participation and benefit.
- Hard separation of non-profit and assistance pools.
- Low-cost hybrid operations.
- Immutable record of 10% and assistance flows where anchored.

## 4. Metrics & Success Criteria
- Capital raised vs. non-profit allocated (exact 10%).
- Assistance pool allocations vs. priority order.
- Homes protected via fund.
- Effective rate reduction.
- Recall vote execution.
- Maintenance of 6-month reserve floor.

## 5. Alignment
- Presidential Packet, src/sophia_core.py, GrantRoles.s.sol, whitepaper, and governance.md remain the foundation.
- New assistance rules are additive and do not alter core homeowner rights or the 10% lock.

**Repository:** https://github.com/1Rbalding/sophia-clarity-protocol
