---
name: effort-impact-matrix
description: Use when there are multiple possible next actions and the user needs quick wins, major projects, fill-ins, or deprioritized items. Use when applying the Effort Impact Matrix consulting method and when a user asks for Effort Impact Matrix, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Effort Impact Matrix

Use this skill to run `Effort Impact Matrix` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Normalize items so each one is an executable action.
- Use quick wins, major bets, fill-ins, and deprioritize/defer.

## Required Inputs

Collect or infer these inputs before execution:

- candidate actions
- impact estimate
- effort estimate
- time or resource constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| List actions | Candidate actions or initiatives. | Rewrite broad ideas into one-action items. | Normalized action list. |
| Define scoring anchors | Objective, constraints, available capacity. | Define what high/medium/low impact and effort mean. | Scoring scale. |
| Score each action | Action list, evidence, effort estimates. | Rate impact and effort separately; mark confidence. | Scored action table. |
| Place quadrants | Scored table. | Classify quick wins, major bets, fill-ins, and defer/drop items. | Effort-impact matrix. |
| Choose sequence | Matrix, dependencies, timing, risk. | Recommend first actions, later actions, and items to reject or validate. | Sequenced action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- 2x2 action map:
- recommended sequence:
- quick wins and no-go items:

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
