# Research Playbook

## Research Thesis

Targeted company research turns a named company into an evidence-backed business map: what the
company is, how it makes money, where it sits in its industry, who funds/supplies/buys from it, how
it is hiring and communicating, and what a job seeker, investor, salesperson, partner, or competitor
should infer from public evidence.

The final answer is not a company encyclopedia or basic company profile. It is a formal deep research
report with an audit trail, evidence appendices, and a PDF output of at least 30 pages, with 50+ pages
as the target.

This skill has only one mode: formal deep research. Do not offer or silently execute light, standard,
or summary modes. If the thresholds cannot be met, produce `INCOMPLETE_RESEARCH.md`, `data_gaps.md`,
and a backfill plan instead of a short `FINAL_REPORT.md`.

The required workflow is always:

1. Expand keywords.
2. Search candidate results.
3. Fetch or capture full sources.
4. Synthesize only from fetched evidence.

The five task areas are coverage templates. They do not replace the four-step workflow.

Purpose changes depth, not baseline scope. Every run should still cover identity, finance, products,
industry trends, competition, customers/channels, suppliers/ecosystem, people/org, marketing narrative,
and risk/compliance. A purpose such as job search, investment, ABM, proposal, competitor, partner, or
supplier research only increases keyword seeds, search coverage, fetch depth, and final-report detail in
the relevant areas.

## Phase 1: Identity Lock

Confirm the target before deep research:

- legal name, common name, brand names, English/Chinese aliases;
- official website and official social/account pages;
- HQ and operating locations;
- parent/subsidiary/issuer relationships;
- similar-name collision risks.

Stop and clarify if two companies plausibly match the same name.

Example identity-lock issue:

```text
长鑫科技集团股份有限公司 may appear together with 长鑫存储 / CXMT / ChangXin Memory.
Lock the issuer/legal entity, the operating brand, and the official domain before using financial,
IPO, product, hiring, or media sources.
```

## Phase 2: Project Setup

Create the skeleton before research:

```text
projects/{project_slug}/
├── task_plan.md
├── task_status.md
├── keyword_matrix.md
├── source_index.md
├── data_gaps.md
├── section_status.md
├── merge_manifest.md
├── sections/
├── task1_identity_finance/task_instructions.md
├── task2_product_technology/task_instructions.md
├── task3_industry_competition/task_instructions.md
├── task4_customers_suppliers/task_instructions.md
├── task5_people_org_narrative/task_instructions.md
├── sources/
├── evidence/
└── images/
```

`task_status.md` format:

```markdown
| Task | Status | Keyword seeds | Searches run | Candidates | Fetched/captured | Findings | Data gaps |
|---|---|---:|---:|---:|---:|---|---|
| Task 1 | running | 20 | 20 | 14 | 9 | - | - |
```

Status values: `pending`, `running`, `done`, `blocked`, `skipped`.

`section_status.md` format:

```markdown
| Section | File | Status | Min length | Tables | Source marks | Frozen |
|---|---|---|---:|---:|---:|---|
| Company identity and finance | sections/10_company_identity_finance.md | frozen | pass | 2 | 12 | yes |
```

Section status values: `pending`, `drafting`, `ready_for_freeze`, `frozen`, `blocked`.

## Phase 3: Keyword Matrix

Build `keyword_matrix.md` before source collection. Update it after each discovery pass.

Target counts:

| Mode | Total keyword seeds | Per standard task |
|---|---:|---:|
| formal | 120+ | 20+ |

| Dimension | Query seeds |
|---|---|
| Identity lock | legal name, brand, ticker, domain, old names, abbreviations, Chinese/English names, similar-name exclusion |
| Ownership/finance | parent, subsidiaries, shareholders, financing, revenue, profit, gross margin, capex, R&D, IPO, valuation, prospectus |
| Product/technology | product lines, model names, SKU names, process terms, datasheets, certifications, patents, roadmap |
| Market dynamics | industry size, growth, cycle, price trend, demand shift, policy, regulation, regional market, downstream change |
| Competition/advantages | competitors, market share, ranking, substitutes, differentiation, cost advantage, technical advantage, channel advantage, moat |
| Customer/channel | customers, clients, case studies, applications, qualification, distributors, OEM/ODM, tenders, sales regions |
| Supplier/ecosystem | equipment, materials, EDA/IP, packaging/testing, logistics, procurement, import/export, partners, dependency risk |
| Marketing/narrative | official news, launches, events, white papers, cases, social accounts, content marketing, interviews, brand narrative |
| People/org | founder, CEO, CFO, CTO, leadership, jobs, hiring, layoffs, compensation, culture, org expansion |
| Risk/compliance | litigation, sanctions, IP disputes, recalls, safety, regulatory penalties, export controls, controversy |
| Source type | `site:`, `filetype:pdf`, registry, exchange, association, trade show, patent, certification |

