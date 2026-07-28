# Sophia Governance Specification

## Core Rule
- One home, one vote.
- Physical verification required for voting rights.
- All governance actions subject to timelocks and upgrade safeguards.
- Institutional exclusion from core pool.

## Founder Governance
- Founder starts with governance participation ("on the governance coin" or equivalent role/rights in the protocol).
- This participation is fully subject to recall by homeowner vote at any time.
- Founder commits to proactively calling for a vote when entering retirement.
- This ensures democratic transition and prevents entrenchment.

## On-Chain Enforcement
- Term-limited roles via GrantRoles.s.sol (ORIGINATOR_ROLE, CLAIMS_ROLE, VERIFIER_ROLE, GUARDIAN_ROLE, etc.).
- PUBLIC_COMPUTER_ROLE for 2/3 upgrade unlocks.
- Guardian and Verifier roles for protection and verification.
- Recall/vote mechanisms can be implemented on-chain (e.g., via governance controller) or hybrid (off-chain vote triggering on-chain role revocation).

## Voting Mechanics
- Proposals: rate changes, upgrades, non-profit allocations, founder recall.
- Quorum and majority: to be defined in code (e.g., simple per-home majority or quadratic).
- Timelock: all passed votes have delay before execution.

## Transition
- Founder role is temporary by design.
- Upon retirement vote, founder governance rights are revoked; new guardians/verifiers elected or rotated per protocol.

## Alignment with Code
See contracts/script/GrantRoles.s.sol for role granting with terms.
Founder initial assignment would use similar term-limited or recallable grant.

This model directly prevents the capture and opacity issues from analyzed pivots.

**Repository:** https://github.com/1Rbalding/sophia-clarity-protocol
