# OpenDEA Concepts Model

The canonical conceptual layer for defining, organizing, relating, and
evolving OpenDEA concepts **before** they are promoted into the
foundational metamodel.

The Concepts Model answers one question:

> What does a concept mean, what concepts does it relate to, in what
> conceptual context does it operate, and when is it sufficiently mature
> to be formalized?

It provides a controlled path from an emerging idea to a formal
metamodel construct:

```text
Emerging Concept
      ↓
Concept Definition
      ↓
Concept Relationship
      ↓
Concept Profile
      ↓
Semantic Stabilization
      ↓
Metamodel Candidate
      ↓
Foundational Metamodel
```

## Architectural position

The Concepts Model sits **between** the DEA Metaframework and the DEA
Metamodel. It consumes the semantic foundation of the Metaframework and
provides candidates to the Metamodel. It does not become a competing
metamodel.

```text
                    OPENDEA SEMANTIC STACK
┌─────────────────────────────────────────────────────────────┐
│ Enterprise Thought / Standards / Research                   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 DEA METAFRAMEWORK                           │
│                                                             │
│ Enterprise Concept Framework                                │
│ Domain × Stage                                              │
│ Enterprise Axioms                                           │
└──────────────────────────────┬──────────────────────────────┘
                               │ contextualizes
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 DEA CONCEPTS MODEL  (this repository)       │
│                                                             │
│ Concepts · Concept Areas · Concept Profiles                 │
│ Relationships · ECF Contexts · External Mappings            │
└──────────────────────────────┬──────────────────────────────┘
                               │ semantic candidates
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 DEA METAMODEL                               │
│                                                             │
│ Entity / EntitySpec · Relationship · Attributes             │
│ Constraints · Schemas                                       │
└──────────────────────────────┬──────────────────────────────┘
                               │ instantiated by
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  DEA CATALOGS / MODELS                      │
└─────────────────────────────────────────────────────────────┘
```

## Background: why this layer exists

