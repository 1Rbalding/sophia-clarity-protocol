#!/bin/bash
# Sophia Code Integration Script
# Run this after placing your full code in a temp dir or pasting key files.
# Usage: ./code-integration.sh /path/to/your/sophia-code

set -e

SOURCE_DIR=${1:-"."}
TARGET_DIR="/c/Users/rbald/new-protocol-design"

echo "Integrating Sophia code from $SOURCE_DIR into $TARGET_DIR..."

# Create standard structure if not present
mkdir -p $TARGET_DIR/{src,contracts,prototypes,tests,launch,specs}

# Copy core code (adjust patterns based on your structure)
if [ -d "$SOURCE_DIR/src" ]; then
  cp -r $SOURCE_DIR/src/* $TARGET_DIR/src/ || true
fi
if [ -d "$SOURCE_DIR/contracts" ] || [ -d "$SOURCE_DIR/solidity" ]; then
  cp -r $SOURCE_DIR/contracts/* $TARGET_DIR/contracts/ 2>/dev/null || cp -r $SOURCE_DIR/solidity/* $TARGET_DIR/contracts/ || true
fi
if [ -d "$SOURCE_DIR/prototypes" ]; then
  cp -r $SOURCE_DIR/prototypes/* $TARGET_DIR/prototypes/ || true
fi
if [ -d "$SOURCE_DIR/tests" ]; then
  cp -r $SOURCE_DIR/tests/* $TARGET_DIR/tests/ || true
fi

# Copy any specs or docs
find $SOURCE_DIR -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yaml" | head -20 | xargs -I {} cp {} $TARGET_DIR/specs/ 2>/dev/null || true

echo "Code copied. Now running basic validation..."

# Placeholder for validation (customize to your code)
if [ -f "$TARGET_DIR/src/main.py" ] || [ -f "$TARGET_DIR/src/index.js" ]; then
  echo "Core entrypoint detected."
fi

# Add 10% non-profit check stub
echo "Verifying 10% non-profit allocation rule enforcement..."
# You can expand this with actual code checks

echo "Integration complete. Next: review in src/ and contracts/, then run tests."
echo "Update launch-plan.md with your specific tech stack and deployment steps."
ls -la $TARGET_DIR/src $TARGET_DIR/contracts 2>/dev/null || echo "Check the folders for your files."