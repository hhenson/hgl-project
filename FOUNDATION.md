# Foundation charter

Date: 2026-11-01. Status: agreed direction; proposed details remain labelled.

## Agreed

- **FND-1 — Language.** Design HGL as a language. Implementations satisfy its
  contracts; implementation history does not define them.
- **FND-2 — Ownership.** `hgl_spec` owns language and runtime concepts.
  `hgl_core` owns the mandatory API, its runtime contract, core code, and all
  runtime conformance expectations. `hgl_std` owns optional library behavior.
  Implementation projects own compilers, engines, and target adapters.
- **FND-3 — Resources.** Use three resource types: specifications with rules,
  examples/APIs, and useful diagrams; explanations with justification and
  references when needed; executable HGL with required native implementation
  and ordinary implementation tests. Avoid duplicate authorities.
- **FND-4 — Documents only.** `hgl_spec` contains specification and explanation
  documents. Illustrative fenced code is part of a document; executable source
  files belong in core or a library. Repository metadata and agent rules are
  permitted.
- **FND-5 — Core.** Specify the minimum facilities required to support HGL.
  Separate the interface visible to HGL code from the contract an implementation
  must supply. Express requirements as behavior before choosing target symbols.
- **FND-6 — Conformance.** Core owns shared runtime cases and expected results.
  Tests observe behavior. Provider-specific code adapts a target without
  changing expectations. Ordinary implementation tests accompany code.
- **FND-7 — Independence.** Member projects require no historical repository or
  experiment record to explain their contracts. This wrapper holds that context.
  Trials stay in their existing locations and are not normative dependencies.
- **FND-8 — Writing.** Keep documentation and discussion terse. Add a separate
  explanation only when a concept needs sustained justification.
- **FND-9 — Workspace.** Use public, independent repositories, pinned as Git
  submodules in this wrapper. The wrapper provides one CLion entry point.

## Proposed first exercise

Freeze a dense scalar `eval` contract, then realize it with core declarations,
portable fixtures, and a target adapter. Demonstrate silence, repeated values,
empty inputs, fresh recordings, outputless targets, and failure separation.
Run with core's declared dependency closure and no optional library.

This exercise proposes behavior; it does not accept earlier drafts wholesale.
No implementation or conformance claim is made by this scaffold.

## Open

- Exact native API, public core names, and mandatory type domains.
- Eval target selection, time model, input profiles, and failure codes.
- Test-host API and observations requiring native instrumentation.
- Location of portable language-only rejection tests.
- Compatibility, versioning, and the first implementation target.

Member documents own detailed questions. Resolve a question explicitly before
promoting its proposed text to an agreed rule.
