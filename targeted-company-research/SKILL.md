---
name: targeted-company-research
description: >-
  为指定公司生成有来源支撑的正式深度公司研究报告。适用于求职研究、投资或尽调、ABM 销售准备、
  竞品分析、合作伙伴或供应商研究、方案准备，以及需要拓展关键词、广泛搜索、fetch/浏览器访问
  原始来源、建立证据索引、记录数据缺口，并输出 30+ 页本地 Markdown + HTML + PDF 的公司深度研究任务。
metadata:
  short-description: 有来源支撑的公司深度研究报告
  version: "2026.06.15"
---

# 定向公司研究

## 触发场景

当用户要求深入研究一个明确的公司、品牌、子公司、上市主体、竞品、客户、供应商、经销商或投资标的时，使用本 skill。

典型请求：

- "帮我全面了解这家公司"
- "我要面试/跳槽，帮我看这家公司值不值得去"
- "我想投资/尽调这家公司，帮我看基本面、股权、客户、供应商、行业地位"
- "帮我研究一个目标客户，用于 ABM / 销售拜访"
- "帮我看某家公司和竞品、上下游、风险、近期新闻"
- "帮我先研究这家公司，再做方案/提案/客户拜访准备"

如果用户没有给出明确公司，不要用这个 skill 做泛行业报告。

## 必要输入

能稳妥推断时可以推断，但进入深度研究前必须锁定目标公司身份。

| 字段 | 含义 | 默认值 |
|---|---|---|
| Target company | 法定名称、常用名、品牌名或股票代码 | 必填 |
| Website | 官方网站 | 查找并核验 |
| Industry | 主营行业 | 基于证据推断 |
| Geography | 总部和重点市场 | 总部国家/地区 + 目标市场 |
| Purpose | job_search, investment, ABM, proposal, competitor, partner, supplier, general | general |
| Language | 报告语言 | 用户使用的语言 |

本 skill 只有正式研究模式，不提供 light、standard、deep 三档。基础信息汇总不叫调研；如果无法完成正式研究门槛，不能把缩水结果包装成最终报告，只能输出 `INCOMPLETE_RESEARCH.md`、`data_gaps.md` 和补采清单。

按目的调整重点：

- `job_search`：组织、招聘、领导层、文化、业务健康度、增长、风险、薪酬信号。
- `investment`：财务、股权、上市/融资、市场位置、客户/供应商、风险、估值信号。
- `ABM`：业务地图、公开战略、决策角色、采购触发点、沟通话术、切入角度。
- `proposal`：业务优先级、痛点、战略动作、方案匹配度、利益相关方叙事。
- `supplier/partner`：产品匹配、渠道、采购、合规、客户案例、生态位置。
- `competitor`：产品、价格、技术、市场份额、客户、渠道打法、弱点。

目的只改变研究加权，不改变基础覆盖范围。无论用户选择哪种目的，都必须覆盖身份、股权/财务、产品/技术、行业趋势、竞争格局、客户/渠道、供应链/生态、组织招聘、营销叙事和风险。不同目的只是在以下方面加深：

- 增加对应维度的关键词种子和搜索次数。
- 覆盖更多搜索结果页和更多来源类型。
- fetch 更多同一主题下的原始来源。
- 最终报告增加该目的相关的判断、表格、启示和行动建议。

目的加深要求：

| Purpose | 额外加深方向 | 最终报告增加内容 |
|---|---|---|
| job_search | 招聘岗位、组织扩张、领导层、薪酬、文化、员工评价、业务健康度 | 值不值得去、适合什么岗位、面试问题、风险提醒 |
| investment | 财务、股权、上市/融资、客户集中、供应链依赖、行业周期、监管风险 | 投资观察点、关键数据表、风险清单、待核实事项 |
| ABM | 业务优先级、公开项目、决策角色、采购触发、活动/内容、合作伙伴 | 账户地图、切入角度、话术方向、可验证触发事件 |
| proposal | 战略动作、痛点、现有方案、竞品弱点、预算/采购信号、行业趋势 | 方案假设、客户问题列表、价值主张、提案结构建议 |
| competitor | 产品对比、价格/渠道、客户、技术差异、营销叙事、弱点 | 竞品矩阵、优势/劣势、可攻击点、替代关系 |
| partner/supplier | 产品匹配、认证、渠道、采购、供应链、合规、客户案例 | 合作可行性、准入条件、依赖风险、下一步验证清单 |

