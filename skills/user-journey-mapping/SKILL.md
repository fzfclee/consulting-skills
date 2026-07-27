---
name: user-journey-mapping
description: Use when improving a customer, employee, partner, or stakeholder experience across a process or lifecycle. Use when applying the User Journey Mapping consulting method and when a user asks for User Journey Mapping, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# User Journey Mapping

Use this skill to run `User Journey Mapping` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Map one persona or segment through a timeline to accomplish one goal.
- Include actions, touchpoints, thoughts, emotions, pain points, and opportunities.

## Required Inputs

Collect or infer these inputs before execution:

- persona or user segment
- journey scope
- known touchpoints
- pain points and evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for all users at once. Choose one segment, scenario, journey, job, or service context.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define persona and goal | User segment, goal, scenario, start/end points. | Choose one journey for one user type. | Journey scope. |
| Map stages | Timeline, observed steps, channels. | Lay out chronological stages from trigger to outcome. | Journey stage map. |
| Add touchpoints and emotions | User actions, touchpoints, thoughts, feelings, evidence. | Fill each stage with actions, touchpoints, thoughts, emotions, and evidence. | Detailed journey map. |
| Find pain points and moments | Detailed map. | Identify friction, unmet needs, trust moments, and drop-off risks. | Pain point and opportunity list. |
| Prioritize interventions | Pain points, business owners, impact, effort. | Choose changes and validation signals by stage. | Journey improvement plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- journey map:
- moments that matter:
- friction points:
- improvement opportunities:

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
