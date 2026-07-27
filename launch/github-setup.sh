#!/bin/bash
# GitHub Setup Script for Sophia (Clarity Protocol)
# Run this to prepare and (optionally) create/push the GitHub repo.
# Requires: git, and optionally the GitHub CLI (gh) logged in.

set -e

REPO_NAME="sophia-clarity-protocol"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="$(dirname "$SCRIPT_DIR")"

echo "Preparing GitHub setup for Sophia (Clarity Protocol)..."

cd "$WORKSPACE"

# Ensure we're on main
git checkout -B main 2>/dev/null || git checkout -b main

# Update .gitignore (idempotent)
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
.env
.env.*
pilot/
pilot_data/
.DS_Store
Thumbs.db
node_modules/
.vscode/
.idea/
*.log
dist/
build/
*.egg-info/
EOF

# Stage everything (new docs, tests, .github structure, etc.)
git add .

# Commit if there are changes
if ! git diff --cached --quiet; then
  git commit -m "Task 8 prep: GitHub community files, CI, expanded tests, updated docs and roadmap

- Added CONTRIBUTING.md, CODE_OF_CONDUCT.md
- Added .github/ issue templates + PR template
- Added basic CI workflow (runs expanded tests + pilot simulation)
- Updated README and .gitignore
- Integrated latest specs/testing_plan and prototype work
"
else
  echo "No new changes to commit."
fi

echo ""
echo "Local repo is ready."
echo ""
echo "Next steps (manual or with gh CLI):"
echo "1. gh repo create $REPO_NAME --private --source=. --remote=origin --push"
echo "   (or create manually on GitHub and: git remote add origin https://github.com/YOURUSER/$REPO_NAME.git && git push -u origin main)"
echo ""
echo "2. After push:"
echo "   - Enable Discussions"
echo "   - Add collaborators / teams"
echo "   - Create initial issues from the roadmap"
echo "   - Review and enable the CI workflow"
echo ""
echo "Repo will start private for legal/entity review, then can be made public."
echo "Update this script or README with the live URL once created."
