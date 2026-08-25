# Metamodel Promotion Mappings

Records of promotion decisions from the Concepts Model into the
foundational metamodel (`technehub-labs/dea-metamodel`).

## The mechanism (CR-CM-001 §4, §19 Rule 7)

Promotion is an **explicit semantic decision**, recorded here as a
mapping and ratified by a subsequent metamodel CR:

```text
Concept ──candidate-for──► EntitySpec     (proposed; metamodel-candidate)
Concept ──maps-to────────► EntitySpec     (explicit correspondence)
Concept ──formalized-as──► EntitySpec     (accepted via metamodel CR)
```

`maps-to` is an association, **never inheritance**: a mapping must not
imply a specialization the foundational metamodel has not formally
accepted. `Concept ≠ Entity` and `Concept Relationship ≠ Metamodel
Relationship` — conceptual meaning precedes formal information
structure.

## Status

No promotion mappings ship with this foundation: no concept has entered
`metamodel-candidate` (see
[`../../governance/concept-lifecycle.md`](../../governance/concept-lifecycle.md)).

## Record shape

Each mapping record states: the concept ID, the metamodel construct,
the relation (`candidate-for` / `maps-to` / `formalized-as`), the
metamodel CR that ratified it (once formalized), and provenance.