Keyword allocation is not even. Entity/identity terms should be few and precise; industry dynamics,
competition, advantages, supply chain, customer/channel, and marketing signals should receive more
detailed search questions.

| Dimension | Formal seeds | Increase when |
|---|---:|---|
| Identity lock | 4-6 | similar-name risk exists |
| Ownership/finance | 12-18 | investment or diligence |
| Product/technology | 15-22 | competitor, supplier, partner, proposal |
| Market dynamics | 18-25 | every run |
| Competition/advantages | 18-25 | competitor, investment, proposal, ABM |
| Customer/channel | 15-22 | ABM, proposal, supplier, partner |
| Supplier/ecosystem | 15-22 | manufacturing, hard tech, supplier, investment |
| Marketing/narrative | 12-18 | ABM, proposal, brand/marketing research |
| People/org | 10-15 | job_search |
| Risk/compliance | 8-12 | investment, diligence, regulated/cross-border industry |

Use exact names first, then alias groups:

```text
"{Company Legal Name}" revenue profit gross margin
"{Company Legal Name}" IPO prospectus filing
"{Brand}" OR "{Abbreviation}" products catalog filetype:pdf
site:{official_domain} (about OR leadership OR news OR products OR jobs)
"{Company}" (customer OR supplier OR distributor OR partner)
"{Company}" (patent OR certification OR ISO OR CE OR JEDEC)
"{Company}" (lawsuit OR litigation OR sanctions OR export controls)
"{Company}" (招聘 OR 薪酬 OR 面试 OR 校招 OR 社招)
"{Executive Name}" "{Company}"
```

Authority-site examples:

```text
site:sse.com.cn {company} 招股说明书
site:static.sse.com.cn {company} pdf
site:cninfo.com.cn {company} 年报
site:hkexnews.hk {company} annual report
site:sec.gov {company} 10-K
site:jobs.{domain} {company} engineer
site:patents.google.com "{company}"
```

## Phase 4: Search Routes

Use all available routes, but keep the source record clear:

1. OpenSEO skills/MCP: keyword research, SERP inspection, domain comparison, search-result quality checks.
2. DataForSEO MCP: Google/Bing/Yahoo SERP, keyword volume, CPC, Labs, OnPage, domain/search data.
3. General web search: broad discovery.
4. Authority-site search: `site:` and official databases.
5. Direct site search: official website, jobs pages, IR pages, product catalog.
6. Browser/CDP: JS-rendered, logged-in, anti-bot, marketplace, public profile, or search result pages.

Search snippets only identify targets. Final facts require full source extraction, PDF text, browser
capture, or user-provided evidence.

## Phase 5: Breadth Search

Run enough searches to simulate a real user trying to find high-quality information. Formal research
requires at least 100 searches across the project and at least 20 searches per task.

Search targets:

| Mode | Searches | Candidate records |
|---|---:|---:|
| formal | 100+ | 70+ |

Record candidate results before deduplication. Similar-looking results can still matter when they come
from different source tiers, dates, entities, or task areas.

Do not deduplicate by title or snippet alone. Fetch first, then compare full text, cited sources,
quoted people, data points, source tier, publication date, supported facts, and task relevance. Keep
similar-title sources separately when their citations, figures, customer/supplier names, interviews, or
risk statements differ.

Save candidate metadata in `source_index.md`:

```markdown
| ID | Tier | Task | Title | Publisher | Date | URL/File | Extraction | Status | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | T1 | Task 1 | Official about page | Company | YYYY-MM-DD | https://... | web_fetch | fetch_success | high | identity |
```

## Phase 6: Deep Fetch

Use `web_fetch`, direct download, PDF extraction, OCR, browser, or CDP as appropriate.

Fetch targets:

| Mode | Fetched/captured sources | High-quality sources |
|---|---:|---:|
| formal | 45+ | 35+ |

Each task must fetch or browser-capture at least 9 sources. Purpose-critical or sparse tasks must reach
12+ sources. Do not stop at a small set of official pages.

Extraction methods:

```text
search_tool | search_snippet_only | web_fetch | direct_download | pdf_text | ocr | headless_browser | cdp_browser | user_provided
```

Fetch status:

```text
fetch_success | fetch_partial | fetch_blocked | fetch_render_required | fetch_ocr_required | source_unavailable | source_conflict
```

