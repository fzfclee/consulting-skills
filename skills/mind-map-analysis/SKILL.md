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

Do not use when the decision requires MECE structure, causal proof, or option scoring. A mind map is for exploration and connection, not final prioritization.

## Adjacent Methods

- `affinity-diagram`: cluster raw qualitative notes into evidence-based themes.
- `issue-tree`: turn an explored topic into a decision-oriented analysis structure.

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
### 1. Central Question
Topic:
Decision use:
Scope:
Source material:

### 2. Theme Map
| Branch | Sub-branch | Evidence / example | Open question |
|---|---|---|---|
|  |  |  |  |

### 3. Connections And Gaps
| Connection / gap | Why it matters |
|---|---|
|  |  |

### 4. Next Analysis
Priority branch:
Needed evidence:
Appropriate next method, if any:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Central Question, Theme Map, Connections And Gaps; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
