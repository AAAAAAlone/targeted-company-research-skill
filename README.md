# 定向公司研究 Skill

`targeted-company-research` 用公开网页证据生成正式深度公司研究报告。它不是通用公司简介，也不是基础资料汇总，而是面向求职、投资、销售、方案、竞品和合作判断的定向搜索报告。

## 版本更新通知

**2026-06-15：正式研究版已更新。**

本次更新已经覆盖旧版 README 和 skill 规则，用户调用时应以当前仓库的 `targeted-company-research/SKILL.md` 为准。

最新规则包括：

- 只有正式研究模式，不再提供轻量版或基础资料版。
- 固定执行四步：拓词、搜索、访问/fetch、结构化整理。
- 正式研究门槛：120+ 关键词、100+ 搜索、70+ 候选来源、45+ fetch/浏览器访问、35+ 高质量来源。
- 最终报告必须先写入 `sections/`，再用 `merge_manifest.md` 物理合并。
- 附录改为证据型附录，不重复正文摘要。
- PDF 必须有封面、目录、页眉页脚、页码，最低 30 页，目标 50+ 页。
- 输出文件统一命名为 `{公司名}_jiascan_report_v1.0.md/html/pdf`，多轮生成递增为 `v1.1`、`v1.2`。

建议用户更新后重启 Codex，确保新的 skill 元数据和默认提示词被重新加载。

## 适用场景

- 求职研究：判断一家公司是否值得加入、增长在哪里、风险在哪里、面试应该问什么。
- 公司分析：梳理身份、股权、财务信号、产品、客户、供应商、竞品、风险和近期方向。
- 投资或轻尽调：核验披露文件、融资、收入信号、股权、市场位置、风险和数据缺口。
- ABM 和销售准备：寻找业务优先级、产品线、公开项目、决策角色、活动、伙伴和切入角度。
- 方案和提案准备：在写方案、pitch、合作计划或大客户策略前，先理解目标客户。
- 竞品追踪：比较产品、渠道、市场叙事、招聘、客户证据和弱点。
- 供应商或合作伙伴研究：核验产品匹配、采购信号、渠道、认证、生态位置和依赖风险。

不同目的不会删减研究范围。身份、财务、产品、行业、竞争、客户、供应链、组织、营销和风险都要覆盖；目的只决定哪些部分要加深，例如增加关键词、扩大搜索页、访问更多来源、最终报告增加更多判断。

## 核心逻辑

这个 skill 模拟真实高意向用户寻找高质量公司信息的过程：

1. 拓展关键词：从公司名、别名、官网、产品、行业、竞品、客户、供应商、管理层、财务、风险和目的相关问题生成搜索矩阵。
2. 搜索候选结果：通过搜索引擎、官网、权威数据库、监管文件、PDF、招聘页、活动页、媒体和行业来源进行足量搜索。
3. 访问和 fetch 来源：打开或 fetch 高质量结果，抽取网页正文或 PDF；静态 fetch 失败时才使用浏览器/CDP；记录失败或阻塞来源。
4. 结构化整理：只基于已访问来源写结论，保留来源 ID，标记弱证据，列出数据缺口，并输出本地 Markdown/HTML/PDF。

搜索摘要只能用于发现候选来源。最终事实必须来自已 fetch 的网页正文、PDF 抽取、浏览器捕获或用户提供的证据。

## 执行门槛

本 skill 只有正式研究模式，不提供轻量版。基础信息不叫调研；未达到以下门槛时，不得把结果包装成最终报告，只能输出未完成研究稿和补采清单。

- 120+ 个关键词种子；
- 100+ 次搜索；
- 70+ 条候选来源记录；
- 45+ 个 fetch 或浏览器访问成功的来源；
- 35+ 个高质量来源；
- 每个标准任务至少 20 个查询种子、20 次搜索、9 个 fetch/访问来源；
- 5 个标准任务文件和 `FINAL_REPORT.md`；
- 分段写入 `sections/`，冻结后按 `merge_manifest.md` 物理合并；
- `Appendix: Evidence Tables And Lists` 中保留证据表、清单、线索和缺口，不重复正文摘要；
- `report.html` 和 `report.pdf`；
- PDF 最低 30 页，正式目标 50+ 页；
- 对重要但无法验证的信息写入 `data_gaps.md`。