## 核心流程

每一个研究任务都必须完成同一个四步循环：

1. 拓展关键词。
2. 搜索候选结果。
3. fetch、下载、抽取或浏览器访问原始来源。
4. 只基于已访问的证据进行结构化整理。

5 个标准研究任务只是覆盖范围模板，不是流程本身。不要用搜索摘要直接写最终结论。必须完成四步循环和质量门槛，或者明确记录阻塞原因后，才可以合并最终报告。

禁止偷懒规则：

- 不允许只做公司简介、官网摘要、新闻摘要或基础资料表。
- 不允许因为用户没有给出方向，就降低研究范围或缩短报告。无方向时按 `general` 目的执行完整正式研究。
- 不允许在来源数量、搜索次数、章节质量、证据型附录或 PDF 页数未达标时生成 `FINAL_REPORT.md` 作为正式交付。
- 不允许用搜索结果摘要、模型记忆或未访问页面填充关键事实。
- 不允许在 fetch 前因为标题相似、摘要相似或转载痕迹删除候选来源。
- 不允许合并时只保留摘要。最终报告必须包含整合版正文和 `Appendix: Evidence Tables And Lists`，附录中保留正文未展开的证据表、清单、线索和缺口，不重复正文摘要。
- 不允许在最终合并时重写、压缩、改写或删除已经冻结的章节文件。
- 不允许在每个章节末尾重复粘贴完整来源表；正文只写 `[Sxx]` 来源标记，完整来源表只放在最终报告最底部。

## 项目初始化

