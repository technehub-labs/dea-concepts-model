# Concepts

Canonical concept artifacts live here, **one directory per Concept
Area**. A concept file lives under its *primary* Concept Area and may
list several areas in its `conceptAreas` field (CR-CM-001 §10 — a
concept may belong to multiple Concept Areas; this is intentional).

```text
concepts/
├── enterprise/
├── operations/
├── intelligence/
├── execution/
├── control/
├── scenario/
├── value/
├── measurement/
└── systems/
```

## Status

**This foundation ships no substantive concepts** (CR-CM-001 §3, §21).
The Agentic / Autonomous / Value concept sets (Agentic Enterprise, HVS,
VOF, KCI / KEI / KBI, R.I.S.E., AI Agent, Closed Loop, …) arrive under
CR-CM-002 and CR-CM-003/004. Nothing here is prematurely declared
canonical.

## Contract

Every concept artifact is a YAML document validating against
[`../schemas/concept.schema.yaml`](../schemas/concept.schema.yaml) and
passing [`../tools/validate.py`](../tools/validate.py). The illustrative
shape (CR-CM-001 §8 — example only, not a landed concept):

```yaml
id: CM-OPS-001
name: Agentic Operations
status: established
maturity: emerging
conceptAreas: [Operations, Intelligence, Execution]
ecfContexts: []
relationships:
  - verb: uses
    target: CM-AI-002
provenance:
  type: OpenDEA
  sources: [internal-concept-development]
version: 0.1.0
```
