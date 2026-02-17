"""Path planner - finds optimal reskilling routes."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List
from .skills_graph import OCCUPATIONS, TRANSITIONS, SKILLS

@dataclass
class PathResult:
    from_id: str; from_title: str; to_id: str; to_title: str
    salary_current: int; salary_target: int; salary_uplift: int; salary_uplift_pct: float
    training_months: int; training_cost: int; success_rate: float; credential: str
    shared_skills: List[str]; new_skills: List[str]
    automation_risk_reduction: float; growth_outlook_target: int; roi_score: float

def plan_paths(from_id: str) -> List[PathResult]:
    source = OCCUPATIONS.get(from_id)
    if source is None:
        return []
    results: List[PathResult] = []
    for t in TRANSITIONS:
        if t.from_id != from_id:
            continue
        dest = OCCUPATIONS.get(t.to_id)
        if dest is None:
            continue
        shared = list(set(source.skills) & set(dest.skills))
        new = [s for s in dest.skills if s not in source.skills]
        uplift = dest.median_salary - source.median_salary
        uplift_pct = uplift / max(source.median_salary, 1) * 100
        risk_reduction = source.automation_risk - dest.automation_risk
        roi = (uplift_pct * 0.30) + (t.success_rate * 100 * 0.25) + (risk_reduction * 100 * 0.25) + (max(0, 12 - t.training_months) / 12 * 100 * 0.20)
        results.append(PathResult(
            from_id=source.id, from_title=source.title, to_id=dest.id, to_title=dest.title,
            salary_current=source.median_salary, salary_target=dest.median_salary,
            salary_uplift=uplift, salary_uplift_pct=round(uplift_pct, 1),
            training_months=t.training_months, training_cost=t.training_cost,
            success_rate=t.success_rate, credential=t.credential,
            shared_skills=[SKILLS[s].name for s in shared],
            new_skills=[SKILLS[s].name for s in new if s in SKILLS],
            automation_risk_reduction=round(risk_reduction, 2),
            growth_outlook_target=dest.growth_outlook, roi_score=round(roi, 1),
        ))
    results.sort(key=lambda r: r.roi_score, reverse=True)
    return results

def plan_all() -> dict:
    out = {}
    for occ in OCCUPATIONS.values():
        paths = plan_paths(occ.id)
        if paths:
            out[occ.id] = [asdict(p) for p in paths]
    return out
