---
name: swot-analysis
description: Use when the situation needs a balanced snapshot of position, options, and external pressure before choosing a strategy. Use when applying the SWOT Analysis consulting method and when a user asks for SWOT Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# SWOT Analysis

Use this skill to run `SWOT Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Strengths and weaknesses are internal; opportunities and threats are external.
- Turn the four quadrants into strategic moves, not a brainstorm archive.

## Required Inputs

Collect or infer these inputs before execution:

- objective
- internal capabilities
- external market or stakeholder context
- constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for generic essay writing. Use it only when external/internal factors must change a strategy, choice, or risk posture.

## Adjacent Methods

- `pestel-analysis`: examine macro external forces in depth.
- `porter-five-forces`: examine industry structure and profit pressure.
- `competitive-positioning`: define the buyer-facing choice and proof versus alternatives.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Frame objective | Business, project, account, or decision scope. | State the decision the SWOT should inform. | SWOT objective. |
| Fill internal factors | Capabilities, assets, constraints, performance, resources. | List strengths and weaknesses that the actor can control or influence. | Strengths and weaknesses. |
| Fill external factors | Market, customer, competitor, regulatory, technology, stakeholder context. | List opportunities and threats outside the actor's direct control. | Opportunities and threats. |
| Prioritize factors | Four-quadrant list and evidence. | Rank by impact, urgency, addressability, and evidence strength. | Priority SWOT factors. |
| Convert to moves | Priority factors. | Define SO, WO, ST, and WT moves or a smaller set of practical actions. | Strategic action implications. |

## Output Template

```markdown
### 1. Objective And Evidence Boundary
Objective:
Scope:
Time horizon:
Evidence cut-off:

### 2. SWOT
| Quadrant | Factor | Evidence | Materiality | Controllability |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Strategic Combinations
| Move | SO / WO / ST / WT | Rationale | Risk |
|---|---|---|---|
|  |  |  |  |

### 4. Priority Action
| Action | Owner | Timing | Signal | Stop condition |
|---|---|---|---|---|
|  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Objective And Evidence Boundary, SWOT, Strategic Combinations; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
