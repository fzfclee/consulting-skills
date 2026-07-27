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

Do not use as a personality-reading exercise. Use it only to clarify decision rights, influence, needs, and next engagement moves.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- communications plan:
- audience-message matrix:
- cadence:
- feedback and escalation path:

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
