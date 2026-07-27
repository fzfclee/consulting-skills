---
name: validation-plan
description: Use when a recommendation, hypothesis, action plan, or business decision needs explicit evidence, tests, decision gates, and continue-adjust-stop criteria. Use when applying validation planning, experiment design, hypothesis test design, decision gates, or learning plan.
license: Apache-2.0
---

# Validation Plan

Use this skill to turn a recommendation into a testable plan with evidence standards and decision gates.

## Method Notes

- Validation is not the same as implementation. It defines what evidence will increase or reduce confidence.
- A good validation plan names the hypothesis, test, signal, threshold, owner, timing, and decision rule.
- It should be proportional to risk: higher-risk decisions need stronger validation.

## Required Inputs

Collect or infer these inputs before execution:

- recommendation or hypothesis to validate
- decision consequence and risk level
- available evidence and current confidence
- feasible tests or evidence sources
- timeline, owner, and decision deadline

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the user has not yet formed a hypothesis or action option. Use `evidence-map`, `issue-tree`, or `hypothesis-tree` first.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the hypothesis | Recommendation, expected outcome, current confidence. | Write the claim to be validated in one testable sentence. | Validation hypothesis. |
| Define decision consequence | Risk, reversibility, cost of wrong action. | Decide how strong the evidence must be before action. | Evidence standard. |
| Select validation method | Evidence sources, access, timeline. | Choose interview, document check, commitment test, pilot, prototype, data analysis, stakeholder signal, or market test. | Validation method. |
| Define success and failure signals | Hypothesis, expected behavior, thresholds. | Make pass, adjust, and stop criteria explicit. | Decision criteria. |
| Plan execution | Owner, timing, script or data need, dependencies. | Specify who does what by when and with what artifact. | Validation workplan. |
| Decide next gate | Test result, action options. | Define what decision will be made after evidence arrives. | Continue / adjust / stop gate. |

## Output Template

```markdown
### 1. Hypothesis To Validate
- Working hypothesis:
- Current confidence:
- Cost of being wrong:

### 2. Evidence Standard
- Required confidence before action:
- Minimum evidence needed:
- Evidence that would weaken the recommendation:

### 3. Validation Plan
| Test | What it validates | Method | Owner / actor | Timing | Pass signal | Adjust signal | Stop signal |
|---|---|---|---|---|---|---|---|
|  |  | interview / document check / pilot / commitment test / data analysis / stakeholder signal / market test |  |  |  |  |  |

### 4. Decision Gate
- Continue if:
- Adjust if:
- Stop if:
- Escalate if:

### 5. Next Step
- First validation action:
- Exact evidence to bring back:
```

## Quality Gate

- Every validation test must connect to a specific hypothesis.
- Do not use vanity signals such as polite interest when commitment is required.
- Define disconfirming evidence, not only confirming evidence.
- Match validation depth to decision risk and reversibility.
- Keep the plan realistic for the user's access and timeline.
