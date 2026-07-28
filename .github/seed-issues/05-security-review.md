**Title:** [Phase 2] Security review of governance and recall mechanics

**Labels:** phase-2, security, governance

**Body:**

Perform a focused security review on the governance layer.

Areas to examine:
- Term-limited roles from GrantRoles.s.sol
- Founder recall flow (propose + tally)
- Timelock implementation (no bypasses)
- Physical verification assumptions (off-chain + anchoring)
- Protection against governance capture
- Separation between protocol pool and non-profit

**References:**
- `specs/governance.md`
- `contracts/script/GrantRoles.s.sol`
- `src/governance_stub.py` + integrated prototype
- Roadmap security checklist

**Acceptance criteria:**
- Written security review document (or issues + comments)
- Any critical findings turned into new issues with fixes
- Updated threat model in `docs/` or `specs/`

**Milestone:** Phase 2 - Testing & Hardening
