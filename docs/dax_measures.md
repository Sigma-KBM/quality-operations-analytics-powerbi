# DAX Measure Documentation

The validated model contains **55 measures** in `_Measures`. This document groups them by analytical purpose and records the business logic actually present in the PBIP master.

## Quality volume and defects

| Measure | Logic / purpose |
|---|---|
| Vehicles Audited | `DISTINCTCOUNT(Fact_QualityAudits[VehicleID])` |
| Accessories Audited | Sum of accessories inspected. |
| Accessory Defects | Sum of accessory defects. |
| Performance Defects | Sum of performance defects. |
| Functional Defects | Sum of functional defects. |
| Appearance Defects | Sum of appearance defects. |
| Parking Defects | Sum of parking defects. |
| Total Defects | Sum of total defects. |

## Quality KPIs

| Measure | Logic / purpose |
|---|---|
| DPV | `[Total Defects] / [Vehicles Audited]`. |
| ADR | `[Accessory Defects] / [Accessories Audited] * 100`. |
| DPV Target | Constant `0.14`. |
| ADR Target | Constant `3.50`. |
| DPV Variance | DPV minus DPV Target. |
| ADR Variance | ADR minus ADR Target. |
| DPV Yellow Tolerance | Maximum process-level DPV yellow tolerance from target table, ignoring auditor filters. |
| DPV Red Tolerance | Maximum process-level DPV red tolerance from target table, ignoring auditor filters. |
| ADR Yellow Tolerance | Equivalent ADR tolerance lookup. |
| ADR Red Tolerance | Equivalent ADR tolerance lookup. |
| DPV Status | Lower-is-better status: GREEN at/below target; YELLOW through yellow limit; otherwise RED. |
| ADR Status | Same lower-is-better status pattern for ADR. |

## Operational performance

| Measure | Logic / purpose |
|---|---|
| Completed Audits | Sum of `CompletedAudits`. |
| Load Line Actual | Completed audits filtered to process `Load Line`. |
| Outbound Actual | Completed audits filtered to process `Outbound`. |
| Load Line Target | Sum of process-level `Load Line Audits` targets in current context, ignoring auditor filters. |
| Outbound Target | Sum of process-level `Outbound Audits` targets in current context, ignoring auditor filters. |
| Load Line Gap | Actual minus target. |
| Outbound Gap | Actual minus target. |
| Load Line Completion % | Actual / Target. |
| Outbound Completion % | Actual / Target. |
| Load Line Yellow Tolerance | Process-level yellow tolerance from targets. |
| Load Line Red Tolerance | Process-level red tolerance from targets. |
| Outbound Yellow Tolerance | Process-level yellow tolerance from targets. |
| Outbound Red Tolerance | Process-level red tolerance from targets. |
| Load Line Status | Higher-is-better: GREEN at/above target; YELLOW through yellow threshold; otherwise RED. |
| Outbound Status | Same higher-is-better pattern for Outbound. |

## Auditor performance

| Measure | Logic / purpose |
|---|---|
| Auditor Actual | Reuses Completed Audits. |
| Auditor Target | Sum of `Auditor Audits` targets at `TargetLevel = Auditor`. |
| Auditor Gap | Actual minus target. |
| Auditor Compliance % | Actual / Target. |
| Auditor Status | GREEN >= 100%; YELLOW >= 90%; otherwise RED. |

## Overall status

| Measure | Logic / purpose |
|---|---|
| Overall Quality Operations Status | Worst-state rollup across DPV, ADR, Load Line and Outbound: any RED -> RED; else any YELLOW -> YELLOW; else GREEN. |
| Overall Quality Operations Status Color | Hex color returned from the overall status. |

## Pareto / defect helper measures

| Measure | Logic / purpose |
|---|---|
| Defects by Type | `SWITCH` over disconnected `Dim_DefectType` to return the corresponding defect measure. |
| Defect Rank | Descending dense `RANKX` across selected defect types. |
| Total Defects Selected | Sum of Defects by Type across `ALLSELECTED` defect categories. |
| Pareto Cumulative Defects | Cumulative defects through current rank. |
| Pareto Cumulative % | Cumulative defects / selected defect total. |

The final Pareto visual uses `Defects by Type` as the column series and `Pareto Cumulative %` as the line series. An empty/redundant percentage series was removed from the visual during final desktop QA; the model itself was not unnecessarily altered.

## Dynamic gauge helper measures

| Measure | Purpose |
|---|---|
| Load Line Gauge Start | Gauge minimum = 0. |
| Load Line Gauge Yellow Start | 95% of current Load Line target. |
| Load Line Gauge Green Start | Current Load Line target. |
| Load Line Gauge End | Max of target × 1.20 or actual × 1.05. |
| Outbound Gauge Start | Gauge minimum = 0. |
| Outbound Gauge Yellow Start | 95% of current Outbound target. |
| Outbound Gauge Green Start | Current Outbound target. |
| Outbound Gauge End | Max of target × 1.20 or actual × 1.05. |

These measures allow operational gauge scales to respond when the filtered target changes.
