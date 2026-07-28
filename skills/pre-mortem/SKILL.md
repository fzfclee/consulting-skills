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

Do not use after a failure has already occurred; use root-cause analysis instead. A pre-mortem requires a specific plan and time horizon, not a generic list of things that might go wrong.

## Adjacent Methods

- `risk-matrix`: prioritize known risk events after they are identified.
- `scenario-planning`: compare plausible external futures, not failure causes of one plan.

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
### 1. Plan And Failure Horizon
Plan:
Launch / decision date:
Assumed failure date:
Success definition:

### 2. Failure Narrative
The plan failed because:
Observed consequences:
Earliest warning:

### 3. Failure Modes
| Failure mode | Cause | Preventability | Evidence | Priority |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Prevention Plan
| Prevention / contingency | Owner | Timing | Trigger |
|---|---|---|---|
|  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Plan And Failure Horizon, Failure Narrative, Failure Modes; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
