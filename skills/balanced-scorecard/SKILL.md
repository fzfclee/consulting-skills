---
name: balanced-scorecard
description: Use when performance management needs a broader view than financial or single KPI tracking. Use when applying the Balanced Scorecard consulting method and when a user asks for Balanced Scorecard, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Balanced Scorecard

Use this skill to run `Balanced Scorecard` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use financial, customer, internal process, and learning/capability perspectives.
- Limit metrics per perspective so the scorecard stays usable.

## Required Inputs

Collect or infer these inputs before execution:

- strategy or objective
- current metrics
- stakeholders
- time horizon

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to create a large KPI catalog. Use it to connect outcomes, drivers, owners, and decisions.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Clarify strategy | Strategic objective and business context. | State the strategy the scorecard must translate into measures. | Strategy frame. |
| Set four perspectives | Financial, customer, internal process, learning/capability context. | Define objectives under each perspective. | Perspective objectives. |
| Choose measures | Objectives, data availability, owners. | Select a few measures per perspective with formula and cadence. | Scorecard metrics. |
| Set targets and initiatives | Measures, baseline, ambition, resources. | Define target, owner, initiative, and review rhythm. | Targets and initiatives. |
| Check balance | Scorecard draft. | Remove overload and check whether short-term financial goals crowd out capability and customer measures. | Balanced scorecard. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- balanced scorecard:
- perspective objectives:
- metrics and targets:
- initiative gaps:

### 3. Implications
- What this changes:
- What to do first:
- What to watch:

### 4. Open Questions
- Missing evidence:
- Validation step:
- Owner / timing:
```

## Quality Gate

- The output must change a decision, action, prioritization, risk view, or validation plan.
- Every major claim must be tied to evidence or labeled as an assumption.
- Each recommendation must name the action, owner or stakeholder, timing, and expected signal.
- Remove framework filler. Do not explain the method unless the explanation helps the user act.
- Keep wording professional and plain enough that a smart non-specialist can use it without translation.
