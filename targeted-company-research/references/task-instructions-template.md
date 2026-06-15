# Task Instructions Template

Replace variables before assigning work:

| Variable | Meaning |
|---|---|
| `{COMPANY}` | Target company full name |
| `{SHORT}` | Short name or brand |
| `{WEBSITE}` | Official website |
| `{WEBSITE_DOMAIN}` | Official website domain |
| `{INDUSTRY}` | Industry |
| `{GEOGRAPHY}` | HQ or priority market |
| `{PROJECT}` | Project slug |
| `{LANGUAGE}` | Output language |
| `{PURPOSE}` | job_search, investment, ABM, proposal, competitor, partner, supplier, or general |

## Shared Task Rules

- Work only on the assigned task.
- This skill has only formal deep-research mode. Do not downgrade to light, standard, quick, summary, or basic-profile mode.
- Complete the four-step loop: expand keywords, search candidates, fetch/capture full sources, synthesize from fetched evidence.
- Use `keyword_matrix.md` before searching; add new terms discovered during the task.
- Generate at least 20 query seeds for the assigned task; use 25+ seeds for purpose-critical tasks.
- Purpose changes weighting, not coverage. Every run still needs identity, finance, product, industry, competition, customer/channel, supplier/ecosystem, people/org, marketing/narrative, and risk/compliance coverage.
- Do not waste many seeds on entity aliases or generic narrative terms. Use more detailed seeds for industry dynamics, trends, competitiveness, supply chain, advantages, customer/channel, and marketing signals.
- Run at least 20 searches for the assigned task; use 25+ searches for purpose-critical, sparse, or newly discovered areas.
- Record candidate results before deduplication. Do not discard similar-looking results until enough high-quality sources have been fetched.
- Title similarity is not enough for deduplication. Fetch first, then deduplicate by full text, cited sources, quoted people, data points, source tier, publication date, supported facts, and task relevance.
- Keep similar-title sources separately when they contain different citations, customer/supplier names, figures, interviews, dates, or risk statements.
- Fetch or browser-capture at least 9 sources for the assigned task; use 12+ sources for purpose-critical tasks.
- Use search for breadth, then fetch/capture full sources for facts.
- Search snippets are discovery only, not final evidence.
- Use browser/CDP when static fetch fails on public or user-authorized pages.
- Save browser/CDP notes in `projects/{PROJECT}/evidence/browser_notes.md`.
- Save raw source extracts under `projects/{PROJECT}/sources/`.
- Add source marks `[Sxx]` to material claims.
- Do not append a full source table to the task report. Use `[Sxx]` marks only; the full source table is assembled once at the bottom of the final report.
- Mark estimates and missing facts explicitly.
- Do not read other task folders until final merge.
- Do not collect private personal contact information or guess private emails/phones.
- Update `task_status.md` after finishing.
- Do not write a short task summary. The task output must be a complete sub-report with at least 8 sections, at least 2 tables/matrices, and at least 1500 Chinese characters or 900 English words.

## Required Task Status Fields

Update `projects/{PROJECT}/task_status.md` with this schema after each task:

```markdown
| Task | Status | Keyword seeds | Searches run | Candidates | Fetched/captured | Findings | Data gaps |
|---|---|---:|---:|---:|---:|---|---|
| Task X | done | 20 | 20 | 14 | 9 | ... | ... |
```

Minimum formal project totals:

- 120+ keyword seeds;
- 100+ searches;
- 70+ candidate source records;
- 45+ fetched or browser-captured sources;
- 35+ high-quality sources;
- 30+ PDF pages, with 50+ pages as the target.

Keyword weighting guidance:

