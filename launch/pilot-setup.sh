#!/bin/bash
# Sophia Pilot Setup Script
# Prepares a basic pilot environment based on the spec.

set -e

WORKSPACE="/c/Users/rbald/new-protocol-design"
PILOT_DIR="$WORKSPACE/pilot"

echo "Setting up Sophia Pilot..."

mkdir -p $PILOT_DIR/{homes,capital,reports}

# Create sample data structures from spec
cat > $PILOT_DIR/sample-home.json << EOF
{
  "home_id": "H001",
  "owner": "Sample Owner",
  "first_note": 150000,
  "second_note": 50000,
  "insurance_fund_contrib": 500,
  "participation_score": 1.0,
  "status": "active"
}
EOF

cat > $PILOT_DIR/capital-raise-example.md << EOF
# Sample Capital Raise
Target: $1,000,000
10% Non-Profit Allocation: $100,000 (locked for foreclosure purchases)
Net to Pool: $900,000
Homes Protected: ~6 (based on avg $150k first note)
EOF

echo "Pilot structure created in $PILOT_DIR"
echo "Next: Replace sample data with real pilot homes, integrate your code's capital engine."
ls -la $PILOT_DIR
