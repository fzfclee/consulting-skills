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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- five forces analysis:
- profit pressure diagnosis:
- strategic implications:

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