| Dimension | Formal seeds | Increase when |
|---|---:|---|
| Identity lock | 4-6 | Similar-name risk exists |
| Ownership/finance | 12-18 | `{PURPOSE}` is investment or diligence |
| Product/technology | 15-22 | competitor, supplier, partner, proposal |
| Market dynamics | 18-25 | every run |
| Competition/advantages | 18-25 | competitor, investment, proposal, ABM |
| Customer/channel | 15-22 | ABM, proposal, supplier, partner |
| Supplier/ecosystem | 15-22 | manufacturing, hard tech, supplier, investment |
| Marketing/narrative | 12-18 | ABM, proposal, brand/marketing research |
| People/org | 10-15 | job_search |
| Risk/compliance | 8-12 | investment, diligence, regulated/cross-border industry |

## Source Index Fields

Use this schema in `projects/{PROJECT}/source_index.md`:

```text
id | tier | task | title | publisher | date | url_or_file | extraction_method | fetch_status | confidence | notes
```

Extraction methods:

```text
search_tool | search_snippet_only | web_fetch | direct_download | pdf_text | ocr | headless_browser | cdp_browser | user_provided
```

Fetch status:

```text
fetch_success | fetch_partial | fetch_blocked | fetch_render_required | fetch_ocr_required | source_unavailable | source_conflict
```

## Project Setup Template

Create this before executing tasks:

```markdown
# {COMPANY} Research Task Plan

| Field | Value |
|---|---|
| Company | {COMPANY} |
| Website | {WEBSITE} |
| Industry | {INDUSTRY} |
| Geography | {GEOGRAPHY} |
| Purpose | {PURPOSE} |
| Language | {LANGUAGE} |
| Run mode | sequential by default; parallel only if supported |

## Formal Task Targets

| Task | Folder | Status | Keyword seeds | Searches | Fetched/captured |
|---|---|---|---:|---:|---:|
| Task 1 | task1_identity_finance | pending | 20+ | 20+ | 9+ |
| Task 2 | task2_product_technology | pending | 20+ | 20+ | 9+ |
| Task 3 | task3_industry_competition | pending | 20+ | 20+ | 9+ |
| Task 4 | task4_customers_suppliers | pending | 20+ | 20+ | 9+ |
| Task 5 | task5_people_org_narrative | pending | 20+ | 20+ | 9+ |

## Section Assembly Targets

| Section | File | Status | Frozen |
|---|---|---|---|
| Cover | sections/00_cover.md | pending | no |
| TOC | sections/01_toc.md | pending | no |
| Executive takeaways | sections/02_executive_takeaways.md | pending | no |
| Identity and finance | sections/10_company_identity_finance.md | pending | no |
| Products and technology | sections/20_products_technology.md | pending | no |
| Industry and competition | sections/30_industry_competition.md | pending | no |
| Customers and supply chain | sections/40_customers_suppliers_channels.md | pending | no |
| People and narrative | sections/50_people_org_narrative.md | pending | no |
| Purpose judgment | sections/60_purpose_judgment.md | pending | no |
| Data gaps | sections/70_data_gaps.md | pending | no |
| Evidence appendices | sections/90_appendix_task1.md - sections/94_appendix_task5.md | pending | no |
| Sources | sections/99_sources.md | pending | no |
```

## Task 1: Identity, Ownership, Finance, Governance

