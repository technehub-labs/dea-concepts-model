CR-CM-001 — OpenDEA Concepts Model Foundation.

This CR should implement the terminology decisions from CR-CM-000 and establish the repository as a durable semantic layer between the dea-metaframework and dea-metamodel.

CR-CM-001 — OpenDEA Concepts Model Foundation

Status: Proposed
Type: Architecture / Repository / Semantic Governance
Priority: Critical
Depends on: CR-CM-000 — OpenDEA Concepts Terminology Alignment
Repository: technehub-labs/dea-concepts-model
Target: Initial v0.1.0 foundation

⸻

1. Objective

Establish the OpenDEA Concepts Model as the canonical conceptual layer for defining, organizing, relating and evolving OpenDEA concepts before they are promoted into the foundational metamodel.

The repository must provide a controlled mechanism for moving from:

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

The Concepts Model must not duplicate or redefine the Enterprise Concept Framework or Foundational Metamodel.

Its role is to answer:

What does a concept mean, what concepts does it relate to, in what conceptual context does it operate, and when is it sufficiently mature to be formalized?

⸻

2. Architectural Position

The repository shall establish this relationship:

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
│                 DEA CONCEPTS MODEL                          │
│                                                             │
│ Concepts                                                     │
│ Concept Areas                                                │
│ Concept Profiles                                             │
│ Relationships                                                │
│ ECF Contexts                                                 │
│ External Mappings                                            │
└──────────────────────────────┬──────────────────────────────┘
                               │ semantic candidates
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 DEA METAMODEL                               │
│                                                             │
│ Entity / EntitySpec                                          │
│ Relationship                                                 │
│ Attributes                                                  │
│ Constraints                                                 │
│ Schemas                                                     │
└──────────────────────────────┬──────────────────────────────┘
                               │ instantiated by
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  DEA CATALOGS / MODELS                      │
└─────────────────────────────────────────────────────────────┘

The direction is deliberate:

The Concepts Model consumes the semantic foundation of the Metaframework and provides candidates to the Metamodel.

It does not become a competing metamodel.

⸻

3. Scope

CR-CM-001 establishes only the foundation.

In scope

* repository structure;
* governance;
* concept lifecycle;
* concept identity;
* concept definition;
* relationship vocabulary;
* Concept Areas;
* Concept Profiles;
* ECF Context;
* provenance;
* external mappings;
* metamodel candidacy;
* PlantUML conventions;
* machine-readable representation;
* validation rules;
* contribution/change-request process.

Not in scope

The CR does not yet finalize:

* Agentic Enterprise;
* Autonomous Enterprise;
* Autonomous Operations;
* HVS;
* VOF;
* KCI / KEI / KBI;
* R.I.S.E.;
* AI Agent;
* Agentic AI;
* Closed Loop;
* Autonomous Closed Loop.

Those become substantive concept content under subsequent CRs.

⸻

4. Core Design Principle

The Concepts Model shall follow this principle:

Conceptual meaning precedes formal information structure.

Therefore:

Concept
   ≠
Entity

and:

Concept Relationship
   ≠
Metamodel Relationship

A concept may eventually map to a metamodel entity, but this requires an explicit semantic decision.

For example:

Agentic Enterprise
       │
       │ conceptual candidate
       ▼
Concept
       │
       │ maps-to
       ▼
EntitySpec

The mapping must not imply:

Agentic Enterprise --|> Enterprise

until that inheritance relationship has been formally accepted by the foundational metamodel.

⸻

5. Canonical Concept Model

The initial conceptual structure shall be:

Concept
│
├── identity
├── definition
├── scope
├── conceptAreas
├── ecfContexts
├── profiles
├── relationships
├── distinctions
├── provenance
└── maturity

A concept therefore has several independent dimensions:

                  Concept
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Definition    Classification  Context
        │            │            │
        │       Concept Area   ECF Context
        │
        └─────────────┬─────────────
                      ▼
                 Relationships
                      │
                      ▼
                   Profiles

⸻

6. Concept Identity

Every canonical concept shall have a stable identifier.

Recommended form:

