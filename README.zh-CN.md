<h1 align="center">Consulting Skills</h1>
<p align="center"><strong>给 AI Agent 用的 58 个咨询方法操作指南</strong></p>
<p align="center">把一件说不清、拿不准的事，整理成可以判断、可以行动、也可以验证的方案。</p>
<p align="center"><a href="https://github.com/fzfclee/consulting-skills/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/fzfclee/consulting-skills/validate.yml?branch=main&amp;style=for-the-badge&amp;label=validation" alt="Validation"></a> <a href="catalog.yaml"><img src="https://img.shields.io/badge/skills-58-0f766e?style=for-the-badge" alt="58 skills"></a> <a href="https://github.com/fzfclee/consulting-skills/stargazers"><img src="https://img.shields.io/github/stars/fzfclee/consulting-skills?style=for-the-badge" alt="GitHub stars"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=for-the-badge" alt="Apache 2.0 license"></a></p>
<p align="center"><a href="#30-秒开始">30 秒开始</a> · <a href="#普通人能用它做什么">日常用途</a> · <a href="#按场景选方法">按场景选方法</a> · <a href="#58-个方法-skill">浏览全部 58 个</a> · <a href="examples/README.md">对照案例</a> · <a href="#怎么检查质量">质量检查</a> · <a href="README.md">English</a> · <a href="https://www.o2vframework.com">O2V Framework</a></p>

---

## 为什么需要这个仓库

很多方法库讲清了一个方法是什么意思，却没有告诉 AI Agent 怎么把它用起来。Agent 还得知道什么时候适合用、缺了哪些信息、每一步怎么走，以及最后应该交出什么。

这些内容不清楚，回答很容易出现下面的问题：

| 常见问题 | Skill 会补上什么 |
|---|---|
| 一遇到战略问题就套 SWOT | 触发条件和 `When Not To Use` 会把范围收窄 |
| 事实、观点和猜测混在一起 | 证据要求会标出置信度和信息缺口 |
| 分析写了很多，却没有改变决策 | 输出必须落到一个能使用的决策成果 |
| 为了显得专业而堆很多框架 | 只有会改变行动、风险、验证或交付物的方法才值得保留 |
| 输入明显不够，答案却说得很确定 | 质量门要求写明假设和下一步验证 |

这里的每个 Skill 都能单独使用。它告诉 Agent 怎么执行一个方法，不只解释概念。

## 30 秒开始

使用开放 Skills CLI 安装：

```bash
npx skills add fzfclee/consulting-skills
```

也可以只安装一个方法：

```bash
gh skill install fzfclee/consulting-skills systems-thinking --agent codex --scope user
```

然后直接告诉你的 Agent：

```text
使用 systems-thinking 分析这个问题为什么在多次修复后仍然反复出现。
区分证据和假设，识别反馈循环、时间延迟、杠杆点、副作用和下一步验证信号。
```

每个方法都按同一套基本逻辑执行：

```text
业务问题
  ↓
检查输入和适用边界
  ↓
执行明确的方法步骤
  ↓
产出可复用的决策成果
  ↓
通过方法自己的质量门
```

## 普通人能用它做什么

你不用学过咨询，也不用背框架。把事情经过、手里的事实、拿不准的地方和想做的决定告诉 Agent，再从一个合适的 Skill 开始。

