import pandas as pd
class SophiaLivingDoubleEngine:
    def __init__(self, property_value, base_market_rate=0.065, coop_points=13):
        # 1. Programmatic 10% Capital Isolation Fence
        self.property_value = property_value
        self.isolated_non_profit_pool = property_value * 0.10
        self.homeowner_credit_principal = property_value * 0.90
        
        # 2. Strict 70/30 Sequential Note Infrastructure
        self.first_note_balance = self.homeowner_credit_principal * 0.70
        self.second_note_balance = self.homeowner_credit_principal * 0.30
        
        # 3. Co-Op Rate Buy-Down Logic (Optimized to 0% effective rate)
        self.effective_annual_rate = max(0.0, base_market_rate - (coop_points * 0.005))
        self.effective_monthly_rate = self.effective_annual_rate / 12.0
        
        # 4. Tracking Matrices
        self.homeowner_equity = 0.0
        self.ledger_history = []
        self.month_counter = 0

    def process_living_month(self, cash_payment, second_note_allocation_pct=0.0):
        """
        Executes a payment cycle where the monthly payment stays completely flat,
        but the internal routing to the 1:1 matching note can shift dynamically.
        """
        self.month_counter += 1
        
        if self.first_note_balance <= 0 and self.second_note_balance <= 0:
            return False
            
        # Calculate systemic overheads
        outstanding_debt = self.first_note_balance + self.second_note_balance
        accrued_interest = outstanding_debt * self.effective_monthly_rate
        mutual_insurance_premium = outstanding_debt * 0.001 if outstanding_debt > 0 else 0
        
        net_principal_capital = max(0.0, cash_payment - (accrued_interest + mutual_insurance_premium))
        
        # Calculate the dynamic internal shift split
        target_to_second = net_principal_capital * second_note_allocation_pct
        target_to_first = net_principal_capital - target_to_second
        
        # ROUTING BLOCK 1: Process allocation targeted to the First Note (0% Base)
        if target_to_first > 0 and self.first_note_balance > 0:
            if target_to_first <= self.first_note_balance:
                self.first_note_balance -= target_to_first
                self.homeowner_equity += target_to_first
                target_to_first = 0
            else:
                target_to_first -= self.first_note_balance
                self.homeowner_equity += self.first_note_balance
                self.first_note_balance = 0
                target_to_second += target_to_first  # Spillover flows automatically to Second Note
                
        # ROUTING BLOCK 2: Process allocation shifted to the Second Note (1:1 Matching Equity)
        if target_to_second > 0 and self.second_note_balance > 0:
            # Apply the 1:1 Co-Op Match Multiplier
            effective_reduction = target_to_second * 2
            if effective_reduction <= self.second_note_balance:
                self.second_note_balance -= effective_reduction
                self.homeowner_equity += effective_reduction
            else:
                # If Second Note is obliterated, spillover cleans out remaining First Note
                excess = (effective_reduction - self.second_note_balance) / 2
                self.homeowner_equity += self.second_note_balance
                self.second_note_balance = 0
                self.first_note_balance = max(0.0, self.first_note_balance - excess)
                self.homeowner_equity += excess

        self.ledger_history.append({
            "Month": self.month_counter,
            "Flat_Payment": cash_payment,
            "Shift_To_Second_%": f"{second_note_allocation_pct * 100}%",
            "First_Note_Bal": round(self.first_note_balance, 2),
            "Second_Note_Bal": round(self.second_note_balance, 2),
            "True_Equity": round(self.homeowner_equity, 2)
        })
        return True

    def generate_report(self):
        return pd.DataFrame(self.ledger_history)

# Run a live test scenario over 6 months with a perfectly flat $1,500 monthly payment
sophia_system = SophiaLivingDoubleEngine(property_value=350000, base_market_rate=0.065, coop_points=13)

# Months 1-3: Conservative Stability Path (0% shifted to Second Note)
for _ in range(3):
    sophia_system.process_living_month(cash_payment=1500, second_note_allocation_pct=0.0)

# Months 4-6: Homeowner chooses to dynamically shift 40% of their payment to accelerate the 1:1 match
for _ in range(3):
    sophia_system.process_living_month(cash_payment=1500, second_note_allocation_pct=0.40)

print(sophia_system.generate_report().to_string(index=False))
