"""Income bridge calculator."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class BridgeResult:
    label: str; monthly_income_loss: int; training_months: int; training_cost: int
    total_gap: int; savings_coverage_months: int; unemployment_benefit: int
    civic_dividend_monthly: int; civic_dividend_total: int; out_of_pocket: int
    post_transition_salary: int; payback_months: int; net_10yr_gain: int

def compute_bridge(label: str, current_salary: int, target_salary: int,
                   training_months: int, training_cost: int,
                   monthly_expenses: int = 3200, savings_months: int = 2,
                   unemployment_monthly: int = 1400) -> BridgeResult:
    monthly_income_loss = max(0, monthly_expenses - unemployment_monthly)
    total_gap = monthly_income_loss * training_months + training_cost
    civic_monthly = max(0, monthly_income_loss - 200)
    civic_total = civic_monthly * training_months
    covered = unemployment_monthly * training_months + civic_total + (savings_months * monthly_expenses)
    out_of_pocket = max(0, total_gap - covered)
    monthly_gain = target_salary // 12 - current_salary // 12
    payback = round(total_gap / max(monthly_gain, 1)) if monthly_gain > 0 else 0
    net_10yr = monthly_gain * 120 - total_gap
    return BridgeResult(label=label, monthly_income_loss=monthly_income_loss,
        training_months=training_months, training_cost=training_cost,
        total_gap=total_gap, savings_coverage_months=savings_months,
        unemployment_benefit=unemployment_monthly, civic_dividend_monthly=civic_monthly,
        civic_dividend_total=civic_total, out_of_pocket=out_of_pocket,
        post_transition_salary=target_salary, payback_months=payback, net_10yr_gain=net_10yr)

def example_bridges() -> List[dict]:
    examples = [
        ("Truck Driver -> Logistics Coordinator",   48310, 55230, 4, 3200),
        ("Retail Cashier -> Community Health Worker",28920, 42000, 6, 4800),
        ("Data Entry -> Data Analyst",               36190, 82360, 8, 7200),
        ("Assembly Worker -> Solar Installer",       38200, 47670, 5, 4200),
        ("Bookkeeper -> Data Analyst",               45560, 82360, 6, 5400),
        ("Fast Food -> Healthcare Tech",             26080, 56420,10, 9500),
    ]
    return [asdict(compute_bridge(*e)) for e in examples]