For each source:

- save raw or extracted material under `sources/` or `evidence/`;
- preserve exact numbers, dates, titles, names, product names, standards, and short representative quotes;
- record page/section for filings and PDFs when possible;
- classify missing or blocked material in `data_gaps.md`.

## Phase 7: Browser/CDP Fetch

Use a CDP-connected browser when static extraction fails or when a page is JavaScript-heavy.

Good targets:

- product listing pages with client-side rendering;
- job pages and hiring portals;
- trade show exhibitor search pages;
- certification lookup tools;
- public LinkedIn-like company/team surfaces in a user-authorized session;
- marketplace pages, review summaries, and distributor locators.

Evidence note format:

```markdown
## Browser Evidence

### B01
- URL:
- Page title:
- Access date:
- Tool: headless_browser / cdp_browser
- Extracted facts:
- Screenshot path, if saved:
- Confidence:
```

Rules:

- Use public pages or user-authorized sessions only.
- Do not bypass login, paywall, captcha, robots restrictions, or rate limits.
- Do not scrape private personal data.
- Prefer DOM text over screenshots.
- Feed discovered entities back into `keyword_matrix.md`.

Avoid foreground focus stealing. Use headless, in-app browser, background tab, or dedicated CDP profile
before touching the user's visible Chrome.

## Phase 8: Task-Specific Search Packs

### Task 1: Identity, Ownership, Finance, Governance

Search:

- `{Company} legal entity headquarters`
- `{Company} history founder CEO CFO CTO`
- `{Company} shareholders ownership financing valuation`
- `{Company} IPO prospectus registration statement`
- `{Company} revenue profit gross margin assets liabilities capex`
- `{Company} lawsuit litigation regulatory sanctions`
- `site:{official_domain} about leadership history investors`

Output:

- identity lock and similar-name risks;
- timeline and milestones;
- ownership, shareholders, subsidiaries, related parties;
- leadership and governance;
- financial table with period, currency, source, page/section;
- compliance, litigation, sanctions, ESG;
- job/investment implication from fundamentals.

### Task 2: Products, Technology, IP, Certifications

Search:

- `{Company} products catalog filetype:pdf`
- `{Company} datasheet specifications`
- `{Company} product model certification standard`
- `{Company} patent technology R&D`
- `site:{official_domain} products catalog support downloads`
- `{Company} roadmap launch next generation`

Output:

- product taxonomy;
- model/specification table;
- patent/IP/standard evidence;
- certifications and quality systems;
- technology differentiation;
- roadmap and data gaps.

### Task 3: Industry, Competitors, Market Position, Policy

Search:

- `{Industry} market size CAGR forecast`
- `{Industry} market share ranking competitors`
- `{Company} market share ranking`
- `{Industry} cycle price trend supply demand`
- `{Industry} policy regulation export control`
- `{Competitor} revenue product market share`

Output:

- value chain and profit pool;
- market size/growth/cycle with source tiers;
- competitor matrix;
- market share or ranking with confidence;
- policy/geopolitical risks;
- strategic position.

### Task 4: Customers, Suppliers, Channels, Ecosystem

Search:

- `{Company} customers clients case study`
- `{Company} supplier equipment material partner`
- `{Company} distributor reseller dealer`
- `{Company} OEM ODM qualification`
- `{Company} import export supplier customs`
- `{Company} procurement sourcing supply chain`
- `{Supplier/Customer} "{Company}"`

Output:

- confirmed customers and evidence strength;
- supplier/ecosystem map;
- channel and sales route;
- procurement and qualification signals;
- concentration or dependency risks;
- partner/sales implications.

### Task 5: People, Organization, Hiring, Narrative

Search:

- `{Company} jobs hiring career campus recruitment`
- `{Company} salary interview culture layoff`
- `{Company} CEO founder CTO CFO speech event`
- `{Company} trade show exhibitor booth webinar`
- `{Company} press release news 2024 2025 2026`
- `{Company} media controversy risk`
- `site:{official_domain} news jobs careers resources`

Output:

- hiring demand by function/location;
- organization and leadership signals;
- culture/employer reputation signals with T3 warning;
- public events and media narrative;
- purpose-specific implications for job seekers, investors, ABM, partner, or competitor view.

## Phase 9: Expansion Loop

After the first pass, rerun searches using discovered:

- product names and technical terms;
- subsidiaries and investment vehicles;
- executives and event speakers;
- customers, suppliers, distributors;
- competitors and standards;
- risk phrases from filings;
- job families and locations.

The second pass often finds better evidence than company-name searches.

