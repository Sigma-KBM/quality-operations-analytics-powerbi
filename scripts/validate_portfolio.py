"""Pre-release validation for the Quality Operations Analytics portfolio."""

from __future__ import annotations

import json
import math
import re
import subprocess
import sys
import zipfile
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Missing validation dependencies. Run: python -m pip install -r requirements-dev.txt")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "data" / "quality_operations_synthetic.xlsx"
MODEL = ROOT / "powerbi" / "Quality_Operations_Analytics_1.SemanticModel" / "definition"
REPORT = ROOT / "powerbi" / "Quality_Operations_Analytics_1.Report" / "definition"

failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def close(actual: float, expected: float, tolerance: float = 1e-9) -> bool:
    return math.isclose(float(actual), float(expected), rel_tol=0, abs_tol=tolerance)


def read_sheet(name: str) -> pd.DataFrame:
    return pd.read_excel(BOOK, sheet_name=name)


def duplicate_count(frame: pd.DataFrame, columns: list[str]) -> int:
    return int(frame.duplicated(columns, keep=False).sum())


def orphan_count(
    fact: pd.DataFrame,
    foreign_key: str,
    dimension: pd.DataFrame,
    primary_key: str,
    allow_null: bool = False,
) -> int:
    values = fact[foreign_key]
    if allow_null:
        values = values.dropna()
    return int((~values.isin(set(dimension[primary_key].dropna()))).sum())


check(BOOK.exists(), f"Missing workbook: {BOOK}")
check(zipfile.is_zipfile(BOOK), "The source workbook is not a valid XLSX/ZIP package")
if failures:
    for failure in failures:
        print(f"FAIL: {failure}")
    raise SystemExit(1)

expected_sheets = {
    "Dim_Date": 365,
    "Dim_Auditor": 12,
    "Dim_Process": 3,
    "Fact_QualityAudits": 6333,
    "Fact_OperationalAudits": 11443,
    "Fact_OperationalTargets": 848,
}
tables = {name: read_sheet(name) for name in expected_sheets}

for name, expected_rows in expected_sheets.items():
    check(len(tables[name]) == expected_rows, f"{name}: expected {expected_rows} rows, found {len(tables[name])}")

date = tables["Dim_Date"]
auditor = tables["Dim_Auditor"]
process = tables["Dim_Process"]
quality = tables["Fact_QualityAudits"]
operational = tables["Fact_OperationalAudits"]
targets = tables["Fact_OperationalTargets"]

required_columns = {
    "Dim_Date": {"DateKey", "Date", "WeekLabel", "IsPartialWeek"},
    "Fact_QualityAudits": {
        "QualityAuditID", "AuditDateKey", "AuditorID", "ProcessID", "VehicleID",
        "AccessoriesAudited", "AccessoriesPassed", "AccessoryDefects", "TotalDefects",
        "PerformanceDefects", "FunctionalDefects", "AppearanceDefects", "ParkingDefects",
    },
    "Fact_OperationalAudits": {
        "OperationalAuditID", "AuditDateKey", "AuditorID", "ProcessID", "CompletedAudits",
    },
    "Fact_OperationalTargets": {
        "TargetID", "WeekStartDateKey", "ProcessID", "AuditorID", "TargetLevel",
        "MetricName", "TargetValue", "YellowTolerancePct", "RedTolerancePct",
    },
}
for name, columns in required_columns.items():
    missing = columns - set(tables[name].columns)
    check(not missing, f"{name}: missing columns {sorted(missing)}")

primary_keys = {
    "Dim_Date": ["DateKey"],
    "Dim_Auditor": ["AuditorID"],
    "Dim_Process": ["ProcessID"],
    "Fact_QualityAudits": ["QualityAuditID"],
    "Fact_OperationalAudits": ["OperationalAuditID"],
    "Fact_OperationalTargets": ["TargetID"],
}
for name, key in primary_keys.items():
    check(duplicate_count(tables[name], key) == 0, f"{name}: duplicate primary keys")
    check(not tables[name].duplicated(keep=False).any(), f"{name}: exact duplicate rows")

relationships = [
    (quality, "AuditDateKey", date, "DateKey", False, "quality/date"),
    (quality, "AuditorID", auditor, "AuditorID", False, "quality/auditor"),
    (quality, "ProcessID", process, "ProcessID", False, "quality/process"),
    (operational, "AuditDateKey", date, "DateKey", False, "operational/date"),
    (operational, "AuditorID", auditor, "AuditorID", False, "operational/auditor"),
    (operational, "ProcessID", process, "ProcessID", False, "operational/process"),
    (targets, "WeekStartDateKey", date, "DateKey", False, "targets/date"),
    (targets, "AuditorID", auditor, "AuditorID", True, "targets/auditor"),
    (targets, "ProcessID", process, "ProcessID", False, "targets/process"),
]
for fact, fk, dimension, pk, allow_null, label in relationships:
    check(orphan_count(fact, fk, dimension, pk, allow_null) == 0, f"Orphan keys in {label}")

components = ["PerformanceDefects", "FunctionalDefects", "AppearanceDefects", "ParkingDefects"]
check((quality[components].sum(axis=1) == quality["TotalDefects"]).all(), "TotalDefects does not reconcile")
check(
    ((quality["AccessoriesPassed"] + quality["AccessoryDefects"]) == quality["AccessoriesAudited"]).all(),
    "Accessory counts do not reconcile",
)
check(
    duplicate_count(targets, ["WeekStartDateKey", "ProcessID", "AuditorID", "TargetLevel", "MetricName"]) == 0,
    "Duplicate target-grain rows",
)
check(
    not (((targets["TargetLevel"] == "Auditor") & targets["AuditorID"].isna()) |
         ((targets["TargetLevel"] == "Process") & targets["AuditorID"].notna())).any(),
    "TargetLevel/AuditorID null rule is violated",
)
check(pd.to_datetime(date["Date"]).dt.year.eq(2025).all(), "Dim_Date contains dates outside 2025")
check(targets["YellowTolerancePct"].between(0, 1).all(), "YellowTolerancePct outside 0..1")
check(targets["RedTolerancePct"].between(0, 1).all(), "RedTolerancePct outside 0..1")

