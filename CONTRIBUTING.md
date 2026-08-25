# Contributing

All change in this repository is **CR-driven** (Change Request). The
Concepts Model is a governed semantic layer; nothing lands by drive-by
edit.

## Proposing a change

1. **Open a CR proposal.** A CR is a markdown document stating
   objective, scope, non-goals, design constraints, acceptance
   criteria, and a phase plan. Mirror the structure of
   [`change-requests/CR-CM-001.md`](change-requests/CR-CM-001.md).
2. **Land as authored.** Once accepted, the CR document lands verbatim
   in `change-requests/` (byte-identical to the accepted proposal).
3. **Sequential implementation.** One CR (or one CR phase) at a time;
   the next is parked until the current ships. Each phase is one PR.
4. **Scorecard close-out.** Every shipped phase ends with a
   deliverables + verification scorecard before merge.

## Proposing a concept

A new concept is content under a CR (typically a content CR such as the
planned CR-CM-002 series). Each concept:

- gets a stable ID (`CM-<AREA>-<NNN>`, Governance Rule 8);
- satisfies the definition contract in
  [`schemas/concept.schema.yaml`](schemas/concept.schema.yaml) — id,
  name, definition, status, conceptAreas, provenance, version,
  maturity are required;
- declares its lifecycle state per
  [`governance/concept-lifecycle.md`](governance/concept-lifecycle.md);
- uses only the controlled relationship verbs
  (Governance Rule 3);
- carries explicit provenance (Governance Rule 6);
- lives under `concepts/<primary-area>/` and may list several Concept
  Areas.

## Proposing a relationship verb

New verbs require governance approval (Governance Rule 3). The proposal
must name the nearest existing verbs and demonstrate the semantic
distinction the new verb carries (see CR-CM-001 §13 for the canonical
examples: `uses` ≠ `specializes`; `contributes-to` ≠ `specializes`).

## Validation

Run the validator before opening a PR:

```bash
pip install pyyaml
python tools/validate.py
```

CI runs the same script on every pull request.
