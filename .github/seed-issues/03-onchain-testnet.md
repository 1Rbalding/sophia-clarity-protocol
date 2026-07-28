**Title:** [Phase 1] Basic on-chain deployment tests (GrantRoles.s.sol on testnet)

**Labels:** phase-1, on-chain, foundation

**Body:**

We have `contracts/script/GrantRoles.s.sol` that defines term-limited roles, timelocks, etc.

Next steps:
- Set up a Foundry project or integrate into the existing contracts folder
- Deploy the role-granting contract to a public testnet (Sepolia recommended)
- Execute the script with realistic role assignments
- Document the deployed addresses and verification steps
- Add basic tests (Foundry or hardhat) for role granting, term expiration, and upgrade unlocks

**References:**
- `contracts/script/GrantRoles.s.sol`
- `docs/Sophia_Whitepaper.md` section on On-Chain Clarity Layer
- `specs/governance.md`

**Acceptance criteria:**
- Contract compiles and deploys cleanly on testnet
- At least one successful role-grant execution recorded
- Deployment instructions and addresses added to README or a new `contracts/README.md`

**Milestone:** Phase 1 - Foundation
