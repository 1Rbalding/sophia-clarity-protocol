#!/bin/bash
# Seed initial GitHub issues for Sophia (Clarity Protocol)
# Run this after the repo is pushed and you have `gh` CLI authenticated.
#
# Usage:
#   chmod +x launch/seed-issues.sh
#   ./launch/seed-issues.sh

set -e

REPO="1Rbalding/sophia-clarity-protocol"

echo "Seeding issues into $REPO ..."

# Function to create an issue from a file
create_issue() {
    local file=$1
    local title=$(head -1 "$file" | sed 's/\*\*Title:\*\* //')
    local body=$(tail -n +3 "$file")
    local labels=$(grep '\*\*Labels:\*\*' "$file" | sed 's/\*\*Labels:\*\* //')
    local milestone=$(grep '\*\*Milestone:\*\*' "$file" | sed 's/\*\*Milestone:\*\* //')

    echo "Creating: $title"
    gh issue create \
        --repo "$REPO" \
        --title "$title" \
        --body "$body" \
        --label "$labels" \
        --milestone "$milestone" || echo "  (milestone may not exist yet - create it manually)"
}

create_issue .github/seed-issues/01-entity-formation.md
create_issue .github/seed-issues/02-full-code-integration.md
create_issue .github/seed-issues/03-onchain-testnet.md
create_issue .github/seed-issues/04-expand-testing.md
create_issue .github/seed-issues/05-security-review.md
create_issue .github/seed-issues/06-pilot-homes.md
create_issue .github/seed-issues/07-legal-agreement.md

echo "Done. Review the created issues on GitHub."
echo "You may want to create milestones (Phase 1 - Foundation, Phase 2 - Testing & Hardening, etc.) first."