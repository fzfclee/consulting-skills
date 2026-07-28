#!/usr/bin/env python3
"""Validate public skill structure, catalog consistency, and leakage boundaries."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_SECTIONS = {
    "## Required Inputs",
    "## When Not To Use",
    "## Step-by-Step Execution",
    "## Output Template",
    "## Quality Gate",
}
FORBIDDEN_PATTERNS = {
    "private product name": re.compile(r"\bs2a-magic\b", re.IGNORECASE),
    "private routing phrase": re.compile(r"\bS2A Handoff\b", re.IGNORECASE),
    "private router": re.compile(r"\bCLEAR (?:Lens )?Router\b", re.IGNORECASE),
    "private workpapers flag": re.compile(r"--workpap(?:ers|ars)\b", re.IGNORECASE),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\"),
    "private KB path": re.compile(r"zhi-consulting-knowledge-base", re.IGNORECASE),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_skill(path: Path, all_names: set[str], errors: list[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(errors, f"{path}: not valid UTF-8 ({exc})")
        return
    if text.startswith("\ufeff"):
        fail(errors, f"{path}: contains UTF-8 BOM")
    name = path.parent.name
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(errors, f"{path}: invalid directory name")
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter_match:
        fail(errors, f"{path}: missing YAML frontmatter")
        return
    try:
        frontmatter = yaml.safe_load(frontmatter_match.group(1))
    except yaml.YAMLError as exc:
        fail(errors, f"{path}: invalid YAML ({exc})")
        return
    if set(frontmatter) != {"name", "description", "license"}:
        fail(errors, f"{path}: frontmatter must contain name, description, and license")
    if frontmatter.get("name") != name:
        fail(errors, f"{path}: frontmatter name does not match directory")
    if frontmatter.get("license") != "Apache-2.0":
        fail(errors, f"{path}: license must be Apache-2.0")
    description = frontmatter.get("description", "")
    if len(description.strip()) < 40:
        fail(errors, f"{path}: description is too short to support triggering")
    missing_sections = sorted(section for section in REQUIRED_SECTIONS if section not in text)
    if missing_sections:
        fail(errors, f"{path}: missing sections {missing_sections}")
    if len(text.splitlines()) > 500:
        fail(errors, f"{path}: exceeds 500-line progressive-disclosure limit")
    for label, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            fail(errors, f"{path}: contains forbidden {label}")
    references = set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", text))
    unknown = sorted(
        reference
        for reference in references
        if "-" in reference and reference not in all_names
    )
    if unknown:
        fail(errors, f"{path}: references unknown adjacent methods {unknown}")


def validate_catalog(all_names: set[str], errors: list[str]) -> None:
    path = ROOT / "catalog.yaml"
    try:
        catalog = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        fail(errors, f"catalog.yaml cannot be loaded: {exc}")
        return
    methods = catalog.get("methods", [])
    catalog_names = [method.get("name") for method in methods]
    if catalog.get("method_count") != 58:
        fail(errors, "catalog.yaml method_count must be 58")
    if len(catalog_names) != len(set(catalog_names)):
        fail(errors, "catalog.yaml contains duplicate method names")
    if set(catalog_names) != all_names:
        fail(errors, "catalog.yaml names do not match skill directories")
    forbidden_keys = {
        "orchestrator",
        "stage",
        "route",
        "clear_stage",
        "primary_method",
        "supporting_methods",
        "dispatch_policy",
    }
    for index, method in enumerate(methods):
        overlap = forbidden_keys.intersection(method)
        if overlap:
            fail(errors, f"catalog method #{index + 1} contains private routing keys {sorted(overlap)}")
        source = method.get("source")
        if source != f"skills/{method.get('name')}/SKILL.md":
            fail(errors, f"catalog source mismatch for {method.get('name')}")


def validate_supporting_assets(errors: list[str]) -> None:
    required = [
        "README.md",
        "README.zh-CN.md",
        "LICENSE",
        "NOTICE",
        "ATTRIBUTIONS.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "examples/README.md",
        "evaluations/README.md",
        "evaluations/representative-cases.yaml",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(errors, f"Missing required repository asset: {relative}")
    examples = list((ROOT / "examples").glob("[0-9][0-9]-*.md"))
    if len(examples) != 7:
        fail(errors, f"Expected 7 numbered examples, found {len(examples)}")
    cases_path = ROOT / "evaluations" / "representative-cases.yaml"
    if cases_path.exists():
        cases = yaml.safe_load(cases_path.read_text(encoding="utf-8"))
        if len(cases.get("cases", [])) != 24:
            fail(errors, "representative-cases.yaml must contain 24 cases")


def main() -> int:
    errors: list[str] = []
    skill_paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    names = {path.parent.name for path in skill_paths}
    if len(skill_paths) != 58 or len(names) != 58:
        fail(errors, f"Expected 58 unique skills, found {len(skill_paths)} files and {len(names)} names")
    for path in skill_paths:
        validate_skill(path, names, errors)
    validate_catalog(names, errors)
    validate_supporting_assets(errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed: 58 skills, neutral catalog, public boundary intact")
    return 0


if __name__ == "__main__":
    sys.exit(main())
