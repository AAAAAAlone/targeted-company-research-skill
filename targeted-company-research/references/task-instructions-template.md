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
| `{PURPOSE}` | job_search, investment, ABM, competitor, partner, supplier, or general |

## Shared Task Rules

- Work only on the assigned task.
- Use `keyword_matrix.md` before searching; add new terms discovered during the task.
- Use search for breadth, then fetch/capture full sources for facts.
- Search snippets are discovery only, not final evidence.
- Use browser/CDP when static fetch fails on public or user-authorized pages.
- Save browser/CDP notes in `projects/{PROJECT}/evidence/browser_notes.md`.
- Save raw source extracts under `projects/{PROJECT}/sources/`.
- Add source marks `[Sxx]` to material claims.
- Mark estimates and missing facts explicitly.
- Do not read other task folders until final merge.
- Do not collect private personal contact information or guess private emails/phones.
- Update `task_status.md` after finishing.

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

## Tasks

| Task | Folder | Status | Source target |
|---|---|---|---:|
| Task 1 | task1_identity_finance | pending | 15+ |
| Task 2 | task2_product_technology | pending | 15+ |
| Task 3 | task3_industry_competition | pending | 12+ |
| Task 4 | task4_customers_suppliers | pending | 15+ |
| Task 5 | task5_people_org_narrative | pending | 15+ |
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
- sources.
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
- sources.
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
- competitor matrix with at least five competitors for standard/deep research;
- market share/ranking evidence and confidence;
- policy/geopolitical risks;
- opportunities, threats, and implications for {SHORT};
- sources.
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
- sources.
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
- sources.
```

## Merge Template

```markdown
# {COMPANY} Targeted Company Research Report

> Research date: {DATE}
> Purpose: {PURPOSE}
> Source count: {SOURCE_COUNT}
> Confidence: high / medium / low

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

## Appendix: Full Task Reports

## Sources

| ID | Tier | Task | Title | URL/File | Extraction | Status | Notes |
|---|---|---|---|---|---|---|---|
```
