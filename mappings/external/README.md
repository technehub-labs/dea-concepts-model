# External Standards Mappings

Mappings between OpenDEA concepts and external standards bodies'
concepts (CR-CM-001 §16).

## The principle

External concepts are **mapped, not copied**. A concept derived from
TM Forum must never be represented as an original OpenDEA definition —
provenance is explicit (CR-CM-001 §15, GOVERNANCE.md Rule 6).

## The mapping distinctions

The four mapping relations are part of the controlled vocabulary
([`../../governance/relationship-vocabulary.yaml`](../../governance/relationship-vocabulary.yaml)
→ `external_mapping_relations`):

| Relation | Meaning |
|---|---|
| `equivalent-to` | Same semantics. |
| `aligned-with` | Compatible semantics, declared non-identical scope. |
| `derived-from` | The OpenDEA concept derives from the external one; provenance records the source. |
| `related-to` | A weaker declared association. |

## Status

No external mappings ship with this foundation. They become load-bearing
with the HVS / KCI / KEI / KBI / VOF / R.I.S.E. and Autonomous Networks
concepts (CR-CM-002 / CR-CM-003 / CR-CM-004).

## Record shape

Each mapping record states: the OpenDEA concept ID, the external body
(e.g. TM Forum, GSMA), the external concept identifier and version, the
mapping relation, and provenance (sourceDate / sourceIdentifier /
mappingStatus where available).
