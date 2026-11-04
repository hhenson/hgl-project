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
| P0 | Reviewed disambiguation rules and examples now cover generic construction, lambda extent, const modifiers/names, generic kinds, constraint precedence, and sequences | Executable source cases remain planned; document checks alone do not prove unambiguity |
| P0 | Numeric baseline, IEEE-default/checked division, tolerance, and full comparison are documented | Configuration order/phase rules, numerical edge cases, and executable conformance still need completion |
| P0 | Runtime conformance links remain planned | Document assertions do not demonstrate execution |
| P1 | Phase/capability/borrow rules span several chapters | A single checked matrix will expose inconsistent permissions |
| P1 | Aggregate/delta/ref boundaries need more discriminating examples | Held values, publications, absence, and lifetime can be confused |
| P1 | Eval storage and timed profiles remain proposed | Recording ownership, key isolation, and pre-start admission need review |
| P2 | Provider/version/imported metadata boundaries need detailed extraction | Interface checking must not depend on executable provider loading |

Follow-up work is tracked in
[the improvement issue](https://github.com/hhenson/hgl_spec/issues/3).
Unresolved design choices stay in [the decision tracker](https://github.com/hhenson/hgl_spec/issues/2).

The grammar review retained angle-bracket generics with declaration-aware
resolution, expression-delimited lambda bodies, and contextual `const` modifiers.
Outside modifier positions, `const` is an ordinary name with no role selector.
Generic kinds follow signature/constraint uses; `type(N)` constrains a
compile-time ordinary value's type. Constraint precedence is `!`, then `&&`,
then `||`. Brackets always denote sequences with either value entries or pair
entries, never a mixture; use sites constrain their interpretation. These
decisions do not accept the proposed eval or delta runtime profiles.

The numeric review agreed operator configuration, symmetric absolute/relative
tolerance, and `<=>` with explicit unordered outcomes. Floating-result `/`
defaults to IEEE outcomes, with NaN and error-producing alternatives. Core owns
the mathematical contract and expected observations; the language owns notation
and binding. Checked division with `zero: error` returns `result<f64, error>`;
signed zero divisors return Err with code `numeric.division_by_zero`. This
policy is fixed during checking, and propagation uses the existing result rules.
Further configuration and numerical choices remain in issues.

## Validation scope

Checked local document links, rule-ID uniqueness, grammar-definition uniqueness,
grammar reference closure, balanced EBNF delimiters, example/status presence,
member independence, and absence of embedded question lists. The workspace's
CMake file target also lists the new documents.

These checks establish document structure. They do not establish parse
unambiguity, full semantic consistency, or runtime conformance. No compiler or
runtime implementation changed in this pass.
