# QA and Release Checklist

## Desktop validation completed

The final master supplied for portfolio packaging was saved, closed, reopened and refreshed successfully in Power BI Desktop after the visual-formatting work was completed.

### Navigation and filters

- [x] Five report pages load.
- [x] Page navigation works in Desktop.
- [x] Year slicer synchronizes across pages.
- [x] Month slicer synchronizes across pages.
- [x] WeekLabel slicer synchronizes across pages.
- [x] Reset clears synchronized filters.
- [x] Month is chronologically sorted by MonthNumber.
- [x] Dim_Date contains 2025 only.

### Baseline reconciliation — filters reset

- [x] Vehicles Audited = 6,333
- [x] Accessories Audited = 25,105
- [x] DPV ≈ 0.18
- [x] DPV Target = 0.14
- [x] ADR ≈ 2.85
- [x] ADR Target = 3.50
- [x] Load Line Actual = 6,390
- [x] Load Line Target = 6,014
- [x] Outbound Actual = 5,053
- [x] Outbound Target = 4,830
- [x] Overall status = RED at baseline

### Auditor Performance

- [x] Total Actual = 11,443
- [x] Total Target = 11,889
- [x] Total Gap = -446
- [x] Compliance = 96.2%
- [x] Total Status = YELLOW
- [x] Table responds to synchronized date filters.

### Defect Analysis

Full-week baseline:

- [x] Performance = 404
- [x] Functional = 298
- [x] Appearance = 264
- [x] Parking = 132
- [x] Pareto recalculates under filters.
- [x] Cumulative percentage reaches 100%.
- [x] Final visual contains only meaningful column/line series.

### Operational Performance

Full-week baseline:

- [x] Load Line Actual = 6,270
- [x] Load Line Target = 5,888
- [x] Load Line Gap = 382
- [x] Load Line Completion ≈ 106.5% / GREEN
- [x] Outbound Actual = 4,949
- [x] Outbound Target = 4,728
- [x] Outbound Gap = 221
- [x] Outbound Completion ≈ 104.7% / GREEN
- [x] Actual, target, gap, completion and status change coherently under date filters.

### Time-scope policy

- [x] Executive Overview includes all selected dates.
- [x] Auditor Performance includes all selected dates.
- [x] Quality Trends excludes partial weeks.
- [x] Defect Analysis excludes partial weeks.
- [x] Operational Performance excludes partial weeks.
- [x] A concise visible note on the three full-week pages prevents comparison of unlike totals without context.

### Target governance

- [x] Displayed DPV target is governed by fixed DAX value 0.14.
- [x] Displayed ADR target is governed by fixed DAX value 3.50.
- [x] Operational and auditor targets are read from `Fact_OperationalTargets` in the active context.
- [x] Future target changes must update the governed source and documentation together and rerun validation.

### Visual QA

- [x] Five pages use a consistent executive design language.
- [x] Defect Pareto uses blue/teal rather than exception red.
- [x] Operational Performance status labels do not clip.
- [x] Auditor Performance redundant subtitle removed.
- [x] `Aditor Performance` corrected to `Auditor Performance`.
- [x] GREEN/YELLOW/RED reserved for status/exception meaning.
- [x] Auditor Status retains explicit text plus font color; solid status backgrounds were intentionally rejected to preserve the banded-table design.

## Publication checks completed

- [x] Run `python scripts/validate_portfolio.py` successfully from the repository root.
- [x] Add meaningful alt text to the principal analytical visuals.
- [x] Configure and review keyboard navigation and tab order on every page.
- [x] Retain explicit text in addition to status color; no independent WCAG certification is claimed.
- [x] Confirm the three full-week pages visibly disclose that partial weeks are excluded.
- [x] Export five final screenshots from the validated Desktop master.
- [x] Review screenshots at 100% for accidental selection outlines/tooltips.
- [x] Confirm no Power BI account name, local username, local path, tooltip, selection outline or authoring pane is visible in screenshots.
- [x] Confirm the Git author email shown publicly is the intended `sigma-emprende.com` address.
- [x] Confirm no `.pbi` cache/settings files, credentials, connection secrets or non-synthetic data are tracked.
- [x] Create GitHub repository and replace placeholder screenshot section with exported images.
- [x] Update the final GitHub URL in the BTN Insights article copy.
- [x] Update the BTN Insights URL in the LinkedIn copy after the article is published.
- [x] Publish the BTN Insights case study and record its final URL.
- [x] Publish the LinkedIn portfolio post and record its final URL.
- [x] Confirm MIT as the intended public repository license.
