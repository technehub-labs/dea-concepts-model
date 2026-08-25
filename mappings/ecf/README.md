# ECF Mappings

Mappings between Concepts Model artifacts and the **Enterprise Concept
Framework** (`technehub-labs/dea-metaframework`).

- [`ecf-coordinates.yaml`](ecf-coordinates.yaml) — the referenced
  Domain × Stage coordinate system used to validate ECF Context entries
  (CR-CM-001 §11). The Concepts Model **references** the ECF vocabulary;
  it never owns or redefines it (GOVERNANCE.md Rule 4).
- A concept's ECF positioning is expressed in the concept artifact
  itself (`ecfContexts: [{domain, stage}, …]`), validated against the
  coordinate reference.

The ECF contextualizes the Concepts Model (see the semantic stack in the
[README](../../README.md)); the flow of authority is one-directional:
metaframework → concepts model.
