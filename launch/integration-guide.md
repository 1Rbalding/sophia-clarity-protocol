# Sophia Code Integration Guide

## Current Workspace State
- Structure created: src/, contracts/, prototypes/, tests/, specs/, launch/, docs/
- README.md and specs/sophia-core.md updated with Presidential Packet details
- Launch plan ready

## How to Integrate Your Code
1. Copy your full code base into the appropriate folders:
   - Core protocol logic → src/
   - Smart contracts / on-chain components → contracts/
   - Prototypes, scripts, or UI → prototypes/
   - Unit/integration tests → tests/

2. Key modules expected from the packet + design:
   - Governance (one-home-one-vote, timelock, physical verification)
   - Sequential notes engine
   - Mutual insurance / rate buy-down logic
   - Non-profit 10% allocation tracker (enforced)
   - Capital raise mechanics with locked rule

3. Once copied, run:
   - Review for 10% non-profit enforcement
   - Add or update tests for foreclosure avoidance and participation mechanics
   - Generate deployment scripts in launch/

## Next Commands (run after you provide code)
- We will:
  - Audit the 10% rule implementation
  - Create a simple pilot simulator
  - Build entity formation + compliance checklist
  - Prepare materials for the Presidential meeting

Please provide the code (paste key files here, give local paths, or attach main modules). We'll move everything into the workspace and start the launch sequence immediately.