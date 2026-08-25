# Relationships

Declared relationship instance sets live here as the concept graph
grows. The **vocabulary** of legal verbs is governed separately at
[`../governance/relationship-vocabulary.yaml`](../governance/relationship-vocabulary.yaml)
(CR-CM-001 §12; GOVERNANCE.md Rule 3).

## Status

No relationship instance sets ship with this foundation — the concept
graph has no substantive nodes yet (CR-CM-001 §3).

## The distinctions that matter (CR-CM-001 §13)

```text
AI Agent ──uses──────────► AI Model      ≠  AI Agent ──specializes──► AI Model
KCI      ──contributes-to─► KEI          ≠  KCI      ──specializes──► KEI
Concept  ──maps-to───────► EntitySpec    ≠  inheritance
```

`maps-to` is an explicit semantic decision, never implied
specialization. These distinctions are foundational to the later
HVS/VOF model.

## Rules

- Only controlled verbs; new verbs require governance approval.
- Every relationship target must resolve to an existing concept ID
  (validator-checked, CR-CM-001 §20).
- Relationship instance files carry stable IDs; IDs are unique across
  the repository (validator-checked).
