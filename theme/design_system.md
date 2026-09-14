# Quality Operations Analytics Design System

| Token | Value | Use |
|---|---|---|
| Canvas | `#EEF3FF` | Report-page background |
| Panel | `#FFFFFF` | Cards and analytical panels |
| Primary Blue | `#1478F2` | Primary data series / accents |
| Dark Navy | `#162A8A` | Strong headings / secondary blue accent |
| Primary Text | `#2F2F2F` | Main labels and titles |
| Secondary Text | `#6B7280` | Supporting labels |
| Border | `#DDE5F0` | Soft panel borders |
| Green | `#1F7A3D` | Positive status only |
| Yellow | `#D4A017` | Warning status only |
| Red | `#C62828` | Exception/negative status only |

Typeface: **Segoe UI**.

## Layout rules

- Consistent white header across all pages.
- Compact text/tab navigation rather than oversized buttons.
- Year / Month / Week dropdown slicers integrated into the header.
- White panels on the light canvas; avoid default Power BI gray containers.
- Use blue for ordinary data. Reserve R/Y/G for status semantics.
- Maintain consistent panel margins, visual titles and spacing.
- Prefer analytical hierarchy over adding additional KPI cards.

## Accessibility rules

- Add meaningful alt text to every data-bearing visual; decorative objects should not create noise for screen readers.
- Set and test a logical keyboard/tab order for every page.
- Maintain at least WCAG AA contrast for text and status labels; do not place pure yellow text on white.
- Never communicate status by color alone. Keep the GREEN/YELLOW/RED text (or an equivalent label/icon) alongside color.
- Provide a visible note on Quality Trends, Defect Analysis and Operational Performance that partial weeks are excluded.
- Make slicer selections fully readable; avoid truncated states such as `Multiple sel...` when the selected period affects interpretation.

## Accepted table-status treatment

Auditor Performance intentionally keeps its alternating row bands and uses the literal GREEN/YELLOW/RED label plus font color. Solid conditional backgrounds were tested and rejected because they competed with the banded-table design. The text label preserves the meaning independently from color. This is the approved portfolio treatment; it is not an independent WCAG conformance certification.

The implemented accessibility and scope controls are recorded in `docs/qa_and_release_checklist.md`.

## Final page system

1. Executive Overview — reference/template page.
2. Auditor Performance — full-width performance table inside clean analytical panel.
3. Quality Trends — two principal weekly trend panels.
4. Defect Analysis — four KPI cards plus category and Pareto analysis.
5. Operational Performance — three analytical charts plus grouped Load Line/Outbound KPI blocks.
