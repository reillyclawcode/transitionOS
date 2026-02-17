"""Generate seed data for the dashboard."""
import json, os
from .skills_graph import to_dict as graph_dict
from .path_planner import plan_all
from .income_calc import example_bridges
from .cohort_sim import simulate_all

def generate() -> dict:
    return {"graph": graph_dict(), "paths": plan_all(), "bridges": example_bridges(), "cohort": simulate_all()}

def main():
    data = generate()
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "dashboard", "public", "data")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "seed.json")
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {os.path.getsize(out_path):,} bytes -> {os.path.abspath(out_path)}")

if __name__ == "__main__":
    main()
