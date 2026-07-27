"""
Sophia Governance Stub (Founder Recall Model)
Ties to on-chain term-limited roles + one-home-one-vote.

Founder starts with governance participation ("governance coin").
- Subject to recall by homeowner vote at any time.
- Founder will proactively call for a vote on retirement.

This prevents capture (aligns with VCIG/TIRXF analysis lessons).
"""

class Governance:
    def __init__(self, founder_on_governance=True):
        self.founder_on_governance = founder_on_governance
        self.homes = {}  # one home, one vote
        self.recall_votes = {}

    def add_home(self, home_id):
        self.homes[home_id] = {"vote_power": 1, "has_voted": False}

    def propose_recall(self, initiator="founder"):
        if initiator == "founder":
            print("Founder proactively calling for recall vote (retirement).")
        self.recall_votes = {h: False for h in self.homes}
        return "Recall proposal active. Homes vote now."

    def cast_vote(self, home_id, vote_for_recall):
        if home_id not in self.homes:
            return "Invalid home"
        self.homes[home_id]["has_voted"] = True
        self.recall_votes[home_id] = vote_for_recall
        return f"Vote from {home_id} recorded: {'Recall' if vote_for_recall else 'Keep'}"

    def tally_recall(self):
        votes = list(self.recall_votes.values())
        if not votes:
            return "No votes yet"
        recall_count = sum(votes)
        total = len(votes)
        if recall_count > total / 2:  # simple majority
            self.founder_on_governance = False
            return f"RECALL PASSED ({recall_count}/{total}). Founder removed from governance."
        return f"Recall failed ({recall_count}/{total}). Founder stays."

    def founder_status(self):
        status = "ON governance coin" if self.founder_on_governance else "VOTED OFF"
        return f"Founder governance status: {status}"

# Demo
gov = Governance()
for i in range(5):
    gov.add_home(f"H{i+1}")

print(gov.propose_recall("founder"))
print(gov.cast_vote("H1", True))
print(gov.cast_vote("H2", True))
print(gov.cast_vote("H3", False))
print(gov.cast_vote("H4", True))
print(gov.cast_vote("H5", False))
print(gov.tally_recall())
print(gov.founder_status())

# Simulate later retirement vote (people vote founder off)
print("\n--- Retirement vote ---")
gov2 = Governance()
for i in range(5):
    gov2.add_home(f"H{i+1}")
print(gov2.propose_recall("founder"))
for h in gov2.homes:
    gov2.cast_vote(h, True)  # unanimous for demo
print(gov2.tally_recall())
print(gov2.founder_status())