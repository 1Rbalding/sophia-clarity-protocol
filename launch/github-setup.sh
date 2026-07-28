#!/bin/bash
# GitHub Setup Helper for Sophia (Clarity Protocol)
# Repo: https://github.com/1Rbalding/sophia-clarity-protocol

set -e

echo "Sophia (Clarity Protocol) GitHub Setup"
echo "Target: https://github.com/1Rbalding/sophia-clarity-protocol"
echo ""

cd "$(dirname "$0")/.."

echo "=== Current local state ==="
git status --short
echo ""
git log --oneline -3
echo ""

echo "=== To finish GitHub setup ==="
echo ""
echo "1. Create the repo on GitHub (if it doesn't exist yet):"
echo "   - Go to https://github.com/new"
echo "   - Name: sophia-clarity-protocol"
echo "   - Make it Private (recommended for now)"
echo "   - Do NOT initialize with README, .gitignore, or license"
echo ""
echo "2. Push the code:"
echo "   git push -u origin main"
echo ""
echo "3. After pushing, go to the repo settings and:"
echo "   - Enable Discussions"
echo "   - Add description: 'Homeowner-governed residential credit & mutual support protocol with 10% non-profit protection arm'"
echo "   - Add topics: sophia, clarity-protocol, homeowner-governance, non-profit, residential-credit"
echo ""
echo "4. Create milestones (recommended):"
echo "   - Phase 1 - Foundation"
echo "   - Phase 2 - Testing & Hardening"
echo "   - Phase 3 - Pilot Launch"
echo "   - Phase 4 - Scale & Charter"
echo ""
echo "5. Seed the initial roadmap issues:"
echo "   ./launch/seed-issues.sh"
echo ""
echo "Done. The repo is ready for launch prep."
