---
name: first-principles-thinking
description: Use when assumptions, analogies, legacy constraints, or accepted ways of working may be hiding a better solution. Use when applying First Principles Thinking, reasoning from fundamentals, assumption stripping, rebuilding from basic truths, or non-incremental problem solving.
license: Apache-2.0
---

# First Principles Thinking

Use this skill to run `First Principles Thinking` as a practical consulting method, not as a generic inspiration quote.

## Method Notes

- First principles thinking breaks a problem into the most basic truths that are still reliable in the current context.
- It deliberately avoids solving only by analogy, precedent, habit, or "how this is usually done."
- A useful first principle is not necessarily a universal law; it can be a context-specific truth that cannot be reduced further for the decision at hand.
- The method should rebuild options from the ground up, then reconnect them to constraints, economics, and execution reality.

## Required Inputs

Collect or infer these inputs before execution:

- problem statement
- current assumptions
- known constraints
- evidence or facts
- desired outcome

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the problem is already well-defined and only needs routine execution, compliance with fixed rules, or a known best-practice checklist. Use `decision-matrix`, `issue-tree`, or `five-whys-root-cause` first if the situation lacks a clear problem statement.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the problem plainly | Problem statement, desired outcome, decision context. | Rewrite the issue without inherited labels, solution language, or organizational shorthand. | Plain problem statement. |
| List assumptions and analogies | Current beliefs, constraints, common practice, benchmark logic. | Separate facts from assumptions, habits, analogies, and rules of thumb. | Assumption inventory. |
| Strip to fundamentals | Evidence, physical/economic/customer/process realities. | Ask what must be true, what is directly observed, and what cannot be reduced further for this decision. | First-principles breakdown. |
| Rebuild options | Fundamental truths, desired outcome, constraints. | Create options from the fundamentals instead of starting from existing solutions. | Rebuilt solution options. |
| Test against reality | Options, constraints, economics, stakeholder needs, validation data. | Check feasibility, risks, tradeoffs, and the fastest test that would prove or disprove each option. | Validation plan and recommended option. |

## Output Template

```markdown
### 1. Problem Frame
- Plain problem statement:
- Desired outcome:
- Decision boundary:

### 2. Assumption Inventory
| Assumption / analogy | Type | Evidence | Keep / challenge / test |
|---|---|---|---|
|  | fact / assumption / analogy / constraint |  |  |

### 3. First Principles
- Fundamental truth 1:
- Fundamental truth 2:
- Fundamental truth 3:

### 4. Rebuilt Options
| Option | Built from which first principle | Why it may work | Main risk | Fastest test |
|---|---|---|---|---|
|  |  |  |  |  |

### 5. Recommendation
- Best next move:
- What to stop assuming:
- Validation signal:
```

## Quality Gate

- Do not confuse first principles with personal opinion.
- Every first principle must be backed by evidence, direct observation, economics, physics, customer reality, process reality, or a clearly stated context boundary.
- The final options must be meaningfully different from the inherited solution set.
- Do not ignore execution constraints; reintroduce constraints after rebuilding options from fundamentals.
- Keep wording professional and plain enough that a smart non-specialist can use it without translation.
