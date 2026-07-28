#!/usr/bin/env python3
"""Validate public skill structure, catalog consistency, and leakage boundaries."""

from __future__ import annotations

import re
import sys
from urllib.parse import unquote
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
EXAMPLE_REQUIRED_PATTERNS = {
    "example note": re.compile(r"\*\*Example note:\*\*"),
    "shared input": re.compile(r"^## Shared Input$", re.MULTILINE),
    "direct answer run": re.compile(
        r"^## Run A: Direct (?:AI )?Answer, No Method Skill$", re.MULTILINE
    ),
    "method-skill run": re.compile(
        r"^## Run B: .+Skill Reasoning Chain$", re.MULTILINE
    ),
    "method selection": re.compile(r"^### Method Selection$", re.MULTILINE),
    "decision artifact": re.compile(r"^## Decision Artifact$", re.MULTILINE),
    "comparison": re.compile(r"^## Comparison$", re.MULTILINE),
    "comparison conclusion": re.compile(
        r"^## What The Comparison Shows$", re.MULTILINE
    ),
}
EXAMPLE_DISALLOWED_LANGUAGE = re.compile(
    r"\b(?:fictional|invented)\b|虚构|杜撰",
    re.IGNORECASE,
)
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


def validate_boundary_uniqueness(skill_paths: list[Path], errors: list[str]) -> None:
    boundaries: dict[str, list[str]] = {}
    for path in skill_paths:
        text = path.read_text(encoding="utf-8")
        match = re.search(
            r"^## When Not To Use\s*\n+(.*?)(?=^## )",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            continue
        normalized = " ".join(match.group(1).split())
        boundaries.setdefault(normalized, []).append(path.parent.name)
    duplicates = [names for names in boundaries.values() if len(names) > 1]
    for names in duplicates:
        fail(
            errors,
            "When Not To Use text is duplicated across methods: "
            + ", ".join(sorted(names)),
        )


def validate_text_files(errors: list[str]) -> None:
    text_suffixes = {".md", ".py", ".txt", ".yaml", ".yml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in text_suffixes:
            continue
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            fail(errors, f"{path}: contains UTF-8 BOM")
        if b"\r\n" in data:
            fail(errors, f"{path}: contains CRLF despite repository LF policy")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(errors, f"{path}: not valid UTF-8 ({exc})")


def validate_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in link_pattern.finditer(text):
            raw_target = match.group(1).strip()
            target = raw_target.split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative and not (path.parent / relative).exists():
                fail(errors, f"{path}: broken relative link {raw_target}")


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


def validate_example(path: Path, all_names: set[str], errors: list[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(errors, f"{path}: not valid UTF-8 ({exc})")
        return
    if text.startswith("\ufeff"):
        fail(errors, f"{path}: contains UTF-8 BOM")
    if EXAMPLE_DISALLOWED_LANGUAGE.search(text):
        fail(errors, f"{path}: contains discouraged example-label language")
    for label, pattern in EXAMPLE_REQUIRED_PATTERNS.items():
        if not pattern.search(text):
            fail(errors, f"{path}: missing controlled-comparison {label}")
    method_links = set(
        re.findall(r"\(\.\./skills/([a-z0-9]+(?:-[a-z0-9]+)*)/SKILL\.md\)", text)
    )
    if len(method_links) < 2:
        fail(errors, f"{path}: must link at least two selected method skills")
    unknown = sorted(method_links - all_names)
    if unknown:
        fail(errors, f"{path}: links unknown method skills {unknown}")
    if len(text.splitlines()) > 500:
        fail(errors, f"{path}: exceeds 500-line example limit")


def validate_supporting_assets(all_names: set[str], errors: list[str]) -> None:
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
        "evaluations/method-selection-cases.yaml",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(errors, f"Missing required repository asset: {relative}")
    examples = list((ROOT / "examples").glob("[0-9][0-9]-*.md"))
    if len(examples) != 7:
        fail(errors, f"Expected 7 numbered examples, found {len(examples)}")
    for path in examples:
        validate_example(path, all_names, errors)
    language_check_paths = list((ROOT / "examples").glob("*.md")) + [
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
    ]
    for path in language_check_paths:
        text = path.read_text(encoding="utf-8")
        if EXAMPLE_DISALLOWED_LANGUAGE.search(text):
            fail(errors, f"{path}: contains discouraged example-label language")
    cases_path = ROOT / "evaluations" / "representative-cases.yaml"
    if cases_path.exists():
        cases = yaml.safe_load(cases_path.read_text(encoding="utf-8"))
        case_list = cases.get("cases", [])
        if len(case_list) != 70:
            fail(errors, "representative-cases.yaml must contain 70 cases")
        case_ids = [case.get("id") for case in case_list]
        if len(case_ids) != len(set(case_ids)):
            fail(errors, "representative-cases.yaml contains duplicate case ids")
        tested_skills = {case.get("skill") for case in case_list}
        unknown_skills = sorted(tested_skills - all_names)
        if unknown_skills:
            fail(
                errors,
                "representative-cases.yaml references unknown skills "
                + ", ".join(unknown_skills),
            )
        missing_skills = sorted(all_names - tested_skills)
        if missing_skills:
            fail(
                errors,
                "representative-cases.yaml does not cover skills "
                + ", ".join(missing_skills),
            )
    selection_path = ROOT / "evaluations" / "method-selection-cases.yaml"
    if selection_path.exists():
        selection = yaml.safe_load(selection_path.read_text(encoding="utf-8"))
        selection_cases = selection.get("cases", [])
        if len(selection_cases) != 24:
            fail(errors, "method-selection-cases.yaml must contain 24 cases")
        selection_ids = [case.get("id") for case in selection_cases]
        if len(selection_ids) != len(set(selection_ids)):
            fail(errors, "method-selection-cases.yaml contains duplicate case ids")
        for case in selection_cases:
            expected = case.get("expected_primary")
            rejected = set(case.get("reject_as_primary", []))
            if expected not in all_names:
                fail(
                    errors,
                    f"method-selection case {case.get('id')} expects unknown skill {expected}",
                )
            unknown_rejected = sorted(rejected - all_names)
            if unknown_rejected:
                fail(
                    errors,
                    f"method-selection case {case.get('id')} rejects unknown skills "
                    + ", ".join(unknown_rejected),
                )
            if expected in rejected:
                fail(
                    errors,
                    f"method-selection case {case.get('id')} rejects its expected method",
                )
            for field in ("situation", "reason"):
                if len(str(case.get(field, "")).strip()) < 40:
                    fail(
                        errors,
                        f"method-selection case {case.get('id')} has weak {field}",
                    )


def main() -> int:
    errors: list[str] = []
    skill_paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    names = {path.parent.name for path in skill_paths}
    if len(skill_paths) != 58 or len(names) != 58:
        fail(errors, f"Expected 58 unique skills, found {len(skill_paths)} files and {len(names)} names")
    for path in skill_paths:
        validate_skill(path, names, errors)
    validate_boundary_uniqueness(skill_paths, errors)
    validate_text_files(errors)
    validate_markdown_links(errors)
    validate_catalog(names, errors)
    validate_supporting_assets(names, errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Repository validation passed: 58 skills, 7 controlled examples, "
        "70 evaluation prompts, 24 selection cases, portability checks passed"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
