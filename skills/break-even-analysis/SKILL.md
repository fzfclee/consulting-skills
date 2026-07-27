---
name: break-even-analysis
description: Use when a commercial, operational, or investment decision needs a threshold for viability. Use when applying the Break Even Analysis consulting method and when a user asks for Break Even Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Break Even Analysis

Use this skill to run `Break Even Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Separate fixed cost, variable cost, unit economics, and time horizon.
- State the exact threshold that makes the option viable.

## Required Inputs

Collect or infer these inputs before execution:

- fixed costs
- variable costs
- price or benefit per unit
- time horizon
- constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define break-even unit | Decision, economics, unit of value. | Choose unit, revenue, margin, savings, or time as the threshold. | Break-even definition. |
| Separate cost types | Fixed cost, variable cost, recurring cost, one-off cost. | Classify costs so the formula is clear. | Cost structure. |
| Estimate unit economics | Price, margin, savings, utilization, adoption. | Calculate contribution or benefit per unit. | Unit economics. |
| Calculate threshold | Cost structure and unit economics. | Compute break-even quantity, revenue, savings, or months. | Break-even threshold. |
| Test realism | Market size, capacity, adoption, timeline. | Assess whether reaching the threshold is plausible. | Viability interpretation. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- break-even threshold:
- sensitivity view:
- viability interpretation:
- assumption risks:

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
