# QOA PBIP Reconciliation - 2026-09-13

This repaired package uses the known-functional `qoa_portfolio(1)` PBIP/report/semantic-model as the source of truth and places it into the GitHub repository structure.

## Repairs applied

1. Restored the functional `Dim_Date` schema, including `YearWeek`, `WeekLabel`, and `IsPartialWeek`.
2. Restored the original report slicer references so the Select Week slicer uses `Dim_Date[WeekLabel]` and the original synchronized week slicer behavior.
3. Restored the functional `AccessoryDefects` column and original `Accessory Defects` measure.
4. Restored the original functional `Fact_OperationalTargets` model/data and the target measures used by the working dashboard.
5. Restored the valid source workbook `data/quality_operations_synthetic.xlsx`; the previously corrupted GitHub workbook is replaced.
6. Updated the restored Power Query source paths from the old portfolio path to the GitHub working path:
   `C:\qoa_portfolio\data\quality_operations_synthetic.xlsx`
7. Restored the functional report definition/pages so the repaired package is not dependent on the damaged GitHub visual metadata.

## Intentional baseline choice

The functional original PBIP was used as the authoritative baseline rather than attempting to merge individual DAX/report changes. This avoids introducing additional differences into a report whose known-good behavior has already been demonstrated.

## Validation performed

- `Dim_Date` contains `WeekLabel`, `YearWeek`, and `IsPartialWeek`.
- The restored report definition references `Dim_Date.WeekLabel` for the week slicers.
- `Fact_QualityAudits` contains `AccessoryDefects`.
- `Accessory Defects` measure references `Fact_QualityAudits[AccessoryDefects]`.
- The restored source workbook is a valid XLSX and contains the expected six model tables.
- The PBIP JSON/TMDL files are structurally present.

Power BI Desktop itself was not executed in this container, so final UI confirmation still requires opening the repaired PBIP in Power BI Desktop and using Refresh All.
