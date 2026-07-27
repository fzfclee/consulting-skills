---
name: empathy-map
description: Use when stakeholder motivation is unclear and the work requires a grounded, human view before messaging or intervention design. Use when applying the Empathy Map consulting method and when a user asks for Empathy Map, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Empathy Map

Use this skill to run `Empathy Map` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use Says, Thinks, Does, Feels; optionally add pains, gains, pressures, and trust signals.
- Never put guesses into Says or Does.

## Required Inputs

Collect or infer these inputs before execution:

- target person or segment
- observed behavior
- quotes or facts
- uncertain assumptions

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a personality-reading exercise. Use it only to clarify decision rights, influence, needs, and next engagement moves.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Choose target | One user, persona, buyer, stakeholder, or segment. | State the person/context and the decision the map should support. | Empathy-map scope. |
| Collect evidence | Quotes, observed behavior, meeting notes, interview notes, usage data. | Separate direct evidence from interpretation before filling quadrants. | Evidence list. |
| Fill quadrants | Evidence list. | Map Says, Thinks, Does, and Feels; optionally add pains, gains, pressures, and trust signals. | Empathy map. |
| Identify patterns | Completed map. | Find contradictions, repeated concerns, hidden anxieties, and unmet needs. | Need and concern diagnosis. |
| Translate to action | Diagnosis, message goal, product/service/action options. | Define message, question, offer, service change, or validation step. | Action implications. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- empathy map:
- needs and fears:
- validated assumptions:
- message implications:

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