## Phase 10: Section Freeze And Physical Assembly

Codex should not generate the final report in one pass. Produce physical section files first, then
assemble them in a deterministic order.

1. Read Task 1-5 outputs.
2. Write integrated report sections under `sections/`.
3. Convert Task 1-5 findings into evidence appendices in `sections/90_appendix_task1.md` through `sections/94_appendix_task5.md`; each appendix must add tables, lists, leads, source-backed gaps, or next-collection routes that were compressed out of the main report.
4. Convert `source_index.md` into `sections/99_sources.md`.
5. Mark section files as `frozen` in `section_status.md` only after they pass length, table, and source-marker checks.
6. Write `merge_manifest.md` with the exact physical file order.
7. Assemble `FINAL_REPORT.md` by concatenating manifest files. Prefer:

```bash
python3 targeted-company-research/scripts/assemble_report.py projects/{project_slug}
```

The assemble script must not insert forced page-break elements. Do not combine section-level
`page-break-after` with heading-level `break-before`; that pattern creates blank pages.

8. Generate `report.html` and `report.pdf` for every completed report. Prefer:

```bash
python3 targeted-company-research/scripts/render_report.py projects/{project_slug} --header-title "{Short Report Title}"
```

The render script should add a running chapter header and page-number footer after PDF generation.
Formal delivery must also produce canonical copies named `{公司名}_jiascan_report_v1.0.md/html/pdf`.
For repeated generations of the same company, increment the minor version: `v1.1`, `v1.2`, etc. Prefer
passing `--basename "{公司名}_jiascan_report" --version "v1.0"` to the render script.
9. Verify the PDF has at least 30 pages. If it does not, expand the evidence appendices, evidence tables,
   competitor matrices, product/model tables, customer/supply-chain tables, source appendix, and data
   gaps before delivery.

If a task is blocked, keep the task heading and write `缺少数据：...`.

Frozen section rules:

- Final assembly must not rewrite, summarize, compress, or delete frozen section content.
- Assembly may add page breaks and normalize heading numbers.
- Section bodies use `[Sxx]` citations only.
- Full source tables must appear only once, in `sections/99_sources.md`, at the bottom of the final report.
- Do not put `## Sources` after each section or evidence appendix.
- Attribution must follow the final source table inline; it must not become a standalone final page.

Default display attribution, unless the user requests white-label output:

```text
@加玮营销洞察 @加玮怎么看
```

Use attribution only as one small line at the end of the Markdown report or at the bottom of the final
PDF page. Do not place it on the cover, subtitle, table of contents, header, footer, or body pages. Do
not treat it as evidence, a source, or a research finding.

## Final Report Rules

Lead with conclusions:

- specific object;
- clear judgment;
- data or source evidence.

Bad:

```text
We researched the company from multiple angles.
```

Good:

```text
{Company} has stronger verified product and hiring signals than customer disclosure; confirmed evidence includes {N} official product pages, {N} filing sections, and {N} job families, while public customer concentration remains a data gap.
```

Final report structure:

```markdown
# {Company} Targeted Company Research Report

## Executive Takeaways

## 1. Identity, History, Ownership And Finance

## 2. Products, Technology And IP

## 3. Industry Position And Competitors

## 4. Customers, Suppliers, Channels And Ecosystem

## 5. People, Organization, Hiring And Public Narrative

## Purpose-Specific Judgment

## Data Gaps

## Appendix: Evidence Tables And Lists

## Sources
```

The final report must use a two-layer structure, but the appendix must not repeat the main report:

1. Integrated main report: synthesis, conclusions, tables, and decision implications.
2. `Appendix: Evidence Tables And Lists`: incremental evidence tables, lists, source snippets, competitor breakdowns, event details, supply-chain leads, and missing-data trackers that were compressed out of the main report. Do not mechanically paste Task 1-5 text.
3. `Sources`: one complete source table at the bottom only.

Evidence appendix requirements:

- Company/finance appendix: identity lock, financial metrics, financing/use-of-proceeds, governance/risk leads, missing-data list.
- Product appendix: product/model series, payload or use case, certifications/accessories/ecosystem, case samples, missing-data list.
- Competitor appendix: UR/JAKA/AUBO/Elite/ABB/FAIRINO website, case library, event, product narrative, and marketing-axis comparison.
- Supply-chain appendix: supplier lead table, component category table, procurement ratio table, localization/multi-sourcing risk table, verification backlog.
- Marketing appendix: event list, partner-event list, case-library samples, competitor marketing asset list, channel/social gaps.
- Source appendix: every visited source, fetch status, confidence, and the claim or use it supports.