| 你可能正在考虑的事 | 可以先用 | 最后能拿到什么 |
|---|---|---|
| 要不要换工作、接 Offer，还是继续观望？ | [`evidence-map`](skills/evidence-map/SKILL.md)、[`scenario-planning`](skills/scenario-planning/SKILL.md) | 事实与猜测的边界、几种可能走向，以及改变选择的条件 |
| 几个产品、供应商或大额方案该选哪个？ | [`decision-matrix`](skills/decision-matrix/SKILL.md)、[`cost-benefit-analysis`](skills/cost-benefit-analysis/SKILL.md) | 看得见取舍、硬约束和证据强弱的比较结果 |
| 工作里的同一个问题为什么总是反复？ | [`change-event-timeline`](skills/change-event-timeline/SKILL.md)、[`systems-thinking`](skills/systems-thinking/SKILL.md) | 事件时间线、反复模式、反馈循环和更稳妥的干预办法 |
| 副业或新产品值不值得继续投入？ | [`business-model-canvas`](skills/business-model-canvas/SKILL.md)、[`break-even-analysis`](skills/break-even-analysis/SKILL.md) | 关键假设、盈亏平衡点，以及继续花钱前要验证的事情 |
| 产品或内部工具为什么没人用？ | [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md)、[`metrics-tree`](skills/metrics-tree/SKILL.md) | 使用率低的可能原因、缺失证据、改进动作和成功指标 |
| 一个方案涉及很多人，怎么推动才不容易卡住？ | [`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md)、[`communications-plan`](skills/communications-plan/SKILL.md) | 决策人、实际影响者、沟通顺序和具体动作 |

先用一个方法。只有第二个方法会回答另一个足以改变决策的问题时，才把它加进来。

## 按场景选方法

先看你要解决什么问题，不要先想自己记得哪个框架。

| 当前情况 | 建议先用 | 应该产出什么 |
|---|---|---|
| 事实、观点和假设混在一起 | [`evidence-map`](skills/evidence-map/SKILL.md) | 证据台账和置信度缺口 |
| 问题太大、太乱 | [`issue-tree`](skills/issue-tree/SKILL.md) | 面向决策的问题树 |
| 问题反复出现 | [`systems-thinking`](skills/systems-thinking/SKILL.md) | 循环、延迟、杠杆点和副作用 |
| 存在多个可能原因 | [`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) | 竞争性解释和区分性验证 |
| 需要比较多个方案 | [`decision-matrix`](skills/decision-matrix/SKILL.md) | 标准、取舍、敏感性和建议 |
| 权力关系和隐性否决复杂 | [`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md) | 影响力地图和沟通动作 |
| 产品采用率或价值实现偏低 | [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) | 需求侧诊断和采用假设 |
| 项目启动前需要预演失败 | [`pre-mortem`](skills/pre-mortem/SKILL.md) | 失败模式、预防动作、触发器和预案 |
| 未来取决于关键未知变量 | [`scenario-planning`](skills/scenario-planning/SKILL.md) | 稳健动作、条件动作和信号 |
| 工作被一个关键瓶颈卡住 | [`constraint-analysis`](skills/constraint-analysis/SKILL.md) | 瓶颈证据和突破方案 |

还拿不准从哪里开始，可以查 [`catalog.yaml`](catalog.yaml)，也可以直接看[七个对照案例](examples/README.md)。

## 58 个方法 Skill

| 方法类别 | 数量 | 常见决策 |
|---|---:|---|
| 问题定义与证据 | 8 | 哪些是真的、缺失的、嘈杂的或定义不清的？ |
| 推理与根因 | 8 | 哪种解释最可信，为什么？ |
| 系统、风险与未来 | 5 | 什么会持续、失败或随时间变化？ |
| 战略、市场与商业 | 10 | 去哪里竞争、如何竞争、如何赢？ |
| 客户、产品与体验 | 7 | 用户需要、采用、重视或拒绝什么？ |
| 优先级与经济性 | 7 | 哪个选项更值得投入时间、预算或优先顺序？ |
| 衡量与绩效 | 3 | 应该衡量和治理什么？ |
| 利益相关者、变革与治理 | 7 | 谁决策、影响、负责或抵制？ |
| 执行与验证 | 3 | 最小可信行动和证明是什么？ |

<details>
<summary><strong>展开查看全部 58 个 Skill</strong></summary>

### 问题定义与证据

[`5w1h-analysis`](skills/5w1h-analysis/SKILL.md) ·
[`affinity-diagram`](skills/affinity-diagram/SKILL.md) ·
[`assumption-inventory`](skills/assumption-inventory/SKILL.md) ·
[`evidence-map`](skills/evidence-map/SKILL.md) ·
[`issue-tree`](skills/issue-tree/SKILL.md) ·
[`mece-framework`](skills/mece-framework/SKILL.md) ·
[`mind-map-analysis`](skills/mind-map-analysis/SKILL.md) ·
[`signal-vs-noise-filter`](skills/signal-vs-noise-filter/SKILL.md)

### 推理与根因

[`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) ·
[`constraint-analysis`](skills/constraint-analysis/SKILL.md) ·
[`deductive-reasoning`](skills/deductive-reasoning/SKILL.md) ·
[`first-principles-thinking`](skills/first-principles-thinking/SKILL.md) ·
[`fishbone-diagram`](skills/fishbone-diagram/SKILL.md) ·
[`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md) ·
[`hypothesis-tree`](skills/hypothesis-tree/SKILL.md) ·
[`inductive-reasoning`](skills/inductive-reasoning/SKILL.md)

### 系统、风险与未来

[`critical-uncertainties`](skills/critical-uncertainties/SKILL.md) ·
[`pre-mortem`](skills/pre-mortem/SKILL.md) ·
[`risk-matrix`](skills/risk-matrix/SKILL.md) ·
[`scenario-planning`](skills/scenario-planning/SKILL.md) ·
[`systems-thinking`](skills/systems-thinking/SKILL.md)

### 战略、市场与商业

[`account-plan`](skills/account-plan/SKILL.md) ·
[`business-model-canvas`](skills/business-model-canvas/SKILL.md) ·
[`competitive-positioning`](skills/competitive-positioning/SKILL.md) ·
[`deal-strategy-map`](skills/deal-strategy-map/SKILL.md) ·
[`go-to-market-diagnosis`](skills/go-to-market-diagnosis/SKILL.md) ·
[`pestel-analysis`](skills/pestel-analysis/SKILL.md) ·
[`porter-five-forces`](skills/porter-five-forces/SKILL.md) ·
[`pricing-strategy-check`](skills/pricing-strategy-check/SKILL.md) ·
[`swot-analysis`](skills/swot-analysis/SKILL.md) ·
[`win-loss-review`](skills/win-loss-review/SKILL.md)

### 客户、产品与体验

[`customer-segmentation`](skills/customer-segmentation/SKILL.md) ·
[`customer-success-health-score`](skills/customer-success-health-score/SKILL.md) ·
[`empathy-map`](skills/empathy-map/SKILL.md) ·
[`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) ·
[`kano-model`](skills/kano-model/SKILL.md) ·
[`service-blueprint`](skills/service-blueprint/SKILL.md) ·
[`user-journey-mapping`](skills/user-journey-mapping/SKILL.md)

