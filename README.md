<h1 align="center">Consulting Skills</h1>
<p align="center"><strong>58 consulting methods, written as runnable skills for AI agents</strong></p>
<p align="center">Give your agent a messy question. Get back a clearer decision, a usable plan, and a way to check whether it worked.</p>
<p align="center"><a href="https://github.com/fzfclee/consulting-skills/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/fzfclee/consulting-skills/validate.yml?branch=main&amp;style=for-the-badge&amp;label=validation" alt="Validation"></a> <a href="catalog.yaml"><img src="https://img.shields.io/badge/skills-58-0f766e?style=for-the-badge" alt="58 skills"></a> <a href="https://github.com/fzfclee/consulting-skills/stargazers"><img src="https://img.shields.io/github/stars/fzfclee/consulting-skills?style=for-the-badge" alt="GitHub stars"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=for-the-badge" alt="Apache 2.0 license"></a></p>
<p align="center"><a href="#30-second-start">30-second start</a> · <a href="#what-can-you-use-these-skills-for">Everyday uses</a> · <a href="#choose-by-situation">Choose a skill</a> · <a href="#the-58-skill-library">Browse all 58</a> · <a href="examples/README.md">Examples</a> · <a href="#how-quality-is-checked">Quality</a> · <a href="README.zh-CN.md">中文</a> · <a href="https://www.o2vframework.com">O2V Framework</a></p>

---

## Why this repo exists

Most method libraries stop at definitions. That is not enough for an AI agent. The agent also needs to know when a method fits, what input is missing, how to work through the steps, and what to produce at the end.

Otherwise, familiar problems show up:

| What goes wrong | What the skill adds |
|---|---|
| The agent reaches for SWOT whenever a question sounds strategic | Triggers and `When Not To Use` rules narrow the choice |
| Facts, opinions, and assumptions get mixed together | Evidence requirements expose confidence and gaps |
| The analysis sounds polished but changes nothing | The output has to support an actual decision |
| Several frameworks are stacked for show | A method stays only if it changes the action, risk, validation, or deliverable |
| The answer sounds certain even though key inputs are missing | Quality gates make assumptions and validation actions visible |

Each skill is a standalone working guide. It tells an agent how to run the method, not just how to describe it.

## 30-second start

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

Every skill follows the same basic pattern:

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

## What can you use these skills for?

You do not need to be a consultant or memorize a framework. Give your agent the situation, the facts you have, what you are unsure about, and the decision you need to make. Then start with one relevant skill.