CM-<AREA>-<NNN>

Examples:

CM-ENT-001
CM-OPS-001
CM-AI-001
CM-FLW-001
CM-VAL-001
CM-MEA-001

The identifier must be stable even if:

* the display name changes;
* the definition is refined;
* the concept moves between Concept Areas.

The identifier represents identity, not classification.

⸻

7. Concept Definition Contract

Each concept must contain, at minimum:

Property	Required	Purpose
id	Yes	Stable identity
name	Yes	Canonical name
definition	Yes	Normative semantic definition
status	Yes	Lifecycle state
conceptAreas	Yes	Organizational context
relationships	No	Known semantic relationships
distinguishesFrom	No	Important semantic boundaries
provenance	Yes	Origin/evidence
version	Yes	Concept revision
maturity	Yes	Semantic maturity

⸻

8. Example Concept Artifact

The repository shall support a representation similar to:

id: CM-OPS-001
name: Agentic Operations
definition: >
  An operational model in which AI agents participate in the
  execution and coordination of operational work within defined
  objectives, policies, authority and governance boundaries.
status: established
maturity: emerging
conceptAreas:
  - Operations
  - Intelligence
  - Execution
ecfContexts: []
profiles:
  - Agentic Operations
  - Agentic Enterprise
relationships:
  - verb: uses
    target: CM-AI-002
  - verb: executes
    target: CM-FLW-001
distinguishesFrom:
  - Autonomous Operations
  - AI-Native Operations
provenance:
  type: OpenDEA
  sources:
    - internal-concept-development
version: 0.1.0

The exact schema can evolve, but the semantic pattern should be established now.

⸻

9. Concept Lifecycle

CR-CM-001 shall establish the following lifecycle:

PROPOSED
   │
   ▼
EXPERIMENTAL
   │
   │ semantic evidence
   ▼
ESTABLISHED
   │
   │ reusable / stable
   ▼
CANONICAL
   │
   │ formalization candidate
   ▼
METAMODEL CANDIDATE
   │
   │ approved by metamodel CR
   ▼
FORMALIZED

With a possible rejection/retirement path:

              ┌──────────────┐
              │   PROPOSED   │
              └──────┬───────┘
                     ▼
              EXPERIMENTAL
                     │
              ┌──────┴──────┐
              ▼             ▼
         ESTABLISHED     RETIRED
              │
              ▼
          CANONICAL
              │
              ▼
     METAMODEL CANDIDATE
              │
              ▼
          FORMALIZED

Important distinction

Canonical does not mean metamodel entity.

A concept can be canonical within the Concepts Model without being part of the foundational metamodel.

⸻

10. Concept Areas

The repository shall use Concept Area, never generic Domain, for thematic organization.

Initial Concept Areas:

Enterprise
Operations
Intelligence
Execution
Control
Scenario
Value
Measurement
Systems

These are organizational structures and must not be interpreted as ECF Domains.

A concept may belong to multiple Concept Areas.

For example:

Agentic Operations
├── Operations
├── Intelligence
└── Execution

This is intentional.

⸻

11. ECF Context

The repository shall implement the terminology decision from CR-CM-000.

ECF Context
├── Domain
└── Stage

The concept does not own or redefine the Domain vocabulary.

Instead:

Concept
   │
   └── has-ecf-context
              │
              ▼
         ECF Context
              │
         ┌────┴────┐
         ▼         ▼
      Domain     Stage

Normative rule

Any property named domain in a Concepts Model artifact must either:

1. explicitly belong to the ECF namespace; or
2. be replaced with conceptArea.

This should be validated automatically where practical.

⸻

12. Relationship Vocabulary

CR-CM-001 shall establish a controlled relationship vocabulary.

Initial canonical verbs:

Structural

specializes
generalizes
distinguishes-from

Semantic

relates-to
depends-on
complements

Operational

uses
executes
orchestrates
controls
governs
enables
realizes

Value

supports
contributes-to
creates
realizes-value
measures
justifies

Contextual

belongs-to
has-context
has-ecf-context
includes
references

Formalization

maps-to
candidate-for
formalized-as