开始收集来源前，先创建本地项目结构：

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
│   ├── 00_cover.md
│   ├── 01_toc.md
│   ├── 02_executive_takeaways.md
│   ├── 10_company_identity_finance.md
│   ├── 20_products_technology.md
│   ├── 30_industry_competition.md
│   ├── 40_customers_suppliers_channels.md
│   ├── 50_people_org_narrative.md
│   ├── 60_purpose_judgment.md
│   ├── 70_data_gaps.md
│   ├── 90_appendix_task1.md
│   ├── 91_appendix_task2.md
│   ├── 92_appendix_task3.md
│   ├── 93_appendix_task4.md
│   ├── 94_appendix_task5.md
│   └── 99_sources.md
├── task1_identity_finance/task_instructions.md
├── task2_product_technology/task_instructions.md
├── task3_industry_competition/task_instructions.md
├── task4_customers_suppliers/task_instructions.md
├── task5_people_org_narrative/task_instructions.md
├── sources/
├── evidence/
└── images/
```

`task_status.md` 必须记录每个任务的执行数量：

```markdown
| Task | Status | Keyword seeds | Searches run | Candidates | Fetched/captured | Findings | Data gaps |
|---|---|---:|---:|---:|---:|---|---|
| Task 1 | pending | 0 | 0 | 0 | 0 | - | - |
```

状态值固定为：`pending`, `running`, `done`, `blocked`, `skipped`。

`section_status.md` 必须记录每个报告章节是否已经冻结：

```markdown
| Section | File | Status | Min length | Tables | Source marks | Frozen |
|---|---|---|---:|---:|---:|---|
| Company identity and finance | sections/10_company_identity_finance.md | frozen | pass | 2 | 12 | yes |
```

状态值固定为：`pending`, `drafting`, `ready_for_freeze`, `frozen`, `blocked`。

## 第一步：拓展关键词

搜索前必须先创建 `keyword_matrix.md`。正式研究至少需要覆盖全项目 120 个关键词种子。每个标准任务至少 20 个查询种子，目的相关任务需要 25 个以上。

关键词矩阵必须覆盖，但不要平均分配。身份锁定类词少而准；行业动态、趋势、竞争力、供应链、优势、营销和客户相关词要更细、更密。

| 维度 | 查询种子 |
|---|---|
| Identity lock | 法定名称、常用名、中英文名、股票代码、官网域名、子公司、曾用名、同名公司排除 |
| Ownership/finance | 股东、融资、IPO、招股书、估值、收入、毛利率、资本开支、现金流、债务、关联方 |
| Product/technology | 产品线、型号、规格、技术路线、专利、认证、标准、路线图、产品迭代 |
| Market dynamics | 行业规模、增长率、周期、价格趋势、需求变化、政策变化、区域市场、下游变化 |
| Competition/advantages | 竞品、市场份额、排名、替代品、差异化、成本优势、技术优势、渠道优势、品牌优势、护城河 |
| Customer/channel | 客户、案例、应用场景、经销商、渠道、OEM/ODM、招投标、采购资格、销售区域 |
| Supplier/ecosystem | 供应商、设备、材料、外协、EDA/IP、物流、采购、进出口、生态伙伴、依赖风险 |
| Marketing/narrative | 官网新闻、发布会、展会、白皮书、案例、社媒、内容营销、媒体采访、品牌叙事、活动赞助 |
| People/org | 创始人、CEO、CFO、CTO、管理层、招聘、岗位、裁员、薪酬、文化、组织扩张 |
| Risk/compliance | 诉讼、制裁、出口管制、安全、召回、监管处罚、知识产权争议、舆情风险 |
| Source operators | `site:`, `filetype:pdf`, 精确引号、OR 组合、日期词、交易所/注册机构名称 |

正式研究的关键词种子最低配额：

| 维度 | 最低种子数 | 说明 |
|---|---:|---|
| Identity lock | 4-6 | 只用于身份锁定和同名排除，不要消耗过多搜索预算 |
| Ownership/finance | 12-18 | 投资/尽调目的提高到 20+ |
| Product/technology | 15-22 | 竞品、供应商、方案目的提高到 25+ |
| Market dynamics | 18-25 | 必须覆盖趋势、周期、政策、区域和需求变化 |
| Competition/advantages | 18-25 | 必须覆盖竞品、差异化、替代品和竞争力证据 |
| Customer/channel | 15-22 | ABM、方案、供应商/合作目的提高到 25+ |
| Supplier/ecosystem | 15-22 | 供应链、制造、硬科技公司提高到 25+ |
| Marketing/narrative | 12-18 | ABM、方案、品牌/营销研究提高到 20+ |
| People/org | 10-15 | 求职目的提高到 20+ |
| Risk/compliance | 8-12 | 投资/尽调、跨境、监管敏感行业提高到 15+ |

拓词规则：

- 先用精确公司名、法定名称、品牌名和官网域名，再使用宽泛词。
- 每个标准任务至少生成 20 个查询种子，但不要把种子平均浪费在身份名、别名和泛叙事词上。
- 涉及上市、监管、专利、认证、招聘、活动、PDF 时，必须加入权威站点搜索词。
- 根据目的加入求职、投资、ABM、方案、合作伙伴、供应商或竞品相关词。
- 对行业动态、趋势、竞争力、供应链、优势、营销信息，要用更具体的问题扩展种子词，例如“为什么增长/下滑”“客户采购什么”“供应商依赖谁”“渠道怎么卖”“竞品强在哪里”“公司最近在讲什么战略”。
- 找到前 8-12 个有用来源后，必须进行第二轮拓词。新增产品名、管理层姓名、子公司、客户、供应商、竞品、文件名称、活动名称、标准、风险词和岗位族。

## 第二步：搜索候选结果

搜索要模拟真实高意向用户寻找高质量信息的过程。正式研究至少需要全项目 100 次搜索，每个标准任务至少 20 次搜索。目的相关任务、信息稀缺任务和发现新实体后的二轮搜索不能低于 25 次。

最低搜索次数：

| 模式 | 每个标准任务 | 全项目 |
|---|---:|---:|
| formal | 20+ | 100+ |

优先使用可用的搜索路线：

1. 通用网页搜索，用于广泛发现。
2. `site:` 和 `filetype:pdf` 权威站点搜索。
3. 公司官网、IR、招聘、产品、新闻、下载页。
4. 交易所、注册机构、专利、认证、法院、海关、招投标、活动、行业协会等公开数据库。
5. 可用时使用 OpenSEO skills/MCP 做关键词研究、SERP 检查、域名对比和搜索结果质量检查。
6. 已有凭证或用户批准时，使用 DataForSEO MCP 查询 Google/Bing/Yahoo SERP、搜索量、CPC、Labs、OnPage、域名/搜索数据。

搜索结果筛选规则：

- 优先 T0/T1 权威来源，不优先二手总结。
- 来源组合要平衡：官方、监管、行业、媒体、客户/供应商、招聘、活动。
- 已知白名单优先：官网、交易所、注册机构、专利/认证库、法院、行业协会、展会、年报、招股书、可信媒体。
- 没有现成白名单时，实时建立优质网站列表：被官方文件、行业协会、展会、客户/供应商披露或多个独立可信来源反复引用的网站优先。
- 有价值的候选结果即使暂时没有 fetch，也要先记录。
- 搜索摘要只能用于发现候选来源，不能作为最终事实依据。

## 第三步：访问和抽取来源

必须 fetch、下载、抽取或浏览器访问足够的原始来源来支撑报告。正式研究至少需要 70 条候选来源记录、45 个 fetch 或浏览器访问成功来源、35 个高质量来源。每个标准任务至少 fetch/访问 9 个来源；目的相关任务至少 12 个。

最低来源数量：

| 模式 | 候选来源记录 | fetch/浏览器访问来源 | 高质量来源 |
|---|---:|---:|---:|
| formal | 70+ | 45+ | 35+ |

来源层级：

1. T0：监管文件、交易所披露、招股书、法院记录、专利/认证数据库、官方注册机构、海关/进出口记录。
2. T1：官网、IR 页面、年报、产品文档、产品目录 PDF、官方新闻、官方社媒、官方招聘页。
3. T2：可信媒体、行业协会、展会、经销商、市场平台、分析/研究报告、客户或供应商披露。
4. T3：估算网站、线索数据库、论坛、评价网站、雇主评价、社交平台。只能作为弱证据或信号。

抽取方式：

```text
search_tool | search_snippet_only | web_fetch | direct_download | pdf_text | ocr | headless_browser | cdp_browser | user_provided
```

访问状态：

```text
fetch_success | fetch_partial | fetch_blocked | fetch_render_required | fetch_ocr_required | source_unavailable | source_conflict
```

在 `source_index.md` 中记录来源：

```text
id | tier | task | title | publisher | date | url_or_file | extraction_method | fetch_status | confidence | notes
```

静态 fetch 失败时：

1. 尝试直接下载或 PDF 抽取。
2. 对公开 JS 渲染页面尝试 headless browser。
3. 尝试 in-app browser 或后台浏览器上下文。
4. 仅在公开页面或用户授权会话中，用独立 profile 的 Chrome CDP。
5. 无法安全访问时，将来源标记为 blocked 或 unavailable。

不要绕过付费墙、验证码、登录墙、robots 限制或访问控制。不要收集私人联系方式，不要猜测私人邮箱或手机号。

## 去重规则

不要在 fetch 前因为标题相似、摘要相似或媒体转载痕迹就删除候选结果。很多标题相近的文章内部引用、数据来源、采访对象、披露日期、客户/供应商名称和风险描述并不相同。

正确流程：

1. 先记录候选 URL、标题、发布方、日期、搜索词和初步判断。
2. 对候选结果进行 fetch、PDF 抽取或浏览器访问，拿到原始正文。
3. 再基于正文内容、引用对象、数据点、来源层级、发布日期、支持的事实和任务归属去重。
4. 对完全重复的转载或镜像，保留来源层级更高、日期更早或正文更完整的一条。
5. 对标题相似但证据不同的来源，不要合并为一条；应分别保留，并在整理时交叉验证。
6. 对同一来源支持多个事实的情况，保留一条来源记录，但在 notes 中说明它支持哪些任务或结论。

去重发生在“已记录候选结果并 fetch 足够高质量来源之后”，不能发生在搜索摘要阶段。

## 第四步：结构化整理证据

只在 fetch 或浏览器访问完成后写结论。每个重要判断都要有来源标记，例如 `[S12]`。没有来源的数字必须标记为 `待核实` 或 `缺少数据：...`。

整理规则：

- 先写结论：具体对象、明确判断、数据或来源依据。
- 保留原始数字、日期、公司名、人名、产品名、来源名和短代表性原话。
- T3 来源必须标记为弱证据，不能用于精确事实。
- 来源冲突要明确说明。
- 重要但无法验证的信息写入 `data_gaps.md`。
- 保留原始任务文件，不要只交付一份润色后的摘要。

## 正式研究任务模板

正式报告默认执行以下 5 个任务，除非用户明确缩小范围。每个任务都必须完成上面的四步循环。即使用户只说“调研这家公司”，也不得减少任务数量。

| Task | 重点 | 最少查询种子 | 最少搜索次数 | 最少 fetch/访问来源 |
|---|---|---:|---:|---:|
| Task 1 | 身份、股权、财务、治理、历史 | 20 | 20 | 9 |
| Task 2 | 产品、技术、IP、认证、路线图 | 20 | 20 | 9 |
| Task 3 | 行业、竞品、市场位置、政策 | 20 | 20 | 9 |
| Task 4 | 客户、供应商、渠道、生态 | 20 | 20 | 9 |
| Task 5 | 人员、组织、招聘、叙事、ABM/求职/方案启示 | 20 | 20 | 9 |

任务覆盖范围：

1. `task1_identity_finance`：身份锁定、历史、股权、股东、治理、融资/上市、财务规模、合规、风险。
2. `task2_product_technology`：产品分类、规格、技术、专利、认证、路线图、差异化。
3. `task3_industry_competition`：价值链、市场规模、竞品、市场份额、周期、政策、战略位置。
4. `task4_customers_suppliers`：客户、供应商、伙伴、渠道、经销商、采购、生态、依赖风险。
5. `task5_people_org_narrative`：领导层、招聘、组织、文化、活动、媒体叙事、目的相关启示。

使用 `references/task-instructions-template.md` 为每个任务生成一个 `task_instructions.md`。

## 分段写作和冻结

最终报告不得一次性生成。必须先把整合版章节和证据型附录分别写入 `sections/` 下的独立 Markdown 文件。

章节文件分两类：

1. 整合版正文：`02_executive_takeaways.md`、`10_company_identity_finance.md`、`20_products_technology.md`、`30_industry_competition.md`、`40_customers_suppliers_channels.md`、`50_people_org_narrative.md`、`60_purpose_judgment.md`、`70_data_gaps.md`。
2. 证据型附录：`90_appendix_task1.md` 到 `94_appendix_task5.md`，分别沉淀公司/财务、产品、竞品、供应链、营销相关的增量证据表、清单、线索和缺口，不重复正文摘要。

每个章节冻结前必须满足：

- 至少 8 个小节；执行摘要和目录除外。
- 至少 1500 个中文字符或 900 个英文单词；执行摘要和目录除外。
- 至少 2 张表格或矩阵；执行摘要、目录和数据缺口除外。
- 所有重要判断带 `[Sxx]` 来源标记，或明确写 `缺少数据：...`。
- 不包含完整来源表，不以 `## Sources`、`## 来源` 或类似来源清单结尾。
- 在 `section_status.md` 中标记为 `frozen` 后，最终合并不得再改写正文。

