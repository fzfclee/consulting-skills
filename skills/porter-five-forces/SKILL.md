---
name: porter-five-forces
description: Use when assessing industry attractiveness, competitive pressure, pricing power, or strategic positioning. Use when applying the Porter Five Forces consulting method and when a user asks for Porter Five Forces, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Porter Five Forces

Use this skill to run `Porter Five Forces` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Analyze the industry or market structure, not one company in isolation.
- Cover rivalry, entrants, substitutes, buyer power, and supplier power.

## Required Inputs

Collect or infer these inputs before execution:

- industry or market
- competitors
- customers
- suppliers
- substitutes

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for generic essay writing. Use it only when external/internal factors must change a strategy, choice, or risk posture.

## Adjacent Methods

- `pestel-analysis`: macro external forces.
- `competitive-positioning`: buyer-facing differentiation and proof.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define industry boundary | Industry, geography, segment, value chain position. | State the market level being analyzed and exclude unrelated markets. | Industry boundary. |
| Analyze five forces | Competitors, buyers, suppliers, entrants, substitutes. | Assess rivalry, buyer power, supplier power, new entrants, and substitutes. | Five-forces evidence table. |
| Rate force strength | Evidence table. | Rate each force high/medium/low with evidence and trend direction. | Force strength profile. |
| Identify profit pressure | Force profile, economics, margins, switching costs. | Explain which forces capture value away from the business. | Industry attractiveness diagnosis. |
| Choose strategic response | Diagnosis and company constraints. | Recommend positioning, differentiation, partnership, pricing, channel, or moat actions. | Competitive strategy implications. |

## Output Template

```markdown
### 1. Industry Boundary
Market:
Geography:
Customer:
Time horizon:

### 2. Five Forces
| Force | Strength | Evidence | Profit mechanism | Trend |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Structural Pressure
Most important pressure:
Attractive niche / position:
Uncertainty:

### 4. Strategic Responses
| Response | Force addressed | Feasibility | Risk | Validation |
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

- Produce the method-specific outputs for Industry Boundary, Five Forces, Structural Pressure; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
