---
name: targeted-company-research
description: >-
  Generate source-backed targeted company research reports for a named company. Use for job-search
  research, investment or light diligence, ABM sales preparation, competitor analysis, partner or
  supplier research, and company deep dives that need keyword-matrix expansion, multi-engine/source
  search, full-text fetch, browser/CDP fallback, financial and ownership evidence, local charts, and
  Markdown + HTML + PDF delivery.
metadata:
  short-description: Source-backed company deep-dive reports
---

# Targeted Company Research

## Trigger

Use this skill when the user asks for a deep dive on one named company, brand, subsidiary, issuer,
competitor, customer, supplier, distributor, or investment target.

Typical prompts:

- "帮我全面了解这家公司"
- "我要面试/跳槽，帮我看这家公司值不值得去"
- "我想投资/尽调这家公司，帮我看基本面、股权、客户、供应商、行业地位"
- "帮我研究一个目标客户，用于 ABM / 销售拜访"
- "帮我看某家公司和竞品、上下游、风险、近期新闻"

Do not use this skill for a broad industry report without a named company. Use a market/industry
research skill first, then return here for company-level depth.

## Core Outcome

Turn the company into a verifiable business map:

1. Identity, history, ownership, financing, leadership, governance, compliance.
2. Financial scale, business model, margin/cash-flow signals, valuation/listing status.
3. Products, technology, IP, certifications, roadmap, differentiation.
4. Industry structure, competitors, market share, cycle, policy, geopolitical risks.
5. Customers, suppliers, channels, ecosystem, procurement and supply-chain signals.
6. Organization, hiring, culture, compensation signals, employer reputation.
7. Marketing, public people, events, media narrative, ABM or stakeholder entry points.
8. Job-search, investment, sales, or partnership implications, depending on purpose.

Default output is local-first:

```text
projects/{project_slug}/
├── task_plan.md
├── task_status.md
├── keyword_matrix.md
├── source_index.md
├── data_gaps.md
├── task1_identity_finance/
│   ├── task_instructions.md
│   └── task1_identity_finance.md
├── task2_product_technology/
│   ├── task_instructions.md
│   └── task2_product_technology.md
├── task3_industry_competition/
│   ├── task_instructions.md
│   └── task3_industry_competition.md
├── task4_customers_suppliers/
│   ├── task_instructions.md
│   └── task4_customers_suppliers.md
├── task5_people_org_narrative/
│   ├── task_instructions.md
│   └── task5_people_org_narrative.md
├── sources/
├── evidence/
├── images/
├── FINAL_REPORT.md
├── report.html
└── report.pdf
```

No external sending, image hosting, CRM upload, Feishu/Slack/Drive delivery, or spreadsheet workbook
is used by default. Use local relative paths for charts and evidence.

## Required Inputs

Infer conservatively when possible, but lock the target identity before deep research.

| Field | Meaning | Default |
|---|---|---|
| Target company | Legal/common name, brand, or ticker | Required |
| Website | Official site | Find and verify |
| Industry | Main business category | Infer with confidence |
| Geography | HQ and priority markets | HQ country + target markets |
| Purpose | job_search, investment, ABM, competitor, partner, supplier, general | general |
| Language | Report language | User language |
| Depth | light, standard, deep | standard |

Purpose-specific emphasis:

- `job_search`: organization, hiring, leadership, culture, business health, risk, growth, compensation signals.
- `investment`: financials, ownership, listing/financing, market position, customers/suppliers, risks, valuation signals.
- `ABM`: business map, decision makers, messaging, priorities, public initiatives, entry angles.
- `supplier/partner`: product fit, channel, procurement, compliance, references, ecosystem.
- `competitor`: product, pricing, technology, market share, customers, go-to-market, weaknesses.

## Source Ladder

Collect evidence in this order:

1. T0: regulatory filings, exchange disclosures, prospectuses, court records, patent/certification databases, official registries, customs/import-export records.
2. T1: official website, IR pages, annual reports, product docs, catalog PDFs, official news, official social accounts, official job pages.
3. T2: credible media, industry associations, trade shows, distributors, marketplaces, analyst/research reports, customer or supplier disclosures.
4. T3: estimates, lead databases, forums, reviews, employer-review sites, social platforms. Use as weak evidence or signal only.

