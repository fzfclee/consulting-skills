---
name: scenario-planning
description: Use when external uncertainty is material and a single forecast would create false confidence. Use when applying the Scenario Planning consulting method and when a user asks for Scenario Planning, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Scenario Planning

Use this skill to run `Scenario Planning` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use critical uncertainties and signposts, not predictions.
- Separate no-regret actions from contingent options.

## Required Inputs

Collect or infer these inputs before execution:

- strategic question
- time horizon
- critical uncertainties
- known trends

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

## Adjacent Methods

- `critical-uncertainties`: identify the variables before building scenarios.
- `pre-mortem`: rehearse failure of one chosen plan.
- `risk-matrix`: prioritize known risk events.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Frame decision and horizon | Strategic question, time horizon, geography/market. | State what decision must stay robust across futures. | Scenario scope. |
| Identify uncertainties | External trends, macro forces, market shifts. | Separate relatively certain trends from high-impact uncertainties. | Uncertainty list. |
| Build scenarios | Top uncertainties and trends. | Create 2-4 plausible scenarios with names and narratives. | Scenario set. |
| Derive implications | Scenario set and business model/strategy. | Assess risks, opportunities, and constraints in each scenario. | Scenario implications. |
| Choose options and signposts | Implications. | Define no-regret moves, contingent bets, and early indicators. | Scenario action plan. |

## Output Template

```markdown
### 1. Decision And Horizon
Focal decision:
Time horizon:
Geography / market:
Predetermined elements:

### 2. Critical Uncertainties
| Uncertainty | Range | Impact | Evidence | Signpost |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Scenarios
| Scenario | Coherent conditions | Implication | Vulnerable assumption |
|---|---|---|---|
|  |  |  |  |

### 4. Robust Moves And Signposts
| Move | Robust / contingent | Trigger | Owner |
|---|---|---|---|
|  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Decision And Horizon, Critical Uncertainties, Scenarios; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
