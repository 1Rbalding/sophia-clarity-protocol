"""
Sophia Core Protocol Stub
Based on Presidential Packet & specs/sophia-core.md

Key Rules:
- One home, one vote
- Sequential notes + mutual insurance (no default foreclosure)
- Rate buy-down via participation fund
- 10% non-profit allocation (locked)
- Governance with timelock, physical verification, institutional exclusion
"""

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
        # Rate buy-down logic stub
        if self.insurance_fund > 500:
            self.participation_score = min(1.5, self.participation_score + 0.1)
        return self.insurance_fund

    def paydown(self, amount):
        # Paydown at own pace
        self.paydown_history.append(amount)
        if self.first_note > 0:
            self.first_note -= amount
        return self.first_note

    def check_foreclosure(self):
        # Mutual insurance prevents default
        if self.insurance_fund > 1000 and self.participation_score > 0.8:
            return "Protected via fund"
        return "At risk - participate to protect"

class SophiaProtocol:
    def __init__(self):
        self.homes = {}
        self.capital_raised = 0.0
        self.non_profit_allocation = 0.10  # Locked 10%
        self.non_profit_balance = 0.0

    def add_home(self, home):
        self.homes[home.home_id] = home

    def raise_capital(self, amount):
        self.capital_raised += amount
        non_profit_share = amount * self.non_profit_allocation
        self.non_profit_balance += non_profit_share
        pool = amount - non_profit_share
        return {"pool": pool, "non_profit": non_profit_share}

    def allocate_non_profit(self, amount, purpose="foreclosure_purchase"):
        if purpose not in ["foreclosure_purchase", "restoration", "sober_living"]:
            raise ValueError("Invalid purpose")
        self.non_profit_balance -= amount
        return f"Allocated ${amount} to {purpose}"

    def vote(self, home_id, vote):
        # One home, one vote stub
        home = self.homes.get(home_id)
        if not home:
            return "Home not found"
        # Timelock / verification would go here
        return f"Vote recorded for {home_id}: {vote}"

    def get_metrics(self):
        protected = sum(1 for h in self.homes.values() if "Protected" in h.check_foreclosure())
        return {
            "total_homes": len(self.homes),
            "protected": protected,
            "capital_raised": self.capital_raised,
            "non_profit_balance": self.non_profit_balance
        }

# Example usage
if __name__ == "__main__":
    protocol = SophiaProtocol()
    h1 = Home("H001", "Sample Owner", 150000, 50000)
    protocol.add_home(h1)
    print(protocol.raise_capital(1000000))
    print(protocol.allocate_non_profit(100000))
    print(h1.contribute_to_fund(600))
    print(h1.check_foreclosure())
    print(protocol.get_metrics())
    print(protocol.vote("H001", "approve_rate_relief"))
