<h1 align="center">Consulting Skills</h1>
<p align="center"><strong>58 execution-ready consulting methods for AI agents</strong></p>
<p align="center">Turn ambiguous business questions into evidence-aware decisions, actions, and validation plans.</p>
<p align="center"><a href="https://github.com/fzfclee/consulting-skills/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/fzfclee/consulting-skills/validate.yml?branch=main&amp;style=for-the-badge&amp;label=validation" alt="Validation"></a> <a href="catalog.yaml"><img src="https://img.shields.io/badge/skills-58-0f766e?style=for-the-badge" alt="58 skills"></a> <a href="https://github.com/fzfclee/consulting-skills/stargazers"><img src="https://img.shields.io/github/stars/fzfclee/consulting-skills?style=for-the-badge" alt="GitHub stars"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=for-the-badge" alt="Apache 2.0 license"></a></p>
<p align="center"><a href="#30-second-start">30-second start</a> · <a href="#choose-by-situation">Choose a skill</a> · <a href="#the-58-skill-library">Browse all 58</a> · <a href="examples/README.md">Examples</a> · <a href="#built-for-reliable-execution">Quality</a> · <a href="README.zh-CN.md">中文</a> · <a href="https://www.o2vframework.com">O2V Framework</a></p>

---

## Why This Repository Exists

Most framework collections tell you **what a method means**. AI agents also need to know **when to use it, when to stop, what evidence is missing, how to execute it, and what usable output to produce**.

Without that execution layer, common failure modes appear:

| Common failure | What an executable skill changes |
|---|---|
| The agent uses SWOT for every strategic question | Trigger and `When Not To Use` rules select a narrower method |
| Facts, opinions, and assumptions are mixed together | Evidence requirements make confidence and gaps visible |
| A polished analysis does not change the decision | Output contracts tie the method to a decision artifact |
| Several frameworks are stacked without purpose | A method is used only when it improves action, risk, validation, or a deliverable |
| The answer sounds complete despite missing inputs | Quality gates force assumptions and validation actions to be stated |

Each skill in this repository is a standalone operating guide, not a framework definition card.

## 30-Second Start

Install the library with the open Skills CLI:

```bash
npx skills add fzfclee/consulting-skills
```

Or install one method with GitHub CLI:

```bash
gh skill install fzfclee/consulting-skills systems-thinking --agent codex --scope user
```

Then ask your agent:

```text
Use systems-thinking to diagnose why this issue keeps returning after repeated fixes.
Separate evidence from assumptions. Identify feedback loops, delays, leverage points,
side effects, and the next validation signal.
```

The execution pattern is consistent across the library:

```text
Business question
      ↓
Check inputs and use boundary
      ↓
Execute explicit method steps
      ↓
Produce a reusable decision artifact
      ↓
Run the method-specific quality gate
```

## Choose By Situation

Start with the problem you have, not the framework you remember.

| Situation | Start with | What it should produce |
|---|---|---|
| Facts, opinions, and assumptions are mixed | [`evidence-map`](skills/evidence-map/SKILL.md) | Evidence ledger and confidence gaps |
| A broad problem needs a clean structure | [`issue-tree`](skills/issue-tree/SKILL.md) | Decision-oriented problem tree |
| A problem keeps returning | [`systems-thinking`](skills/systems-thinking/SKILL.md) | Loops, delays, leverage points, side effects |
| Several causes remain plausible | [`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) | Competing explanations and discriminating tests |
| Multiple options need comparison | [`decision-matrix`](skills/decision-matrix/SKILL.md) | Criteria, tradeoffs, sensitivity, recommendation |
| Stakeholders hold hidden veto power | [`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md) | Influence map and engagement moves |
| Product adoption or realized value is weak | [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) | Demand-side diagnosis and adoption hypotheses |
| A plan needs a failure rehearsal | [`pre-mortem`](skills/pre-mortem/SKILL.md) | Failure modes, prevention, triggers, contingencies |
| The future depends on critical unknowns | [`scenario-planning`](skills/scenario-planning/SKILL.md) | Robust moves, contingent moves, signposts |
| Work is blocked by one limiting factor | [`constraint-analysis`](skills/constraint-analysis/SKILL.md) | Constraint proof and exploitation plan |

Not sure where to start? Browse the neutral discovery metadata in [`catalog.yaml`](catalog.yaml), or open one of the [seven fixed examples](examples/README.md).

## The 58-Skill Library

