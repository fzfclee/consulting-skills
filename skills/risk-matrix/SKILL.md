---
name: risk-matrix
description: Use when a plan, deal, project, or stakeholder move has material downside that needs explicit controls. Use when applying the Risk Matrix consulting method and when a user asks for Risk Matrix, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Risk Matrix

Use this skill to run `Risk Matrix` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Define risk as event + cause + consequence.
- Score likelihood, impact, and optional detectability, then assign owner and trigger.

## Required Inputs

Collect or infer these inputs before execution:

- planned action or project
- risk list
- impact definitions
- owners

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define objective | Plan/project/decision and success criteria. | State what outcome risks threaten. | Risk scope. |
| List risks | Assumptions, dependencies, history, stakeholder input. | Write each risk as event + cause + consequence. | Risk register. |
| Score risks | Likelihood, impact, detectability/evidence. | Rate each risk using consistent anchors. | Risk matrix. |
| Plan responses | Top risks and constraints. | Assign mitigation, contingency, owner, and trigger. | Risk response plan. |
| Set monitoring | Triggers, cadence, governance. | Define review rhythm and escalation threshold. | Risk monitoring plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- risk matrix:
- top risks:
- mitigation actions:
- early warning indicators:

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