Every material claim needs a source mark such as `[S12]`. Unsourced numbers must be marked `待核实`
or `缺少数据：...`.

## Keyword Matrix First

Before collecting sources, create `keyword_matrix.md`. The initial matrix must cover:

| Axis | Query seeds |
|---|---|
| Entity | legal name, common name, English/Chinese name, ticker, domain, subsidiaries, former names |
| Ownership/finance | shareholders, financing, IPO, prospectus, valuation, revenue, gross margin, capex, cash flow |
| Product/technology | product names, models, process node, patents, certifications, standards, roadmap |
| Market/industry | category, market size, market share, cycle, regulation, policy, competitors |
| Customer/channel | customers, clients, case studies, distributors, OEM/ODM, sales channels |
| Supplier/ecosystem | suppliers, equipment, materials, EDA/IP, logistics, procurement, import/export |
| People/org | founder, CEO, CFO, CTO, leadership, hiring, job postings, layoffs, compensation, culture |
| Narrative/risk | lawsuit, sanctions, export controls, safety, recall, controversy, media coverage |
| Source operators | `site:`, `filetype:pdf`, exact quotes, OR groups, date terms, exchange/registry names |

Run a second expansion loop after the first 8-12 useful sources. Newly discovered product names,
executives, subsidiaries, customers, suppliers, competitors, filings, and risk terms become new query seeds.

## Search Routes

Use the best available search/data routes:

1. OpenSEO skills/MCP for keyword research, SERP inspection, domain comparison, and search-result quality checks.
2. DataForSEO MCP for Google/Bing/Yahoo SERP, keyword volume, CPC, Labs, OnPage, and domain/search data.
3. General web search for discovery.
4. Authority-site searches with `site:` and `filetype:pdf`.
5. User browser/CDP for logged-in, anti-bot, JS-rendered, or search-result pages where direct fetch fails.

OpenSEO optional install:

```bash
npx skills add every-app/open-seo --skill '*' --agent codex
```

DataForSEO MCP optional:

```bash
npx dataforseo-mcp-server@latest
```

Only use paid-data tools when credentials already exist or the user explicitly approves.

## Search And Fetch Strategy

Search snippets discover candidates; they do not support final facts. Fetch or capture the source.

Extraction methods:

```text
search_tool | search_snippet_only | web_fetch | direct_download | pdf_text | ocr | headless_browser | cdp_browser | user_provided
```

Fetch status:

```text
fetch_success | fetch_partial | fetch_blocked | fetch_render_required | fetch_ocr_required | source_unavailable | source_conflict
```

Save source records in `source_index.md` with:

```text
id | tier | task | title | publisher | date | url_or_file | extraction_method | fetch_status | confidence | notes
```

If a source fails, classify it and write the missing data into `data_gaps.md`. Do not turn an
unfetched source into a conclusion.

## Browser And CDP Rules

Use the user's real browser or a CDP-connected browser only for public pages or user-authorized sessions.
Do not steal foreground focus.

Preferred order:

1. Direct fetch or PDF extraction.
2. Headless browser for public JS-rendered pages.
3. Background browser context or in-app browser.
4. Chrome CDP with a dedicated browser profile.
5. Foreground browser control only after explicit user approval.

CDP launch pattern:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.chrome-cdp-research" \
  --no-first-run
