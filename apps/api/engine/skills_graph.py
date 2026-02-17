"""
Skills & occupation graph for TransitionOS.
20 occupations across 3 categories, 31 skills, 38+ transition paths.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Dict

@dataclass(frozen=True)
class Skill:
    id: str
    name: str
    category: str
    transferability: float

SKILLS: Dict[str, Skill] = {s.id: s for s in [
    Skill("vehicle_operation",   "Vehicle Operation",      "Physical", 0.35),
    Skill("physical_endurance",  "Physical Endurance",     "Physical", 0.50),
    Skill("manual_dexterity",    "Manual Dexterity",       "Physical", 0.55),
    Skill("equipment_operation", "Equipment Operation",    "Physical", 0.50),
    Skill("construction",        "Construction Skills",    "Physical", 0.45),
    Skill("electrical_work",     "Electrical Work",        "Physical", 0.60),
    Skill("programming",         "Programming",            "Technical", 0.90),
    Skill("data_analysis",       "Data Analysis",          "Technical", 0.88),
    Skill("machine_learning",    "Machine Learning",       "Technical", 0.80),
    Skill("network_security",    "Network Security",       "Technical", 0.78),
    Skill("database_mgmt",       "Database Management",    "Technical", 0.82),
    Skill("cloud_computing",     "Cloud Computing",        "Technical", 0.85),
    Skill("computer_literacy",   "Computer Literacy",      "Digital",  0.95),
    Skill("spreadsheets",        "Spreadsheet Proficiency","Digital",  0.80),
    Skill("digital_comms",       "Digital Communication",  "Digital",  0.90),
    Skill("software_nav",        "Software Navigation",    "Digital",  0.85),
    Skill("customer_interaction","Customer Interaction",   "Communication", 0.80),
    Skill("written_comms",       "Written Communication",  "Communication", 0.90),
    Skill("public_speaking",     "Public Speaking",        "Communication", 0.75),
    Skill("conflict_resolution", "Conflict Resolution",    "Communication", 0.80),
    Skill("empathy_care",        "Empathy & Care",         "Communication", 0.70),
    Skill("problem_solving",     "Problem Solving",        "Analytical", 0.95),
    Skill("critical_thinking",   "Critical Thinking",      "Analytical", 0.92),
    Skill("project_mgmt",        "Project Management",     "Analytical", 0.85),
    Skill("financial_analysis",  "Financial Analysis",     "Analytical", 0.78),
    Skill("research_methods",    "Research Methods",       "Analytical", 0.82),
    Skill("solar_installation",  "Solar Installation",     "Green", 0.40),
    Skill("wind_systems",        "Wind Turbine Systems",   "Green", 0.38),
    Skill("energy_auditing",     "Energy Auditing",        "Green", 0.55),
    Skill("hvac_systems",        "HVAC Systems",           "Green", 0.50),
    Skill("patient_care",        "Patient Care",           "Green", 0.45),
    Skill("ux_design",           "UX/UI Design",           "Technical", 0.75),
]}

@dataclass(frozen=True)
class Occupation:
    id: str
    title: str
    category: str
    sector: str
    median_salary: int
    automation_risk: float
    growth_outlook: int
    workers_estimate: int
    skills: List[str]

OCCUPATIONS: Dict[str, Occupation] = {o.id: o for o in [
    # At-Risk
    Occupation("truck_driver",    "Truck Driver",            "At-Risk", "Transportation",   48310, 0.79, -15, 1_900_000,
               ["vehicle_operation", "physical_endurance", "equipment_operation", "problem_solving"]),
    Occupation("retail_cashier",  "Retail Cashier",          "At-Risk", "Retail",            28920, 0.97, -22, 3_300_000,
               ["customer_interaction", "computer_literacy", "conflict_resolution"]),
    Occupation("data_entry",      "Data Entry Clerk",        "At-Risk", "Administrative",    36190, 0.99, -30, 155_000,
               ["computer_literacy", "spreadsheets", "software_nav"]),
    Occupation("assembly_worker", "Assembly Line Worker",    "At-Risk", "Manufacturing",     38200, 0.82, -12, 1_500_000,
               ["manual_dexterity", "equipment_operation", "physical_endurance", "problem_solving"]),
    Occupation("telemarketer",    "Telemarketer",            "At-Risk", "Sales",             31200, 0.99, -25, 98_000,
               ["customer_interaction", "digital_comms", "conflict_resolution"]),
    Occupation("bookkeeper",      "Bookkeeper",              "At-Risk", "Finance",           45560, 0.98, -18, 1_500_000,
               ["spreadsheets", "financial_analysis", "software_nav", "computer_literacy"]),
    Occupation("fast_food",       "Fast Food Cook",          "At-Risk", "Food Service",      26080, 0.81,  -8, 3_600_000,
               ["manual_dexterity", "physical_endurance", "customer_interaction"]),
    # Transitioning
    Occupation("customer_svc",    "Customer Service Rep",    "Transitioning", "Services",     36920, 0.55,  -5, 2_900_000,
               ["customer_interaction", "digital_comms", "conflict_resolution", "computer_literacy", "problem_solving"]),
    Occupation("admin_assistant", "Administrative Assistant", "Transitioning", "Administrative", 42080, 0.46, -8, 3_400_000,
               ["computer_literacy", "spreadsheets", "written_comms", "software_nav", "project_mgmt"]),
    Occupation("warehouse",       "Warehouse Worker",        "Transitioning", "Logistics",    34440, 0.64, -10, 1_800_000,
               ["physical_endurance", "equipment_operation", "manual_dexterity", "computer_literacy"]),
    # Growth
    Occupation("solar_installer", "Solar Panel Installer",   "Growth", "Green Energy",  47670, 0.04, 52, 330_000,
               ["solar_installation", "electrical_work", "construction", "physical_endurance", "problem_solving"]),
    Occupation("wind_tech",       "Wind Turbine Technician", "Growth", "Green Energy",  57320, 0.05, 44, 12_000,
               ["wind_systems", "electrical_work", "equipment_operation", "physical_endurance", "problem_solving"]),
    Occupation("cybersecurity",   "Cybersecurity Analyst",   "Growth", "Technology",   103590, 0.05, 35, 168_000,
               ["network_security", "programming", "critical_thinking", "research_methods", "cloud_computing"]),
    Occupation("data_analyst",    "Data Analyst",            "Growth", "Technology",    82360, 0.12, 26, 105_000,
               ["data_analysis", "programming", "spreadsheets", "critical_thinking", "problem_solving"]),
    Occupation("ux_designer",     "UX Designer",             "Growth", "Technology",    85280, 0.08, 16, 109_000,
               ["ux_design", "research_methods", "written_comms", "critical_thinking", "digital_comms"]),
    Occupation("healthcare_tech", "Healthcare Technician",   "Growth", "Healthcare",    56420, 0.09, 18, 430_000,
               ["patient_care", "computer_literacy", "empathy_care", "problem_solving", "manual_dexterity"]),
    Occupation("retrofit_spec",   "Building Retrofit Spec.", "Growth", "Green Energy",  52100, 0.04, 38, 85_000,
               ["construction", "energy_auditing", "hvac_systems", "electrical_work", "problem_solving"]),
    Occupation("ev_technician",   "EV Technician",           "Growth", "Automotive",    52460, 0.08, 30, 75_000,
               ["electrical_work", "equipment_operation", "problem_solving", "manual_dexterity", "computer_literacy"]),
    Occupation("comm_health",     "Community Health Worker", "Growth", "Healthcare",    42000, 0.04, 14, 61_000,
               ["empathy_care", "customer_interaction", "public_speaking", "conflict_resolution", "written_comms"]),
    Occupation("logistics_coord", "Logistics Coordinator",   "Growth", "Logistics",     55230, 0.18, 12, 190_000,
               ["project_mgmt", "spreadsheets", "digital_comms", "problem_solving", "software_nav"]),
]}

@dataclass(frozen=True)
class Transition:
    from_id: str
    to_id: str
    shared_skills: int
    new_skills_needed: int
    training_months: int
    training_cost: int
    success_rate: float
    credential: str

TRANSITIONS: List[Transition] = [
    # From Truck Driver
    Transition("truck_driver", "logistics_coord",  2, 3, 4,  3200, 0.88, "Logistics Management Certificate"),
    Transition("truck_driver", "wind_tech",        2, 3, 8,  8500, 0.78, "Wind Energy Technician Certificate"),
    Transition("truck_driver", "ev_technician",    2, 3, 6,  6800, 0.82, "EV Service Certification"),
    Transition("truck_driver", "solar_installer",  2, 3, 5,  4200, 0.85, "NABCEP PV Associate"),
    # From Retail Cashier
    Transition("retail_cashier", "customer_svc",   2, 2, 2,  1200, 0.92, "Customer Experience Certificate"),
    Transition("retail_cashier", "comm_health",    2, 3, 6,  4800, 0.80, "CHW State Certification"),
    Transition("retail_cashier", "admin_assistant",1, 3, 3,  2400, 0.85, "Administrative Professional Certificate"),
    Transition("retail_cashier", "healthcare_tech",1, 4, 10, 9500, 0.72, "Medical Assistant Certificate"),
    # From Data Entry Clerk
    Transition("data_entry", "data_analyst",       2, 3, 8,  7200, 0.75, "Google Data Analytics Certificate"),
    Transition("data_entry", "admin_assistant",    3, 1, 2,  1500, 0.95, "Office Administration Certificate"),
    Transition("data_entry", "logistics_coord",    2, 2, 4,  3600, 0.85, "Supply Chain Fundamentals"),
    Transition("data_entry", "ux_designer",        1, 4, 10, 8800, 0.68, "Google UX Design Certificate"),
    # From Assembly Line Worker
    Transition("assembly_worker", "solar_installer",2, 3, 5, 4200, 0.85, "NABCEP PV Associate"),
    Transition("assembly_worker", "ev_technician", 3, 2, 5,  5200, 0.84, "EV Service Certification"),
    Transition("assembly_worker", "wind_tech",     2, 3, 8,  8500, 0.76, "Wind Energy Technician Certificate"),
    Transition("assembly_worker", "retrofit_spec", 2, 3, 6,  5800, 0.80, "BPI Building Analyst"),
    # From Telemarketer
    Transition("telemarketer", "customer_svc",     2, 2, 1,  800,  0.94, "Customer Experience Certificate"),
    Transition("telemarketer", "comm_health",      2, 3, 6,  4800, 0.78, "CHW State Certification"),
    Transition("telemarketer", "admin_assistant",  1, 3, 3,  2400, 0.82, "Administrative Professional Certificate"),
    # From Bookkeeper
    Transition("bookkeeper", "data_analyst",       2, 3, 6,  5400, 0.82, "Google Data Analytics Certificate"),
    Transition("bookkeeper", "logistics_coord",    2, 2, 3,  2800, 0.90, "Supply Chain Fundamentals"),
    Transition("bookkeeper", "cybersecurity",      1, 4, 12, 14200, 0.60, "CompTIA Security+"),
    Transition("bookkeeper", "admin_assistant",    3, 1, 1,  600,  0.97, "Office Administration Certificate"),
    # From Fast Food Cook
    Transition("fast_food", "retail_cashier",      2, 0, 0,  0,    0.98, "No additional credential"),
    Transition("fast_food", "warehouse",           2, 1, 1,  500,  0.92, "Forklift Operator Certificate"),
    Transition("fast_food", "comm_health",         1, 4, 8,  5200, 0.72, "CHW State Certification"),
    Transition("fast_food", "healthcare_tech",     1, 4, 10, 9500, 0.65, "Medical Assistant Certificate"),
    # From Customer Service Rep
    Transition("customer_svc", "admin_assistant",  3, 1, 2,  1200, 0.93, "Administrative Professional Certificate"),
    Transition("customer_svc", "logistics_coord",  2, 2, 4,  3200, 0.86, "Supply Chain Fundamentals"),
    Transition("customer_svc", "comm_health",      3, 2, 4,  3800, 0.84, "CHW State Certification"),
    Transition("customer_svc", "ux_designer",      1, 4, 10, 8800, 0.62, "Google UX Design Certificate"),
    # From Administrative Assistant
    Transition("admin_assistant", "data_analyst",  2, 3, 8,  6400, 0.78, "Google Data Analytics Certificate"),
    Transition("admin_assistant", "logistics_coord",3, 1, 3, 2200, 0.90, "Supply Chain Fundamentals"),
    Transition("admin_assistant", "ux_designer",   2, 3, 8,  7600, 0.72, "Google UX Design Certificate"),
    Transition("admin_assistant", "cybersecurity", 1, 4, 12, 14200, 0.55, "CompTIA Security+"),
    # From Warehouse Worker
    Transition("warehouse", "solar_installer",     2, 3, 5,  4200, 0.83, "NABCEP PV Associate"),
    Transition("warehouse", "ev_technician",       2, 3, 6,  6000, 0.80, "EV Service Certification"),
    Transition("warehouse", "logistics_coord",     1, 3, 5,  3800, 0.82, "Logistics Management Certificate"),
    Transition("warehouse", "retrofit_spec",       2, 3, 7,  6200, 0.76, "BPI Building Analyst"),
    # Growth-to-Growth lateral
    Transition("solar_installer", "wind_tech",     3, 2, 4,  4800, 0.88, "Wind Energy Technician Certificate"),
    Transition("solar_installer", "ev_technician", 3, 1, 3,  3200, 0.90, "EV Service Certification"),
    Transition("solar_installer", "retrofit_spec", 3, 2, 4,  4000, 0.87, "BPI Building Analyst"),
    Transition("wind_tech", "solar_installer",     3, 2, 3,  3000, 0.90, "NABCEP PV Associate"),
    Transition("wind_tech", "ev_technician",       3, 1, 3,  3400, 0.88, "EV Service Certification"),
    Transition("wind_tech", "retrofit_spec",       2, 3, 5,  5200, 0.82, "BPI Building Analyst"),
    Transition("cybersecurity", "data_analyst",    3, 1, 2,  1800, 0.92, "Data Analytics Specialization"),
    Transition("cybersecurity", "ux_designer",     2, 3, 6,  5400, 0.72, "Google UX Design Certificate"),
    Transition("cybersecurity", "logistics_coord", 2, 2, 3,  2600, 0.85, "IT Supply Chain Management"),
    Transition("data_analyst", "cybersecurity",    2, 3, 8, 10200, 0.75, "CompTIA Security+"),
    Transition("data_analyst", "ux_designer",      2, 2, 5,  4200, 0.80, "Google UX Design Certificate"),
    Transition("data_analyst", "logistics_coord",  2, 1, 2,  1600, 0.92, "Supply Chain Analytics Certificate"),
    Transition("ux_designer", "data_analyst",      2, 2, 4,  3600, 0.82, "Data Analytics Specialization"),
    Transition("ux_designer", "comm_health",       2, 3, 6,  4800, 0.74, "CHW State Certification"),
    Transition("ux_designer", "cybersecurity",     1, 4, 10, 12800, 0.60, "CompTIA Security+"),
    Transition("healthcare_tech", "comm_health",   3, 2, 3,  2200, 0.90, "CHW State Certification"),
    Transition("healthcare_tech", "retrofit_spec", 1, 4, 8,  7200, 0.68, "BPI Building Analyst"),
    Transition("healthcare_tech", "data_analyst",  1, 4, 10, 8400, 0.62, "Google Data Analytics Certificate"),
    Transition("retrofit_spec", "solar_installer", 3, 1, 2,  2000, 0.92, "NABCEP PV Associate"),
    Transition("retrofit_spec", "wind_tech",       2, 2, 5,  5600, 0.80, "Wind Energy Technician Certificate"),
    Transition("retrofit_spec", "ev_technician",   2, 2, 4,  4200, 0.84, "EV Service Certification"),
    Transition("ev_technician", "solar_installer", 3, 2, 3,  3000, 0.88, "NABCEP PV Associate"),
    Transition("ev_technician", "wind_tech",       2, 3, 6,  6800, 0.78, "Wind Energy Technician Certificate"),
    Transition("ev_technician", "retrofit_spec",   2, 3, 5,  5200, 0.82, "BPI Building Analyst"),
    Transition("comm_health", "healthcare_tech",   3, 2, 6,  6400, 0.80, "Medical Assistant Certificate"),
    Transition("comm_health", "customer_svc",      3, 1, 1,   600, 0.95, "Customer Experience Certificate"),
    Transition("comm_health", "admin_assistant",   2, 3, 4,  3200, 0.82, "Administrative Professional Certificate"),
    Transition("logistics_coord", "data_analyst",  2, 3, 6,  5800, 0.78, "Data Analytics Specialization"),
    Transition("logistics_coord", "cybersecurity", 1, 4, 12, 14200, 0.55, "CompTIA Security+"),
    Transition("logistics_coord", "admin_assistant",3, 1, 1,  800, 0.95, "Office Administration Certificate"),
]

def to_dict() -> dict:
    return {
        "skills": [asdict(s) for s in SKILLS.values()],
        "occupations": [asdict(o) for o in OCCUPATIONS.values()],
        "transitions": [asdict(t) for t in TRANSITIONS],
    }