If a field is not publicly found, write `缺少数据：...` in the table and provide the next collection route.

Minimum content requirements:

- `Executive Takeaways`: 10-15 sourced conclusions, with bold judgment labels or highlighted summary boxes.
- Each core section: at least five subsections, two tables/matrices, and one explicit judgment.
- Each evidence appendix: at least three tables or lists, with incremental details not already fully covered in the main report.
- Sources appendix: at least 35 high-quality sources.
- `FINAL_REPORT.md` is assembled from frozen section files listed in `merge_manifest.md`.

## HTML/PDF Rules

`report.html` must include:

- cover page with company, purpose, date, source count, page target, and confidence; do not include attribution on the cover;
- simple table of contents with only top-level numbered sections;
- one short table-of-contents summary sentence per top-level section;
- designed cover layout, not a plain text page;
- designed appendix/divider pages with reader-facing titles, not workflow names;
- highlighted summary boxes for chapter conclusions;
- running page header with current top-level chapter and short report title;
- page footer with current page and total pages, such as `6 / 33`;
- clear H1/H2/H3 hierarchy;
- readable financial, competitor, customer/supplier, and hiring tables;
- local images from `images/`;
- source appendix and data gaps.
- one small attribution line at the bottom of the final PDF page only.
- 30+ PDF pages; target 50+ pages.

Blank-page rules:

- Do not fill blank pages with filler content. Remove the redundant page-break rule instead.
- Use `break-before: page` for H1/top-level chapters only.
- Do not add `page-break-after` after every assembled section.
- Cover, TOC, and executive summary may start on separate pages, but no page should be blank.
- After rendering, detect blank or near-blank pages and rerender before delivery.
- Keep attribution directly after the source table; do not insert a page break before attribution.

Cover, TOC, divider, and summary rules:

- If image generation is available, create a no-text cover background image and overlay title/meta in HTML. If not, use CSS gradients, geometric bands, grid textures, and strong typography.
- Cover text contrast must be verified. Do not place white text over a bright or busy image area.
- TOC should be a designed directory page: use numbered items, short titles, summaries, and spacing proportional to the number of items.
- Appendix divider pages should use titles such as `附录四｜供应链与渠道分析`, plus an English decorative kicker such as `APPENDIX 04` and a one-sentence description.
- Do not expose workflow labels like `Appendix Task 4` to readers.
- The divider page is the appendix cover. Do not create a second page with the same appendix title after it.
- Appendix body content should start with H2 or lower-level headings so it does not trigger another standalone title page.
- Chapter summaries should be visually distinct: light background, left accent rule, and bold keywords for the main judgment, risk, or action.

Do not auto-generate a deep nested table of contents from all headings. Do not include H3/H4 headings
or long question titles in the table of contents. Use simple numbered sections such as:

```markdown
1. Executive Takeaways
2. Company Basics
3. Products And Technology
4. Industry And Competition
5. Customers And Supply Chain
6. Organization And Narrative
7. Purpose-Specific Judgment
8. Data Gaps And Sources
```

Export `report.pdf` from HTML and verify that the cover, simple table of contents, tables, charts, and
source appendix render. If the table of contents breaks, shorten the TOC labels and summaries before
adding CSS complexity.

## Quality Checklist

- Official identity locked.
- All five task files exist.
- `sections/`, `section_status.md`, and `merge_manifest.md` exist.
- All required section files are marked frozen before assembly.
- `keyword_matrix.md` exists and has a second expansion pass.
- Formal runs have at least 120 keyword seeds, 100 searches, 70 candidate records, 45 fetched/captured sources, and 35 high-quality sources unless blocked.
- Each task has at least 20 query seeds, 20 searches, and 9 fetched/captured sources.
- Source index has tier, extraction method, fetch status, and confidence.
- No duplicate URLs unless notes differ materially.
- Every important number has a source mark or `待核实`.
- Financial data has period, currency, unit, basis, page/section when available.
- T3 evidence is weak evidence only.
- Browser/CDP observations are logged.
- Inferences are labeled.
- Missing evidence is explicit.
- Final report preserves raw numbers, years, platform names, people names, product names, source names, and short representative quotes.
- Final report has one source appendix at the bottom; no duplicated source tables after each section.
- Final PDF has running headers, page numbers, and no blank pages.
- Cover, TOC, appendix dividers, and chapter summary boxes use report-quality visual hierarchy.
- Attribution is on the final source page, not on a standalone page.
- Final PDF has 30+ pages. If not, mark the report incomplete and continue expanding.