关键词不是平均分配。身份锁定类词少而准；行业动态、趋势、竞争力、供应链、优势、营销和客户相关词要更多、更细。

不允许偷懒：

- 不允许只做公司简介、官网摘要或新闻摘要。
- 不允许因为用户没有给出方向就缩短报告；无方向时按完整 `general` 调研执行。
- 不允许在 fetch 前按标题或摘要相似去重。
- 不允许使用搜索摘要直接写关键事实。
- 不允许合并时只保留摘要；最终报告必须包含整合正文和证据型附录。
- 不允许在最终合并时重写、压缩或删除已经冻结的章节。
- 不允许在每个章节后重复放完整来源表；完整来源表只放在最终报告底部。

完整执行规则在 `targeted-company-research/SKILL.md`。5 个标准研究任务只是覆盖模板；真正流程始终是：拓词、搜索、访问/fetch、整理。

## 默认输出

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
├── task1_identity_finance/
├── task2_product_technology/
├── task3_industry_competition/
├── task4_customers_suppliers/
├── task5_people_org_narrative/
├── sources/
├── evidence/
├── images/
├── FINAL_REPORT.md
├── report.html
└── report.pdf
```

默认不外发、不上传图片、不写入 CRM、不发送到 Feishu/Slack/Drive，也不收集私人联系方式。

## 分段合并

最终报告不是一次性生成，而是先把章节写成物理文件，再按 manifest 拼接：

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

每个章节冻结后不再重写。最终 `FINAL_REPORT.md` 通过 `merge_manifest.md` 物理拼接生成；拼接阶段不做摘要、不改写、不删除表格。

完整来源表只放在 `sections/99_sources.md`，也就是最终报告底部。正文和证据型附录只保留 `[Sxx]` 引用标记。

可用脚本执行拼接：

```bash
python3 targeted-company-research/scripts/assemble_report.py projects/{project_slug}
```

拼接脚本只拼接文件，不插入强制分页。不要同时使用章节后 `page-break-after` 和下一章 `h1 break-before`，否则容易生成空白页。

## 展示署名

默认报告可以保留一个轻量展示署名：

```text
@加玮营销洞察 @加玮怎么看
```

署名只出现在 Markdown 文档最后一段，或 PDF 最后一页底部一行小字。不放封面、副标题、目录、页眉、页脚或正文页面，不参与研究结论，不作为来源，不影响质量判断。若用户要求白标交付，可以删除署名。

## PDF 交付

正式研究默认生成 `report.html` 和 `report.pdf`。PDF 应包含：

- 封面：公司名、研究目的、日期、来源数量、置信度。封面不放展示署名，必须按正式报告封面设计。
- 简单目录：只列 1、2、3、4、5、6 等一级板块，避免多级目录和长标题。
- 目录摘要：每个一级板块配 1 句短摘要，帮助读者快速理解内容。
- 清晰层级：H1/H2/H3 分明，表格、图表、来源附录可读。
- 页眉页脚：正文页显示当前章节短标题、报告短标题和页码，例如 `6 / 33`。
- 现代感设计：留白充足、字体清晰、颜色克制、适合打印和屏幕阅读。
- 最后一页署名：PDF 最后一页来源表之后保留一行小字 `@加玮营销洞察 @加玮怎么看`，字号小、低干扰；不要让署名单独占一页。
- 页数要求：最低 30 页，目标 50+ 页。若不足 30 页，必须继续扩展证据型附录、证据表、竞品矩阵、产品型号表、客户/供应链表、来源附录和数据缺口。

目录不要自动抓取所有标题。目录应手写成一个简单结构，避免 HTML/PDF 渲染时因为长标题、嵌套层级或自动目录脚本导致样式崩溃。

版式要求：

- 封面优先使用无文字封面背景图，文字由 HTML 覆盖；无法生成图片时，用 CSS 渐变、色块和排版兜底。
- 目录要像目录页，可以使用两列网格、编号、短标题和摘要。
- 附录分隔页不要写 `Appendix Task 4`，改成 `附录四｜供应链与渠道分析` 这类读者可理解的标题。
- 分隔页使用大标题、短描述和英文装饰性 kicker，例如 `APPENDIX 04`。
- 分隔页就是附录封面，后面不要再单独生成同名标题页；附录正文用二级标题直接开始。
- 每章小结用浅色背景、强调线和加粗关键词增加层次，不要写成普通段落。
- 附录必须是证据型附录，不要重复正文摘要。公司/财务、产品、竞品、供应链、营销附录分别补充表格、清单、原始证据摘录、待核实事项和下一步搜索路线。
- 供应链附录至少包含供应商线索表、零部件类别表、采购占比表、国产替代/多供应商风险表、待核实名单；缺少公开证据时直接写 `缺少数据：...`。

优先用脚本生成 HTML/PDF：

```bash
python3 targeted-company-research/scripts/render_report.py projects/{project_slug} --header-title "{Short Report Title}"
```

正式交付文件使用统一命名：`{公司名}_jiascan_report_v1.0.md/html/pdf`。同一公司多轮生成时递增为 `v1.1`、`v1.2`。推荐命令：

```bash
python3 targeted-company-research/scripts/render_report.py projects/{project_slug} --header-title "{Short Report Title}" --basename "{公司名}_jiascan_report" --version "v1.0"
```

PDF 生成后检查：没有空白页；页眉页脚正常；来源表只在底部；署名不单独成页。

## 可选搜索工具

这个 skill 可以使用通用网页搜索和直接 fetch。已有以下工具时，可以提升覆盖度：

- OpenSEO skills/MCP：关键词研究、SERP 检查、域名对比、搜索结果质量检查。
- DataForSEO MCP：Google/Bing/Yahoo SERP、搜索量、CPC、Labs、OnPage、域名/搜索数据。
- 浏览器/CDP：用于公开 JS 渲染页面或用户授权会话。

OpenSEO 可选安装：

```bash
npx skills add every-app/open-seo --skill '*' --agent codex
```

DataForSEO MCP 可选启动：

```bash
npx dataforseo-mcp-server@latest
```

## 安装

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo AAAAAAlone/targeted-company-research-skill \
  --path targeted-company-research \
  --method git
```

