---
name: power-interest-grid
description: Use when stakeholders need to be grouped into manage closely, keep satisfied, keep informed, or monitor categories. Use when applying the Power Interest Grid consulting method and when a user asks for Power Interest Grid, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Power Interest Grid

Use this skill to run `Power Interest Grid` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use four cells: manage closely, keep satisfied, keep informed, monitor.
- Power means ability to change the outcome; interest means concern about the outcome.

## Required Inputs

Collect or infer these inputs before execution:

- stakeholder list
- decision context
- power evidence
- interest evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a personality-reading exercise. Use it only to clarify decision rights, influence, needs, and next engagement moves.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the change or decision | Decision/change, deadline, affected groups. | State what outcome the grid is meant to influence. | Grid scope. |
| Identify stakeholders | Named people, teams, customers, regulators, partners. | List actors and remove duplicates or irrelevant observers. | Stakeholder list. |
| Score power and interest | Authority, influence, dependency, impact, concern level. | Place each actor on high/low power and high/low interest axes. | 2x2 power-interest grid. |
| Choose engagement strategy | Grid placement and relationship constraints. | Assign manage closely, keep satisfied, keep informed, or monitor. | Engagement category per actor. |
| Define communication actions | Category, message need, channel, owner, cadence. | Specify message, sender, timing, and feedback signal. | Communication and engagement plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- power-interest grid:
- engagement category for each stakeholder:
- priority communication actions:

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
