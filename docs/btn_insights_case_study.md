# Building a Quality & Operations Analytics Dashboard in Power BI: From Synthetic Audit Data to Actionable KPIs

## Introduction

Quality reporting becomes much more useful when it moves beyond counting defects. Leaders also need to understand whether audits are being completed, whether operational targets are being met, how performance is changing over time, and where improvement work should be prioritized.

I built **Quality Operations Analytics** as a five-page Power BI portfolio case study to bring those questions into one decision-oriented reporting experience. The project combines quality KPIs, auditor performance, operational targets, weekly trends and Pareto prioritization using a synthetic 2025 dataset.

The objective was not simply to build attractive charts. It was to create a model in which the numbers reconcile, filters behave consistently, targets respond correctly to context, and the visual design helps the user move from executive status to root-priority analysis.

## The business problem

Quality and operations teams often work with several different reporting questions:

- Are quality defects increasing or decreasing?
- Are we above or below the accepted defect target?
- Are operational audits being completed at the expected volume?
- Which auditors are meeting their targets?
- Which defect categories account for most of the observed problems?
- Are performance signals consistent when the user changes month or week?

When those answers live in separate reports, it becomes difficult to see the relationship between quality outcomes and operational execution. This project consolidates them into five focused views:

1. Executive Overview
2. Auditor Performance
3. Quality Trends
4. Defect Analysis
5. Operational Performance

## Synthetic data and confidentiality

This project is inspired by real-world quality and operations analytics workflows, but the published dataset is **fully synthetic/anonymized**. It does not contain real employee names, customer data, supplier information, confidential facilities, internal standards or proprietary operational records.

The synthetic model contains 2025 data with 365 date rows, 12 synthetic auditors, three analytical processes, 6,333 quality-audit rows, 11,443 operational-audit rows and 848 operational-target rows.

Using synthetic data was an intentional design choice: it allows the analytical techniques and Power BI engineering work to be demonstrated publicly without exposing confidential business information.

## Data model: a star-schema approach

The semantic model separates descriptive dimensions from event and target facts.

Dimensions:

- `Dim_Date`
- `Dim_Auditor`
- `Dim_Process`
- `Dim_DefectType`

Facts:

- `Fact_QualityAudits`
- `Fact_OperationalAudits`
- `Fact_OperationalTargets`

A dedicated `_Measures` table centralizes the DAX logic.

The shared Date, Auditor and Process dimensions filter the relevant fact tables. `Dim_DefectType` is used as a helper dimension for the dynamic Pareto calculation.

This architecture makes it possible to analyze the same operating period from several perspectives without duplicating business logic in individual visuals.

## Power Query and data preparation

The source workbook contains the synthetic tables used by the model. Power Query loads and types the source data before it enters the semantic model.

One important lesson from the project was that **portability and refresh behavior should be validated in Power BI Desktop, not assumed from structurally valid project files**. During development I tested external PBIP/TMDL changes for a portable source path. The project files could be structurally valid while still failing to materialize correctly in Desktop. I therefore returned to the stable model and completed the final visual work directly in Power BI Desktop.

That recovery step became part of the engineering story: a BI project is not complete because its JSON parses; it is complete when the semantic model refreshes and the report behaves correctly in the target client.

## DAX and KPI design

### Defects per Vehicle (DPV)

DPV measures total defects relative to audited vehicles:

`DPV = Total Defects / Vehicles Audited`

The portfolio target is fixed at **0.14**, and DPV is a **lower-is-better** KPI.

### Accessory Defect Rate (ADR)

ADR measures accessory defects per 100 accessories inspected:

`ADR = Accessory Defects / Accessories Audited × 100`

The target is fixed at **3.50**, also lower-is-better.

### Operational completion

Load Line and Outbound use context-sensitive targets from the operational target fact table:

`Completion % = Actual / Target`

Unlike DPV and ADR, these are higher-is-better measures. Their target, gap, completion and status recalculate together as the user changes the date context.

### Auditor compliance

Auditor Performance compares completed audits against auditor-level targets and calculates a compliance percentage. The status logic uses:

- GREEN at or above 100%
- YELLOW from 90% to below 100%
- RED below 90%

## Executive Overview

The Executive Overview is designed to answer the first question a leader normally asks: **Where do we stand?**

It combines DPV, ADR, Load Line and Outbound with overall status plus vehicles and accessories audited. With filters reset, the validated baseline includes:

- 6,333 vehicles audited
- 25,105 accessories audited
- DPV ≈ 0.18 vs 0.14 target
- ADR ≈ 2.85 vs 3.50 target
- Load Line 6,390 vs 6,014 target
- Outbound 5,053 vs 4,830 target

The baseline overall status is RED because the rollup uses the worst state among the four principal KPIs and DPV is above target.

## Quality Trends

The Quality Trends page separates current status from temporal behavior. Weekly DPV and ADR are plotted against their fixed target lines.

The fixed targets are important analytically: when the user changes Month or Week, the actual series changes while 0.14 and 3.50 remain stable. That makes movement relative to the expected standard immediately visible.

## Auditor Performance

The Auditor Performance page moves from process-level status to individual execution. It presents:

- Auditor
- Role
- Shift
- Actual
- Target
- Gap
- Compliance %
- Status