章节冻结规则：

- 冻结前可以补证据、补表格、补判断。
- 冻结后只允许修复明显错别字、断链、Markdown 表格语法和标题编号。
- 冻结后不允许压缩段落、删除表格、合并相似内容，或把证据型附录改成空泛摘要。

## 物理合并

最终 `FINAL_REPORT.md` 必须按 `merge_manifest.md` 中的文件顺序物理拼接，不得让模型重新生成整份报告。

`merge_manifest.md` 只保留文件路径顺序：

```markdown
- sections/00_cover.md
- sections/01_toc.md
- sections/02_executive_takeaways.md
- sections/10_company_identity_finance.md
- sections/20_products_technology.md
- sections/30_industry_competition.md
- sections/40_customers_suppliers_channels.md
- sections/50_people_org_narrative.md
- sections/60_purpose_judgment.md
- sections/70_data_gaps.md
- sections/90_appendix_task1.md
- sections/91_appendix_task2.md
- sections/92_appendix_task3.md
- sections/93_appendix_task4.md
- sections/94_appendix_task5.md
- sections/99_sources.md
```

合并前必须把 `source_index.md` 转成 `sections/99_sources.md`。这是最终报告中唯一的完整来源表。正文和证据型附录只保留 `[Sxx]` 标记，不重复粘贴来源清单。