```markdown
# Task 1: {COMPANY} Identity, Ownership, Finance, Governance

## Objective

Lock the legal/company identity and collect verified facts on history, ownership, shareholders,
leadership, governance, financing/listing status, financial scale, compliance, and major risks.

## Known Inputs

- Company: {COMPANY}
- Short name: {SHORT}
- Website: {WEBSITE}
- Industry: {INDUSTRY}
- Geography: {GEOGRAPHY}
- Purpose: {PURPOSE}
- Output language: {LANGUAGE}

## Search Seeds

- "{COMPANY}" legal entity headquarters
- "{COMPANY}" history founder CEO CFO CTO
- "{COMPANY}" shareholders ownership financing valuation
- "{COMPANY}" IPO prospectus registration statement
- "{COMPANY}" revenue profit gross margin assets liabilities capex R&D
- "{COMPANY}" lawsuit litigation regulatory sanctions export controls
- site:{WEBSITE_DOMAIN} about leadership history investors
- site:sse.com.cn "{COMPANY}" OR "{SHORT}"
- site:static.sse.com.cn "{COMPANY}" OR "{SHORT}" filetype:pdf
- site:cninfo.com.cn "{COMPANY}" OR "{SHORT}"

## Fetch Targets

- Official about/history/contact pages.
- Filings, prospectuses, regulatory records, exchange pages.
- Annual/interim reports or investor documents.
- Court, patent, certification, sanctions/export-control records when relevant.
- Credible databases only for estimates.

## Output

Write to `projects/{PROJECT}/task1_identity_finance/task1_identity_finance.md`.

Include:

- identity lock and similar-name risks;
- company timeline;
- ownership/shareholders/subsidiaries;
- leadership and governance;
- financial table with period, currency, unit, accounting basis, source ID, page/section;
- compliance, litigation, sanctions/export-control facts;
- job-search or investment implication from fundamentals;
- data gaps;
- `[Sxx]` source marks only; do not append a source table.
```

## Task 2: Products, Technology, IP, Certifications

```markdown
# Task 2: {COMPANY} Products, Technology, IP, Certifications

## Objective

Map product lines, technical capabilities, IP/patent evidence, certification signals, roadmap, and
technology differentiation.

## Search Seeds

- "{COMPANY}" products catalog filetype:pdf
- "{COMPANY}" datasheet specifications
- "{SHORT}" product model certification standard
- site:{WEBSITE_DOMAIN} products catalog support downloads
- "{COMPANY}" patent technology R&D roadmap
- "{COMPANY}" launch next generation
- site:patents.google.com "{COMPANY}" OR "{SHORT}"

## Fetch Targets

- Product pages and catalog PDFs.
- Datasheets, certification documents, standards pages.
- Patent and IP pages.
- Official product news and roadmap statements.
- Distributor or customer technical pages when official sources are thin.

## Output

Write to `projects/{PROJECT}/task2_product_technology/task2_product_technology.md`.

Include:

- product taxonomy;
- model/specification table;
- patent/IP and certification matrix;
- technology roadmap and differentiation;
- technical risks and data gaps;
- `[Sxx]` source marks only; do not append a source table.
```

## Task 3: Industry, Competitors, Market Position, Policy

```markdown
# Task 3: {SHORT} Industry, Competitors, Market Position, Policy

## Objective

Explain the industry context, value chain, competitors, market position, cycle, regulation, and policy/geopolitical risks.

## Search Seeds

- "{INDUSTRY}" market size CAGR forecast
- "{INDUSTRY}" market share ranking competitors
- "{COMPANY}" market share ranking
- "{INDUSTRY}" price cycle supply demand
- "{INDUSTRY}" policy regulation export control sanctions
- "{Competitor}" revenue products market share
- "{SHORT}" Samsung SK hynix Micron competitors

## Fetch Targets

- Market reports with accessible summaries.
- Industry association pages.
- Competitor official pages and filings.
- Analyst/media reports with dates and publishers.
- Policy, export-control, and regulatory pages.

## Output

Write to `projects/{PROJECT}/task3_industry_competition/task3_industry_competition.md`.

Include:

- market size/growth/cycle with source tiers;
- value chain and profit pool;
- competitor matrix with at least five competitors for formal research;
- market share/ranking evidence and confidence;
- policy/geopolitical risks;
- opportunities, threats, and implications for {SHORT};
- `[Sxx]` source marks only; do not append a source table.
```

## Task 4: Customers, Suppliers, Channels, Ecosystem

