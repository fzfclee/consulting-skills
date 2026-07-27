---
name: assumption-inventory
description: Use when a recommendation, plan, diagnosis, or stakeholder judgment depends on unstated assumptions that must be named and tested. Use when applying assumption inventory, assumption mapping, leap-of-faith assumption review, or critical assumption testing.
license: Apache-2.0
---

# Assumption Inventory

Use this skill to expose the assumptions underneath a diagnosis or plan and decide which ones need testing first.

## Method Notes

- An assumption is something the plan relies on but has not yet proven.
- Not all assumptions require immediate testing. Prioritize assumptions by impact if wrong and uncertainty.
- This skill is useful before investing effort, making stakeholder moves, or committing to a strategy.

## Required Inputs

Collect or infer these inputs before execution:

- current diagnosis, plan, or recommendation
- intended outcome
- key stakeholders or users
- known facts and constraints
- major risks if the plan is wrong

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the issue is primarily role ownership, numerical prioritization, or root cause analysis. Use `raci-matrix`, `wsjf-prioritization`, or `five-whys-root-cause` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the plan or diagnosis | Current recommendation, target outcome. | Write the conclusion in one plain sentence. | Plan / diagnosis statement. |
| Extract assumptions | Plan components, stakeholder beliefs, constraints, evidence gaps. | Ask what must be true for this plan to work. | Assumption list. |
| Classify assumptions | Assumption list. | Label each as market, customer, stakeholder, capability, resource, timing, risk, economics, or compliance. | Classified assumptions. |
| Rate criticality | Impact if wrong, uncertainty, reversibility. | Score impact and uncertainty as high / medium / low. Mark whether the assumption is reversible. | Critical assumption table. |
| Prioritize tests | Critical assumptions, available access, deadline. | Select the few assumptions that must be tested before action. | Test priority list. |
| Define evidence needed | Assumption, test method, success criteria. | State what evidence would confirm, weaken, or disprove the assumption. | Assumption test plan. |

## Output Template

```markdown
### 1. Current Plan / Diagnosis
- Working conclusion:
- Desired outcome:
- Main consequence if wrong:

### 2. Assumption Inventory
| Assumption | Type | Evidence now | Impact if wrong | Uncertainty | Reversible? | Test priority |
|---|---|---|---|---|---|---|
|  | stakeholder / market / customer / capability / resource / timing / economics / risk / compliance |  | high / medium / low | high / medium / low | yes / no / partly | high / medium / low |

### 3. Critical Assumptions To Test First
1. [Critical assumption]
2. [Critical assumption]
3. [Critical assumption]

### 4. Test Plan
| Critical assumption | Evidence needed | Fastest test | Confirm signal | Disconfirm signal |
|---|---|---|---|---|
|  |  |  |  |  |

### 5. Decision Implication
- Proceed now:
- Wait until tested:
- Adjust plan:
```

## Quality Gate

- Do not list generic assumptions that would not change the plan.
- Prioritize by impact and uncertainty, not by ease alone.
- Separate assumption testing from action execution.
- Name what decision can be made now and what should wait.
- Keep wording professional and practical.
