import pandas as pd
import numpy as np

class LivingDoubleAmortization:
    def __init__(self, property_value, base_market_rate=0.065, coop_points=0):
        # 1. Core Structural Splitting (10% Rule)
        self.property_value = property_value
        self.isolated_non_profit_pool = property_value * 0.10
        self.homeowner_credit_principal = property_value * 0.90
        
        # 2. Sequential Note Allocation (60/40 Split)
        self.first_note_balance = self.homeowner_credit_principal * 0.60
        self.second_note_balance = self.homeowner_credit_principal * 0.40
        
        # 3. Dynamic Interest Environment (Co-Op Mutual Rate Buy-Down)
        # Each co-op participation point permanently shaves off 0.5%
        self.effective_annual_rate = max(0.0, base_market_rate - (coop_points * 0.005))
        self.effective_monthly_rate = self.effective_annual_rate / 12.0
        
        # 4. Tracking Ledgers
        self.homeowner_equity = 0.0
        self.total_premiums_paid = 0.0
        self.ledger_history = []
        self.month_counter = 0

    def process_living_month(self, cash_payment, community_active=True):
        """
        Executes a single month lifecycle inside the living double ledger.
        Accepts variable cash inputs to simulate real-world family volatility.
        """
        self.month_counter += 1
        
        # If balances are fully paid, short-circuit processing
        if self.first_note_balance <= 0 and self.second_note_balance <= 0:
            return False
            
        # Calculate systemic interest charges across remaining credit
        outstanding_debt = self.first_note_balance + self.second_note_balance
        accrued_interest = outstanding_debt * self.effective_monthly_rate
        
        # Deduct mutual insurance safety premium (0.1% of remaining debt)
        # This builds the firewall that completely replaces predatory institutional foreclosure
        mutual_insurance_premium = outstanding_debt * 0.001 if outstanding_debt > 0 else 0
        self.total_premiums_paid += mutual_insurance_premium
        
        # Determine available liquid capital to reduce principal
        total_overhead = accrued_interest + mutual_insurance_premium
        principal_allocation = max(0.0, cash_payment - total_overhead)
        
        # Track initial states for ledger logging
        initial_first = self.first_note_balance
        initial_second = self.second_note_balance
        
        # EXECUTE AMORTIZATION PATH 1: The Primary First Note
        if self.first_note_balance > 0:
            if principal_allocation <= self.first_note_balance:
                self.first_note_balance -= principal_allocation
                self.homeowner_equity += principal_allocation
                principal_allocation = 0.0
            else:
                principal_allocation -= self.first_note_balance
                self.homeowner_equity += self.first_note_balance
                self.first_note_balance = 0.0
                
        # EXECUTE AMORTIZATION PATH 2: The Second Equity Note (with 1:1 Match)
        if self.second_note_balance > 0 and principal_allocation > 0:
            # 1:1 Co-Op Matching Triggered Natively
            effective_reduction = principal_allocation * 2
            if effective_reduction <= self.second_note_balance:
                self.second_note_balance -= effective_reduction
                self.homeowner_equity += effective_reduction
            else:
                self.homeowner_equity += self.second_note_balance
                self.second_note_balance = 0.0
                
        # Log this state into the Living Ledger History Matrix
        self.ledger_history.append({
            "Month": self.month_counter,
            "Cash_Injected": cash_payment,
            "Interest_Overhead": accrued_interest,
            "Mutual_Insurance": mutual_insurance_premium,
            "First_Note_Bal": round(self.first_note_balance, 2),
            "Second_Note_Bal": round(self.second_note_balance, 2),
            "True_Homeowner_Equity": round(self.homeowner_equity, 2)
        })
        return True

    def generate_report(self):
        return pd.DataFrame(self.ledger_history)

# ==========================================
# SIMULATION WORKLOAD: Stress Testing the Math
# ==========================================
# Family buys a $350,000 home. They rollover 401k capital to earn 13 co-op points,
# hitting a pure 0% effective interest rate wrapper.
sophia_engine = LivingDoubleAmortization(property_value=350000, base_market_rate=0.065, coop_points=13)

# Simulate 5 standard months, followed by a 3-month sudden financial crisis (0 income)
payment_stream = [1200, 1200, 1500, 1200, 1200, 0, 0, 0, 1200, 2000]

for cash in payment_stream:
    sophia_engine.process_living_month(cash_payment=cash)

# Output the verifiable data matrix
df_ledger = sophia_engine.generate_report()
print(df_ledger.to_string(index=False))
