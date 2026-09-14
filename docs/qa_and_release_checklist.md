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

### Visual QA

- [x] Five pages use a consistent executive design language.
- [x] Defect Pareto uses blue/teal rather than exception red.
- [x] Operational Performance status labels do not clip.
- [x] Auditor Performance redundant subtitle removed.
- [x] GREEN/YELLOW/RED reserved for status/exception meaning.

## Publication checks still required

- [ ] Export five final screenshots from the validated Desktop master.
- [ ] Review screenshots at 100% for accidental selection outlines/tooltips.
- [ ] Confirm no local usernames/paths are visible in screenshots.
- [ ] Create GitHub repository and replace placeholder screenshot section with exported images.
- [ ] Update GitHub URL in blog/LinkedIn copy after repository creation.
- [ ] Verify licensing choice before public release.
