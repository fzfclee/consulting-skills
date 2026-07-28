---
name: communications-plan
description: Use when a decision, change, project, or stakeholder move needs coordinated communication. Use when applying the Communications Plan consulting method and when a user asks for Communications Plan, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Communications Plan

Use this skill to run `Communications Plan` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Segment by audience role and concern, not by org chart only.
- Every message must specify sender, channel, timing, and requested action.

## Required Inputs

Collect or infer these inputs before execution:

- communication objective
- audiences
- messages
- channels
- timing constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before the audience, required behavior, sender, channel, timing, and feedback path are clear. Communication cannot compensate for missing authority, broken process, or misaligned incentives.

## Adjacent Methods

- `change-impact-analysis`: identify who is affected and what adoption support is needed.
- `raci-matrix`: clarify who owns each communication decision and action.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Set communication objective | Decision/change, desired audience behavior, timing. | Define what each audience must know, feel, decide, or do. | Communication objective. |
| Segment audiences | Stakeholders, power map, impact analysis, relationship facts. | Group audiences by role, concern, impact, and required action. | Audience segments. |
| Build message matrix | Audience segments, evidence, likely objections. | Write message, proof, tone, sender, channel, and timing for each segment. | Audience-message matrix. |
| Set cadence and feedback | Channels, decision timeline, meeting rhythm. | Define update cadence, feedback collection, and escalation route. | Cadence and feedback plan. |
| Check readiness | Draft plan, risks, missing approvals. | Identify message gaps, sensitive audiences, and first communication action. | Ready-to-send communication plan. |

## Output Template

```markdown
### 1. Communication Objective
Decision / behavior needed:
Audience scope:
Constraints:
Known concerns:

### 2. Audience Message Matrix
| Audience | Needed action | Message | Evidence / proof | Channel | Sender |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 3. Cadence And Feedback
| Touchpoint | Timing | Owner | Feedback signal | Response rule |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Readiness Check
| Risk | Prevention | Trigger | Escalation |
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

- Produce the method-specific outputs for Communication Objective, Audience Message Matrix, Cadence And Feedback; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