The Enterprise Concept Framework (ECF —
[`technehub-labs/dea-metaframework`](https://github.com/technehub-labs/dea-metaframework))
models the enterprise as a **7×7 foundation matrix M = D × S**: seven
Domains (what the enterprise does — Governance & Existence … Finance &
Value) crossed with seven Stages (how the work evolves — Conceive …
Retire). Every business object lives in one cell of that matrix.

Two vocabulary collisions made a dedicated conceptual layer necessary,
and CR-CM-000 settled them **before** this model shipped:

1. **Domain / Stage are reserved for the ECF.** The Concepts Model
   needed thematic groupings of its own, and the natural-but-wrong move
   would have been to reuse *Domain*. One word, two meanings — every
   catalog, profile, and tool would have to guess. The Concepts Model
   therefore speaks in **Concept Area** (thematic grouping), **Concept
   Profile** (reusable perspective over the concept graph), **Concept
   Classification**, and **ECF Context** (a concept's position in the
   ECF's Domain × Stage coordinate system). See
   [`governance/terminology-registry.yaml`](governance/terminology-registry.yaml).
2. **A concept is not an entity.** *Conceptual meaning precedes formal
   information structure* (CR-CM-001 §4). `Concept ≠ Entity` and
   `Concept Relationship ≠ Metamodel Relationship`. A concept may
   eventually `maps-to` a metamodel `EntitySpec`, but that is an
   explicit semantic decision — and `maps-to` never implies
   inheritance. "AI Agent uses AI Model" does not mean "AI Agent
   specializes AI Model"; "KCI contributes-to KEI" does not mean "KCI
   specializes KEI" (§13).

Two further distinctions govern everything in this repository:

- **Canonical does not mean metamodel entity.** A concept can be
  canonical within the Concepts Model without being part of the
  foundational metamodel (§9). Promotion requires an explicit mapping
  and a subsequent metamodel CR (Governance Rule 7).
- **Concepts are mapped, not copied, from external standards.** A
  concept derived from TM Forum is never represented as an original
  OpenDEA definition; provenance and the mapping distinctions
  (`equivalent-to` / `aligned-with` / `derived-from` / `related-to`)
  are preserved (§15, §16).

## Repository layout

```text
dea-concepts-model/
│
├── README.md                     ← this file
├── LICENSE                       ← Apache-2.0
├── CONTRIBUTING.md               ← how to propose concepts / changes
├── GOVERNANCE.md                 ← the eight normative rules (CR-CM-001 §19)
│
├── governance/
│   ├── terminology-registry.yaml ← canonical terminology registry (migrated
│   │                               from dea-metamodel interim home, CR-CM-000A §14)
│   ├── concept-lifecycle.md      ← PROPOSED → … → FORMALIZED + retirement
│   └── relationship-vocabulary.yaml ← controlled verbs (§12) + external mapping relations (§16)
│
├── concepts/                     ← one directory per Concept Area; a concept
│   ├── enterprise/                   file lives under its primary area and may
│   ├── operations/                   list several areas (§10)
│   ├── intelligence/
│   ├── execution/
│   ├── control/
│   ├── scenario/
│   ├── value/
│   ├── measurement/
│   └── systems/
│
├── concept-areas/                ← the nine Concept Areas (concept-areas.yaml)
├── profiles/                     ← Concept Profiles (perspectives; none yet)
├── relationships/                ← declared relationship instances (none yet)
│
├── models/
│   ├── terminology-alignment.puml   ← the ECF ↔ Concepts Model boundary
│   ├── master/
│   │   └── concepts-model.puml   ← the semantic architecture (CR-CM-001 §18)
│   ├── concept-areas/            ← per-area models (subsequent CRs)
│   └── profiles/                 ← per-profile models (subsequent CRs)
│
├── mappings/
│   ├── ecf/                      ← ECF coordinate reference (Domain × Stage)
│   ├── dea-metamodel/            ← maps-to / candidate-for promotion records
│   └── external/                 ← external standards alignments
│
├── change-requests/              ← the CR programme for this repository
│
├── schemas/
│   └── concept.schema.yaml       ← machine-readable concept contract (§7)
│
└── tools/
    └── validate.py               ← lightweight semantic validation (§20)
```

> PlantUML sources (`.puml`) are the committed artifacts. Render locally
> with `plantuml -tsvg models/master/concepts-model.puml` (or the
> Docker image); the public PlantUML server is not relied upon in CI.

## Validation

Semantic discipline first, automation second (§20). The validator checks
— as artifacts appear — unique concept/relationship IDs, required
definitions, valid lifecycle states, valid Concept Areas, controlled
relationship verbs, valid ECF Domain/Stage references, valid profile
references, provenance, the reserved-term rules, and unresolved
relationship targets:

```bash
pip install pyyaml
python tools/validate.py
```

It also enforces the repository contract itself: the mandated layout
exists and the forbidden path `domains/` never appears.

## What is deliberately not here yet

No substantive business concepts are declared canonical in this
foundation (§3, §21): Agentic Enterprise, Autonomous Operations, HVS,
VOF, KCI / KEI / KBI, R.I.S.E., AI Agent, Agentic AI, Closed Loop, and
their siblings arrive as content under subsequent CRs — CR-CM-002
(Agentic & Autonomous Concept Model), then the
HVS → Initiative → KCI → KEI → KBI → VOF/R.I.S.E. model as
CR-CM-003/004. This repository ships the *machinery of meaning* first.

## Provenance

Established by [CR-CM-001](change-requests/CR-CM-001.md), implementing
the terminology decisions of CR-CM-000 and CR-CM-000A (landed in
[`technehub-labs/dea-metamodel`](https://github.com/technehub-labs/dea-metamodel)
`change-requests/`). License: Apache-2.0.
