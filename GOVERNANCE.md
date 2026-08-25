# Governance

The eight normative rules of the OpenDEA Concepts Model
(CR-CM-001 §19). These rules bind every artifact, contribution, and
change request in this repository.

## The rules

**Rule 1 — No semantic duplication.**
The Concepts Model must not redefine concepts already owned
authoritatively by the Metaframework or the Metamodel. If a concept is
governed elsewhere, reference it; never restate it.

**Rule 2 — No premature formalization.**
A concept must not be treated as a metamodel entity merely because it
exists in the Concepts Model. Canonical ≠ metamodel entity (CR-CM-001
§9). Formalization is a gated lifecycle transition, not a side effect
of documentation.

**Rule 3 — Controlled relationship verbs.**
New relationship verbs require governance approval. The controlled
vocabulary lives in
[`governance/relationship-vocabulary.yaml`](governance/relationship-vocabulary.yaml);
arbitrary synonyms are not permitted to proliferate. A proposal for a
new verb must state which existing verb it differs from and why the
distinction is load-bearing.

**Rule 4 — Domain protection.**
`Domain` and `Stage` retain their ECF meaning. Any property named
`domain` in a Concepts Model artifact must either explicitly belong to
the ECF namespace (inside an ECF Context) or be renamed `conceptArea`
(CR-CM-001 §11). The validator enforces this automatically.

**Rule 5 — Concept Area for thematic grouping.**
No new thematic grouping may be called Domain. Thematic organization
uses Concept Areas (`concept-areas/concept-areas.yaml`), and a concept
may belong to several.

**Rule 6 — Explicit provenance.**
Every externally derived concept requires provenance — source, and
where available sourceVersion, sourceDate, sourceIdentifier, and
mappingStatus (CR-CM-001 §15). A concept derived from TM Forum must
never read as an original OpenDEA definition.

**Rule 7 — Explicit metamodel mapping.**
Promotion into `dea-metamodel` requires an explicit `maps-to` /
`candidate-for` mapping record (under `mappings/dea-metamodel/`) and a
subsequent metamodel CR. `maps-to` is an association, never
inheritance: the mapping must not imply a specialization that the
foundational metamodel has not formally accepted (CR-CM-001 §4).

**Rule 8 — Stable identity.**
Concept IDs (`CM-<AREA>-<NNN>`) remain stable across semantic
revisions — display names may change, definitions may be refined, and
a concept may move between Concept Areas without its identity
changing (CR-CM-001 §6). The identifier represents identity, not
classification.

## Decision process

- Changes arrive as **Change Requests** (see
  [`CONTRIBUTING.md`](CONTRIBUTING.md)); each CR lands verbatim in
  `change-requests/` and is implemented in phases, one PR per phase.
- Governance approval for controlled-vocabulary changes (Rule 3) is
  recorded in the CR that introduces the verb.
- The terminology registry
  ([`governance/terminology-registry.yaml`](governance/terminology-registry.yaml))
  is the authority on reserved and governed terms; its term shape
  (name / namespace / status / owner) is preserved exactly across
  migrations (CR-CM-000A §14).