The vocabulary must be treated as controlled terminology rather than allowing arbitrary synonyms to proliferate.

⸻

13. Relationship Semantics

The Concepts Model must distinguish:

specializes

from:

uses

from:

contributes-to

from:

maps-to

For example:

AI Agent
   │
   └── uses ──► AI Model

does not mean:

AI Agent
   │
   └── specializes ──► AI Model

Likewise:

KCI
   │
   └── contributes-to ──► KEI

does not mean:

KCI
   │
   └── specializes ──► KEI

This distinction is foundational to the later HVS/VOF model.

⸻

14. Concept Profile

A Concept Profile is a reusable perspective over the concept graph.

For example:

Value Realization Profile
│
├── Enterprise Objective
├── High-Value Scenario
├── Initiative
├── KCI
├── KEI
├── KBI
├── Value Model
├── Value Contribution
└── R.I.S.E.

The profile does not own those concepts.

It composes them.

Concept Profile
       │
       ├── includes ──► Concept
       ├── includes ──► Relationship
       └── references ─► ECF Context

⸻

15. Provenance

Every concept must be traceable to its origin.

Supported provenance categories should include:

OpenDEA
TM Forum
GSMA
Industry Standard
Academic
Industry Practice
Project Research
Derived
Proposed

A concept derived from TM Forum must not be represented as though it were an original OpenDEA definition.

The repository should preserve:

source
sourceVersion
sourceDate
sourceIdentifier
mappingStatus

where available.

⸻

16. External Standards Mapping

External concepts should be mapped rather than copied.

For example:

OpenDEA Concept
       │
       │ externally-aligned-with
       ▼
TM Forum Concept

or:

OpenDEA Concept
       │
       │ derived-from
       ▼
External Concept

The distinction between:

equivalent-to
aligned-with
derived-from
related-to

should be preserved.

This will become particularly important for:

* HVS;
* KCI;
* KEI;
* KBI;
* VOF;
* R.I.S.E.;
* Autonomous Networks.

⸻

17. Repository Structure

The initial repository shall use:

dea-concepts-model/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── GOVERNANCE.md
│
├── governance/
│   ├── terminology-registry.yaml
│   ├── concept-lifecycle.md
│   └── relationship-vocabulary.yaml
│
├── concepts/
│   ├── enterprise/
│   ├── operations/
│   ├── intelligence/
│   ├── execution/
│   ├── control/
│   ├── scenario/
│   ├── value/
│   ├── measurement/
│   └── systems/
│
├── concept-areas/
│
├── profiles/
│
├── relationships/
│
├── models/
│   ├── master/
│   ├── concept-areas/
│   └── profiles/
│
├── mappings/
│   ├── ecf/
│   ├── dea-metamodel/
│   └── external/
│
├── change-requests/
│
└── schemas/
    └── concept.schema.yaml

⸻

18. Master PlantUML

The first canonical model should establish the semantic architecture rather than all of the business concepts.

@startuml OpenDEA_Concepts_Model
title OpenDEA Concepts Model — Semantic Architecture
skinparam backgroundColor white
skinparam packageStyle rectangle
skinparam shadowing false
package "DEA MetaFramework" {
    class "Enterprise Concept Framework" as ECF
    class "ECF Domain" as Domain
    class "ECF Stage" as Stage
    ECF --> Domain : defines
    ECF --> Stage : defines
}
package "OpenDEA Concepts Model" {
    class Concept
    class "Concept Area" as ConceptArea
    class "Concept Profile" as ConceptProfile
    class "ECF Context" as ECFContext
    class "Concept Relationship" as ConceptRelationship
    class "Concept Classification" as ConceptClassification
    class Provenance
    ECFContext --> Domain : uses-domain
    ECFContext --> Stage : uses-stage
    Concept --> ECFContext : has-ecf-context
    Concept --> ConceptArea : belongs-to
    ConceptProfile --> Concept : includes
    ConceptProfile --> ConceptRelationship : includes
    Concept --> ConceptRelationship : participates-in
    Concept --> ConceptClassification : has
    Concept --> Provenance : has-provenance
}
package "DEA Foundational Metamodel" {
    class EntitySpec
    class Relationship
}
Concept --> EntitySpec : maps-to
ConceptRelationship --> Relationship : candidate-for
@enduml

