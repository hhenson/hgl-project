# Language baseline review

Status: non-normative extraction and improvement review.

The first pass fills thirteen language chapters in `hgl_spec`. It retains
reviewed rules and labels proposed extensions. The authoring conventions and
outline were accepted separately; their acceptance does not ratify all features.

Source snapshot and extraction cautions are in
[the source map](language-specification-extraction.md). The source is
`hgraph_spec` revision `606e77a75d8542f145672d24e44edb7036161cb5`.

## Coverage and status

| Chapter | Source sections/records | Treatment |
| --- | --- | --- |
| Source text | Syntax chapter: lexical rules and temporal literals | Lexical baseline, token/domain separation |
| Units and names | Module boundary; ADR 0006/0013; default binding scope | Modules/defaults retained; general lookup remains proposed |
| Types and values | Type extensions; atomic scalar equivalence; bytes/any; recursive fields | Reviewed type rules; delta storage/mutable aggregate proposals separated |
| Expressions and bindings | Syntax expressions; contextual bindings; tuple construction | Expression/binding baseline; sparse construction remains proposed |
| Functions and phases | ADR 0008/0007; value-function guide; classification | Role, lifting, pack, and phase distinctions retained |
| Generics and operators | Syntax generics; operator/module policy; WIR-16–24 | Nominal selection retained; core domains remain independently specified |
| Temporal model | Handler selectors; ADR 0010/0011; capability/clock records | Admission/state/cache retained; alarm/keyed-state proposals separated |
| Control flow and sources | Conditional, switch, iteration records; ADR 0015 | Branch/loop rules retained; generator details remain proposed |
| Native boundaries | ADR 0014; implementation parts; native atomic values | Portable contracts retained; target implementation details excluded |
| Errors and diagnostics | Accepted lookup/result/capture records; error catalogue | Distinct data/failure channels and stable code conditions retained |
| Tests and eval | Test syntax; error assertions/rejections; eval/storage records | Proposed harness profile; structured failure expectations preserved |
| Program execution | Running-a-module rules | Entry/lifecycle model; tool-specific configuration excluded |
| Source documentation | Documentation and declaration-formatting records | Reviewed attachment, markup, and preservation rules retained |

This is a consolidated baseline, not proof of complete semantic coverage.
Detailed native/cardinality and collection-publication profiles need further
rule-level extraction and examples. Target AST, emitted layouts, historical
implementation limits, and build recipes were excluded deliberately.

## Improvement priorities

| Priority | Finding | Consequence |
| --- | --- | --- |
| P0 | Grammar references close, but contextual/generic forms still need disambiguation cases | A closed grammar is not necessarily an unambiguous language definition |
| P0 | Core numeric/operation domains and failure phases are incomplete | Equivalent source can otherwise admit inconsistent results or errors |
| P0 | Runtime conformance links remain planned | Document assertions do not demonstrate execution |
| P1 | Phase/capability/borrow rules span several chapters | A single checked matrix will expose inconsistent permissions |
| P1 | Aggregate/delta/ref boundaries need more discriminating examples | Held values, publications, absence, and lifetime can be confused |
| P1 | Eval storage and timed profiles remain proposed | Recording ownership, key isolation, and pre-start admission need review |
| P2 | Provider/version/imported metadata boundaries need detailed extraction | Interface checking must not depend on executable provider loading |

Follow-up work is tracked in
[the improvement issue](https://github.com/hhenson/hgl_spec/issues/3).
Unresolved design choices stay in [the decision tracker](https://github.com/hhenson/hgl_spec/issues/2).

## Validation scope

Checked local document links, rule-ID uniqueness, grammar-definition uniqueness,
grammar reference closure, balanced EBNF delimiters, example/status presence,
member independence, and absence of embedded question lists. The workspace's
CMake file target also lists the new documents.

These checks establish document structure. They do not establish parse
unambiguity, full semantic consistency, or runtime conformance. No compiler or
runtime implementation changed in this pass.
