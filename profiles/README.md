# Concept Profiles

A **Concept Profile** is a reusable perspective over the concept graph
(CR-CM-001 §14). It composes concepts, relationships, and ECF Contexts
for a particular architectural viewpoint — it does **not own** them.

```text
Concept Profile
       │
       ├── includes ──► Concept
       ├── includes ──► Relationship
       └── references ─► ECF Context
```

The CR-CM-001 §14 illustration (not yet a landed profile): a *Value
Realization Profile* composing Enterprise Objective, High-Value
Scenario, Initiative, KCI, KEI, KBI, Value Model, Value Contribution,
and R.I.S.E.

## Status

No profiles ship with this foundation (CR-CM-001 §3). Profiles arrive
with the content CRs that define the concepts they compose.

## Rules

- A profile is a **perspective**, never a grouping: it is never called
  a Domain (GOVERNANCE.md Rules 4–5).
- A profile references concepts by their stable IDs (Rule 8); the
  validator checks that every referenced concept resolves.
