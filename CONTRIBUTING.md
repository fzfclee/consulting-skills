# Contributing

Contributions are welcome when they make a method more accurate, executable, evidence-aware, or decision-useful.

## Before Opening A Pull Request

1. Explain the user situation the change improves.
2. Cite a primary or authoritative source for a material method change.
3. Preserve the method's independent, portable design.
4. Do not add private orchestration rules, customer information, or local paths.
5. Run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/build_catalog.py --check
python scripts/validate_repository.py
```

## Skill Contract

Every `skills/<name>/SKILL.md` must:

- use lowercase hyphenated names;
- contain `name`, `description`, and `license: Apache-2.0` in YAML frontmatter;
- explain required inputs;
- state when not to use the method;
- provide explicit execution steps;
- include a reusable output template;
- define a method-specific quality gate;
- label missing evidence and assumptions;
- remain independent from any private orchestration product.

## Method Inclusion Gate

A new method should be added only when it:

- solves a recurring decision or diagnostic need;
- is materially different from existing methods;
- has an authoritative basis;
- produces a reusable output;
- changes the quality of a decision, action, risk judgment, or validation plan.

Method-count growth is not a goal by itself.
