---
name: affinity-diagram
description: Use when many raw ideas, observations, quotes, pain points, risks, requirements, or research notes need to be grouped into natural themes. Use when applying affinity diagramming, affinity mapping, KJ method, qualitative clustering, theme synthesis, or sensemaking from messy inputs.
license: Apache-2.0
---

# Affinity Diagram

Use this skill to turn scattered qualitative inputs into clear, evidence-backed theme clusters.

## Method Notes

- Affinity diagramming groups raw observations by natural relationship, not by a pre-decided framework.
- It is strongest when the input contains many notes, quotes, feedback items, ideas, symptoms, or concerns.
- The method should preserve traceability from each cluster back to the raw input.
- The output should help the next step: problem framing, prioritization, journey mapping, root-cause diagnosis, or solution design.

## Required Inputs

Collect or infer these inputs before execution:

- raw items to cluster
- source or context of each item when available
- purpose of the clustering
- audience or decision context
- any known constraints, such as time, segment, process stage, or stakeholder group

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the categories are already fixed by a required taxonomy, compliance rule, financial chart of accounts, or formal decision criteria. Use `mece-framework`, `decision-matrix`, or `weighted-scorecard` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the synthesis question | Purpose, decision context, audience. | State what the clustering needs to clarify. Keep it broad enough for themes to emerge. | Synthesis question. |
| Normalize raw items | Notes, quotes, observations, ideas, risks, requirements. | Split compound items, remove duplicates only when meaning is truly identical, and keep source labels when possible. | Clean item list. |
| Cluster by natural similarity | Clean item list. | Group items that express the same need, friction, cause, behavior, or opportunity. Avoid imposing a favorite framework too early. | Draft clusters. |
| Name each cluster | Draft clusters, representative items. | Give each cluster a plain, specific label that explains the shared meaning. | Cluster names. |
| Test cluster quality | Cluster list, raw items. | Check whether each cluster is internally coherent and distinct from other clusters. Move or split weak clusters. | Refined affinity map. |
| Extract implications | Refined clusters, synthesis question. | Identify what each cluster implies for the decision, diagnosis, or next analysis. | Theme implications. |
| Identify outliers and gaps | Unclustered items, missing sources, thin clusters. | Preserve outliers that may represent weak signals, minority needs, or evidence gaps. | Outlier and gap list. |

## Output Template

```markdown
### 1. Synthesis Question
- Purpose:
- Input scope:
- Decision or next use:

### 2. Affinity Map
| Cluster | Shared meaning | Raw items included | Evidence strength | Implication |
|---|---|---|---|---|
|  |  |  | strong / medium / weak |  |

### 3. Cluster Quality Check
| Cluster | Internally coherent? | Distinct from others? | Needs split / merge / keep |
|---|---|---|---|
|  | yes / partly / no | yes / partly / no |  |

### 4. Outliers And Gaps
- Outlier item:
- Why it may matter:
- Missing input:

### 5. Next Use
- Best next method or decision step:
- What to validate before acting:
```

## Quality Gate

- Do not force raw items into a pre-existing framework unless the user requires one.
- Keep cluster labels specific; avoid vague labels such as "process issues" if the shared meaning is narrower.
- Preserve outliers instead of hiding them in miscellaneous.
- Avoid double-counting the same raw item across clusters unless it genuinely has two meanings.
- Keep traceability from conclusion back to source item.