This model intentionally does not yet place Agentic Enterprise, HVS, VOF, etc. into the master architecture. Those belong to subsequent CRs.

⸻

19. Governance Rules

The following become normative:

Rule 1 — No semantic duplication

The Concepts Model must not redefine concepts already owned authoritatively by the Metaframework or Metamodel.

Rule 2 — No premature formalization

A concept must not be treated as a metamodel entity merely because it exists in the Concepts Model.

Rule 3 — Controlled relationship verbs

New relationship verbs require governance approval.

Rule 4 — Domain protection

Domain and Stage retain their ECF meaning.

Rule 5 — Concept Area for thematic grouping

No new thematic grouping may be called Domain.

Rule 6 — Explicit provenance

Every externally derived concept requires provenance.

Rule 7 — Explicit metamodel mapping

Promotion into dea-metamodel requires an explicit mapping and subsequent metamodel CR.

Rule 8 — Stable identity

Concept IDs remain stable across semantic revisions.

⸻

20. Validation Requirements

The repository should eventually validate:

✓ unique concept IDs
✓ unique relationship IDs
✓ required definition
✓ valid lifecycle status
✓ valid Concept Areas
✓ valid relationship verbs
✓ valid ECF Domain references
✓ valid ECF Stage references
✓ valid profile references
✓ valid provenance
✓ no generic Domain misuse
✓ no unresolved relationship targets

The initial implementation may use lightweight scripts rather than a sophisticated ontology engine.

The objective is semantic discipline first, automation second.

⸻

21. Definition of Done

CR-CM-001 is complete when:

* dea-concepts-model repository exists.
* Repository README establishes its architectural purpose.
* Relationship to dea-metaframework is documented.
* Relationship to dea-metamodel is documented.
* CR-CM-000 terminology decisions are incorporated.
* Domain is reserved for ECF semantics.
* Concept Area is established.
* Concept Profile is established.
* ECF Context is established.
* Concept lifecycle is defined.
* Concept identity convention is defined.
* Concept definition structure is defined.
* Relationship vocabulary is established.
* Provenance model is established.
* External mapping mechanism is established.
* Metamodel promotion mechanism is established.
* Master conceptual PlantUML exists.
* Machine-readable concept schema exists.
* Terminology registry exists.
* Governance/contribution rules exist.
* No substantive Agentic/Autonomous/VOF concepts are prematurely declared canonical.

⸻

22. Expected Result

Once CR-CM-001 is implemented, the OpenDEA architecture will have a clean semantic progression:

                    DEA METAFRAMEWORK
                           │
                 Enterprise Concept
                      Framework
                           │
                     Domain × Stage
                           │
                           ▼
                 ┌───────────────────┐
                 │   ECF Context     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │     CONCEPT       │
                 └─────────┬─────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
       Concept Area   Relationship   Provenance
              │            │
              └──────┬─────┘
                     ▼
              Concept Profile
                     │
                     │ semantic
                     │ stabilization
                     ▼
              Metamodel Candidate
                     │
                     │ CR
                     ▼
              DEA METAMODEL

This is the foundation we need before loading the Agentic–Autonomous–Value concepts into the model.

Next CR after implementation

CR-CM-002 — Agentic and Autonomous Concept Model

That CR should take the already-developed master concept set—Agentic AI, AI Agent, Agentic Workflow, Agentic Operations, Agentic Enterprise, AI-Native Operations, Autonomous Operations, Autonomous Enterprise, Autonomous System, Autonomous Network, Autonomous Value Stream, Agentic Value Stream, Closed Loop, AI Closed Loop, Autonomous Closed Loop, etc.—and formalize their definitions, distinctions and relationship verbs using the foundation established here.

The HVS → Initiative → KCI → KEI → KBI → VOF/R.I.S.E. model should then follow as CR-CM-003/004, rather than being mixed into the foundation.