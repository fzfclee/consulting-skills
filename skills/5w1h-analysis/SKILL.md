---
name: 5w1h-analysis
description: Use when a situation, request, problem, event, stakeholder issue, process, or plan needs basic fact clarification through who, what, when, where, why, and how. Use when applying 5W1H, 4W1H, fact clarification, situation framing, or first-pass problem understanding.
license: Apache-2.0
---

# 5W1H Analysis

Use this skill to clarify the basic facts of a situation before deeper analysis.

## Method Notes

- 5W1H means Who, What, When, Where, Why, and How.
- It is a simple clarification method, not a full diagnosis.
- It is useful when the input is messy, missing basic context, or mixing facts and interpretations.
- The method should produce clear missing-information questions and a sharper problem statement.

## Required Inputs

Collect or infer these inputs before execution:

- raw situation description
- known stakeholders or actors
- event, problem, decision, or plan
- timing and location or context
- current explanation or desired outcome

If an input is missing, mark it as `unknown` and add a targeted question.

## When Not To Use

Do not use when the basic facts are already clear and the issue needs prioritization, root cause, or system diagnosis. Use a more specific method instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Clarify who | Stakeholders, actors, owners, affected parties. | Identify who is involved, who decides, who acts, and who is affected. | Who map. |
| Clarify what | Event, decision, problem, action, object. | State what happened, what is being decided, or what must be done. | What statement. |
| Clarify when | Timing, sequence, deadline, frequency. | Record when it happened, when it changed, and when action is needed. | Timing view. |
| Clarify where | Location, channel, process step, market, context. | State where the issue appears or where action must happen. | Context boundary. |
| Clarify why | Stated purpose, reason, motive, cause, expected value. | Separate stated reason from inferred reason. | Why view. |
| Clarify how | Process, mechanism, approach, resources. | Describe how it happens now and how action could happen. | How view. |
| Summarize gaps | Unknown fields. | Convert missing or weak fields into precise questions. | Clarification questions. |

## Output Template

```markdown
### 1. 5W1H Fact Frame
| Dimension | Current answer | Evidence strength | Missing / unclear |
|---|---|---|---|
| Who |  | strong / medium / weak / unknown |  |
| What |  | strong / medium / weak / unknown |  |
| When |  | strong / medium / weak / unknown |  |
| Where |  | strong / medium / weak / unknown |  |
| Why |  | strong / medium / weak / unknown |  |
| How |  | strong / medium / weak / unknown |  |

### 2. Sharpened Situation Statement
- In one sentence:

### 3. Clarification Questions
1.
2.
3.

### 4. Recommended Next Method
- If facts remain unclear:
- If facts are clear enough:
```

## Quality Gate

- Separate stated facts from inferred motives or causes.
- Do not over-analyze before basic who/what/when/where/why/how are clear.
- Keep questions specific and answerable.
- Use 5W1H to prepare for deeper methods, not to replace them.
- Mark unknowns plainly rather than guessing.
