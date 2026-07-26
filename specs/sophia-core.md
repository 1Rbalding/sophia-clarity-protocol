# Sophia Core Specification (from Presidential Packet + Design)

## Overview
Sophia is a homeowner-governed residential credit and mutual-support protocol.
It is designed to prevent the extraction patterns seen in 2025-2026 public market pivots (pump-dump via splits, hidden fee degradation, stock-to-coin decoupling).

**Core Rule:** One home, one vote. Participation, not capture.

## Key Modules (to be implemented from your code)
1. **Governance**
   - One home, one vote.
   - Physical verification required.
   - Timelock on upgrades.
   - Institutional exclusion from core pool.

2. **Credit / Notes**
   - Sequential First + Second notes.
   - Equity with 1:1 match.
   - Paydown at owner's own pace.
   - Hardship path + reverse option (age 55 or First note paid).

3. **Insurance & Rate Relief**
   - Mandatory cooperative/mutual insurance.
   - Foreclosure is never the default.
   - Rate buy-down linked to shared participation fund (target 0% where funded).

4. **Non-Profit Allocation (Locked 10%)**
   - 10% of every capital raise flows to separate Sophia non-profit.
   - Permitted uses ONLY: acquire foreclosed/distressed homes → restoration or sober living / safe withdrawal housing.
   - Prohibited: private yield padding, institutional voting rights, political use.
   - Reporting: homes acquired, funds used, people sheltered.

5. **Value Preservation**
   - Designed to avoid gas/swap fee leakage and hidden degradation.
   - Transparent correlation between participation and benefit (no stock-to-coin style decoupling).

## Non-Goals (Explicit from Packet)
- No government ownership of the pool.
- No institutional control of homeowner votes.
- No exemption from licensing or honest disclosure.
- No secrecy around the 10% non-profit mandate.

## Technical Notes
- Full design and technical specification already complete (per packet).
- Your code base contains the implementation.
- Workspace ready to receive src/, contracts/, prototypes/.

Please drop the main code files or point to their locations so we can:
- Move them into the proper structure.
- Add tests and deployment scripts.
- Generate architecture diagrams.
- Build the first pilot checklist.

This is the people's document. Once started, it is theirs to maintain.