合并时允许新增：

- 统一标题编号；
- 封面、目录和执行摘要；
- 最底部来源表；
- 最后一行展示署名。

合并时禁止：

- 重写章节正文；
- 压缩章节正文；
- 删除表格、证据或数据缺口；
- 合并相似段落；
- 把证据型附录改成正文摘要或空泛段落；
- 把完整来源表放到报告中间。

优先使用 `scripts/assemble_report.py` 执行物理合并：

```bash
python3 targeted-company-research/scripts/assemble_report.py projects/{project_slug}
```

脚本只拼接 `merge_manifest.md` 中列出的文件，不做摘要、改写、来源去重或强制分页。

不要在物理合并阶段插入 `<div style="page-break-after: always">`、`page-break-after` 或其他章节后分页标记。PDF 分页应由渲染 CSS 控制：一级章节可以 `break-before: page`，但不要同时使用“上一章 page-break-after + 下一章 h1 break-before”，否则容易产生空白页。

## 展示署名

默认报告可以保留一个轻量展示署名：

```text
@加玮营销洞察 @加玮怎么看
```

执行规则：

- 署名只用于展示，不参与研究流程、搜索、来源判断、事实结论或质量评分。
- 署名只能放在 Markdown 文档最后一段，或 PDF 最后一页底部一行小字。
- 不要把署名放在封面、副标题、目录、页眉、页脚或正文页面。
- 不要把署名写成来源、赞助声明、数据来源或事实依据。
- 用户要求白标、匿名或纯内部报告时，删除署名。
- 不要把署名放进 `source_index.md`，也不要给它分配来源 ID。

