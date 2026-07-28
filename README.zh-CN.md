<h1 align="center">咨询方法 Skills</h1>
<p align="center"><strong>为 AI Agent 准备的 58 个可执行咨询方法</strong></p>
<p align="center">把模糊的业务问题，转化为有证据支撑的判断、行动和验证计划。</p>
<p align="center"><a href="https://github.com/fzfclee/consulting-skills/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/fzfclee/consulting-skills/validate.yml?branch=main&amp;style=for-the-badge&amp;label=validation" alt="Validation"></a> <a href="catalog.yaml"><img src="https://img.shields.io/badge/skills-58-0f766e?style=for-the-badge" alt="58 skills"></a> <a href="https://github.com/fzfclee/consulting-skills/stargazers"><img src="https://img.shields.io/github/stars/fzfclee/consulting-skills?style=for-the-badge" alt="GitHub stars"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=for-the-badge" alt="Apache 2.0 license"></a></p>
<p align="center"><a href="#30-秒开始">30 秒开始</a> · <a href="#按场景选方法">按场景选方法</a> · <a href="#58-个方法-skill">浏览全部 58 个</a> · <a href="examples/README.md">固定案例</a> · <a href="#为可靠执行而设计">质量保证</a> · <a href="README.md">English</a> · <a href="https://www.o2vframework.com">O2V Framework</a></p>

---

## 为什么需要这个仓库

大多数方法库会解释一个框架**是什么意思**。AI Agent 还需要知道：**什么时候该用、什么时候不该用、缺什么证据、每一步怎么做，以及最后要交付什么能直接使用的成果**。

缺少执行层时，常见问题包括：

| 常见问题 | 可执行 Skill 带来的改变 |
|---|---|
| 战略问题一律套 SWOT | 通过触发条件和 `When Not To Use` 选择更合适的方法 |
| 事实、观点和假设混在一起 | 明确证据要求、置信度和缺口 |
| 分析写得很完整，却没有改变决策 | 输出契约必须连接到实际决策成果 |
| 为了显得专业而堆叠多个框架 | 只有能改善行动、风险、验证或交付物时才使用方法 |
| 输入明显不足，答案却看起来很确定 | 质量门要求标明假设并给出验证动作 |

这里的每个 Skill 都是一份可以独立执行的方法操作指南，不是只有定义的“框架卡片”。

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

58 个方法遵循一致的执行逻辑：

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

还不确定时，可以查看中立目录 [`catalog.yaml`](catalog.yaml)，或者从[七个固定案例](examples/README.md)开始。

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

## 为可靠执行而设计

每个 Skill 都包含五个固定执行契约：

1. `Required Inputs`
2. `When Not To Use`
3. `Step-by-Step Execution`
4. `Output Template`
5. `Quality Gate`

公共仓库还提供以下检查：

| 质量证明 | 当前覆盖 |
|---|---:|
| 已校验的独立 Skill | 58 |
| 代表性评价题 | 24 |
| 固定端到端案例 | 6 |
| 中立目录条目 | 58 |
| 允许出现的专有产品或本机路径泄露 | 0 |

校验器会检查名称唯一性、frontmatter、固定章节、相对链接、UTF-8、目录一致性和公开边界。评价集公开题目与评分标准，不用隐藏答案冒充真实测试。

## 七个对照案例

| 决策问题 | 示例路径 |
|---|---|
| 澄清一个模糊问题 | [Evidence Map → Issue Tree](examples/01-clarify-an-ambiguous-problem.md) |
| 诊断反复出现的问题 | [Timeline → Systems Thinking → Constraint Analysis](examples/02-diagnose-a-recurring-problem.md) |
| 比较多个选项 | [Decision Matrix → Risk Matrix](examples/03-prioritize-options.md) |
| 制定利益相关者策略 | [Stakeholder Power Map → Account Plan](examples/04-build-a-stakeholder-strategy.md) |
| 提升产品采用率和 ROI | [Evidence Map → JTBD → Metrics Tree](examples/05-improve-product-adoption-and-roi.md) |
| 评估市场进入 | [PESTEL → Five Forces → Positioning](examples/06-assess-a-market-entry.md) |
| 评估一个虚构换工作决策 | [不使用方法 vs Evidence Map → Stakeholder Power Map → Scenario Planning → Weighted Scorecard](examples/career-change-comparison.zh-CN.md) |

这些案例是控制变量式的说明，不是万能路由，也不是统计意义上的模型基准测试。每个案例都会对同一份虚构输入运行两次：第一次由普通 AI 直接回答，不调用具名方法；第二次使用表中列出的方法链。对照会保留证据边界、方法底稿、对下一步的影响、最终决策成果、行动计划、成功指标和推翻条件。

### 除了最终结论，方法链还能多交付什么？

[七个对照案例](examples/README.md)显示，普通 AI 往往也能快速给出合理方向；方法版不一定改变最终结论，但会额外保留中间底稿、方法之间的推导交接、带 Owner 和时间的行动计划、成功指标、决策门槛和调整触发条件。

这才是方法链的实际价值：让推理可以复核、计划可以执行、结果可以衡量。它并不保证结论自动正确。

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
examples/                      7 个固定决策案例
evaluations/                   公开评价题与评分标准
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

**如果这个方法库帮助你的 Agent 做出了更好的判断，欢迎 Star，并一起把下一个方法做得更好。**

</div>