| Method family | Skills | Typical decisions |
|---|---:|---|
| Problem framing and evidence | 8 | What is true, missing, noisy, or poorly framed? |
| Reasoning and root cause | 8 | Which explanation is strongest, and why? |
| Systems, risk, and futures | 5 | What could persist, fail, or change over time? |
| Strategy, market, and commercial | 10 | Where to play, how to compete, and how to win? |
| Customer, product, and experience | 7 | What do users need, adopt, value, or reject? |
| Prioritization and economics | 7 | Which option deserves time, money, or sequence priority? |
| Measurement and performance | 3 | What should be measured and governed? |
| Stakeholder, change, and governance | 7 | Who decides, influences, owns, or resists? |
| Execution and validation | 3 | What is the smallest credible action and proof? |

<details>
<summary><strong>Browse all 58 skills by method family</strong></summary>

### Problem Framing And Evidence

[`5w1h-analysis`](skills/5w1h-analysis/SKILL.md) ·
[`affinity-diagram`](skills/affinity-diagram/SKILL.md) ·
[`assumption-inventory`](skills/assumption-inventory/SKILL.md) ·
[`evidence-map`](skills/evidence-map/SKILL.md) ·
[`issue-tree`](skills/issue-tree/SKILL.md) ·
[`mece-framework`](skills/mece-framework/SKILL.md) ·
[`mind-map-analysis`](skills/mind-map-analysis/SKILL.md) ·
[`signal-vs-noise-filter`](skills/signal-vs-noise-filter/SKILL.md)

### Reasoning And Root Cause

[`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) ·
[`constraint-analysis`](skills/constraint-analysis/SKILL.md) ·
[`deductive-reasoning`](skills/deductive-reasoning/SKILL.md) ·
[`first-principles-thinking`](skills/first-principles-thinking/SKILL.md) ·
[`fishbone-diagram`](skills/fishbone-diagram/SKILL.md) ·
[`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md) ·
[`hypothesis-tree`](skills/hypothesis-tree/SKILL.md) ·
[`inductive-reasoning`](skills/inductive-reasoning/SKILL.md)

### Systems, Risk, And Futures

[`critical-uncertainties`](skills/critical-uncertainties/SKILL.md) ·
[`pre-mortem`](skills/pre-mortem/SKILL.md) ·
[`risk-matrix`](skills/risk-matrix/SKILL.md) ·
[`scenario-planning`](skills/scenario-planning/SKILL.md) ·
[`systems-thinking`](skills/systems-thinking/SKILL.md)

### Strategy, Market, And Commercial

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

### Customer, Product, And Experience

[`customer-segmentation`](skills/customer-segmentation/SKILL.md) ·
[`customer-success-health-score`](skills/customer-success-health-score/SKILL.md) ·
[`empathy-map`](skills/empathy-map/SKILL.md) ·
[`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) ·
[`kano-model`](skills/kano-model/SKILL.md) ·
[`service-blueprint`](skills/service-blueprint/SKILL.md) ·
[`user-journey-mapping`](skills/user-journey-mapping/SKILL.md)

### Prioritization And Economics

[`break-even-analysis`](skills/break-even-analysis/SKILL.md) ·
[`cost-benefit-analysis`](skills/cost-benefit-analysis/SKILL.md) ·
[`decision-matrix`](skills/decision-matrix/SKILL.md) ·
[`effort-impact-matrix`](skills/effort-impact-matrix/SKILL.md) ·
[`rice-scoring`](skills/rice-scoring/SKILL.md) ·
[`weighted-scorecard`](skills/weighted-scorecard/SKILL.md) ·
[`wsjf-prioritization`](skills/wsjf-prioritization/SKILL.md)

### Measurement And Performance

[`balanced-scorecard`](skills/balanced-scorecard/SKILL.md) ·
[`metrics-tree`](skills/metrics-tree/SKILL.md) ·
[`north-star-metric`](skills/north-star-metric/SKILL.md)

### Stakeholder, Change, And Governance

[`change-event-timeline`](skills/change-event-timeline/SKILL.md) ·
[`change-impact-analysis`](skills/change-impact-analysis/SKILL.md) ·
[`communications-plan`](skills/communications-plan/SKILL.md) ·
[`force-field-analysis`](skills/force-field-analysis/SKILL.md) ·
[`power-interest-grid`](skills/power-interest-grid/SKILL.md) ·
[`raci-matrix`](skills/raci-matrix/SKILL.md) ·
[`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md)

### Execution And Validation

[`fifteen-percent-solutions`](skills/fifteen-percent-solutions/SKILL.md) ·
[`min-specs`](skills/min-specs/SKILL.md) ·
[`validation-plan`](skills/validation-plan/SKILL.md)