## 报告输出

`FINAL_REPORT.md` 应包含：

```markdown
# {Company} Targeted Company Research Report

> Research date: {date}
> Purpose: {purpose}
> Source count: {N}
> Confidence: high / medium / low

## Executive Takeaways
10-15 条带来源标记的具体结论。每条使用 `**判断标签：**` 开头，或用 `summary-box` 等浅色高亮块呈现，避免写成普通长列表。

## 1. Identity, History, Ownership And Finance

## 2. Products, Technology And IP

## 3. Industry Position And Competitors

## 4. Customers, Suppliers, Channels And Ecosystem

## 5. People, Organization, Hiring And Public Narrative

## Purpose-Specific Judgment

## Data Gaps

## Appendix: Evidence Tables And Lists

## Sources

---

<small>@加玮营销洞察 @加玮怎么看</small>
```

必须生成 `report.html` 和 `report.pdf`。正式报告的 PDF 正文目标是 50+ 页；无论目标公司信息多少，最低不得少于 30 页。若 PDF 少于 30 页，必须回到证据型附录、证据表、竞品矩阵、客户/供应链表、产品型号表、来源附录和数据缺口继续展开，而不是交付短报告。

正式交付文件必须同时生成规范命名版本：`{公司名}_jiascan_report_v1.0.md`、`{公司名}_jiascan_report_v1.0.html`、`{公司名}_jiascan_report_v1.0.pdf`。同一公司多轮生成时递增小版本号，例如 `v1.1`、`v1.2`；不要用重复的 `report(1).pdf`、`final_new.pdf`、`最新版.pdf` 作为交付名。

最终报告必须采用“双层结构”，但附录不得重复正文：

1. 前半部分是整合版深度报告：核心结论、公司基础、产品技术、行业竞争、客户供应链、组织叙事、目的判断、数据缺口。
2. 后半部分是 `Appendix: Evidence Tables And Lists`：只放正文没有完整展开的证据表、清单、原始来源摘录、竞品拆解、展会明细、供应链线索和待核实事项；不要机械粘贴 Task 1-5 全文。

证据型附录最低要求：

- 公司与财务附录：身份锁定表、关键财务表、募资用途表、治理/风险线索、缺失数据清单。
- 产品附录：产品型号/系列、负载或应用场景、认证/配件/生态、案例样本、缺失数据清单。
- 竞品附录：UR/JAKA/AUBO/Elite/ABB/FAIRINO 等官网、案例库、展会、产品叙事和营销主轴逐项对比。
- 供应链附录：供应商线索表、零部件类别表、采购占比表、国产替代/多供应商风险表、待核实名单。
- 营销附录：展会清单、伙伴会清单、案例库样本、竞品营销素材清单、国内外渠道或社媒缺口。
- 来源附录：所有访问过的来源、fetch 状态、可信度、对应结论或用途。

如果某一项没有找到足够公开证据，必须在附录表格中写 `缺少数据：...`，并给出下一步搜索路线。不要用泛泛段落填充。

最终报告必须采用“末尾来源”规则：

- 正文、整合章节和证据型附录只出现 `[Sxx]` 引用标记。
- 不在每个章节或每个附录后面重复放来源清单。
- `## Sources` 是最终报告倒数第二个板块，只出现一次，位于全部正文和全部证据型附录之后。
- 展示署名是最终报告最后一行，位于来源表之后。

内容量最低要求：

