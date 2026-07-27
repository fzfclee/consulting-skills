---
name: fishbone-diagram
description: Use when a problem may have multiple operational, human, process, system, or environmental causes. Use when applying the Fishbone Diagram consulting method and when a user asks for Fishbone Diagram, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Fishbone Diagram

Use this skill to run `Fishbone Diagram` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use categories such as people, process, systems, policy, environment, and measurement.
- Prioritize cause branches for evidence testing.

## Required Inputs

Collect or infer these inputs before execution:

- problem statement
- observed symptoms
- process context
- candidate cause categories

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to assign blame. Use it to find controllable causes and recurrence prevention.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define effect | Problem statement, defect, service failure, or outcome gap. | Place the problem at the head of the fishbone. | Effect statement. |
| Choose categories | Domain context. | Select people, process, systems, policy, environment, measurement, or custom categories. | Cause categories. |
| Populate causes | Evidence, team input, process facts. | List possible causes under each category. | Fishbone cause map. |
| Mark evidence | Cause map and available data. | Label causes as evidenced, assumed, contradicted, or unknown. | Evidence-coded fishbone. |
| Prioritize tests | Evidence-coded fishbone. | Choose top cause branches and validation tests. | Root-cause test plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- fishbone cause map:
- most likely cause branches:
- evidence gaps:
- test plan:

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
