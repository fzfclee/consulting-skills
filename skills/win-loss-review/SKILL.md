---
name: win-loss-review
description: Use after a deal, project, pitch, proposal, or client pursuit to learn why the outcome happened. Use when applying the Win Loss Review consulting method and when a user asks for Win Loss Review, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Win Loss Review

Use this skill to run `Win Loss Review` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Separate factual timeline from interpretation.
- Classify drivers as controllable, influenceable, or external.

## Required Inputs

Collect or infer these inputs before execution:

- opportunity history
- outcome
- buyer feedback
- competitor information
- sales actions

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a blame review. Use it to improve the next pursuit, decision, or operating process.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Reconstruct timeline | Opportunity data, meetings, proposal, feedback, outcome. | Write factual chronology without interpretation. | Win/loss timeline. |
| Map decision drivers | Buyer criteria, stakeholders, competitors, price, proof. | Identify why the buyer chose the outcome. | Decision driver map. |
| Classify drivers | Decision driver map. | Mark each driver as controllable, influenceable, or external. | Controllability view. |
| Extract lessons | Controllability view and future pursuits. | Convert drivers into specific behavior or asset changes. | Lessons learned. |
| Update playbook | Lessons, owners, next opportunities. | Define qualification, messaging, proof, pricing, or relationship changes. | Improvement action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- win/loss diagnosis:
- decision drivers:
- repeatable lessons:
- improvement actions:

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