- `Executive Takeaways`：10-15 条结论，每条必须有来源标记或明确数据缺口；关键判断必须加粗或放入浅色高亮块。
- 每个核心章节至少 5 个二级小节、2 张表格或矩阵、1 段判断。
- 每个证据型附录至少 3 张表格或清单，必须提供正文未完整展开的增量信息；没有增量信息时写成缺口表，不得重复正文段落。
- `Sources` 附录至少 35 个高质量来源；不足则不能标记为正式完成。

## HTML/PDF 设计规则

`report.html` 和 `report.pdf` 必须包含：

- 封面：公司名、研究目的、研究日期、来源数量、置信度。封面不放展示署名。封面必须像正式报告封面，而不是普通正文页。
- 页数：PDF 最低 30 页，正式目标 50+ 页；封面可标注来源数量和页数目标。
- 页眉：正文页显示当前一级章节短标题，右侧显示报告短标题。
- 页脚：显示当前页码和总页数，例如 `6 / 33`。
- 简单目录：只列一级板块，使用 `1、2、3、4、5、6...` 结构。目录应是独立目录页，而不是普通列表。
- 目录摘要：每个一级板块配 1 句短摘要，不超过 30 个中文字符或 18 个英文单词。
- 清晰层级：H1/H2/H3 明确，正文不要用过深标题层级。
- 关键表格：财务、竞品、客户/供应商、招聘、风险和数据缺口表格要可读。
- 来源附录：保留来源 ID、标题、发布方、URL/文件、访问方式、状态和备注。
- 现代感视觉：留白充足、字体清晰、颜色克制，适合屏幕阅读和打印。
- 最后一页署名：PDF 最后一页来源表之后保留一行小字 `@加玮营销洞察 @加玮怎么看`，字号小、低干扰；正文页和封面不出现署名。不要让署名单独占一页。

封面设计规则：

- 在 Codex 或可用图像生成环境中，优先生成无文字封面背景图：机器人、工厂自动化、抽象网格、深色/浅色留白、适合压字。生成图放入 `images/cover-background.png`，封面文字由 HTML 覆盖，避免图片文字乱码。
- 无法稳定生成或落地图片时，用 HTML/CSS 做封面背景，例如深色渐变、斜向金属色块、细网格纹理和咨询报告式排版。
- 封面文字必须有足够对比度。深色背景用白字，浅色背景用深色字，标题区不得压在复杂图像上。
- 封面应包含报告标题、副标题、研究日期、目标公司、来源数量和置信度；这些信息可以保留，但必须以封面排版呈现。
- 封面不显示页眉、报告页脚或展示署名。

目录页设计规则：

- 目录应作为完整一页设计，可以用两列网格、编号、标题、短描述和分隔线。
- 根据目录项数量调整间距、字号和列数。8-12 项优先两列；少于 6 项可以单列加大间距。
- 目录只写一级板块和一句摘要，不放 H3/H4，不自动抓取所有标题。

分隔页规则：

- 附录和大板块分隔页不要使用 `Appendix Task 4` 这类工作流名称。
- 使用读者可理解的正式标题，例如 `附录四｜供应链与渠道分析`、`附录五｜营销与展会分析`。
- 分隔页应居中或垂直居中，使用更大标题、短描述、英文装饰性 kicker，例如 `APPENDIX 04`。
- 分隔页是视觉过渡，不承担正文解释；正文标题在下一页继续。
- 分隔页本身就是附录封面；分隔页后不要再出现同名标题页，例如不要再写一页 `# 附录五｜营销与展会分析`。
- 附录正文开始时使用二级标题或正文小节，例如 `## 5. 营销、展会与竞品营销`，不要使用新的 H1 触发单独标题页。
- CSS 中分隔页应 `break-before: page` 和 `break-after: page`，确保分隔页独立，正文从下一页直接开始。

小结高亮规则：

- 每个核心章节和证据型附录结尾应有 `小结` 或 `本章结论`。
- 小结不要写成普通段落堆叠。使用浅色背景、左侧强调线、加粗关键词或 2-4 条短句，突出判断层次。
- 小结中的关键对象、数字、风险和动作建议应加粗，例如 `**直接材料占比**`、`**海外展会应用包**`、`**实名案例不足**`。

优先使用 `scripts/render_report.py` 生成 HTML/PDF：

```bash
python3 targeted-company-research/scripts/render_report.py projects/{project_slug} --header-title "{Short Report Title}"
```

正式交付时必须带规范命名参数：

```bash
python3 targeted-company-research/scripts/render_report.py projects/{project_slug} --header-title "{Short Report Title}" --basename "{公司名}_jiascan_report" --version "v1.0"
```

