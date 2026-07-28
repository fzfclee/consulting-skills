---
name: rice-scoring
description: Use when ranking product, business, GTM, process, or analysis initiatives with explicit uncertainty and effort. Use when applying the RICE Scoring consulting method and when a user asks for RICE Scoring, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# RICE Scoring

Use this skill to run `RICE Scoring` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use Reach x Impact x Confidence / Effort.
- Use the same time window and reach unit for every item.

## Required Inputs

Collect or infer these inputs before execution:

- candidate initiatives
- reach estimate
- impact estimate
- confidence level
- effort estimate

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when reach, impact, confidence, and effort are measured at incompatible levels or when compliance and dependency gates dominate the choice. RICE ranks comparable initiatives; it does not make strategy.

## Adjacent Methods

- `decision-matrix`: choose among strategic alternatives.
- `weighted-scorecard`: repeatable vendor or governance scoring.
- `wsjf-prioritization`: use when Cost of Delay is the central economic logic.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define scoring window | Time horizon, audience, product/business objective. | Set the same reach period and outcome for all items. | RICE scope. |
| Estimate Reach | Users/accounts/transactions affected in the window. | Count or estimate how many units each initiative reaches. | Reach values. |
| Estimate Impact and Confidence | Expected outcome change, evidence strength. | Score impact and confidence using consistent anchors. | Impact/confidence values. |
| Estimate Effort | People/time/cost needed. | Estimate total effort in the same unit for every initiative. | Effort values. |
| Calculate and rank | Reach, Impact, Confidence, Effort. | Compute Reach x Impact x Confidence / Effort and inspect low-confidence winners. | Ranked RICE backlog. |

## Output Template

```markdown
### 1. Scope And Scale
Backlog:
Time horizon:
Reach unit:
Impact scale:
Effort unit:

### 2. Scores
| Initiative | Reach | Impact | Confidence | Effort | RICE | Evidence |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### 3. Ranking And Caveats
| Rank | Initiative | Main uncertainty | Dependency |
|---|---|---|---|
|  |  |  |  |

### 4. Decision
Fund now:
Validate first:
Do not prioritize:
Review trigger:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Scope And Scale, Scores, Ranking And Caveats; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
