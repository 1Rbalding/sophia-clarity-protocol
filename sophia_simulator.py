import pandas as pd

class SophiaProtocol:
    def __init__(self, property_value, coop_fund_points=0):
        # 10% Non-Profit Capital Isolation Rule
        self.non_profit_pool = property_value * 0.10
        self.total_credit_needed = property_value * 0.90
        
        # Split credit into Sequential Notes
        self.first_note_principal = self.total_credit_needed * 0.60
        self.second_note_principal = self.total_credit_needed * 0.40
        
        # Determine Rate Buy-Down via Co-Op Mutual Fund
        # Base market rate drops by 0.5% per co-op funding point down to 0%
        base_market_rate = 0.065
        self.effective_rate = max(0.0, base_market_rate - (coop_fund_points * 0.005))
        
        # Tracking States
        self.first_note_balance = self.first_note_principal
        self.second_note_balance = self.second_note_principal
        self.homeowner_equity = 0.0

    def process_payment(self, amount):
        """Processes payments at a family's own pace across sequential notes."""
        if amount <= 0:
            return "Payment must be greater than zero."
            
        # Allocate interest overhead based on the effective rate buy-down
        interest_charge = (self.first_note_balance + self.second_note_balance) * (self.effective_rate / 12)
        principal_payment = max(0.0, amount - interest_charge)
        
        # Pay down First Note to secure baseline shelter stability
        if self.first_note_balance > 0:
            if principal_payment <= self.first_note_balance:
                self.first_note_balance -= principal_payment
                self.homeowner_equity += principal_payment
            else:
                remainder = principal_payment - self.first_note_balance
                self.homeowner_equity += self.first_note_balance
                self.first_note_balance = 0.0
                self.process_second_note(remainder)
        else:
            self.process_second_note(principal_payment)

    def process_second_note(self, amount):
        """Applies a 1:1 match onto the Second Note to fast-track wealth."""
        if self.second_note_balance > 0:
            # 1:1 Matching Protocol via Cooperative Pool
            total_reduction = amount * 2 
            if total_reduction <= self.second_note_balance:
                self.second_note_balance -= total_reduction
                self.homeowner_equity += total_reduction
            else:
                self.homeowner_equity += self.second_note_balance
                self.second_note_balance = 0.0

# Initialize a standard $300,000 property using 13 Co-Op Fund points to hit 0% interest
sophia_system = SophiaProtocol(property_value=300000, coop_fund_points=13)
print(f"Isolated 10% Non-Profit Restoration Pool: ${sophia_system.non_profit_pool:,.2f}")
print(f"Effective Open-Source Co-Op Interest Rate: {sophia_system.effective_rate * 100}%")
