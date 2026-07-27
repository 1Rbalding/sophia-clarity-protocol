"""
Sophia Pilot Simulation
Expands the core stub with:
- Sequential notes (First + Second)
- Participation-based rate buy-down
- Mutual insurance claims
- Multi-home capital raises + non-profit usage
- Timelock simulation (simple)
- Governance recall demo
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from sophia_core import SophiaProtocol, Home
import time


class Timelock:
    """Simple timelock simulation for governance actions (from requirements spec)."""
    def __init__(self, delay_days=14):
        self.delay_days = delay_days
        self.proposals = []

    def propose(self, action, details):
        proposal = {
            "action": action,
            "details": details,
            "proposed_at": "now",
            "executable_after": f"+{self.delay_days} days",
            "status": "pending"
        }
        self.proposals.append(proposal)
        return f"Proposal created: {action}. Executable after {self.delay_days} days (timelock)."

    def execute(self, index=-1):
        if not self.proposals:
            return "No proposals"
        prop = self.proposals[index]
        prop["status"] = "executed"
        return f"Executed: {prop['action']} with details {prop['details']} (after timelock delay)."

    def get_status(self):
        return self.proposals


class EnhancedHome(Home):
    def __init__(self, home_id, owner, first_note, second_note, age=45):
        super().__init__(home_id, owner, first_note, second_note)
        self.second_note = second_note
        self.age = age
        self.insurance_fund = 0.0
        self.participation_score = 1.0
        self.effective_rate = 0.06  # starting 6%
        self.claims = []

    def contribute_to_fund(self, amount):
        self.insurance_fund += amount
        # Participation scoring
        self.participation_score = min(2.0, self.participation_score + (amount / 1000))
        self._update_rate()
        return self.insurance_fund

    def paydown(self, amount, note="first"):
        if note == "first" and self.first_note > 0:
            self.first_note -= amount
        elif note == "second" and self.second_note > 0:
            self.second_note -= amount
        self.paydown_history.append((note, amount))
        return {"first": self.first_note, "second": self.second_note}

    def _update_rate(self):
        # Simple rate buy-down: higher participation = lower rate
        reduction = min(0.06, (self.participation_score - 1.0) * 0.03)
        self.effective_rate = max(0.0, 0.06 - reduction)

    def file_insurance_claim(self, amount, reason="hardship"):
        if self.insurance_fund >= amount:
            self.insurance_fund -= amount
            self.claims.append({"amount": amount, "reason": reason, "status": "paid"})
            return f"Claim paid: ${amount} for {reason}"
        else:
            return "Claim denied - insufficient fund"

    def check_reverse_eligible(self):
        return self.first_note <= 0 or self.age >= 55

    def get_status(self):
        return {
            "first_note": self.first_note,
            "second_note": self.second_note,
            "insurance": self.insurance_fund,
            "participation": round(self.participation_score, 2),
            "effective_rate": f"{self.effective_rate*100:.1f}%",
            "protected": "Protected" in self.check_foreclosure(),
            "reverse_eligible": self.check_reverse_eligible()
        }

def run_pilot_simulation():
    print("=== Sophia Pilot Simulation ===\n")

    protocol = SophiaProtocol()

    # Add 5 homes with realistic starting notes
    homes_data = [
        ("H001", "Homeowner1", 180000, 60000, 42),
        ("H002", "Homeowner2", 220000, 45000, 38),
        ("H003", "Homeowner3", 150000, 30000, 51),
        ("H004", "Homeowner4", 275000, 80000, 29),
        ("H005", "Homeowner5", 195000, 55000, 57),
    ]

    for hid, owner, fn, sn, age in homes_data:
        h = EnhancedHome(hid, owner, fn, sn, age)
        protocol.add_home(h)
        # Initial participation contribution
        h.contribute_to_fund(800)

    print("Initial Homes Added. Sample status H001:")
    print(protocol.homes["H001"].get_status())

    # Capital raises with 10% non-profit (guarded)
    print("\n--- Capital Raises ---")
    r1 = protocol.raise_capital(500000)
    print("Raise 1:", r1)
    print("Non-profit balance:", protocol.non_profit_balance)

    r2 = protocol.raise_capital(750000)
    print("Raise 2:", r2)
    print("Total non-profit:", protocol.non_profit_balance)

    # Non-profit allocation (safe)
    print("\n--- Non-Profit Allocations ---")
    print(protocol.allocate_non_profit(120000, "foreclosure_purchase"))
    print(protocol.allocate_non_profit(50000, "sober_living"))
    print("Remaining non-profit:", protocol.non_profit_balance)

    # Timelock simulation (new)
    print("\n--- Timelock Simulation ---")
    print("Proposing rate relief with 14-day timelock...")
    timelock = Timelock(delay_days=14)
    print(timelock.propose("rate_relief", {"target_rate": 0.03}))
    print("... (time passes)")
    print(timelock.execute())

    # Rate buy-down & paydowns
    print("\n--- Participation & Rate Relief ---")
    for hid in ["H001", "H002", "H003"]:
        h = protocol.homes[hid]
        h.contribute_to_fund(1200)  # more participation
        h.paydown(15000)
        print(f"{hid}: {h.get_status()}")

    # Insurance claim
    print("\n--- Insurance Claim (H004) ---")
    h4 = protocol.homes["H004"]
    print(h4.file_insurance_claim(2500, "hardship"))
    print("H004 status:", h4.get_status())

    # Governance recall (founder triggers)
    print("\n--- Founder Retirement Vote ---")
    print(protocol.founder_recall_vote("founder"))
    for hid in list(protocol.homes.keys())[:3]:
        print(protocol.cast_recall_vote(hid, True))
    print(protocol.cast_recall_vote("H004", False))
    print(protocol.cast_recall_vote("H005", False))
    print(protocol.tally_recall())
    print(protocol.founder_status())

    # Final metrics
    print("\n--- Final Pilot Metrics ---")
    metrics = protocol.get_metrics()
    metrics["average_rate"] = "See individual homes"
    print(metrics)

    print("\nReverse eligible homes:")
    for hid, h in protocol.homes.items():
        if h.check_reverse_eligible():
            print(f"  {hid} ({h.owner}) - eligible")

    print("\nSimulation complete. Protocol demonstrates core rules + participation economics.")

if __name__ == "__main__":
    run_pilot_simulation()