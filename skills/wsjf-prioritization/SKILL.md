---
name: wsjf-prioritization
description: Use when sequencing backlog items, initiatives, features, epics, or projects where delay cost and job size both matter. Use when applying Weighted Shortest Job First, WSJF, Cost of Delay divided by Job Size, economic sequencing, backlog prioritization, or lean/agile prioritization.
license: Apache-2.0
---

# WSJF Prioritization

Use this skill to run `WSJF Prioritization` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- WSJF means Weighted Shortest Job First.
- Core formula: `WSJF = Cost of Delay / Job Size`.
- Cost of Delay is commonly estimated as `User/Business Value + Time Criticality + Risk Reduction / Opportunity Enablement`.
- Use relative scoring for comparison. Do not pretend the numbers are precise financial forecasts unless real financial data is available.
- Revisit WSJF when market timing, risk, dependency, or job size changes.

## Required Inputs

Collect or infer these inputs before execution:

- candidate jobs or backlog items
- user/business value estimate
- time criticality estimate
- risk reduction or opportunity enablement estimate
- job size estimate

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use WSJF when options are too vague to size, when the work is purely exploratory with no meaningful delay cost, or when a hard dependency makes sequencing mathematically irrelevant. Use `effort-impact-matrix` first if the items are still broad themes.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Normalize jobs | Candidate jobs, initiatives, features, epics, or projects. | Rewrite each item so it is one comparable job with a clear outcome and boundary. | Normalized job list. |
| Estimate Cost of Delay components | User/business value, time criticality, risk reduction, opportunity enablement evidence. | Score each component on the same relative scale, such as Fibonacci or 1-10; record rationale and confidence. | Component scoring table. |
| Calculate Cost of Delay | Component scores. | Add User/Business Value + Time Criticality + Risk Reduction / Opportunity Enablement. | Cost of Delay score per job. |
| Estimate Job Size | Scope, complexity, duration, effort, dependencies, delivery capacity. | Score relative job size using the same sizing discipline for every item. | Job Size score per job. |
| Calculate and sequence | Cost of Delay and Job Size scores. | Divide Cost of Delay by Job Size and rank high to low; then check dependencies and confidence. | WSJF-ranked sequence with caveats. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Scoring scale:
- Evidence used:
- Key assumptions:

### 2. WSJF Scoring Table
| Job | User / business value | Time criticality | Risk reduction / opportunity enablement | Cost of Delay | Job Size | WSJF | Confidence | Notes |
|---|---:|---:|---:|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |  |  |

### 3. Recommended Sequence
1.
2.
3.

### 4. Caveats
- Dependency constraints:
- Low-confidence estimates:
- What would change the ranking:

### 5. Next Action
- First job to start:
- Owner:
- Validation signal:
```

## Quality Gate

- Every job must be normalized before scoring.
- Cost of Delay must include time sensitivity, not only generic importance.
- Job Size must reflect delivery effort or duration, not business value.
- Do not let sunk cost influence the score.
- If two jobs have similar WSJF scores, prefer the one with higher confidence, fewer blocking dependencies, or faster learning value.
- Keep wording professional and plain enough that a smart non-specialist can use it without translation.
