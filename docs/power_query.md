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

The desktop-validated master retains the fixed absolute Excel path `C:\qoa_portfolio\data\quality_operations_synthetic.xlsx` used during development. This path is reliable in the validated environment, but it is not portable. This was an intentional stability decision after experimental external edits to PBIP/TMDL source definitions failed Desktop-load/refresh validation.

For another user/machine, point the Excel source to:

`data/quality_operations_synthetic.xlsx`

using Power BI Desktop / Power Query, then refresh and run the QA checklist.

Do not rewrite the source M expressions or report/model definition files externally to change this path. Repoint it in Power BI Desktop, refresh, save, close, reopen and refresh again before accepting the change.

## Production consideration

A production implementation should replace the local workbook dependency with a governed source and environment-aware configuration. The portfolio package intentionally preserves the Desktop-validated master rather than claiming a portability change that was not validated.
