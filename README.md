# Consulting Skills

58 executable consulting methods for better business decisions, diagnosis, strategy, and action.

[![Validate](https://github.com/fzfclee/consulting-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/fzfclee/consulting-skills/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-58-0f766e.svg)](catalog.yaml)

[中文说明](README.zh-CN.md)

## Why This Repository

Most framework collections explain what a method is. These skills are written to help an AI agent execute the method:

- identify the required inputs;
- state when the method should not be used;
- work through explicit steps;
- produce a reusable decision artifact;
- mark missing evidence and assumptions;
- pass a method-specific quality gate.

Each method is portable and can be installed or used independently. This repository does not contain a private orchestration engine or force a framework onto every problem.

## Start In One Minute

Install a single skill with GitHub CLI:

```bash
gh skill install fzfclee/consulting-skills systems-thinking --agent codex --scope user
```

Install through the open skills ecosystem:

```bash
npx skills add fzfclee/consulting-skills
```

Then ask your agent:

```text
Use systems-thinking to diagnose why this problem keeps returning despite repeated fixes.
Separate evidence from assumptions and identify feedback loops, delays, leverage points,
side effects, and validation signals.
```

## Choose By Situation

| Situation | Start with |
|---|---|
| The facts are incomplete or mixed with opinions | [`evidence-map`](skills/evidence-map/SKILL.md) |
| A broad problem needs a clean structure | [`issue-tree`](skills/issue-tree/SKILL.md) |
| A problem keeps returning | [`systems-thinking`](skills/systems-thinking/SKILL.md) |
| Several plausible causes need to be separated | [`abductive-reasoning`](skills/abductive-reasoning/SKILL.md) |
| Options need a defensible comparison | [`decision-matrix`](skills/decision-matrix/SKILL.md) |
| Stakeholders hold hidden veto power | [`stakeholder-power-map`](skills/stakeholder-power-map/SKILL.md) |
| A product has weak adoption | [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) |
| A plan needs a failure rehearsal | [`pre-mortem`](skills/pre-mortem/SKILL.md) |

The complete neutral catalog is in [`catalog.yaml`](catalog.yaml). Six fixed examples are in [`examples/`](examples/README.md).

## What Makes A Skill Executable

Every skill contains:

1. `Required Inputs`
2. `When Not To Use`
3. `Step-by-Step Execution`
4. `Output Template`
5. `Quality Gate`

If evidence is missing, the skill must label it as missing, state any temporary assumption, and propose a validation action. A method is useful only when it materially improves the decision, action, risk judgment, or validation plan.

## Repository Structure

```text
skills/<skill-name>/SKILL.md   # 58 standalone method skills
catalog.yaml                   # neutral discovery metadata
examples/                      # six fixed, public use cases
evaluations/                   # behavior-test cases and rubric
scripts/                       # catalog generation and validation
```

## Quality And Evaluation

The repository validator checks:

- exactly 58 unique skill directories;
- valid frontmatter and matching names;
- required execution sections;
- catalog-to-directory consistency;
- forbidden private routing and local-path markers;
- example and evaluation coverage;
- UTF-8 text and portable relative links.

The public evaluation set intentionally contains prompts and a scoring rubric, not hidden expected answers. See [`evaluations/README.md`](evaluations/README.md).

## Intellectual Property

This project does not claim ownership of established consulting tools or analytical methods. Names such as SWOT, RACI, the Kano Model, and Porter's Five Forces refer to methods developed or popularized by their respective creators.

The Apache-2.0 license applies to this repository's original skill text, executable structure, templates, catalog, examples, and code. See [`NOTICE`](NOTICE) and [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md) for the boundary and source notes.

## Contributing

Contributions should improve method fidelity, trigger clarity, evidence discipline, output usability, or decision impact. Do not add a method only to increase the count. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Disclaimer

These skills support structured analysis. They do not replace legal, financial, medical, regulatory, or other licensed professional advice. Users remain responsible for decisions and outcomes.
