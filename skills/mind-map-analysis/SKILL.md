---
name: mind-map-analysis
description: Use when ideas, concerns, stakeholders, causes, or options are scattered and need a clear structure before deeper analysis. Use when applying the Mind Map Analysis consulting method and when a user asks for Mind Map Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Mind Map Analysis

Use this skill to run `Mind Map Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use this for exploration before forcing a decision matrix or issue tree.
- Cluster raw ideas into themes, then convert themes into next questions.

## Required Inputs

Collect or infer these inputs before execution:

- topic
- raw ideas or notes
- constraints
- desired output

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to decorate an answer. Use it when the problem is too messy to analyze directly.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Set center | Topic, decision, or messy input. | Write the central idea as a short phrase or question. | Mind-map center. |
| Cluster raw inputs | Notes, concerns, ideas, stakeholders, facts. | Group inputs into first-level branches. | Theme branches. |
| Expand branches | Theme branches. | Add causes, evidence, implications, options, owners, and open questions. | Expanded mind map. |
| Clean structure | Expanded map. | Merge duplicates, split overloaded branches, and flag weak links. | Usable map. |
| Choose next method | Usable map and decision need. | Decide whether to move to issue tree, stakeholder map, risk matrix, or action plan. | Next-analysis recommendation. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- mind map outline:
- theme clusters:
- priority branches:
- next analysis questions:

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