安装后重启 Codex。

如果已经安装过旧版，重新执行同一条安装命令即可覆盖到最新版。也可以手动确认：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/targeted-company-research
```

确认调用到最新版的方法：

- skill 列表中应出现 `targeted-company-research`。
- 默认提示词应包含“正式研究模式”“证据型附录”“公司名_jiascan_report_v1.0”。
- 调研输出目录中应出现 `sections/`、`merge_manifest.md`、`source_index.md`、`report.html` 和 `report.pdf`。

## 使用示例

```text
请使用 targeted-company-research 正式研究模式，调研长鑫科技 / 长鑫存储 / CXMT。

我不太懂股票，请判断：
1. 这家公司现在是否有公开股价、是否能直接买入；如果不能直接买，应该关注哪些相关上市公司、影子股或产业链标的。
2. 从基本面、行业周期、国产替代、供应链、估值线索和风险看，现在是否值得关注，什么条件下可以考虑买，什么条件下应该回避。
3. 同行业板块应该重点关注哪些公司、指标和风险信号。
4. 现在去长鑫科技入职或投简历是否还值得，适合哪些岗位，不适合哪些人。

请生成 30 页以上中文正式报告，文件名使用：长鑫科技_jiascan_report_v1.0。
重点不要写基础介绍，要给判断、证据型附录、来源和 PDF。
```

```text
请使用 targeted-company-research 正式研究模式，调研 Universal Power Group，用于 ABM 销售准备。

重点看产品线、分销渠道、竞品、公开客户、公开决策角色、采购触发点和切入角度。
请输出中文 Markdown、HTML 和 PDF，保留来源标记和证据型附录。
```

```text
请使用 targeted-company-research 正式研究模式，调研 {公司名}。

重点看产品线、渠道、竞品、客户供应商、组织招聘和数据缺口。
输出中文正式报告，保留来源标记、证据型附录和 PDF。
```

## 仓库结构

```text
targeted-company-research/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── research-playbook.md
│   └── task-instructions-template.md
└── scripts/
    ├── assemble_report.py
    └── render_report.py
```

## 数据边界

允许：

- 公开公司、产品、业务角色、披露文件、招聘、活动、专利、认证和媒体信息；
- 官方公司联系方式；
- 用户授权的公开或授权页面浏览器会话。

不允许：

- 绕过登录、付费墙、验证码、robots 限制或访问控制；
- 提取私有系统；
- 猜测私人邮箱或手机号；
- 批量收集个人联系方式；
- 使用泄露的凭证、cookie 或 token。

## 授权

MIT License.
