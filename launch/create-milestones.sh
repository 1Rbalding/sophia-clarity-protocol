#!/bin/bash
# Creates the four phase milestones on GitHub for Sophia (Clarity Protocol)
# Run this after the repo is pushed and you have `gh` authenticated.
#
# Usage:
#   chmod +x launch/create-milestones.sh
#   ./launch/create-milestones.sh

set -e

REPO="1Rbalding/sophia-clarity-protocol"

echo "Creating milestones for $REPO ..."

gh milestone create \
  --repo "$REPO" \
  --title "Phase 1 - Foundation" \
  --description "Core requirements, tokenomics, governance spec. Basic prototype + pilot simulation. GitHub prep, entity formation, full code integration, basic on-chain tests (GrantRoles)." \
  --due-date 2026-09-30 || echo "Phase 1 may already exist"

gh milestone create \
  --repo "$REPO" \
  --title "Phase 2 - Testing & Hardening" \
  --description "Unit & integration tests for 10% rule, participation scoring, sequential notes, timelocks, recall. Security review of roles, verification, founder recall. Pilot data simulation with real CSVs." \
  --due-date 2026-10-31 || echo "Phase 2 may already exist"

gh milestone create \
  --repo "$REPO" \
  --title "Phase 3 - Pilot Launch" \
  --description "Select 5-20 pilot homes. $1 seed + matching capital. Legal operating agreement with 10% rule + one home one vote. On-chain anchoring and public dashboard." \
  --due-date 2026-12-31 || echo "Phase 3 may already exist"

gh milestone create \
  --repo "$REPO" \
  --title "Phase 4 - Scale & Charter" \
  --description "Request charter of recognition. Multi-state expansion. Full non-profit reporting. Optional on-chain tokenized notes. Community governance transition (founder steps back via vote)." \
  --due-date 2027-12-31 || echo "Phase 4 may already exist"

echo ""
echo "Milestones created (or already existed)."
echo "You can now run ./launch/seed-issues.sh to assign issues to milestones."
