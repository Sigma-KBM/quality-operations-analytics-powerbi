# Audit Remediation Status

This document separates controls that can be completed safely in the repository from changes that must be made and validated in Power BI Desktop.

## Closed in the repository

- The source workbook was restored from the known-good Git backup and validated against the semantic model.
- Baseline and complete-week KPI values are independently reconciled by `scripts/validate_portfolio.py`.
- Primary keys, foreign keys, target grain, defect totals and accessory totals are checked automatically.
- Report JSON validity, required model names, page-level partial-week policy and tracked PBIP cache/settings files are checked automatically.
- Documentation now states the fixed local source path instead of describing it as portable.
- Documentation now identifies the current target authority: fixed DAX for displayed DPV/ADR targets and `Fact_OperationalTargets` for operational/auditor targets.
- Publication guidance now includes screenshot privacy, Git identity, secrets/cache and production-security gates.

## Desktop remediation completed

The following work was completed and saved through Power BI Desktop, then checked after close/refresh:

1. Meaningful alt text was added to the principal analytical visuals.
2. Keyboard/tab order was configured across the five pages.
3. Status remains explicitly communicated with the GREEN/YELLOW/RED label as well as font color.
4. A visible “Complete weeks only — partial weeks are excluded.” note was added to Quality Trends, Defect Analysis and Operational Performance.
5. The Week slicer was adjusted so its selected state is readable.
6. The visible/internal typo `Aditor Performance` was corrected to `Auditor Performance`.

### Accepted status-format decision

Solid conditional backgrounds in the Auditor Status column were tested and rejected because they reduced visual harmony and readability against the table's alternating row bands. The approved design retains the alternating row background and uses explicit GREEN/YELLOW/RED text with status color. This is an intentional portfolio design decision, not an assertion of independent WCAG certification.

## Owner release decisions completed

- The existing Git author identity using the `sigma-emprende.com` domain is approved for public commits; no history rewrite is required.
- The MIT license is confirmed as the intended public repository license.
- If the report is ever connected to real operational data, perform a separate production security review for access, row-level security, sensitivity labels, export and retention.

Audit remediation is complete within the agreed portfolio scope. The portfolio is numerically and structurally validated, its principal accessibility controls are documented, the five clean gallery screenshots have been installed and verified, and the current owner publication decisions are complete.
