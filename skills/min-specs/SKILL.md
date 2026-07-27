---
name: min-specs
description: Use when a plan, partnership, deal, product, change, or stakeholder move needs the minimum necessary conditions for success. Use when applying Min Specs, minimum specifications, must-have constraints, no-go criteria, or success conditions.
license: Apache-2.0
---

# Min Specs

Use this skill to define the smallest set of must-have conditions that make an action viable.

## Method Notes

- Min Specs identify what is truly required, not a wish list.
- The method helps prevent overbuilding, over-negotiating, and pursuing deals that cannot work.
- A good Min Spec is binary enough to guide proceed / adjust / stop decisions.

## Required Inputs

Collect or infer these inputs before execution:

- desired outcome
- proposed action, deal, solution, or change
- constraints and non-negotiables
- known failure modes
- stakeholder or customer requirements

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the user needs to rank attractive options rather than define viability. Use `decision-matrix`, `weighted-scorecard`, or `wsjf-prioritization` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define success | Desired outcome, decision boundary. | State what must be true for the initiative to be considered successful. | Success definition. |
| List possible requirements | Stakeholder needs, constraints, risks, operating needs. | Create a broad list of candidate conditions. | Requirement pool. |
| Remove nice-to-haves | Candidate requirements, success definition. | Ask whether success fails without this condition. If not, move it to nice-to-have. | Trimmed requirements. |
| Convert to minimum specs | Must-have conditions. | Rewrite each condition as observable, testable, and binary where possible. | Min Specs list. |
| Define no-go criteria | Failure modes, risk tolerance, constraints. | State what would make the action non-viable or require redesign. | No-go list. |
| Link to next action | Current plan, validation access, owners. | Decide what to confirm first and what action is allowed before confirmation. | Decision gate. |

## Output Template

```markdown
### 1. Success Definition
- Desired outcome:
- Decision boundary:
- What would count as failure:

### 2. Min Specs
| Minimum condition | Why it is required | Evidence now | How to verify | Pass / fail / unknown |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Nice-To-Haves Removed
- Nice-to-have:
- Why it is not required now:

### 4. No-Go Criteria
| No-go condition | Trigger signal | Response |
|---|---|---|
|  |  |  |

### 5. Decision Gate
- Proceed if:
- Adjust if:
- Stop if:
- First thing to verify:
```

## Quality Gate

- Keep Min Specs few and strict. If everything is required, nothing is clarified.
- Avoid vague wording such as "good support" or "strong alignment"; define observable behavior.
- Separate minimum conditions from preferences.
- Include stop or redesign criteria.
- Keep the output usable in a real decision conversation.
