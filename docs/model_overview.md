# Dimensional Model Overview

## Architecture

`Quality Operations Analytics` uses a star-schema-oriented semantic model. Shared dimensions filter quality audits, operational audits and operational targets, while measures centralize business logic.

```text
                         Dim_Auditor
                        /     |      \
                       /      |       \
Fact_QualityAudits ----       |        ---- Fact_OperationalTargets
        |                     |                    |
        |                Fact_OperationalAudits    |
        |                     |                    |
        +------ Dim_Process --+--------------------+
        |                     |                    |
        +-------- Dim_Date ---+--------------------+

Dim_DefectType -> disconnected helper dimension used by defect/Pareto measures
_Measures      -> centralized DAX measure table
```

## Relationships

The model contains nine relationships, each from a fact foreign key to its corresponding dimension key:

| Fact | Foreign key | Dimension | Key |
|---|---|---|---|
| Fact_QualityAudits | AuditorID | Dim_Auditor | AuditorID |
| Fact_OperationalAudits | AuditorID | Dim_Auditor | AuditorID |
| Fact_OperationalTargets | AuditorID | Dim_Auditor | AuditorID |
| Fact_QualityAudits | ProcessID | Dim_Process | ProcessID |
| Fact_OperationalAudits | ProcessID | Dim_Process | ProcessID |
| Fact_OperationalTargets | ProcessID | Dim_Process | ProcessID |
| Fact_QualityAudits | AuditDateKey | Dim_Date | DateKey |
| Fact_OperationalAudits | AuditDateKey | Dim_Date | DateKey |
| Fact_OperationalTargets | WeekStartDateKey | Dim_Date | DateKey |

## Grain

- `Fact_QualityAudits`: quality-audit observation/vehicle audit grain.
- `Fact_OperationalAudits`: operational work-item/audit grain.
- `Fact_OperationalTargets`: target grain by week/process/auditor/target level/metric as supplied by the synthetic source.
- `Dim_Date`: one row per calendar date in 2025.
- `Dim_Auditor`: one row per synthetic auditor.
- `Dim_Process`: one row per analytical process.
- `Dim_DefectType`: one row per modeled defect category.

## Date behavior

`Dim_Date` contains 2025 only. `Month` is sorted by `MonthNumber`. The report uses synchronized Year, Month and WeekLabel slicers. Several analytical pages intentionally filter `IsPartialWeek = FALSE` so weekly comparisons and Pareto results use completed weeks.

## Design rationale

The model separates descriptive attributes from events and targets. This avoids embedding target logic directly in visuals and allows operational target measures to respond to date/process context. A dedicated measure table keeps DAX discoverable and simplifies documentation.
