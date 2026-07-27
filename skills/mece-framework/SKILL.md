---
name: mece-framework
description: Use when a problem, issue tree, option set, segmentation, workplan, hypothesis set, risk list, or recommendation structure must be mutually exclusive and collectively exhaustive. Use when applying MECE, no-overlap/no-gap structuring, consulting issue decomposition, taxonomy cleanup, or structured problem solving.
license: Apache-2.0
---

# MECE Framework

Use this skill to check and improve whether a structure is clear, non-overlapping, and complete enough for decision work.

## Method Notes

- MECE means Mutually Exclusive and Collectively Exhaustive.
- Mutually exclusive means categories do not overlap in a way that creates double counting or unclear ownership.
- Collectively exhaustive means the structure covers all material parts of the question within the chosen scope.
- MECE is a discipline, not a slogan. Use it to improve clarity, not to make every real-world situation artificially neat.

## Required Inputs

Collect or infer these inputs before execution:

- core question or decision
- current structure, list, tree, segmentation, options, hypotheses, or workplan
- scope boundary
- intended use of the structure
- known exclusions, constraints, or edge cases

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use MECE when the user is still exploring raw ideas and premature structure would hide weak signals. Use `affinity-diagram` or `mind-map-analysis` first.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the scope | Core question, intended use, boundary. | Define what the structure must cover and what it deliberately excludes. | Scope statement. |
| List current branches | Existing list, tree, segments, options, hypotheses, or actions. | Put all current items at the same logical level when possible. | Current structure. |
| Test mutual exclusivity | Current branches, definitions. | Check whether two items overlap, duplicate, mix levels, or create ambiguous ownership. | Overlap diagnosis. |
| Test collective exhaustiveness | Scope, edge cases, known exclusions. | Ask what important case, stakeholder, cause, option, segment, or risk is missing. | Gap diagnosis. |
| Fix level and logic | Overlaps, gaps, mixed levels. | Rename, split, merge, move, or add branches so each item has one clear place. | Revised structure. |
| Define inclusion rules | Revised structure. | Write a short rule for what belongs in each branch and what does not. | Category rules. |
| Stress test with examples | Edge cases, sample facts, known scenarios. | Place sample items into the structure and check if any item fits nowhere or fits multiple places. | Stress-test result. |

## Output Template

```markdown
### 1. Scope
- Core question:
- Structure being tested:
- In scope:
- Out of scope:

### 2. Current Structure
| Branch / item | Current definition | Level | Issue detected |
|---|---|---|---|
|  |  | same level / mixed level | overlap / gap / unclear / ok |

### 3. MECE Diagnosis
| Problem | Where it appears | Why it matters | Fix |
|---|---|---|---|
| overlap / duplicate / mixed level / missing branch / unclear boundary |  |  |  |

### 4. Revised MECE Structure
| Branch | Inclusion rule | Exclusion rule | Example items |
|---|---|---|---|
|  |  |  |  |

### 5. Stress Test
- Item that fits clearly:
- Edge case:
- Remaining ambiguity:
- Next refinement:
```

## Quality Gate

- Do not confuse MECE with excessive completeness. The structure only needs to be complete for the current decision scope.
- Keep items at the same logical level whenever possible.
- Avoid mixing causes, symptoms, actions, owners, and metrics in the same branch set unless that is the deliberate design.
- Define inclusion and exclusion rules for ambiguous branches.
- If full MECE is impossible, state the practical boundary and remaining ambiguity.
