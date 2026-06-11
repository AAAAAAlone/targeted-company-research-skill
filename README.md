# Targeted Company Research Skill

`targeted-company-research` is a local-first company deep-dive skill. It turns one named company into
a source-backed business map for job search, investment or light diligence, ABM sales preparation,
competitor tracking, partner research, supplier research, and strategic account planning.

## What It Covers

- Identity, history, legal entity, ownership, shareholders, subsidiaries.
- Financial scale, IPO/listing/financing status, revenue, profit, margin, capex, risk factors.
- Products, technology, patents, certifications, roadmap, technical differentiation.
- Industry structure, market position, competitors, market share, policy and cycle risk.
- Customers, suppliers, channels, distributors, ecosystem, procurement signals.
- People, leadership, organization, hiring, culture and employer signals.
- Marketing, events, media narrative, public stakeholders and ABM entry angles.
- Purpose-specific judgment for job seekers, investors, sales teams, partners or competitors.

## Output

Default output is a local project folder:

```text
projects/{project_slug}/
├── task_plan.md
├── task_status.md
├── keyword_matrix.md
├── source_index.md
├── data_gaps.md
├── task1_identity_finance/task_instructions.md
├── task1_identity_finance/task1_identity_finance.md
├── task2_product_technology/task_instructions.md
├── task2_product_technology/task2_product_technology.md
├── task3_industry_competition/task_instructions.md
├── task3_industry_competition/task3_industry_competition.md
├── task4_customers_suppliers/task_instructions.md
├── task4_customers_suppliers/task4_customers_suppliers.md
├── task5_people_org_narrative/task_instructions.md
├── task5_people_org_narrative/task5_people_org_narrative.md
├── sources/
├── evidence/
├── images/
├── FINAL_REPORT.md
├── report.html
└── report.pdf
```

No external delivery, image hosting, CRM upload, Feishu/Slack/Drive sending, or private contact
collection is used by default.

## Search Logic

The skill starts with a keyword matrix, then searches and fetches evidence.

Search routes:

- OpenSEO skills/MCP for keyword research, SERP inspection, domain comparison and AI visibility.
- DataForSEO MCP for Google/Bing/Yahoo SERP, keyword volume, CPC, Labs, OnPage and AI Optimization data.
- General web search.
- Authority-site search with `site:` and `filetype:pdf`.
- Direct official site, exchange, registry, patent, certification, job and event searches.
- Browser/CDP fallback when static fetch fails.

OpenSEO optional install:

```bash
npx skills add every-app/open-seo --skill '*' --agent codex
```

DataForSEO MCP optional:

```bash
npx dataforseo-mcp-server@latest
```

Search snippets only discover candidates. Final claims require fetched source text, PDF extraction,
browser capture, or user-provided evidence.

## Example: ChangXin / CXMT-Style Research

For a company like 长鑫科技 / 长鑫存储 / CXMT, the skill should be able to cover:

- legal identity and brand/entity relationship;
- IPO/prospectus/exchange disclosure status;
- founding history, fabs, capacity, products and technology generations;
- DRAM industry position, global competitors and domestic ecosystem;
- revenue, profit, margin, assets, liabilities, capex, R&D and forecast where disclosed;
- ownership, shareholders, state capital, employee plans and related parties;
- customers and application fields;
- suppliers, equipment/materials/EDA/IP ecosystem and supply-chain risks;
- hiring demand, leadership, culture and employer signals;
- risks including export controls, IP disputes, memory-cycle volatility and IPO risk factors;
- white-collar decision layer: whether to work there, watch/invest, sell to them, partner with them or benchmark them.

Anything not publicly verifiable must be written as `缺少数据：...`.

## Install

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo AAAAAAlone/targeted-company-research-skill \
  --path targeted-company-research \
  --method git
```

Restart Codex after installation.

## Usage Examples

```text
Use $targeted-company-research to research 长鑫科技 / 长鑫存储 for job-search and investment understanding. Output Chinese Markdown + HTML + PDF. Focus on identity, IPO, financials, DRAM industry position, customers, suppliers, hiring and risks.
```

```text
Use $targeted-company-research to research Universal Power Group for ABM sales preparation. Output in Chinese. Focus on products, distributors, competitors and public decision makers.
```

```text
Use $targeted-company-research to research {公司名}. 重点看产品线、渠道、竞品、客户供应商、组织招聘和数据缺口，输出中文报告，保留来源标注。
```

## Repository Structure

```text
targeted-company-research/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── research-playbook.md
    └── task-instructions-template.md
```

## Data Boundary

This skill supports legitimate public business research and user-authorized browser sessions.

Allowed:

- public business names and roles;
- official profile URLs;
- public event, speech, press, filing, job and product pages;
- official company contact channels.

Not allowed:

- bypassing login, paywalls, captchas or access controls;
- extracting private systems;
- guessing private emails or phone numbers;
- bulk personal contact harvesting;
- using leaked credentials, cookies or tokens.

## License

MIT License.
