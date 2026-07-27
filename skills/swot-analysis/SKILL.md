---
name: swot-analysis
description: Use when the situation needs a balanced snapshot of position, options, and external pressure before choosing a strategy. Use when applying the SWOT Analysis consulting method and when a user asks for SWOT Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# SWOT Analysis

Use this skill to run `SWOT Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Strengths and weaknesses are internal; opportunities and threats are external.
- Turn the four quadrants into strategic moves, not a brainstorm archive.

## Required Inputs

Collect or infer these inputs before execution:

- objective
- internal capabilities
- external market or stakeholder context
- constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for generic essay writing. Use it only when external/internal factors must change a strategy, choice, or risk posture.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Frame objective | Business, project, account, or decision scope. | State the decision the SWOT should inform. | SWOT objective. |
| Fill internal factors | Capabilities, assets, constraints, performance, resources. | List strengths and weaknesses that the actor can control or influence. | Strengths and weaknesses. |
| Fill external factors | Market, customer, competitor, regulatory, technology, stakeholder context. | List opportunities and threats outside the actor's direct control. | Opportunities and threats. |
| Prioritize factors | Four-quadrant list and evidence. | Rank by impact, urgency, addressability, and evidence strength. | Priority SWOT factors. |
| Convert to moves | Priority factors. | Define SO, WO, ST, and WT moves or a smaller set of practical actions. | Strategic action implications. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- SWOT table:
- strategic implications:
- defensive and offensive moves:

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