</details>

## Built For Reliable Execution

Every skill contains the same five execution contracts:

1. `Required Inputs`
2. `When Not To Use`
3. `Step-by-Step Execution`
4. `Output Template`
5. `Quality Gate`

The repository adds public checks around those contracts:

| Quality proof | Current coverage |
|---|---:|
| Standalone skills validated | 58 |
| Representative evaluation prompts | 24 |
| Fixed end-to-end examples | 7 |
| Neutral catalog entries | 58 |
| Repository-specific routing or local-path leakage allowed | 0 |

The validator checks unique names, frontmatter, required sections, portable links, UTF-8 text, catalog consistency, and public-boundary rules. The evaluation set contains prompts and a rubric rather than hidden expected answers.

## Seven Fixed Examples

| Decision problem | Example route |
|---|---|
| Clarify an ambiguous problem | [Evidence Map → Issue Tree](examples/01-clarify-an-ambiguous-problem.md) |
| Diagnose a recurring issue | [Timeline → Systems Thinking → Constraint Analysis](examples/02-diagnose-a-recurring-problem.md) |
| Prioritize competing options | [Decision Matrix → Risk Matrix](examples/03-prioritize-options.md) |
| Build a stakeholder strategy | [Stakeholder Power Map → Account Plan](examples/04-build-a-stakeholder-strategy.md) |
| Improve product adoption and ROI | [Evidence Map → JTBD → Metrics Tree](examples/05-improve-product-adoption-and-roi.md) |
| Assess market entry | [PESTEL → Five Forces → Positioning](examples/06-assess-a-market-entry.md) |
| Compare direct advice with a method chain | [No method vs Evidence Map → Stakeholder Power Map → Scenario Planning → Weighted Scorecard](examples/07-career-change-baseline-vs-method-chain.md) |

These are fixed illustrations, not a universal router. Each one records the input boundary, why the selected method matters, intermediate output, effect on the next step, methods deliberately not used, and the final decision artifact.

### Does A Method Skill Actually Improve The Answer?

The [career-change comparison](examples/07-career-change-baseline-vs-method-chain.md) uses the same input twice. The direct answer is sensible and concise. The four-skill run reaches the same current recommendation, but makes the evidence boundary, stakeholder power, plausible scenarios, option scores, sensitivity, and reversal gates visible.

That is the standard for using a method here: it should improve the decision, validation, or risk control, not merely add framework terminology.

## What This Is, And What It Is Not

| This repository is | This repository is not |
|---|---|
| A portable library of standalone consulting method skills | A claim of ownership over established methods |
| A set of execution instructions for AI agents | A substitute for evidence or professional judgment |
| A neutral catalog with explicit boundaries | A rule that every problem needs a framework |
| An open method resource in the O2V Framework ecosystem | The complete O2V Framework or CLEAR / Signal-to-Action methodology |

Consulting Skills is initiated by Li Zhi and maintained as an open method library in the broader [O2V Framework](https://www.o2vframework.com) knowledge ecosystem. O2V Framework and CLEAR / Signal-to-Action are maintained separately as complete methodology assets.

## Repository Structure

```text
skills/<skill-name>/SKILL.md   58 standalone method skills
catalog.yaml                   neutral discovery metadata
examples/                      seven fixed decision examples
evaluations/                   public prompts and scoring rubric
scripts/                       catalog generation and validation
```

## Contributing

Contributions should improve method fidelity, trigger clarity, evidence discipline, output usability, or decision impact. A new method should fill a real decision need rather than increase the count.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), open an [issue](https://github.com/fzfclee/consulting-skills/issues), or submit a pull request.

## Intellectual Property

This project does not claim ownership of established consulting tools, analytical methods, academic theories, or management frameworks. Method names are used descriptively; their rights and academic contributions remain with their respective creators, researchers, institutions, and rights holders.

Apache License 2.0 applies to this repository's original skill text, executable structure, examples, catalog, and validation code. O2V Framework, CLEAR, Signal-to-Action, and their original framework expressions and assets are separate works by Li Zhi and are not licensed under this repository's Apache-2.0 license.

See [`NOTICE`](NOTICE) and [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md).

## Contact

Official website: [www.o2vframework.com](https://www.o2vframework.com)

Email: [contact@o2vframework.com](mailto:contact@o2vframework.com)

---

<div align="center">

**If this library helps your agent make a better decision, star the repository and help improve the next method.**

</div>
