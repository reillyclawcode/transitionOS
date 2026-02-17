"""10-year cohort simulation across 3 policy scenarios."""
from __future__ import annotations
import random, math
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class YearState:
    year: int; poverty_rate: float; median_reskill_months: float
    placement_rate: float; stipend_utilization: float
    household_liquidity: float; employment_rate: float
    emissions_intensity: float; charter_audit_coverage: float

def _simulate_scenario(scenario: str, seed: int = 42) -> dict:
    rng = random.Random(seed)
    years = list(range(2026, 2036))
    configs = {
        "baseline":      {"pov": 12.4, "reskill": 14.0, "place": 42.0, "stip": 0.0,  "liq": 1800, "emp": 93.5, "emi": 0.42, "cha": 5.0},
        "transition_os": {"pov": 12.4, "reskill": 14.0, "place": 42.0, "stip": 15.0, "liq": 1800, "emp": 93.5, "emi": 0.42, "cha": 12.0},
        "full_stack":    {"pov": 12.4, "reskill": 14.0, "place": 42.0, "stip": 25.0, "liq": 1800, "emp": 93.5, "emi": 0.42, "cha": 18.0},
    }
    rates = {
        "baseline":      {"pov": 0.3, "reskill": -0.2, "place": 1.0, "stip": 0.5, "liq": 30, "emp": -0.15, "emi": -0.008, "cha": 1.5},
        "transition_os": {"pov": -0.6, "reskill": -0.8, "place": 3.5, "stip": 5.0, "liq": 80, "emp": 0.1, "emi": -0.015, "cha": 5.0},
        "full_stack":    {"pov": -1.0, "reskill": -1.1, "place": 5.0, "stip": 6.5, "liq": 150, "emp": 0.25, "emi": -0.022, "cha": 7.0},
    }
    c = configs[scenario]; r = rates[scenario]
    trajectory = []
    for i, yr in enumerate(years):
        noise = rng.gauss(0, 0.15)
        pov = max(2.0, c["pov"] + r["pov"] * i + noise * 0.5)
        resk = max(3.0, c["reskill"] + r["reskill"] * i + noise * 0.3)
        plac = min(98.0, max(20.0, c["place"] + r["place"] * i + noise * 2))
        stip = min(95.0, max(0.0, c["stip"] + r["stip"] * i + noise))
        liq = max(500, c["liq"] + r["liq"] * i + noise * 50)
        emp = min(99.0, max(85.0, c["emp"] + r["emp"] * i + noise * 0.2))
        emi = max(0.05, c["emi"] + r["emi"] * i + noise * 0.005)
        cha = min(100.0, max(0.0, c["cha"] + r["cha"] * i + noise))
        trajectory.append(YearState(yr, round(pov,1), round(resk,1), round(plac,1),
            round(stip,1), round(liq), round(emp,1), round(emi,3), round(cha,1)))
    return {"scenario": scenario, "years": years, "trajectory": [asdict(t) for t in trajectory], "final": asdict(trajectory[-1])}

def simulate_all() -> List[dict]:
    return [_simulate_scenario(s) for s in ["baseline", "transition_os", "full_stack"]]
