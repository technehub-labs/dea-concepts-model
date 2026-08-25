# Concept Lifecycle

CR-CM-001 §9 establishes the canonical concept lifecycle. The lifecycle
is the governance spine of the Concepts Model: it controls how a concept
moves from an emerging idea to a formal metamodel construct, and it is
the guard against premature formalization (Governance Rule 2).

## The states

```text
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
```

With the rejection / retirement path:

```text
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
```

## State semantics

| State | Meaning | Gate to enter |
|---|---|---|
| `proposed` | A candidate concept under discussion. | A contribution naming the concept and its intended meaning. |
| `experimental` | Definition drafted; semantics being exercised. | A definition contract-conformant artifact (`schemas/concept.schema.yaml`). |
| `established` | Semantic evidence gathered; definition holds up in use. | Demonstrated usage without contradiction. |
| `canonical` | Reusable, stable; the concept is an authority *within the Concepts Model*. | Stability across revisions and consumers. |
| `metamodel-candidate` | Proposed for formalization into the foundational metamodel. | An explicit `candidate-for` mapping record under `mappings/dea-metamodel/`. |
| `formalized` | Accepted into the foundational metamodel. | Approval via a metamodel CR (Governance Rule 7). |
| `retired` | Withdrawn; retained for provenance, never deleted silently. | Explicit retirement decision recorded in the concept artifact. |

## The load-bearing distinction

**Canonical does not mean metamodel entity** (CR-CM-001 §9). A concept
can be canonical within the Concepts Model — reusable, stable,
authoritative for concept work — without being part of the foundational
metamodel. Only the `metamodel-candidate → formalized` transition, gated
by an explicit mapping and a metamodel CR, crosses that boundary.

## Lifecycle and identity

Lifecycle transitions never change the concept's identifier
(Governance Rule 8): `CM-<AREA>-<NNN>` is stable across semantic
revisions, renames, and Concept Area moves. The `status` field in the
concept artifact carries the lifecycle state; the `version` field
carries the concept revision.
