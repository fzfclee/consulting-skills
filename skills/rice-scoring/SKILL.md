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

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- RICE scores:
- ranked list:
- confidence caveats:
- recommended backlog:

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
