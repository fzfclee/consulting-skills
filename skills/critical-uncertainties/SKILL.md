---
name: critical-uncertainties
description: Use when a decision depends on a few uncertain variables whose direction could materially change the plan. Use when applying critical uncertainties, uncertainty mapping, scenario driver selection, strategic uncertainty review, or signpost planning.
license: Apache-2.0
---

# Critical Uncertainties

Use this skill to identify which unknowns matter most and how to monitor them.

## Method Notes

- A critical uncertainty is both highly uncertain and highly consequential.
- The method prevents false confidence when one forecast is not enough.
- It can feed scenario planning, validation plans, stakeholder strategy, and risk control.

## Required Inputs

Collect or infer these inputs before execution:

- decision question or strategic choice
- possible uncertainties
- decision time horizon
- consequences of different outcomes
- early indicators or data sources when available

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for ordinary risks with known mitigation paths. Use `risk-matrix` or `pre-mortem` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the decision horizon | Decision question, time horizon, action deadline. | State how far ahead the uncertainty matters. | Decision horizon. |
| List uncertainties | Unknowns, external variables, stakeholder unknowns, market shifts. | Write each uncertainty as a variable that can move in more than one direction. | Uncertainty list. |
| Rate uncertainty and impact | Evidence, volatility, consequence, controllability. | Rate uncertainty and impact as high / medium / low. | Uncertainty-impact table. |
| Select critical uncertainties | Rating table. | Choose the 1-3 uncertainties with high impact and high uncertainty. | Critical uncertainty set. |
| Define poles or outcomes | Critical uncertainties. | For each, define plausible opposite states or outcome ranges. | Uncertainty poles. |
| Create signposts | Evidence sources, leading indicators, stakeholder signals. | Define early signs that show which way the uncertainty is moving. | Signpost list. |
| Link to actions | Current plan, options, thresholds. | Decide what to do under each signal. | Contingent action logic. |

## Output Template

```markdown
### 1. Decision Frame
- Decision question:
- Time horizon:
- Why uncertainty matters:

### 2. Uncertainty Map
| Uncertainty | Impact | Uncertainty | Controllability | Why it matters | Critical? |
|---|---|---|---|---|---|
|  | high / medium / low | high / medium / low | high / medium / low |  | yes / no |

### 3. Critical Uncertainties
| Critical uncertainty | Possible direction A | Possible direction B | Signposts to watch | Action if A | Action if B |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 4. Decision Implication
- Robust action regardless of uncertainty:
- Action to delay until signal improves:
- Decision gate:
```

## Quality Gate

- Do not confuse uncertainty with general risk.
- A useful uncertainty must have more than one plausible outcome.
- Focus on variables that would change the plan.
- Include signposts, not just abstract possibilities.
- Keep output concrete enough to guide monitoring and next action.