如果未指定 `--version`，脚本会扫描同目录已存在的 `{公司名}_jiascan_report_v*.pdf` 并递增小版本号。

该脚本使用 Chrome 渲染正文，再用 PyMuPDF 添加页眉、页脚、当前章节和页码。若改用其他渲染方式，也必须保留相同效果。

空白页处理规则：

- 不要用内容硬填空白页；空白页通常是分页规则冲突，应删除冗余分页。
- 只能在一级章节前分页，不在章节后强制分页。
- 封面、目录、执行摘要可以单独起页，但不得出现完全空白页。
- PDF 生成后必须检测空白页；若有接近空白页面，先检查 `page-break-after`、`break-before` 和空 section。
- 署名必须跟随 `Sources` 表自然流动，不能被单独分页。

目录稳定性规则：

- 不要用自动目录脚本抓取所有标题。
- 不要把 H3/H4、小节标题、长问题句放进目录。
- 不要在目录中嵌套多级列表。
- 目录只保留最终报告主板块，例如：

```markdown
## 目录

1. 核心结论：公司最重要的 10-15 个判断。
2. 公司基础：身份、历史、股权、财务和治理。
3. 产品与技术：产品线、技术、认证和路线图。
4. 行业与竞争：趋势、竞品、优势和风险。
5. 客户与供应链：客户、渠道、供应商和生态。
6. 组织与叙事：招聘、管理层、营销和公开叙事。
7. 目的判断：围绕求职、投资、ABM、方案或合作的结论。
8. 数据缺口与来源：未验证事项和来源附录。
```

PDF 生成后必须检查封面、目录、表格、页码、来源附录和最后一页小字署名是否渲染正常。目录崩溃时，优先删减目录项和缩短目录摘要，而不是增加样式复杂度。

## 质量门槛

最终交付前必须满足：

- 官方身份和同名公司风险已经解决。
- `keyword_matrix.md` 存在，并达到 120+ 个关键词种子。
- 完成第二轮关键词拓展。
- `task_status.md` 记录每个任务的关键词数、搜索数、候选来源数、fetch/访问来源数。
- 至少完成 100 次搜索、70 条候选来源记录、45 个 fetch/访问来源、35 个高质量来源，除非明确阻塞。
- 每个任务至少 20 个查询种子、20 次搜索、9 个 fetch/访问来源。
- 每个来源都有层级、抽取方式、访问状态和置信度。
- 每个重要数字都有来源标记，或标记为 `待核实`。
- 财务数据有期间、币种、单位、会计口径，以及可用时的页码/章节。
- T3 证据标记为弱证据，不用于精确事实。
- 浏览器/CDP 观察记录已经写入。
- 缺失数据明确写入 `data_gaps.md`。
- 已经生成 `report.html` 和 `report.pdf`。
- PDF 不少于 30 页；正式目标为 50+ 页。
- HTML/PDF 本地渲染通过，封面、简单目录、正文层级、关键表格和来源附录没有明显错位或溢出。
- 原始任务文件仍然保留。

未达标处理：

- 不要生成短版 `FINAL_REPORT.md` 冒充正式报告。
- 生成 `INCOMPLETE_RESEARCH.md`，第一屏写明未达标项。
- 在 `task_status.md` 中标明每个任务缺口。
- 在 `data_gaps.md` 中列出下一轮必须补采的关键词、来源类型、搜索路线和阻塞原因。
- 只有用户明确要求“先看半成品”时，才可以交付未完成稿，并且标题必须标注“未完成研究稿”。

## OpenClaw 和 Codex 执行说明

OpenClaw 在通过子代理执行任务说明时，可能更容易完整遵循流程。Codex 单线程执行时，必须用可见的本地检查点补偿：`keyword_matrix.md`、`source_index.md`、`task_status.md`、`data_gaps.md`，以及每个任务一个任务文件。

Codex 不要在 fetch 前压缩看起来相似的来源。必须先记录候选 URL，并 fetch 足够多的高质量来源，再做去重。多个相似结果如果来自不同来源层级、不同日期、不同实体、不同引用对象或不同任务范围，都可能有研究价值。

## 公开数据和伦理边界

本 skill 只支持合法的公开公司研究和用户授权的浏览器会话。不支持滥用凭证、绕过访问控制、提取私有系统、批量收集个人联系方式，或猜测私人邮箱/手机号。
