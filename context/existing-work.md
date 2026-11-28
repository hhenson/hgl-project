# Existing work

Status: context only. This wrapper is the only new project that needs it.

| Public source | Useful material |
| --- | --- |
| [hgraph_spec](https://github.com/hhenson/hgraph_spec) | Language drafts, runtime rules, wiring, examples, and the base-layer proposal |
| [hgraph](https://github.com/hhenson/hgraph) | Runtime implementation and native authoring experience |
| [hgraph_lang](https://github.com/hhenson/hgraph_lang) | Compiler, CLI, lowering, packaging, and test execution |
| [hgraph_std](https://github.com/hhenson/hgraph_std) | Portable library bodies, replay/record, and test cases |

For each topic, carry forward the reviewed rule, rationale, example, and expected
observation. Preserve agreed/proposed/open distinctions. Keep historical status,
experiments, and migration notes here or in their existing repositories.

The new member projects state complete contracts directly. They neither import
historical source nor use observed behavior as their authority. Existing projects
remain intact during this work.

[Language specification extraction](language-specification-extraction.md)
records the source snapshot and candidate topics for the first drafting pass.

[Language baseline review](language-baseline-review.md) records extraction
coverage, validation scope, and prioritized improvement areas.

[hgraph operators against core](hgraph-operator-inventory.md) places each
public hgraph operator against core and the language, by name.

## Runtime conformance examples

The first HGL tick corpus drew scenarios from hgraph's [input activity
tests](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/python/tests/test_input_activity.py),
[delta tests](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/tests/cpp/test_ts_delta.cpp),
[scheduler tests](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/tests/cpp/test_node_scheduler.cpp)
and [switch tests](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/python/tests/ported/_wiring/test_switch.py).
Core's [shared HGL cases](https://github.com/hhenson/hgl_core/blob/82c6b7b953bdb30e18b554be39b7fc13d89ddf5a/tests/conformance/README.md) give the
expected observations and the status of each rule.

[Observing scalar invalidation in hgraph](hgraph-invalidation.md) records the
released engine's observable behavior and the approach taken by Alex Balabin's
`hg_cpp` development branch.