```markdown
# Task 4: {SHORT} Customers, Suppliers, Channels, Ecosystem

## Objective

Map public evidence of customers, suppliers, partners, channels, distributors, ecosystem dependencies,
procurement signals, and concentration risks.

## Search Seeds

- "{COMPANY}" customers clients case study
- "{COMPANY}" supplier equipment material partner
- "{COMPANY}" distributor reseller dealer channel
- "{COMPANY}" OEM ODM qualification supply chain
- "{COMPANY}" import export supplier customs
- "{COMPANY}" procurement sourcing supply chain
- "{Supplier or Customer}" "{COMPANY}" OR "{SHORT}"
- "{SHORT}" Xiaomi Oppo Vivo Lenovo customer supplier

## Fetch Targets

- Customer case studies and disclosed qualification pages.
- Supplier/customer filings that mention the company.
- Distributor/reseller/channel pages.
- Trade show, association, and ecosystem pages.
- Job pages mentioning procurement, logistics, sourcing, sales, equipment, materials.

## Output

Write to `projects/{PROJECT}/task4_customers_suppliers/task4_customers_suppliers.md`.

Include:

- confirmed customers and evidence strength;
- supplier/ecosystem map;
- channel map by region/type;
- procurement and qualification signals;
- concentration/dependency risks;
- ABM, partner, supplier, or investment implications;
- `[Sxx]` source marks only; do not append a source table.
```

## Task 5: People, Organization, Hiring, Narrative

```markdown
# Task 5: {SHORT} People, Organization, Hiring, Narrative

## Objective

Analyze leadership, organization, hiring demand, employer signals, culture/reputation, events, public
media narrative, and purpose-specific decision implications.

## Search Seeds

- "{COMPANY}" jobs hiring career campus recruitment
- "{COMPANY}" salary interview culture layoff
- "{COMPANY}" CEO founder CTO CFO speech event
- "{COMPANY}" trade show exhibitor booth webinar
- "{COMPANY}" press release news 2024 2025 2026
- "{COMPANY}" media controversy risk
- site:{WEBSITE_DOMAIN} news jobs careers resources

## Fetch Targets

- Official careers/jobs pages.
- Official leadership/news pages.
- Public event speaker pages and conference agendas.
- Credible media coverage.
- Employer-review or social sources only as T3 weak evidence.

## Output

Write to `projects/{PROJECT}/task5_people_org_narrative/task5_people_org_narrative.md`.

Include:

- leadership and public business people;
- hiring demand by function/location;
- organization and culture signals;
- media narrative and event presence;
- job-search implications if `{PURPOSE}=job_search`;
- investment/ABM/partner implications when relevant;
- T3 warning for employer-review or social sources;
- `[Sxx]` source marks only; do not append a source table.
```

## Merge Template

```markdown
# {COMPANY} Targeted Company Research Report

> Research date: {DATE}
> Purpose: {PURPOSE}
> Source count: {SOURCE_COUNT}
> Confidence: high / medium / low

## 目录

1. 核心结论：公司最重要的 10-15 个判断。
2. 公司基础：身份、历史、股权、财务和治理。
3. 产品与技术：产品线、技术、认证和路线图。
4. 行业与竞争：趋势、竞品、优势和风险。
5. 客户与供应链：客户、渠道、供应商和生态。
6. 组织与叙事：招聘、管理层、营销和公开叙事。
7. 目的判断：围绕求职、投资、ABM、方案或合作的结论。
8. 数据缺口与来源：未验证事项和来源附录。

## Executive Takeaways

1. ...

## 1. Identity, History, Ownership And Finance

## 2. Products, Technology And IP

## 3. Industry Position And Competitors

## 4. Customers, Suppliers, Channels And Ecosystem

## 5. People, Organization, Hiring And Public Narrative

## Purpose-Specific Judgment

## Data Gaps

- 缺少数据：...

## Appendix: Evidence Tables And Lists

Add evidence tables and lists that were compressed out of the main report. Do not repeat main-report paragraphs. Include supplier leads, component categories, procurement ratios, competitor marketing assets, event lists, product/model tables, source-backed gaps, and next collection routes.

## Sources

| ID | Tier | Task | Title | URL/File | Extraction | Status | Notes |
|---|---|---|---|---|---|---|---|

---

<small>@加玮营销洞察 @加玮怎么看</small>
```

