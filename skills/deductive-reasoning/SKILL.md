---
name: deductive-reasoning
description: Use when a conclusion must be tested against explicit rules, principles, criteria, policies, definitions, premises, or if-then logic. Use when applying deductive reasoning, rule-based reasoning, premise-to-conclusion testing, logical consistency checks, or validity review.
license: Apache-2.0
---

# Deductive Reasoning

Use this skill to test whether a conclusion follows from stated premises, rules, or criteria.

## Method Notes

- Deductive reasoning moves from general rules or premises to a specific conclusion.
- A deductive conclusion is only as reliable as the premises and the logic connecting them.
- This method is strongest when rules, definitions, criteria, or constraints are explicit.
- It should separate validity from truth: an argument can be logically valid but built on a false or weak premise.

## Required Inputs

Collect or infer these inputs before execution:

- conclusion or decision to test
- stated rules, criteria, principles, policies, or premises
- facts of the specific case
- scope boundary
- exceptions or override conditions

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when there are no clear premises or rules and the task is pattern discovery. Use `inductive-reasoning`, `abductive-reasoning`, or `affinity-diagram` first.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the conclusion | Decision, claim, or recommendation. | Write the conclusion in one testable sentence. | Conclusion to test. |
| List premises | Rules, criteria, policies, principles, definitions. | Separate general premises from case-specific facts. | Premise list. |
| Check premise quality | Source, evidence, authority, scope. | Mark each premise as strong, medium, weak, or missing. | Premise quality table. |
| Map logic chain | Premises, case facts, conclusion. | Build the if-then path from premises to conclusion. | Logic chain. |
| Test validity | Logic chain, exceptions. | Check whether the conclusion necessarily follows if premises are true. | Validity judgment. |
| Check exceptions | Scope, edge cases, override conditions. | Identify conditions that weaken or reverse the conclusion. | Exception list. |
| Rewrite conclusion | Validity and premise quality. | State a careful conclusion that matches the actual logic strength. | Revised conclusion. |

## Output Template

```markdown
### 1. Conclusion To Test
- Claim / decision:
- Scope:

### 2. Premise Table
| Premise | Type | Evidence / source | Strength | Scope limit |
|---|---|---|---|---|
|  | rule / criterion / principle / fact / assumption |  | strong / medium / weak / missing |  |

### 3. Logic Chain
1.
2.
3.

### 4. Validity Check
- Does the conclusion follow if the premises are true?
- Weakest premise:
- Exception or edge case:
- Revised conclusion:
```

## Quality Gate

- Do not treat an assumption as a rule.
- Do not hide weak premises inside confident logic.
- Separate logical validity from real-world truth.
- Identify exceptions and scope limits.
- Use plain wording so the conclusion can be challenged or reused.