| A question you might have | Useful starting skills | What you get back |
|---|---|---|
| Should I stay in this job, take an offer, or keep looking? | [`evidence-map`](skills/evidence-map/SKILL.md), [`scenario-planning`](skills/scenario-planning/SKILL.md) | Facts and assumptions, plausible futures, and conditions for changing course |
| Which product, supplier, or large purchase should I choose? | [`decision-matrix`](skills/decision-matrix/SKILL.md), [`cost-benefit-analysis`](skills/cost-benefit-analysis/SKILL.md) | A comparison that shows tradeoffs, weak evidence, and hard constraints |
| Why does the same problem keep coming back at work? | [`change-event-timeline`](skills/change-event-timeline/SKILL.md), [`systems-thinking`](skills/systems-thinking/SKILL.md) | A timeline, recurring pattern, feedback loops, and a safer intervention |
| Does a side business or new product make economic sense? | [`business-model-canvas`](skills/business-model-canvas/SKILL.md), [`break-even-analysis`](skills/break-even-analysis/SKILL.md) | Key assumptions, the break-even threshold, and what to test before spending more |
| Why are people not using a product or internal tool? | [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md), [`metrics-tree`](skills/metrics-tree/SKILL.md) | Adoption hypotheses, missing evidence, actions, and success measures |
| How do I get a proposal through a complicated group? | [`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md), [`communications-plan`](skills/communications-plan/SKILL.md) | Decision makers, informal influence, engagement moves, and a communication plan |

Use one method first. Add a second only when it answers a different question that could change the decision.

## Choose by situation

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

If the right starting point is still unclear, browse [`catalog.yaml`](catalog.yaml) or look at the [seven controlled comparisons](examples/README.md).

## The 58-skill library

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

### Problem framing and evidence

[`5w1h-analysis`](skills/5w1h-analysis/SKILL.md) ·
[`affinity-diagram`](skills/affinity-diagram/SKILL.md) ·
[`assumption-inventory`](skills/assumption-inventory/SKILL.md) ·
[`evidence-map`](skills/evidence-map/SKILL.md) ·
[`issue-tree`](skills/issue-tree/SKILL.md) ·
[`mece-framework`](skills/mece-framework/SKILL.md) ·
[`mind-map-analysis`](skills/mind-map-analysis/SKILL.md) ·
[`signal-vs-noise-filter`](skills/signal-vs-noise-filter/SKILL.md)

### Reasoning and root cause

[`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) ·
[`constraint-analysis`](skills/constraint-analysis/SKILL.md) ·
[`deductive-reasoning`](skills/deductive-reasoning/SKILL.md) ·
[`first-principles-thinking`](skills/first-principles-thinking/SKILL.md) ·
[`fishbone-diagram`](skills/fishbone-diagram/SKILL.md) ·
[`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md) ·
[`hypothesis-tree`](skills/hypothesis-tree/SKILL.md) ·
[`inductive-reasoning`](skills/inductive-reasoning/SKILL.md)

### Systems, risk, and futures

[`critical-uncertainties`](skills/critical-uncertainties/SKILL.md) ·
[`pre-mortem`](skills/pre-mortem/SKILL.md) ·
[`risk-matrix`](skills/risk-matrix/SKILL.md) ·
[`scenario-planning`](skills/scenario-planning/SKILL.md) ·
[`systems-thinking`](skills/systems-thinking/SKILL.md)

### Strategy, market, and commercial

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

### Customer, product, and experience

[`customer-segmentation`](skills/customer-segmentation/SKILL.md) ·
[`customer-success-health-score`](skills/customer-success-health-score/SKILL.md) ·
[`empathy-map`](skills/empathy-map/SKILL.md) ·
[`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) ·
[`kano-model`](skills/kano-model/SKILL.md) ·
[`service-blueprint`](skills/service-blueprint/SKILL.md) ·
[`user-journey-mapping`](skills/user-journey-mapping/SKILL.md)

### Prioritization and economics

[`break-even-analysis`](skills/break-even-analysis/SKILL.md) ·
[`cost-benefit-analysis`](skills/cost-benefit-analysis/SKILL.md) ·
[`decision-matrix`](skills/decision-matrix/SKILL.md) ·
[`effort-impact-matrix`](skills/effort-impact-matrix/SKILL.md) ·
[`rice-scoring`](skills/rice-scoring/SKILL.md) ·
[`weighted-scorecard`](skills/weighted-scorecard/SKILL.md) ·
[`wsjf-prioritization`](skills/wsjf-prioritization/SKILL.md)

### Measurement and performance

[`balanced-scorecard`](skills/balanced-scorecard/SKILL.md) ·
[`metrics-tree`](skills/metrics-tree/SKILL.md) ·
[`north-star-metric`](skills/north-star-metric/SKILL.md)

### Stakeholder, change, and governance