The merge template is the final assembled shape, not a one-pass writing prompt. Create the physical
section files first:

```text
sections/00_cover.md
sections/01_toc.md
sections/02_executive_takeaways.md
sections/10_company_identity_finance.md
sections/20_products_technology.md
sections/30_industry_competition.md
sections/40_customers_suppliers_channels.md
sections/50_people_org_narrative.md
sections/60_purpose_judgment.md
sections/70_data_gaps.md
sections/90_appendix_task1.md
sections/91_appendix_task2.md
sections/92_appendix_task3.md
sections/93_appendix_task4.md
sections/94_appendix_task5.md
sections/99_sources.md
```

`sections/99_sources.md` is the only complete source table in the final report. Earlier section files
and task appendices contain `[Sxx]` marks only.

Write `merge_manifest.md` with the section files in order, then physically assemble:

```bash
python3 targeted-company-research/scripts/assemble_report.py projects/{PROJECT}
```

Do not rewrite, summarize, compress, or delete frozen section content during final assembly. Do not
insert `page-break-after` or blank-page separators during assembly.

For every completed formal report, also generate `report.html` and `report.pdf`. Use a cover page, simple
top-level numbered table of contents, clear section hierarchy, readable tables, and source appendix.
Do not auto-build a nested TOC from all headings. If the TOC layout breaks in PDF, shorten TOC labels
and summaries. Put attribution only as one small line at the bottom of the final PDF page, not on the
cover, table of contents, header, footer, or body pages.

Prefer the rendering script:

```bash
python3 targeted-company-research/scripts/render_report.py projects/{PROJECT} --header-title "{Short Report Title}"
```

Formal delivery must also create canonical copies named `{公司名}_jiascan_report_v1.0.md/html/pdf`.
For later rounds on the same company, increment the minor version to `v1.1`, `v1.2`, etc. Prefer:

```bash
python3 targeted-company-research/scripts/render_report.py projects/{PROJECT} --header-title "{Short Report Title}" --basename "{公司名}_jiascan_report" --version "v1.0"
```

The PDF must have running headers with the current chapter, a short report title, and page numbers.
Avoid blank pages by using H1 `break-before: page` only, not section-level `page-break-after`.
Attribution must follow the final source table inline and must not become a standalone page.

Layout requirements:

- Cover page should be designed as a report cover. Use a generated no-text background image when available; otherwise use CSS gradients, geometric bands, grid textures, and strong typography.
- TOC should be a designed directory page with numbered items, short titles, and one-line summaries.
- Appendix divider pages must use reader-facing titles such as `附录四｜供应链与渠道分析`, not `Appendix Task 4`.
- Divider pages should include a decorative English kicker such as `APPENDIX 04`, a large title, and a short description.
- The divider page is enough. Do not add a separate same-title page after the divider. Start appendix body with H2-level content.
- Executive takeaways, chapter summaries, and task conclusions should use highlighted summary boxes with bold keywords, not plain paragraphs.

Every completed formal report must generate `report.html` and `report.pdf`. The PDF must be at least
30 pages, with 50+ pages as the target. If it is shorter, expand evidence appendices instead of
repeating main-report paragraphs: product/model tables, competitor matrices, customer/channel/supplier
tables, event lists, source appendix, and data gaps. If thresholds remain blocked, create
`INCOMPLETE_RESEARCH.md` instead of a short final report.

Appendix content must be evidence-first:

- Company/finance: identity, financial, financing, governance, and missing-data tables.
- Product: product/model, payload/use-case, accessory/ecosystem, case-sample, and gap tables.
- Competition: competitor website/case/event/product-narrative/marketing-axis matrix.
- Supply chain: supplier leads, component categories, procurement ratios, localization risks, verification backlog.
- Marketing: event list, partner-event list, case samples, competitor marketing assets, channel/social gaps.

If a cell cannot be verified, write `缺少数据：...` and the next collection route.
