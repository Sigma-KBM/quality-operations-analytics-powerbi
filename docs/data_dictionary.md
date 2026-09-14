# Data Dictionary

All records in this portfolio dataset are synthetic/anonymized.

## Dim_Date

| Column | Meaning |
|---|---|
| DateKey | Integer date surrogate/key used by facts. |
| Date | Calendar date. |
| Year | Calendar year. |
| Quarter | Calendar quarter. |
| MonthNumber | Numeric month used to sort Month. |
| Month | Full month name. |
| MonthShort | Abbreviated month label. |
| YearMonth | Year-month reporting label. |
| WeekOfYear | Week number. |
| WeekStartDateKey | Date key for the start of the week. |
| WeekStartDate | Calendar start date of the week. |
| DayOfMonth | Day number within month. |
| DayOfWeekNumber | Numeric day-of-week ordering. |
| DayName | Day name. |
| IsWeekend | Weekend indicator. |
| YearWeek | Year/week key or label. |
| WeekLabel | User-facing week slicer label. |
| IsPartialWeek | Identifies incomplete boundary weeks. |

## Dim_Auditor

| Column | Meaning |
|---|---|
| AuditorID | Synthetic auditor key. |
| AuditorName | Synthetic display name. |
| Role | Auditor/inspection role. |
| Shift | Assigned shift. |
| Team | Synthetic team grouping. |
| ExperienceLevel | Experience classification. |
| PrimaryProcessID | Primary process assignment. |
| IsActive | Active-status indicator. |

## Dim_Process

| Column | Meaning |
|---|---|
| ProcessID | Process key. |
| ProcessName | Process name, including Quality, Load Line and Outbound. |
| ProcessGroup | Higher-level process grouping. |
| ProcessDescription | Process description. |
| PrimaryKPI | Primary KPI associated with the process. |
| KPIDirection | Directionality such as lower-is-better where applicable. |

## Dim_DefectType

| Column | Meaning |
|---|---|
| DefectType | Defect category used by the defect/Pareto analysis. |
| SortOrder | Supporting category sort field. |

## Fact_QualityAudits

| Column | Meaning |
|---|---|
| QualityAuditID | Synthetic quality-audit identifier. |
| AuditDateKey | Date foreign key. |
| AuditorID | Auditor foreign key. |
| ProcessID | Process foreign key. |
| Shift | Shift at audit grain. |
| VehicleID | Synthetic vehicle identifier. |
| VehiclesAudited | Vehicle-audit quantity. |
| AccessoriesAudited | Number of accessories inspected. |
| AccessoriesPassed | Accessories passing inspection. |
| AccessoryDefects | Accessory defect count. |
| PerformanceDefects | Performance defect count. |
| FunctionalDefects | Functional defect count. |
| AppearanceDefects | Appearance defect count. |
| ParkingDefects | Parking defect count. |
| TotalDefects | Total modeled defects. |
| QualityResult | Quality result classification. |
| DefectSeverity | Synthetic severity classification. |
| AuditDurationMin | Audit duration in minutes. |
| DataSource | Synthetic-data provenance flag. |

## Fact_OperationalAudits

| Column | Meaning |
|---|---|
| OperationalAuditID | Synthetic operational-audit identifier. |
| AuditDateKey | Date foreign key. |
| AuditorID | Auditor foreign key. |
| ProcessID | Process foreign key. |
| Shift | Shift at audit grain. |
| WorkItemID | Synthetic work-item identifier. |
| CompletedAudits | Completed audit count. |
| UnitsReviewed | Units reviewed. |
| ExceptionsFound | Exceptions identified. |
| ReworkRequired | Rework indicator/count supplied by source. |
| ComplianceScorePct | Compliance score percentage. |
| AuditDurationMin | Audit duration in minutes. |
| AuditStatus | Operational audit status. |
| DataSource | Synthetic-data provenance flag. |

## Fact_OperationalTargets

| Column | Meaning |
|---|---|
| TargetID | Synthetic target identifier. |
| WeekStartDateKey | Week/date foreign key. |
| ProcessID | Process foreign key. |
| AuditorID | Auditor foreign key when target applies at auditor grain. |
| TargetLevel | Level at which target applies, such as Process. |
| MetricName | Metric controlled by the target. |
| TargetValue | Numeric target. |
| TargetUnit | Target unit. |
| LowerIsBetter | Directionality flag. |
| YellowTolerancePct | Yellow status tolerance. |
| RedTolerancePct | Red status tolerance. |
| Role | Role context when applicable. |
| DataSource | Synthetic-data provenance flag. |
