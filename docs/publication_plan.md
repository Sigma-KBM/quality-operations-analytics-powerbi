# Publication Plan

## Recommended repository

**Name:** `quality-operations-analytics-powerbi`

**Short description:** `Five-page Power BI portfolio case study combining quality KPIs, auditor compliance, dynamic operational targets, weekly trends and Pareto defect analysis using synthetic data.`

## GitHub release sequence

1. Create the repository using the recommended name.
2. Upload the contents of this portfolio package.
3. Export and add the five final screenshots to `/images`.
4. Add the final GitHub repository URL to the blog draft. Completed.
5. Confirm the README screenshots render correctly on GitHub.
6. Add repository topics such as `power-bi`, `dax`, `power-query`, `data-analytics`, `business-intelligence`, `data-visualization`, `star-schema`.
7. Review whether MIT is the license you want before publishing; replace/remove it if not.
8. Run `python scripts/validate_portfolio.py` and resolve every failure.
9. Check the public Git author identity/email and confirm it is intentional.
10. Create a `v1.0` release only after a clean clone/open/refresh test.

## BTN Insights sequence

Published article: https://btninsights.blogspot.com/2026/09/building-quality-operations-analytics.html

1. Publish the GitHub repository first so the article can link to it.
2. Use `docs/btn_insights_case_study.md` as the article body.
3. Add Executive Overview near the introduction.
4. Add model diagram/screenshot in the Data Model section.
5. Add Defect Analysis in the Pareto section.
6. Add Operational Performance in its corresponding section.
7. Add final GitHub and LinkedIn links. Completed.
8. Suggested SEO title: **Building a Quality & Operations Analytics Dashboard in Power BI: From Synthetic Audit Data to Actionable KPIs**.
9. Suggested search description: **A practical Power BI case study using synthetic quality and operations data to build DPV/ADR KPIs, auditor performance, dynamic targets, Pareto analysis and an executive dashboard.**

## LinkedIn sequence

Published post: https://lnkd.in/p/gjbAJNJ5

The post was published after GitHub and the BTN Insights article using the main copy from `docs/linkedin_posts.md` and the recommended five-image sequence with Executive Overview first.

## Screenshot export rules

- Reset filters unless the screenshot intentionally demonstrates a filter behavior.
- Use a consistent Power BI canvas zoom.
- Capture the report canvas in reading view or another clean presentation state.
- Hide authoring, selection, data and format panes, visual headers, tooltips and selection borders.
- Do not expose the Power BI account name, Windows username, local file paths, activity IDs or other account information.
- Use PNG at sufficient resolution for LinkedIn and blog display.
- Use the same page order everywhere.

## Privacy and governance gate

- Publish only the bundled synthetic/anonymized workbook and documented PBIP assets.
- Confirm ignored `.pbi` cache/settings files are not tracked.
- Search tracked content for credentials, tokens, private URLs, emails and local paths before release.
- Confirm the public Git author identity/email is intentional; changing historical commits is a separate destructive decision and is not part of routine cleanup.
- If this case study is ever connected to real data, complete a new security review covering access control, row-level security, sensitivity labels, export policy and retention. The current synthetic portfolio review does not approve a production deployment.
