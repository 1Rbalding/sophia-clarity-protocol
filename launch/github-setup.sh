#!/bin/bash
# GitHub Setup Script for Sophia (Clarity Protocol)
# Run after code integration. Assumes gh CLI installed and logged in.

set -e

REPO_NAME="sophia-clarity-protocol"
WORKSPACE="/c/Users/rbald/new-protocol-design"

echo "Setting up GitHub repo for Sophia..."

cd $WORKSPACE

# Init git if needed
if [ ! -d .git ]; then
  git init
  git branch -M main
fi

# Create .gitignore
cat > .gitignore << EOF
__pycache__/
*.pyc
.env
pilot/
.DS_Store
node_modules/
EOF

# Add initial files
git add .
git commit -m "Initial Sophia (Clarity Protocol) workspace: PDF solution, specs, architecture, stub prototype, launch plan" || true

# Create repo (private for legal review initially)
gh repo create $REPO_NAME --private --source=. --remote=origin --push || echo "Repo may already exist or gh not configured. Manual push needed."

echo "Repo created/pushed. Next: add collaborators, issues for tasks, enable GitHub Actions for CI."

echo "Suggested repo structure:"
ls -R | head -20

echo "Update README with GitHub link once live."