process_names = dict(zip(process["ProcessID"], process["ProcessName"]))
operational = operational.assign(ProcessName=operational["ProcessID"].map(process_names))


def metrics(full_weeks_only: bool) -> dict[str, float]:
    selected_dates = date.loc[~date["IsPartialWeek"]] if full_weeks_only else date
    keys = set(selected_dates["DateKey"])
    q = quality[quality["AuditDateKey"].isin(keys)]
    o = operational[operational["AuditDateKey"].isin(keys)]
    t = targets[targets["WeekStartDateKey"].isin(keys)]
    vehicles = int(q["VehicleID"].nunique())
    accessories = int(q["AccessoriesAudited"].sum())
    total_defects = int(q["TotalDefects"].sum())
    accessory_defects = int(q["AccessoryDefects"].sum())
    load_actual = int(o.loc[o["ProcessName"] == "Load Line", "CompletedAudits"].sum())
    outbound_actual = int(o.loc[o["ProcessName"] == "Outbound", "CompletedAudits"].sum())
    load_target = int(t.loc[(t["TargetLevel"] == "Process") & (t["MetricName"] == "Load Line Audits"), "TargetValue"].sum())
    outbound_target = int(t.loc[(t["TargetLevel"] == "Process") & (t["MetricName"] == "Outbound Audits"), "TargetValue"].sum())
    auditor_target = int(t.loc[(t["TargetLevel"] == "Auditor") & (t["MetricName"] == "Auditor Audits"), "TargetValue"].sum())
    result: dict[str, float] = {
        "vehicles": vehicles,
        "accessories": accessories,
        "total_defects": total_defects,
        "accessory_defects": accessory_defects,
        "dpv": total_defects / vehicles,
        "adr": accessory_defects / accessories * 100,
        "load_actual": load_actual,
        "load_target": load_target,
        "outbound_actual": outbound_actual,
        "outbound_target": outbound_target,
        "auditor_actual": int(o["CompletedAudits"].sum()),
        "auditor_target": auditor_target,
    }
    result.update({column: int(q[column].sum()) for column in components})
    return result


expected_full_year = {
    "vehicles": 6333, "accessories": 25105, "total_defects": 1113, "accessory_defects": 715,
    "dpv": 1113 / 6333, "adr": 715 / 25105 * 100,
    "load_actual": 6390, "load_target": 6014, "outbound_actual": 5053, "outbound_target": 4830,
    "auditor_actual": 11443, "auditor_target": 11889,
}
expected_complete_weeks = {
    "PerformanceDefects": 404, "FunctionalDefects": 298, "AppearanceDefects": 264, "ParkingDefects": 132,
    "load_actual": 6270, "load_target": 5888, "outbound_actual": 4949, "outbound_target": 4728,
}
for label, actual, expected in [
    ("full-year", metrics(False), expected_full_year),
    ("complete-week", metrics(True), expected_complete_weeks),
]:
    for key, expected_value in expected.items():
        check(close(actual[key], expected_value), f"{label} {key}: expected {expected_value}, found {actual[key]}")

json_files = list(REPORT.rglob("*.json"))
check(len(json_files) == 101, f"Expected 101 report JSON files after the three scope notes, found {len(json_files)}")
alt_text_hits = 0
complete_week_note_hits = 0
for path in json_files:
    try:
        raw = path.read_text(encoding="utf-8-sig")
        json.loads(raw)
        alt_text_hits += raw.count('"altText"')
        complete_week_note_hits += raw.count("Complete weeks only")
    except Exception as exc:
        failures.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")
check(alt_text_hits >= 12, f"Expected at least 12 analytical alt-text entries, found {alt_text_hits}")
check(complete_week_note_hits == 3, f"Expected three complete-week scope notes, found {complete_week_note_hits}")

page_scope = {}
for page_file in (REPORT / "pages").glob("*/page.json"):
    page = json.loads(page_file.read_text(encoding="utf-8-sig"))
    page_scope[page["displayName"]] = '"Property":"IsPartialWeek"' in json.dumps(page, separators=(",", ":"))
expected_scope = {
    "Executive Overview": False,
    "Auditor Performance": False,
    "Quality Trends": True,
    "Defect Analysis": True,
    "Operational Performance": True,
}
check(page_scope == expected_scope, f"Unexpected page partial-week policy: {page_scope}")

model_text = "\n".join(path.read_text(encoding="utf-8-sig") for path in MODEL.rglob("*.tmdl"))
for required_name in ["AccessoryDefects", "WeekLabel", "DPV", "ADR", "Overall Quality Operations Status"]:
    check(re.search(rf"\b{re.escape(required_name)}\b", model_text) is not None, f"Model is missing {required_name}")

try:
    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    sensitive = [path for path in tracked if path.lower().endswith(("/.pbi/localsettings.json", "/.pbi/cache.abf"))]
    check(not sensitive, f"Tracked Power BI cache/settings files: {sensitive}")
except (FileNotFoundError, subprocess.CalledProcessError):
    failures.append("Could not inspect tracked files with Git")

if failures:
    print(f"Validation failed with {len(failures)} issue(s):")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)

print("PASS: workbook, keys, relationships, reconciliations, KPI baselines, page scope, report JSON and PBIP hygiene")
