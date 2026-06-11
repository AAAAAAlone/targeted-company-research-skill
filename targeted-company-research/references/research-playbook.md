# Research Playbook

## Research Thesis

Targeted company research turns a named company into an evidence-backed business map: what the
company is, how it makes money, where it sits in its industry, who funds/supplies/buys from it, how
it is hiring and communicating, and what a job seeker, investor, salesperson, partner, or competitor
should infer from public evidence.

The final answer is not a company encyclopedia. It is a decision brief with an audit trail.

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
| Task | Status | Sources | Fetch/browser | Major findings | Data gaps |
|---|---|---:|---:|---|---|
| Task 1 | running | 0 | 0 | - | - |
```

Status values: `pending`, `running`, `done`, `blocked`, `skipped`.

## Phase 3: Keyword Matrix

Build `keyword_matrix.md` before source collection. Update it after each discovery pass.

| Dimension | Query seeds |
|---|---|
| Entity | legal name, brand, ticker, domain, old names, abbreviations, Chinese/English names |
| Ownership | parent, subsidiaries, shareholder names, employee plans, investment funds, state capital |
| Finance | revenue, profit, gross margin, assets, liabilities, capex, R&D, IPO, valuation, prospectus |
| Product | product lines, model names, SKU names, process terms, datasheets, certifications, patents |
| Market | industry, buyer industry, market size, share, cycle, policy, regulation, export controls |
| Customers | customers, clients, case studies, application fields, qualification, supply chain entry |
| Suppliers | equipment, materials, EDA/IP, packaging/testing, logistics, procurement, import/export |
| People/org | founder, CEO, CFO, CTO, leadership, jobs, hiring, layoffs, compensation, culture |
| Narrative/risk | litigation, sanctions, IP disputes, recalls, safety, controversy, media narratives |
| Source type | `site:`, `filetype:pdf`, registry, exchange, association, trade show, patent, certification |

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

1. OpenSEO skills/MCP: keyword research, SERP inspection, domain comparison, AI visibility.
2. DataForSEO MCP: Google/Bing/Yahoo SERP, keyword volume, CPC, Labs, OnPage, AI Optimization data.
3. General web search: broad discovery.
4. Authority-site search: `site:` and official databases.
5. Direct site search: official website, jobs pages, IR pages, product catalog.
6. Browser/CDP: JS-rendered, logged-in, anti-bot, marketplace, public profile, or search result pages.

Search snippets only identify targets. Final facts require full source extraction, PDF text, browser
capture, or user-provided evidence.

## Phase 5: Breadth Search

Collect 25-50 candidate sources across the five task areas before deep writing.

Save candidate metadata in `source_index.md`:

```markdown
| ID | Tier | Task | Title | Publisher | Date | URL/File | Extraction | Status | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | T1 | Task 1 | Official about page | Company | YYYY-MM-DD | https://... | web_fetch | fetch_success | high | identity |
```

## Phase 6: Deep Fetch

Use `web_fetch`, direct download, PDF extraction, OCR, browser, or CDP as appropriate.

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

## Phase 10: Sequential Merge

Codex should default to sequential merge:

1. Read Task 1-5 outputs.
2. Extract the strongest sourced findings into executive takeaways.
3. Preserve complete task outputs in `Appendix: Full Task Reports`.
4. Deduplicate source rows by canonical URL/file, while preserving notes when one source supports multiple facts.
5. Write `FINAL_REPORT.md`.
6. Generate `report.html` and `report.pdf` for standard/deep reports or when requested.

If a task is blocked, keep the task heading and write `缺少数据：...`.

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

## Appendix: Full Task Reports

## Sources
```

## HTML/PDF Rules

`report.html` must include:

- cover page;
- table of contents;
- clear H1/H2/H3 hierarchy;
- readable financial, competitor, customer/supplier, and hiring tables;
- local images from `images/`;
- source appendix and data gaps.

Export `report.pdf` from HTML and verify that the cover, tables, charts, and source appendix render.

## Quality Checklist

- Official identity locked.
- All five task files exist for standard/deep reports.
- `keyword_matrix.md` exists and has a second expansion pass.
- Source index has tier, extraction method, fetch status, and confidence.
- No duplicate URLs unless notes differ materially.
- Every important number has a source mark or `待核实`.
- Financial data has period, currency, unit, basis, page/section when available.
- T3 evidence is weak evidence only.
- Browser/CDP observations are logged.
- Inferences are labeled.
- Missing evidence is explicit.
- Final report preserves raw numbers, years, platform names, people names, product names, source names, and short representative quotes.
