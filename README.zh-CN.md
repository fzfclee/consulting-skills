# 咨询方法 Skills

这是一套面向业务决策、问题诊断、战略分析和行动设计的 58 个可执行咨询方法 Skill。

Consulting Skills 由李智发起，是 [O2V Framework](https://www.o2vframework.com)
知识生态中的开放方法库，也可以脱离 O2V 独立使用。本仓库不包含 O2V Framework
本身，也不公开 CLEAR / Signal-to-Action 的私有路由、客户交付逻辑或内部评分规则。

它不是只有方法定义的“框架百科”。每个 Skill 都会告诉 AI：

- 执行前需要哪些输入；
- 什么情况下不该使用这个方法；
- 每一步如何执行；
- 应该产出什么可复用成果；
- 如何标记证据不足和临时假设；
- 最终结果需要通过哪些质量检查。

## 一分钟开始

安装一个独立 Skill：

```bash
gh skill install fzfclee/consulting-skills systems-thinking --agent codex --scope user
```

也可以通过开放 Skills 生态安装：

```bash
npx skills add fzfclee/consulting-skills
```

安装后，可以直接要求 AI：

```text
使用 systems-thinking 分析这个问题为什么反复出现。
区分事实和假设，识别反馈循环、时间延迟、杠杆点、副作用和验证信号。
```

## 如何选择

| 当前情况 | 建议先用 |
|---|---|
| 事实、观点和假设混在一起 | [`evidence-map`](skills/evidence-map/SKILL.md) |
| 问题太大、太乱 | [`issue-tree`](skills/issue-tree/SKILL.md) |
| 问题反复出现 | [`systems-thinking`](skills/systems-thinking/SKILL.md) |
| 存在多个可能原因 | [`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) |
| 需要比较多个方案 | [`decision-matrix`](skills/decision-matrix/SKILL.md) |
| 权力关系和隐性否决复杂 | [`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md) |
| 数字化产品使用率偏低 | [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) |
| 项目启动前需要预演失败 | [`pre-mortem`](skills/pre-mortem/SKILL.md) |

完整目录见 [`catalog.yaml`](catalog.yaml)，六个固定使用案例见
[`examples/`](examples/README.md)。

## 公开边界

本仓库只发布可以独立使用的通用方法 Skill，不包含任何私有 CLEAR/S2A
路由、客户底稿、私有评分规则、PPT 交付逻辑或知识库路径。

这些方法只有在能够明显改善决策、行动、风险判断或验证计划时才应该使用。
简单回答已经足够时，不应为了使用框架而使用框架。

## 知识产权说明

本项目不主张对 SWOT、RACI、Kano Model、Porter's Five Forces 等通用咨询工具、
分析方法、学术理论或管理框架本身拥有权利。相关方法及其名称的权利与学术贡献，
属于各自的创作者、研究者、机构或相应权利人。

Apache-2.0 许可证只适用于本仓库原创的 Skill 文字表达、可执行结构、模板、目录、
案例和代码。具体边界与来源说明见 [`NOTICE`](NOTICE) 和
[`ATTRIBUTIONS.md`](ATTRIBUTIONS.md)。

O2V Framework、CLEAR、Signal-to-Action 及其原创文字表达、框架结构、图示和品牌化
交付资产，是李智创作的独立作品，不属于本仓库 Apache-2.0 许可范围。本仓库可以作为
O2V 产品引用的公共方法依赖，但不会公开 O2V 的私有决策路由系统。

O2V Framework 官网：[www.o2vframework.com](https://www.o2vframework.com)

联系邮箱：[contact@o2vframework.com](mailto:contact@o2vframework.com)

## 免责声明

这些 Skill 用于辅助结构化分析，不能替代法律、财务、医疗、监管等需要专业资质的意见。
使用者仍需对最终判断、决策和结果负责。