```

If the macOS path above is unavailable, use the local Chrome binary path in the environment.

Rules:

- Do not bypass paywalls, captchas, login walls, access controls, or robots restrictions.
- Do not collect private personal contact data or guess private emails/phones.
- Public business identity is acceptable: name, role, company, official profile URL, event reference, official contact channel.
- Prefer DOM text over screenshots. Screenshots are evidence only when text extraction is unreliable.

## Execution Model

Sequential execution is the default for Codex. Parallel workers are optional.

1. Create `task_plan.md`, `task_status.md`, `keyword_matrix.md`, `source_index.md`, `data_gaps.md`, `sources/`, `evidence/`, `images/`, and task folders.
2. Generate one `task_instructions.md` per task from `references/task-instructions-template.md`.
3. Execute Task 1 to Task 5 in order.
4. After each task, update `task_status.md` with status, source count, fetch/browser count, findings, and gaps.
5. Merge only after all available tasks are done or explicitly blocked.

| Task | Focus | Minimum search | Minimum fetch/browser | Target sources |
|---|---:|---:|---:|---:|
| Task 1 | Identity, ownership, finance, governance, history | 15 | 10 | 15 |
| Task 2 | Products, technology, IP, certifications, roadmap | 15 | 10 | 15 |
| Task 3 | Industry, competitors, market position, policy | 15 | 10 | 12 |
| Task 4 | Customers, suppliers, channels, ecosystem | 18 | 12 | 15 |
| Task 5 | People, organization, hiring, narrative, ABM/job/investment implications | 18 | 12 | 15 |

Depth controls:

| Depth | Use when | Target sources |
|---|---|---:|
| light | Fast company brief | 25-35 total |
| standard | Normal company deep dive | 60-75 total |
| deep | Diligence, job/investment decision, strategic account plan | 80+ total |

## Report Structure

`FINAL_REPORT.md` should contain:

```markdown
# {Company} Targeted Company Research Report

> Research date: {date}
> Purpose: {purpose}
> Source count: {N}
> Confidence: high / medium / low

## Executive Takeaways
5-10 specific conclusions with source marks.

## 1. Identity, History, Ownership And Finance

## 2. Products, Technology And IP

## 3. Industry Position And Competitors

## 4. Customers, Suppliers, Channels And Ecosystem

## 5. People, Organization, Hiring And Public Narrative

## Purpose-Specific Judgment
For job_search, investment, ABM, supplier, partner, or competitor purpose.

## Data Gaps

## Appendix: Full Task Reports

## Sources
```

Also generate `report.html` and `report.pdf` when the user asks for a complete deliverable or when
depth is `standard`/`deep`.

HTML/PDF requirements:

- cover page with company, purpose, date, scope, and source count;
- table of contents;
- clear H1/H2/H3 hierarchy;
- readable financial, competitor, customer/supplier, and hiring tables;
- local image paths under `images/`;
- source appendix and data gaps.

## ChangXin-Style Coverage Stress Test

For a strategic private/IPO-track semiconductor company such as 长鑫科技 / 长鑫存储 / CXMT, the skill
should cover at least:

- identity lock: 长鑫科技集团股份有限公司 vs 长鑫存储品牌/主体 and official domain;
- listing status: IPO/prospectus/regulatory files, sponsor reports, exchange inquiries and replies;
- history: founding, fabs, capacity, milestones, technology generations;
- products: DDR, LPDDR, modules, process/packaging signals, product pages, patent evidence;
- industry position: DRAM market share, China/global ranking, competitors Samsung/SK hynix/Micron and domestic ecosystem;
- financials: revenue, profit, gross margin, assets/liabilities, capex, R&D, forecast, accounting basis;
- ownership: shareholders, state capital, employee share plans, related parties, lockups;
- customers: disclosed customers, verified media claims, application fields, consumer/PC/server/mobile channels;
- suppliers: semiconductor equipment, materials, EDA/IP, interface chips, packaging/testing, disclosed related listed companies;
- hiring/org: job postings, R&D roles, fab operations, leadership, employer-risk signals;
- risk: export controls, IP disputes, cycle volatility, customer concentration, supply-chain dependence, IPO risk factors;
- white-collar decision layer: should I work there, invest/watch the IPO, sell to them, partner with them, or benchmark them.

If any item is not publicly verifiable, keep it as `缺少数据：...`.

## Quality Gates

Before final delivery:

- Official identity and similar-name risks are resolved.
- `keyword_matrix.md` exists and has a second expansion pass for standard/deep runs.
- Every source has tier, extraction method, fetch status, and confidence.
- Every important number has a source mark or is marked `待核实`.
- Financial data has period, currency, unit, accounting basis, and page/section when available.
- T3 evidence is marked weak and not used for precise facts.
- Browser/CDP observations are logged.
- Missing data is explicit.
- HTML/PDF renders locally when generated.
- Raw task files remain available; do not only deliver a polished summary.

## Public Data And Ethics

This skill supports legitimate public company research and user-authorized browser sessions. It does
not support credential misuse, evading access controls, private system extraction, personal contact
harvesting, or private email/phone guessing.
