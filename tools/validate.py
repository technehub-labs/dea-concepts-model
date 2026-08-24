#!/usr/bin/env python3
"""CR-CM-001 §20 — lightweight semantic validation for the Concepts Model.

Semantic discipline first, automation second. This validator enforces:

Repository contract
  * required layout present (governance/terminology-registry.yaml → repository block)
  * forbidden path `domains/` absent (Concept Area, never Domain)

Concept artifacts (concepts/**/*.yaml)
  * schema-conformant (schemas/concept.schema.yaml): required definition,
    valid lifecycle status, valid provenance, id pattern CM-<AREA>-<NNN>
  * unique concept IDs across the repository
  * valid Concept Areas (against the terminology registry)
  * file lives under its primary Concept Area directory
  * valid relationship verbs (governance/relationship-vocabulary.yaml)
  * relationship targets resolve to existing concept IDs
  * valid ECF Domain / Stage references (mappings/ecf/ecf-coordinates.yaml)
  * profile references resolve to profiles/ artifacts
  * no generic `domain` key outside ecfContexts (Domain protection,
    CR-CM-001 §11 / GOVERNANCE.md Rule 4)

Relationship instance sets (relationships/**/*.yaml)
  * unique relationship IDs
  * controlled verbs only; targets resolve

Consistency
  * concept-areas/concept-areas.yaml ≡ terminology registry initial_concept_areas
  * relationship vocabulary verbs unique across categories
  * .puml sources well-formed (@startuml … @enduml)

Usage: python tools/validate.py   (exit 0 = PASS, exit 1 = FAIL)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

REGISTRY_PATH = REPO_ROOT / "governance/terminology-registry.yaml"
VOCAB_PATH = REPO_ROOT / "governance/relationship-vocabulary.yaml"
AREAS_PATH = REPO_ROOT / "concept-areas/concept-areas.yaml"
SCHEMA_PATH = REPO_ROOT / "schemas/concept.schema.yaml"
ECF_COORDS_PATH = REPO_ROOT / "mappings/ecf/ecf-coordinates.yaml"

CONCEPT_ID_RE = re.compile(r"^CM-[A-Z]{2,6}-[0-9]{3}$")

errors: list[str] = []
checks: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def ok(msg: str) -> None:
    checks.append(msg)


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


# --------------------------------------------------------------------------
# Repository contract (terminology registry → repository block)
# --------------------------------------------------------------------------
def check_repository_contract(registry: dict) -> None:
    repo = registry.get("repository") or {}
    for rel in repo.get("required_layout") or []:
        if not (REPO_ROOT / rel).exists():
            fail(f"required layout entry missing: {rel}")
    ok(f"required layout present ({len(repo.get('required_layout') or [])} entries)")
    for rel in repo.get("forbidden_paths") or []:
        if (REPO_ROOT / rel).exists():
            fail(f"forbidden path exists: {rel} (Concept Area, never Domain)")
    ok("no forbidden paths (domains/ absent)")


# --------------------------------------------------------------------------
# Vocabulary / areas consistency
# --------------------------------------------------------------------------
def check_vocabularies(registry: dict) -> dict:
    vocab = load_yaml(VOCAB_PATH)
    verbs: list[str] = []
    for cat in (vocab.get("categories") or {}).values():
        for verb in cat.get("verbs") or []:
            if verb["id"] in verbs:
                fail(f"duplicate verb in relationship vocabulary: {verb['id']}")
            verbs.append(verb["id"])
    ok(f"relationship vocabulary: {len(verbs)} unique controlled verbs")

    registry_areas = registry.get("initial_concept_areas") or []
    areas_doc = load_yaml(AREAS_PATH)
    file_areas = [a["name"] for a in areas_doc.get("conceptAreas") or []]
    if file_areas != registry_areas:
        fail(
            "concept-areas/concept-areas.yaml does not match registry "
            f"initial_concept_areas: {file_areas} != {registry_areas}"
        )
    else:
        ok(f"concept areas ≡ registry ({len(registry_areas)} areas)")

    area_dirs = sorted(
        p.name for p in (REPO_ROOT / "concepts").iterdir() if p.is_dir()
    )
    expected_dirs = sorted(a.lower() for a in registry_areas)
    if area_dirs != expected_dirs:
        fail(
            f"concepts/ directories {area_dirs} do not match the nine "
            f"Concept Areas {expected_dirs}"
        )
    else:
        ok("concepts/ layout matches the nine Concept Areas")
    return {"verbs": verbs, "areas": registry_areas}


# --------------------------------------------------------------------------
# Generic Domain misuse (CR-CM-001 §11 normative rule)
# --------------------------------------------------------------------------
def check_domain_protection(doc, path: Path, context: str = "") -> None:
    """A property named `domain` is legal only inside ecfContexts (ECF
    namespace). Anywhere else it must be `conceptArea`."""
    if isinstance(doc, dict):
        for key, value in doc.items():
            if key == "domain" and not context.endswith("ecfContexts"):
                fail(
                    f"{path}: generic `domain` property outside ecfContexts "
                    f"(at {context or 'top level'}) — use `conceptArea` or an "
                    "explicit ECF namespace (Rule 4)"
                )
            next_context = f"{context}.{key}" if context else str(key)
            check_domain_protection(value, path, next_context)
    elif isinstance(doc, list):
        for item in doc:
            check_domain_protection(item, path, context)


# --------------------------------------------------------------------------
# Concept artifacts
# --------------------------------------------------------------------------
def check_concepts(vocab: dict) -> None:
    concepts_dir = REPO_ROOT / "concepts"
    concept_files = sorted(concepts_dir.glob("**/*.yaml"))
    if not concept_files:
        ok("no concept artifacts yet (foundation — CR-CM-001 §3); "
           "concept checks will activate with the first content CR")
        return

    try:
        from jsonschema import Draft202012Validator
        schema = load_yaml(SCHEMA_PATH)
        validator = Draft202012Validator(schema)
    except ImportError:
        validator = None
        ok("jsonschema not installed — schema validation skipped "
           "(CI installs it)")

    coords = load_yaml(ECF_COORDS_PATH)["ecf_coordinates"]
    ecf_domains = set(coords["domains"])
    ecf_stages = set(coords["stages"])

    profile_ids = {
        p.stem for p in (REPO_ROOT / "profiles").glob("*.yaml")
    }

    seen_ids: dict[str, Path] = {}
    for path in concept_files:
        doc = load_yaml(path)
        if not isinstance(doc, dict):
            fail(f"{path}: not a mapping")
            continue

        if validator is not None:
            for err in validator.iter_errors(doc):
                fail(f"{path}: schema violation: {err.message}")

        cid = doc.get("id", "<missing>")
        if cid in seen_ids:
            fail(f"{path}: duplicate concept id {cid} (also in {seen_ids[cid]})")
        seen_ids[cid] = path
        if isinstance(cid, str) and not CONCEPT_ID_RE.match(cid):
            fail(f"{path}: id {cid!r} does not match CM-<AREA>-<NNN>")

        for area in doc.get("conceptAreas") or []:
            if area not in vocab["areas"]:
                fail(f"{path}: unknown Concept Area {area!r}")
        # File lives under its primary Concept Area directory.
        primary = (doc.get("conceptAreas") or [None])[0]
        if primary and path.parent.name != primary.lower():
            fail(
                f"{path}: lives under concepts/{path.parent.name}/ but "
                f"primary Concept Area is {primary!r}"
            )

        check_domain_protection(doc, path)

        for rel in doc.get("relationships") or []:
            if rel.get("verb") not in vocab["verbs"]:
                fail(f"{path}: uncontrolled verb {rel.get('verb')!r} "
                     "(Rule 3 — governance approval required)")

        for ctx in doc.get("ecfContexts") or []:
            if ctx.get("domain") not in ecf_domains:
                fail(f"{path}: ecfContexts domain {ctx.get('domain')!r} "
                     "not an ECF Domain (mappings/ecf/ecf-coordinates.yaml)")
            if ctx.get("stage") not in ecf_stages:
                fail(f"{path}: ecfContexts stage {ctx.get('stage')!r} "
                     "not an ECF Stage")

        for profile in doc.get("profiles") or []:
            slug = re.sub(r"[^a-z0-9]+", "-", str(profile).lower()).strip("-")
            if slug not in profile_ids:
                fail(f"{path}: profile reference {profile!r} does not "
                     "resolve to a profiles/ artifact")

    # Unresolved relationship targets (needs the full ID set first).
    for path in concept_files:
        doc = load_yaml(path)
        for rel in (doc or {}).get("relationships") or []:
            target = rel.get("target")
            if isinstance(target, str) and target.startswith("CM-") \
                    and target not in seen_ids:
                fail(f"{path}: unresolved relationship target {target!r}")
    ok(f"concept artifacts validated ({len(concept_files)} files)")


# --------------------------------------------------------------------------
# Relationship instance sets
# --------------------------------------------------------------------------
def check_relationship_instances(vocab: dict, concept_ids: set[str]) -> None:
    rel_files = sorted((REPO_ROOT / "relationships").glob("**/*.yaml"))
    if not rel_files:
        ok("no relationship instance sets yet (foundation)")
        return
    seen: set[str] = set()
    for path in rel_files:
        doc = load_yaml(path) or {}
        for rel in doc.get("relationships") or []:
            rid = rel.get("id")
            if rid in seen:
                fail(f"{path}: duplicate relationship id {rid!r}")
            seen.add(rid)
            if rel.get("verb") not in vocab["verbs"]:
                fail(f"{path}: uncontrolled verb {rel.get('verb')!r}")
            for end in ("source", "target"):
                ref = rel.get(end)
                if isinstance(ref, str) and ref.startswith("CM-") \
                        and concept_ids and ref not in concept_ids:
                    fail(f"{path}: unresolved {end} {ref!r}")
    ok(f"relationship instance sets validated ({len(rel_files)} files)")


# --------------------------------------------------------------------------
# PlantUML sanity
# --------------------------------------------------------------------------
def check_puml() -> None:
    pumls = sorted(REPO_ROOT.glob("models/**/*.puml"))
    for path in pumls:
        text = path.read_text(encoding="utf-8")
        if "@startuml" not in text or "@enduml" not in text:
            fail(f"{path}: not a well-formed PlantUML source")
    ok(f"PlantUML sources well-formed ({len(pumls)} files)")


def main() -> int:
    registry = load_yaml(REGISTRY_PATH)
    check_repository_contract(registry)
    vocab = check_vocabularies(registry)
    check_concepts(vocab)
    concept_ids = set()
    for path in sorted((REPO_ROOT / "concepts").glob("**/*.yaml")):
        doc = load_yaml(path) or {}
        if isinstance(doc.get("id"), str):
            concept_ids.add(doc["id"])
    check_relationship_instances(vocab, concept_ids)
    check_puml()

    print("OpenDEA Concepts Model — validation")
    print("=" * 60)
    for msg in checks:
        print(f"  OK   {msg}")
    if errors:
        print()
        for msg in errors:
            print(f"  FAIL {msg}")
        print(f"\n{len(errors)} error(s)")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
