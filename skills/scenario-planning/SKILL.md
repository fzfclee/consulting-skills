---
name: scenario-planning
description: Use when external uncertainty is material and a single forecast would create false confidence. Use when applying the Scenario Planning consulting method and when a user asks for Scenario Planning, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Scenario Planning

Use this skill to run `Scenario Planning` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use critical uncertainties and signposts, not predictions.
- Separate no-regret actions from contingent options.

## Required Inputs

Collect or infer these inputs before execution:

- strategic question
- time horizon
- critical uncertainties
- known trends

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Frame decision and horizon | Strategic question, time horizon, geography/market. | State what decision must stay robust across futures. | Scenario scope. |
| Identify uncertainties | External trends, macro forces, market shifts. | Separate relatively certain trends from high-impact uncertainties. | Uncertainty list. |
| Build scenarios | Top uncertainties and trends. | Create 2-4 plausible scenarios with names and narratives. | Scenario set. |
| Derive implications | Scenario set and business model/strategy. | Assess risks, opportunities, and constraints in each scenario. | Scenario implications. |
| Choose options and signposts | Implications. | Define no-regret moves, contingent bets, and early indicators. | Scenario action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- scenario set:
- signposts:
- strategic implications:
- robust and contingent actions:

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