### 优先级与经济性

[`break-even-analysis`](skills/break-even-analysis/SKILL.md) ·
[`cost-benefit-analysis`](skills/cost-benefit-analysis/SKILL.md) ·
[`decision-matrix`](skills/decision-matrix/SKILL.md) ·
[`effort-impact-matrix`](skills/effort-impact-matrix/SKILL.md) ·
[`rice-scoring`](skills/rice-scoring/SKILL.md) ·
[`weighted-scorecard`](skills/weighted-scorecard/SKILL.md) ·
[`wsjf-prioritization`](skills/wsjf-prioritization/SKILL.md)

### 衡量与绩效

[`balanced-scorecard`](skills/balanced-scorecard/SKILL.md) ·
[`metrics-tree`](skills/metrics-tree/SKILL.md) ·
[`north-star-metric`](skills/north-star-metric/SKILL.md)

### 利益相关者、变革与治理

[`change-event-timeline`](skills/change-event-timeline/SKILL.md) ·
[`change-impact-analysis`](skills/change-impact-analysis/SKILL.md) ·
[`communications-plan`](skills/communications-plan/SKILL.md) ·
[`force-field-analysis`](skills/force-field-analysis/SKILL.md) ·
[`power-interest-grid`](skills/power-interest-grid/SKILL.md) ·
[`raci-matrix`](skills/raci-matrix/SKILL.md) ·
[`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md)

### 执行与验证

[`fifteen-percent-solutions`](skills/fifteen-percent-solutions/SKILL.md) ·
[`min-specs`](skills/min-specs/SKILL.md) ·
[`validation-plan`](skills/validation-plan/SKILL.md)

</details>

## 怎么检查质量

每个 Skill 都必须写清五件事：

1. `Required Inputs`
2. `When Not To Use`
3. `Step-by-Step Execution`
4. `Output Template`
5. `Quality Gate`

仓库会自动检查这些内容：

| 检查项目 | 当前覆盖 |
|---|---:|
| 已校验的独立 Skill | 58 |
| 覆盖全部方法的评价题 | 70 |
| 方法辨析题 | 24 |
| 受控对照案例 | 7 |
| 中立目录条目 | 58 |
| 允许出现的可移植性或本机路径错误 | 0 |

校验器会检查名称、frontmatter、必需章节、链接、UTF-8、目录一致性和可移植性。这些属于结构检查，能发现包装和方法契约的问题，但不能证明模型一定会做出正确判断。因此，评价题和评分标准都放在仓库里，结果需要单独运行和记录。

## 七个对照案例

| 决策问题 | 示例路径 |
|---|---|
| 澄清一个模糊问题 | [Evidence Map → Issue Tree](examples/01-clarify-an-ambiguous-problem.md) |
| 诊断反复出现的问题 | [Timeline → Systems Thinking → Constraint Analysis](examples/02-diagnose-a-recurring-problem.md) |
| 比较多个选项 | [Decision Matrix → Risk Matrix](examples/03-prioritize-options.md) |
| 制定利益相关者策略 | [Stakeholder Power Map → Account Plan](examples/04-build-a-stakeholder-strategy.md) |
| 提升产品采用率和 ROI | [Evidence Map → JTBD → Metrics Tree](examples/05-improve-product-adoption-and-roi.md) |
| 评估市场进入 | [PESTEL → Five Forces → Positioning](examples/06-assess-a-market-entry.md) |
| 评估换工作决策 | [不使用方法 vs Evidence Map → Stakeholder Power Map → Scenario Planning → Weighted Scorecard](examples/career-change-comparison.zh-CN.md) |

这些案例不是万能路由，也不是统计意义上的模型基准测试。每个案例都对同一份输入运行两次：第一次让普通 AI 直接回答，不调用具名方法；第二次使用表中列出的方法链。对照会保留证据边界、方法底稿、步骤之间的交接、最终决策成果、行动计划、成功指标和推翻条件。

### 方法链多交付了什么？

[七个对照案例](examples/README.md)里，普通 AI 往往也能很快给出一个合理方向。方法版不一定改变结论，但会留下中间底稿、方法之间的推导关系、带 Owner 和时间的行动计划、成功指标、决策门槛，以及什么时候应该调整。

方法链的价值主要在这里：别人能复核推理，执行人知道下一步做什么，之后也能判断方案有没有奏效。它不会让结论自动变正确。

## 它是什么，不是什么

| 它是 | 它不是 |
|---|---|
| 可独立使用的通用咨询方法 Skill 库 | 对既有咨询方法主张所有权 |
| 面向 AI Agent 的方法执行说明 | 证据和专业判断的替代品 |
| 有明确边界的中立方法目录 | 要求每个问题都必须使用框架 |
| O2V Framework 知识生态中的开放方法资源 | 完整的 O2V Framework 或 CLEAR / Signal-to-Action 方法论 |

Consulting Skills 由李智发起，是 [O2V Framework](https://www.o2vframework.com)
知识生态中的开放方法库。O2V Framework 与 CLEAR / Signal-to-Action 作为完整方法论资产分别维护。

## 仓库结构

```text
skills/<skill-name>/SKILL.md   58 个独立方法 Skill
catalog.yaml                   中立发现目录
examples/                      7 个受控决策对照案例
evaluations/                   效果评价题与方法辨析题
scripts/                       目录生成与质量校验
```

## 参与贡献

贡献应该真正改善方法准确性、触发条件、证据纪律、输出可用性或决策影响。新增方法应该补足真实决策需要，而不是只增加数量。

请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，也可以提交
[Issue](https://github.com/fzfclee/consulting-skills/issues) 或 Pull Request。

## 知识产权说明

本项目不主张对通用咨询工具、分析方法、学术理论或管理框架本身拥有权利。方法名称仅用于描述，其相关权利和学术贡献仍属于各自的创作者、研究者、机构和权利人。

Apache License 2.0 适用于本仓库原创的 Skill 文字表达、可执行结构、案例、目录和校验代码。O2V Framework、CLEAR、Signal-to-Action 及其原创框架表达和资产，是李智创作的独立作品，不属于本仓库 Apache-2.0 许可范围。

具体说明见 [`NOTICE`](NOTICE) 和 [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md)。

## 联系方式

官方网站：[www.o2vframework.com](https://www.o2vframework.com)

邮箱：[contact@o2vframework.com](mailto:contact@o2vframework.com)

---

<div align="center">

**觉得有用，可以点个 Star；发现哪一步站不住脚，请提 Issue。**

</div>
