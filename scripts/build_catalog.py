#!/usr/bin/env python3
"""Build the neutral public catalog from standalone SKILL.md files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_PATH = ROOT / "catalog.yaml"
VERSION = "0.2.1"

CATEGORIES = {
    "problem-framing-and-evidence": {
        "5w1h-analysis",
        "affinity-diagram",
        "assumption-inventory",
        "evidence-map",
        "issue-tree",
        "mece-framework",
        "mind-map-analysis",
        "signal-vs-noise-filter",
    },
    "reasoning-and-root-cause": {
        "abductive-reasoning",
        "constraint-analysis",
        "deductive-reasoning",
        "first-principles-thinking",
        "fishbone-diagram",
        "five-whys-root-cause",
        "hypothesis-tree",
        "inductive-reasoning",
    },
    "systems-risk-and-futures": {
        "critical-uncertainties",
        "pre-mortem",
        "risk-matrix",
        "scenario-planning",
        "systems-thinking",
    },
    "strategy-market-and-commercial": {
        "account-plan",
        "business-model-canvas",
        "competitive-positioning",
        "deal-strategy-map",
        "go-to-market-diagnosis",
        "pestel-analysis",
        "porter-five-forces",
        "pricing-strategy-check",
        "swot-analysis",
        "win-loss-review",
    },
    "customer-product-and-experience": {
        "customer-segmentation",
        "customer-success-health-score",
        "empathy-map",
        "jobs-to-be-done",
        "kano-model",
        "service-blueprint",
        "user-journey-mapping",
    },
    "prioritization-and-economics": {
        "break-even-analysis",
        "cost-benefit-analysis",
        "decision-matrix",
        "effort-impact-matrix",
        "rice-scoring",
        "weighted-scorecard",
        "wsjf-prioritization",
    },
    "measurement-and-performance": {
        "balanced-scorecard",
        "metrics-tree",
        "north-star-metric",
    },
    "stakeholder-change-and-governance": {
        "change-event-timeline",
        "change-impact-analysis",
        "communications-plan",
        "force-field-analysis",
        "power-interest-grid",
        "raci-matrix",
        "stakeholder-power-map",
    },
    "execution-and-validation": {
        "fifteen-percent-solutions",
        "min-specs",
        "validation-plan",
    },
}


def parse_skill(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter_match:
        raise ValueError(f"Missing frontmatter: {path}")
    frontmatter = yaml.safe_load(frontmatter_match.group(1))
    body = text[frontmatter_match.end() :]
    sections = split_sections(body)
    name = frontmatter["name"]
    required_inputs = extract_bullets(sections.get("Required Inputs", ""))
    when_not = compact_text(sections.get("When Not To Use", ""))
    outputs = extract_step_outputs(sections.get("Step-by-Step Execution", ""))
    known_names = {item.name for item in SKILLS_DIR.iterdir() if item.is_dir()}
    adjacent = sorted(
        {
            candidate
            for candidate in re.findall(r"`([a-z0-9-]+)`", when_not)
            if candidate in known_names and candidate != name
        }
    )
    return {
        "name": name,
        "title": extract_title(body),
        "category": category_for(name),
        "use_when": frontmatter["description"],
        "do_not_use_when": when_not,
        "required_inputs": required_inputs,
        "primary_outputs": outputs,
        "adjacent_methods": adjacent,
        "version": VERSION,
        "source": f"skills/{name}/SKILL.md",
    }


def split_sections(body: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (.+)$", body, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections[match.group(1).strip()] = body[start:end].strip()
    return sections


def extract_title(body: str) -> str:
    match = re.search(r"^# (.+)$", body, re.MULTILINE)
    if not match:
        raise ValueError("Missing H1 title")
    return match.group(1).strip()


def extract_bullets(section: str) -> list[str]:
    return [
        match.group(1).strip()
        for match in re.finditer(r"^- (.+)$", section, re.MULTILINE)
        if not match.group(1).startswith("If ")
    ]


def compact_text(section: str) -> str:
    paragraphs = [
        line.strip()
        for line in section.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    return " ".join(paragraphs)


def extract_step_outputs(section: str) -> list[str]:
    outputs: list[str] = []
    for line in section.splitlines():
        if not line.startswith("|") or re.match(r"^\|[-| ]+\|$", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4 or cells[0] == "Step":
            continue
        output = cells[3].rstrip(".")
        if output and output not in outputs:
            outputs.append(output)
    return outputs


def category_for(name: str) -> str:
    matches = [category for category, names in CATEGORIES.items() if name in names]
    if len(matches) != 1:
        raise ValueError(f"Skill must have exactly one category: {name}, got {matches}")
    return matches[0]


def build_catalog() -> dict:
    skills = [
        parse_skill(path)
        for path in sorted(SKILLS_DIR.glob("*/SKILL.md"), key=lambda item: item.parent.name)
    ]
    return {
        "catalog_version": 1,
        "library_version": VERSION,
        "name": "consulting-skills",
        "description": (
            "Neutral discovery metadata for standalone consulting method skills. "
            "This catalog contains no private orchestration or CLEAR/S2A routing fields."
        ),
        "method_count": len(skills),
        "categories": [
            {"name": category, "method_count": len(names)}
            for category, names in CATEGORIES.items()
        ],
        "methods": skills,
    }


def render_catalog(catalog: dict) -> str:
    return yaml.safe_dump(
        catalog,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when catalog.yaml does not match the generated catalog.",
    )
    args = parser.parse_args()
    rendered = render_catalog(build_catalog())
    if args.check:
        current = CATALOG_PATH.read_text(encoding="utf-8") if CATALOG_PATH.exists() else ""
        if current != rendered:
            print("catalog.yaml is out of date. Run: python scripts/build_catalog.py")
            return 1
        print("catalog.yaml is current")
        return 0
    CATALOG_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Wrote {CATALOG_PATH} with 58 methods")
    return 0


if __name__ == "__main__":
    sys.exit(main())
