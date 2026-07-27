---
name: pestel-analysis
description: Use when market, policy, macro, or operating context may materially affect strategy or risk. Use when applying the PESTEL Analysis consulting method and when a user asks for PESTEL Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# PESTEL Analysis

Use this skill to run `PESTEL Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Scan Political, Economic, Social, Technological, Environmental, and Legal forces.
- Keep only external forces that can change the decision.

## Required Inputs

Collect or infer these inputs before execution:

- market or situation
- geography
- time horizon
- known external trends

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for generic essay writing. Use it only when external/internal factors must change a strategy, choice, or risk posture.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Set horizon and geography | Market, geography, industry, time horizon. | Define external environment boundary. | PESTEL scope. |
| Scan six categories | Political, Economic, Social, Technological, Environmental, Legal evidence. | List external forces under each category with source or confidence. | PESTEL factor list. |
| Filter material forces | Factor list, decision objective. | Keep only factors that can change opportunity, risk, cost, demand, or feasibility. | Material external forces. |
| Assess impact and timing | Material factors. | Rate direction, magnitude, likelihood, timing, and uncertainty. | Prioritized PESTEL table. |
| Define responses | Prioritized table. | Recommend adaptation, watch items, hedges, or validation needs. | External-context action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- PESTEL scan:
- material forces:
- implications:
- watchlist:

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