At the reset baseline, the total is 11,443 actual audits against 11,889 target audits, a gap of -446 and 96.2% compliance, resulting in YELLOW status.

The value of this view is not ranking people for its own sake. It provides a structured way to identify where workload attainment differs and where additional investigation or support may be appropriate.

## Defect Analysis and Pareto prioritization

Counting defects is useful; prioritizing them is better.

The Defect Analysis page uses four modeled categories:

- Performance
- Functional
- Appearance
- Parking

For completed weeks in the baseline view, the counts are 404, 298, 264 and 132 respectively. The first three categories represent roughly 88% of the modeled defects.

The Pareto calculation is dynamic. It ranks the selected categories using DAX and calculates cumulative defects and cumulative percentage with `ALLSELECTED`, allowing the prioritization to recalculate when the user changes the date filters.

This transforms the page from a static distribution chart into a continuous-improvement tool: focus first on the categories responsible for the largest share of defects.

## Operational Performance

Operational Performance compares weekly Load Line and Outbound audit volume with their filtered targets and adds process/shift context.

For completed weeks in the full-year baseline:

- Load Line: 6,270 actual vs 5,888 target, approximately 106.5% completion
- Outbound: 4,949 actual vs 4,728 target, approximately 104.7% completion

The most important feature is not the baseline itself. When the user selects a different month or week, Actual, Target, Gap, Completion and Status move together. That behavior was explicitly tested during final QA.

## Dashboard design system

I wanted to avoid the appearance of a default Power BI report. The final design uses:

- light blue-gray canvas (`#EEF3FF`)
- white analytical panels
- primary blue (`#1478F2`)
- dark navy (`#162A8A`)
- dark and secondary gray typography
- green/yellow/red only for status or exceptions
- Segoe UI
- compact tab-style navigation
- synchronized Year, Month and Week filters
- consistent spacing, headers and visual hierarchy

The Executive Overview became the visual template for the remaining pages rather than redesigning every page independently.

## What the analysis shows

The synthetic case study produces several useful analytical signals:

1. **Quality and operational performance can tell different stories.** Operational audit volumes can exceed target while DPV remains above its quality target.
2. **A single overall status should not replace diagnosis.** The RED executive status quickly signals attention, but Quality Trends and Defect Analysis explain where to look next.
3. **Pareto prioritization matters.** The first three modeled defect categories account for approximately 88% of completed-week defects at baseline.
4. **Targets need the correct context.** Fixed DPV/ADR targets and dynamic operational targets serve different analytical purposes and should not be implemented identically.
5. **Dashboard QA is part of analytics engineering.** Navigation, synchronized filters, refresh behavior, status logic and numerical reconciliation were tested before the project was frozen as the final master.

## Limitations

This is a portfolio case study, not a production deployment. The dataset is synthetic and intentionally simplified. The local Excel source would normally be replaced by governed enterprise data sources in production. Some visuals may also require environment-specific approval if custom Power BI visuals are used.

The KPI definitions are specific to this synthetic case study and should not be interpreted as universal industry standards.

## Conclusion

Quality Operations Analytics demonstrates how Power BI can connect data modeling, DAX, operational targets, quality metrics, Pareto analysis and dashboard design into a single decision-support experience.

The most valuable part of the project was not any one visual. It was ensuring that the model, filters, targets, status logic and presentation all told the same story.

**Project repository:** [ADD FINAL GITHUB URL]

**LinkedIn:** https://www.linkedin.com/in/marinmanuel

If you work with quality, manufacturing, operations or BI, I would be interested to hear how you balance executive KPIs with the deeper diagnostic views needed for continuous improvement.

---

## Suggested screenshots and captions

1. **Executive Overview** — “A single executive view connects quality outcomes with operational target attainment.”
2. **Quality Trends** — “Weekly DPV and ADR remain anchored to fixed quality targets while actual performance responds to filter context.”
3. **Auditor Performance** — “Auditor-level actual vs target makes workload attainment and exceptions immediately visible.”
4. **Defect Analysis** — “Dynamic Pareto analysis converts defect counts into a prioritization sequence for improvement work.”
5. **Operational Performance** — “Context-sensitive targets allow Load Line and Outbound performance to be evaluated by month and week.”

## Final dashboard gallery

### Executive Overview
![Executive Overview](../images/01-executive-overview.png)
*Executive health view combining quality KPIs, operational target attainment, audited volume and overall status.*

### Quality Trends
![Quality Trends](../images/03-quality-trends.png)
*Weekly DPV and ADR remain anchored to fixed targets while actual performance changes over time. Completed-week analytical context can produce a slightly different aggregate from the all-record Executive Overview.*

### Auditor Performance
![Auditor Performance](../images/02-auditor-performance.png)
*Auditor-level actual versus target, gap, compliance and status expose workload attainment and exceptions.*

### Defect Analysis
![Defect Analysis](../images/04-defect-analysis.png)
*Pareto analysis shows that Performance, Functional and Appearance defects account for 88% of the full-week analytical baseline.*

### Operational Performance
![Operational Performance](../images/05-operational-performance.png)
*Load Line and Outbound actuals are evaluated against context-sensitive targets, with gap, completion and status presented alongside weekly trends.*
