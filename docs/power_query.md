# Power Query / Source Notes

The semantic model imports six source tables from the synthetic Excel workbook through Power Query (M):

- Dim_Date
- Dim_Auditor
- Dim_Process
- Fact_QualityAudits
- Fact_OperationalAudits
- Fact_OperationalTargets

`Dim_DefectType` and `_Measures` are model-side helper structures rather than workbook source tables.

## Current source-path behavior

The desktop-validated master retains the original local Excel path used during development. This was an intentional stability decision after experimental external edits to PBIP/TMDL source definitions failed Desktop-load/refresh validation.

For another user/machine, point the Excel source to:

`data/quality_operations_synthetic.xlsx`

using Power BI Desktop / Power Query, then refresh and run the QA checklist.

## Production consideration

A production implementation should replace the local workbook dependency with a governed source and environment-aware configuration. The portfolio package intentionally preserves the Desktop-validated master rather than claiming a portability change that was not validated.
