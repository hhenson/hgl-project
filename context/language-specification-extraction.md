# Language specification extraction

Status: context only. New language rules require separate review.

Source snapshot: [hgraph_spec at 606e77a](https://github.com/hhenson/hgraph_spec/tree/606e77a75d8542f145672d24e44edb7036161cb5).
Source locations below are relative to that snapshot.

| Source | Extract into |
| --- | --- |
| `language/docs/developer-guide/syntax-and-semantics.md`, lexical and compilation-unit sections | Source text; module structure; production notation |
| Same chapter, types, expressions, scopes, and classification | Types/values; expressions/bindings; functions/phases |
| Same chapter, temporal metadata, lifecycle, output, and tests | Temporal model; tests/eval; core API requirements |
| `language/docs/design/language-model.md` | Concept vocabulary and feature inventory |
| `language/docs/design/modules.md` and `operators.md` | Modules; generics; nominal operator resolution |
| `language/docs/design/documentation.md` | Source documentation; separate from specification authoring rules |
| `language/examples/midpoint.hgl`, `when-defaults.hgl`, and `test-contexts.hgl` | Dependency and expected-observation checks for practical examples |

## Candidate rules to review first

- UTF-8 source; ASCII identifier spelling; keyword/contextual-name distinctions.
- Double-quoted strings and explicit escapes; literal range and token boundaries.
- `#` line comments, non-nesting block comments, and `//` floor division.
- Significant newline and continuation rules; braces; indentation; EOF handling.
- Module headers, parts, imports, exports, declaration scope, and duplicates.

These are extraction candidates, not accepted HGL rules. Preserve example
observations as review questions until their governing rule is explicit.

## Extraction cautions

- The large syntax chapter calls its EBNF descriptive and mixes static/dynamic
  rules with compiler representations. Extract the language obligations only.
- Source documentation syntax and declaration formatting do not define how
  specification documents should be written.
- Testing sections retain proposed labels. The eval target differs between the
  syntax chapter (function/operator) and user guide (module function).
- Keep lexical policy, grammar, phase/type constraints, runtime API, and target
  implementation decisions distinct. Move no status claim automatically.

The conventions and chapter outline live in `hgl_spec`. Historical
source mapping stays here; member documents stand alone.

The conventions and outline are now agreed. The
[baseline review](language-baseline-review.md) maps the completed first pass
and its remaining precision/coverage work.
