---
name: pre-mortem
description: Use before launching a plan, project, deal, or change when failure modes should be surfaced early. Use when applying the Pre Mortem consulting method and when a user asks for Pre Mortem, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Pre Mortem

Use this skill to run `Pre Mortem` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use prospective hindsight: assume the plan failed, then explain why.
- Convert failure causes into prevention actions and early warnings.

## Required Inputs

Collect or infer these inputs before execution:

- planned action
- success criteria
- timeline
- stakeholders
- known risks

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Describe plan | Plan, launch date, success criteria. | State the plan as if the team believes it will work. | Plan frame. |
| Assume failure | Future date and failed outcome. | Write a short future failure narrative. | Failure scenario. |
| Generate causes | Team concerns, dependencies, assumptions. | List plausible reasons the plan failed. | Failure cause list. |
| Prioritize preventable causes | Cause list, likelihood, impact, controllability. | Pick the causes worth preventing now. | Priority failure modes. |
| Design prevention | Priority causes. | Define prevention actions, early warnings, owners, and contingencies. | Pre-mortem action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- failure narrative:
- likely failure causes:
- prevention actions:
- early warning signals:

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