[`change-event-timeline`](skills/change-event-timeline/SKILL.md) ·
[`change-impact-analysis`](skills/change-impact-analysis/SKILL.md) ·
[`communications-plan`](skills/communications-plan/SKILL.md) ·
[`force-field-analysis`](skills/force-field-analysis/SKILL.md) ·
[`power-interest-grid`](skills/power-interest-grid/SKILL.md) ·
[`raci-matrix`](skills/raci-matrix/SKILL.md) ·
[`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md)

### Execution and validation

[`fifteen-percent-solutions`](skills/fifteen-percent-solutions/SKILL.md) ·
[`min-specs`](skills/min-specs/SKILL.md) ·
[`validation-plan`](skills/validation-plan/SKILL.md)

</details>

## How quality is checked

Every skill must include five practical sections:

1. `Required Inputs`
2. `When Not To Use`
3. `Step-by-Step Execution`
4. `Output Template`
5. `Quality Gate`

The repository checks those sections automatically:

| Check | Current coverage |
|---|---:|
| Standalone skills validated | 58 |
| Evaluation prompts covering all skills | 70 |
| Method-selection discrimination cases | 24 |
| Controlled comparisons | 7 |
| Neutral catalog entries | 58 |
| Portability or local-path failures allowed | 0 |

The validator checks names, frontmatter, required sections, links, UTF-8 text, catalog consistency, and portability. These are structural checks. They catch broken packages and weak method contracts, but they do not prove that a model will make the right decision. The evaluation set therefore keeps its prompts and scoring rubric in the open.

## Seven controlled comparisons

| Decision problem | Example route |
|---|---|
| Clarify an ambiguous problem | [Evidence Map → Issue Tree](examples/01-clarify-an-ambiguous-problem.md) |
| Diagnose a recurring issue | [Timeline → Systems Thinking → Constraint Analysis](examples/02-diagnose-a-recurring-problem.md) |
| Prioritize competing options | [Decision Matrix → Risk Matrix](examples/03-prioritize-options.md) |
| Build a stakeholder strategy | [Stakeholder Power Map → Account Plan](examples/04-build-a-stakeholder-strategy.md) |
| Improve product adoption and ROI | [Evidence Map → JTBD → Metrics Tree](examples/05-improve-product-adoption-and-roi.md) |
| Assess market entry | [PESTEL → Five Forces → Positioning](examples/06-assess-a-market-entry.md) |
| Evaluate a career decision | [No method vs Evidence Map → Stakeholder Power Map → Scenario Planning → Weighted Scorecard](examples/07-career-change-baseline-vs-method-chain.md) |

These examples are not a universal router or a scientific model benchmark. Each one runs the same input twice: first as a direct AI answer with no named method, then with the listed method chain. The comparison keeps the evidence boundary, method workpapers, handoff between steps, final decision artifact, action plan, success measures, and reversal conditions.

### What does a method chain add?

In the [seven comparisons](examples/README.md), the direct answer often reaches a sensible recommendation quickly. The method-based run may reach the same conclusion. The difference is that it leaves behind workpapers, the handoff from one method to the next, owners and timing, success measures, decision gates, and triggers for changing course.

A method chain makes the reasoning easier to review and the plan easier to run. It does not make the conclusion automatically correct.

## What this is, and what it is not

| This repository is | This repository is not |
|---|---|
| A portable library of standalone consulting method skills | A claim of ownership over established methods |
| A set of execution instructions for AI agents | A substitute for evidence or professional judgment |
| A neutral catalog with explicit boundaries | A rule that every problem needs a framework |
| An open method resource in the O2V Framework ecosystem | The complete O2V Framework or CLEAR / Signal-to-Action methodology |

Consulting Skills is initiated by Li Zhi and maintained as an open method library in the broader [O2V Framework](https://www.o2vframework.com) knowledge ecosystem. O2V Framework and CLEAR / Signal-to-Action are maintained separately as complete methodology assets.

## Repository structure

```text
skills/<skill-name>/SKILL.md   58 standalone method skills
catalog.yaml                   neutral discovery metadata
examples/                      seven controlled decision comparisons
evaluations/                   behavior and method-selection test cases
scripts/                       catalog generation and validation
```

## Contributing

Contributions should improve method fidelity, trigger clarity, evidence discipline, output usability, or decision impact. A new method should fill a real decision need rather than increase the count.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), open an [issue](https://github.com/fzfclee/consulting-skills/issues), or submit a pull request.

## Intellectual property

This project does not claim ownership of established consulting tools, analytical methods, academic theories, or management frameworks. Method names are used descriptively; their rights and academic contributions remain with their respective creators, researchers, institutions, and rights holders.

Apache License 2.0 applies to this repository's original skill text, executable structure, examples, catalog, and validation code. O2V Framework, CLEAR, Signal-to-Action, and their original framework expressions and assets are separate works by Li Zhi and are not licensed under this repository's Apache-2.0 license.

See [`NOTICE`](NOTICE) and [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md).

## Contact

Official website: [www.o2vframework.com](https://www.o2vframework.com)

Email: [contact@o2vframework.com](mailto:contact@o2vframework.com)

---

<div align="center">

**Found it useful? A star helps others find it. Found a weak method? Open an issue.**

</div>
