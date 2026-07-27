"""
Sophia Core Protocol Stub (integrated)
Based on Presidential Packet, specs, and governance rule:
- One home, one vote + physical/timelock verification
- Sequential notes + mutual insurance (no default foreclosure)
- Rate buy-down via participation
- Locked 10% non-profit
- Founder on governance coin; subject to people vote; founder calls retirement vote
"""

from governance_stub import Governance

class Home:
    def __init__(self, home_id, owner, first_note, second_note):
        self.home_id = home_id
        self.owner = owner
        self.first_note = first_note
        self.second_note = second_note
        self.insurance_fund = 0.0
        self.participation_score = 1.0
        self.status = "active"
        self.paydown_history = []

    def contribute_to_fund(self, amount):
        self.insurance_fund += amount
        if self.insurance_fund > 500:
            self.participation_score = min(1.5, self.participation_score + 0.1)
        return self.insurance_fund

    def paydown(self, amount):
        self.paydown_history.append(amount)
        if self.first_note > 0:
            self.first_note -= amount
        return self.first_note

    def check_foreclosure(self):
        if self.insurance_fund > 1000 and self.participation_score > 0.8:
            return "Protected via fund"
        return "At risk - participate to protect"

class SophiaProtocol:
    def __init__(self):
        self.homes = {}
        self.capital_raised = 0.0
        self.non_profit_allocation = 0.10
        self.non_profit_balance = 0.0
        self.gov = Governance(founder_on_governance=True)

    def add_home(self, home):
        self.homes[home.home_id] = home
        self.gov.add_home(home.home_id)

    def raise_capital(self, amount):
        self.capital_raised += amount
        np = amount * self.non_profit_allocation
        self.non_profit_balance += np
        return {"pool": amount - np, "non_profit": np}

    def allocate_non_profit(self, amount, purpose="foreclosure_purchase"):
        if purpose not in ["foreclosure_purchase", "restoration", "sober_living"]:
            raise ValueError("Invalid purpose")
        amount = min(amount, self.non_profit_balance)
        self.non_profit_balance -= amount
        return f"Allocated ${amount} to {purpose}"

    def vote(self, home_id, vote):
        home = self.homes.get(home_id)
        if not home:
            return "Home not found"
        # Timelock + physical verification would be enforced here
        return f"Vote recorded for {home_id}: {vote}"

    def founder_recall_vote(self, initiator="founder"):
        """Founder proactively triggers retirement vote per rule."""
        return self.gov.propose_recall(initiator)

    def cast_recall_vote(self, home_id, for_recall):
        return self.gov.cast_vote(home_id, for_recall)

    def tally_recall(self):
        return self.gov.tally_recall()

    def founder_status(self):
        return self.gov.founder_status()

    def get_metrics(self):
        protected = sum(1 for h in self.homes.values() if "Protected" in h.check_foreclosure())
        return {
            "total_homes": len(self.homes),
            "protected": protected,
            "capital_raised": self.capital_raised,
            "non_profit_balance": self.non_profit_balance,
            "founder_governance": self.founder_status()
        }

if __name__ == "__main__":
    protocol = SophiaProtocol()
    for hid, owner in [("H001", "Owner1"), ("H002", "Owner2"), ("H003", "Owner3"), ("H004", "Owner4"), ("H005", "Owner5")]:
        h = Home(hid, owner, 150000, 50000)
        protocol.add_home(h)
        h.contribute_to_fund(600)

    print("Capital raise + 10%:", protocol.raise_capital(1000000))
    print("Non-profit alloc:", protocol.allocate_non_profit(100000))

    print("\n--- Founder calls retirement vote (per rule) ---")
    print(protocol.founder_recall_vote("founder"))
    print(protocol.cast_recall_vote("H001", True))
    print(protocol.cast_recall_vote("H002", True))
    print(protocol.cast_recall_vote("H003", True))
    print(protocol.cast_recall_vote("H004", False))
    print(protocol.cast_recall_vote("H005", False))
    print(protocol.tally_recall())
    print(protocol.founder_status())

    print("\nMetrics:", protocol.get_metrics())
    print("Vote on rate relief:", protocol.vote("H001", "approve_rate_relief"))