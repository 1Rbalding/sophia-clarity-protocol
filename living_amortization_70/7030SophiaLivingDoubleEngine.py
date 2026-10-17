import pandas as pd

class SophiaSovereignLiquidityEngine:
    def __init__(self, property_value, base_market_rate=0.065, coop_points=13):
        self.property_value = property_value
        self.isolated_non_profit_pool = property_value * 0.10
        self.homeowner_credit_principal = property_value * 0.90
        
        # Initialize 70/30 Note Splits
        self.first_note_balance = self.homeowner_credit_principal * 0.70
        self.second_note_balance = self.homeowner_credit_principal * 0.30
        
        # Track Interest Environment
        self.base_market_rate = base_market_rate
        self.coop_points = coop_points
        self.update_interest_rates()
        
        # State Ledger Primitives
        self.homeowner_equity = 0.0
        self.ledger_history = []
        self.month_counter = 0

    def update_interest_rates(self):
        """Programmatically calculates the 401(k) Co-Op Rate Buy-Down."""
        self.effective_annual_rate = max(0.0, self.base_market_rate - (self.coop_points * 0.005))
        self.effective_monthly_rate = self.effective_annual_rate / 12.0

    def pull_equity(self, withdraw_amount):
        """
        Allows the homeowner to pull liquid cash out of their equity stack from Day 1.
        The withdrawn amount is re-applied to the Second Note balance.
        """
        if withdraw_amount > self.homeowner_equity:
            return f"Error: Requested ${withdraw_amount:,.2f} but only ${self.homeowner_equity:,.2f} is available."
        
        # Execute immediate sovereign equity liquidity pull
        self.homeowner_equity -= withdraw_amount
        self.second_note_balance += withdraw_amount
        
        self.ledger_history.append({
            "Month": f"{self.month_counter} (EQUITY PULL)",
            "Flat_Payment": 0,
            "Event": f"Pulled ${withdraw_amount:,.2f} Cash",
            "First_Note_Bal": round(self.first_note_balance, 2),
            "Second_Note_Bal": round(self.second_note_balance, 2),
            "True_Equity": round(self.homeowner_equity, 2)
        })
        return f"Successfully pulled ${withdraw_amount:,.2f} from equity."

    def execute_refinance(self, new_market_rate=None, new_coop_points=None):
        """
        Executes a zero-fee refinance instantly on-chain. Recalculates interest 
        structures based on current parameters without administrative friction.
        """
        if new_market_rate is not None:
            self.base_market_rate = new_market_rate
        if new_coop_points is not None:
            self.coop_points = new_coop_points
            
        self.update_interest_rates()
        
        self.ledger_history.append({
            "Month": f"{self.month_counter} (REFI RESET)",
            "Flat_Payment": 0,
            "Event": f"Refi Lock: {self.effective_annual_rate*100:.1f}% Rate",
            "First_Note_Bal": round(self.first_note_balance, 2),
            "Second_Note_Bal": round(self.second_note_balance, 2),
            "True_Equity": round(self.homeowner_equity, 2)
        })

    def process_living_month(self, cash_payment, second_note_allocation_pct=0.0):
        self.month_counter += 1
        outstanding_debt = self.first_note_balance + self.second_note_balance
        accrued_interest = outstanding_debt * self.effective_monthly_rate
        mutual_insurance_premium = outstanding_debt * 0.001 if outstanding_debt > 0 else 0
        
        net_principal_capital = max(0.0, cash_payment - (accrued_interest + mutual_insurance_premium))
        
        target_to_second = net_principal_capital * second_note_allocation_pct
        target_to_first = net_principal_capital - target_to_second
        
        if target_to_first > 0 and self.first_note_balance > 0:
            if target_to_first <= self.first_note_balance:
                self.first_note_balance -= target_to_first
                self.homeowner_equity += target_to_first
            else:
                target_to_first -= self.first_note_balance
                self.homeowner_equity += self.first_note_balance
                self.first_note_balance = 0
                target_to_second += target_to_first
                
        if target_to_second > 0 and self.second_note_balance > 0:
            effective_reduction = target_to_second * 2
            if effective_reduction <= self.second_note_balance:
                self.second_note_balance -= effective_reduction
                self.homeowner_equity += effective_reduction
            else:
                excess = (effective_reduction - self.second_note_balance) / 2
                self.homeowner_equity += self.second_note_balance
                self.second_note_balance = 0
                self.first_note_balance = max(0.0, self.first_note_balance - excess)
                self.homeowner_equity += excess

        self.ledger_history.append({
            "Month": str(self.month_counter),
            "Flat_Payment": cash_payment,
            "Event": f"Normal Routing ({int(second_note_allocation_pct*100)}% to 2nd)",
            "First_Note_Bal": round(self.first_note_balance, 2),
            "Second_Note_Bal": round(self.second_note_balance, 2),
            "True_Equity": round(self.homeowner_equity, 2)
        })

# ==========================================
# RUNNING THE LIQUIDITY SIMULATION TEST
# ==========================================
sophia_engine = SophiaSovereignLiquidityEngine(property_value=350000, base_market_rate=0.065, coop_points=13)

# Month 1 & 2: Building Initial Equity
sophia_engine.process_living_month(cash_payment=2500, second_note_allocation_pct=0.0)
sophia_engine.process_living_month(cash_payment=2500, second_note_allocation_pct=0.0)

# Day 1 Action: Homeowner pulls $3,000 liquid equity out for a sudden emergency
sophia_engine.pull_equity(withdraw_amount=3000)

# Month 3: Market rates jump, homeowner immediately executes a free Refi on the fly to protect terms
sophia_engine.execute_refinance(new_market_rate=0.080, new_coop_points=16) # Added 3 more points to negate market jump

# Month 4: Resume normal tracking under new optimized refi matrix
sophia_engine.process_living_month(cash_payment=2500, second_note_allocation_pct=0.20)

print(pd.DataFrame(sophia_engine.ledger_history).to_string(index=False))

