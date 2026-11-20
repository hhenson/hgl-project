# Native engine review for the Rust port

The hgraph source reviewed here is [`c9a70d5`][hg]. The HGL contracts are
the [language and core revisions][pins] used by compiler `ce056c9`.
The [runtime design][design] is proposed.

| C++ mechanism | Consequence for the port |
| --- | --- |
| Wiring ranks dependencies before constructing a graph. The graph planner computes storage offsets and a schedule entry per node. Evaluation walks the ordered nodes. [Ranking][rank] · [Layout and evaluation][graph] | Keep planning separate from execution. Resolve fixed routes at construction. A contiguous rank walk gives a baseline against which to measure sparse scheduling. |
| The TS data plan selects operations per shape. An input target link can cache a direct scalar route. Clearing owned data notifies observers and clears its publication time. [Data plan][data] · [Target link][link] · [Clear][clear] | Keep payload and publication metadata at the producer, activity on the receiving binding, and wake state on the node. Exercise clear, silence and repeated publication independently. |
| Keyed child graphs occupy stable slots. Graph stop attempts every stop in reverse order before unbinding edges. [Slots][slots] · [Stop][stop] | Preserve surviving child state during growth. Retain routes through stop. An expired child's identity must never resolve to a replacement occupying its slot. |
| Duration windows can register an expiry deadline with the root evaluator. [Expiry service][expiry] · [Evaluation][graph] | HGL END-9 evicts on the next arrival and keeps a value exactly at maximum age. An idle interval has no departure wake. Port the arrival buffer with HGL's eviction rule. [Core endpoint contract][end] |

### Rust/C++ wrapper

In the compiler prototype, shared lowering describes scalar kernels and a
keyed child. Generated Rust supplies the hook bodies and builds connections.
The C bridge turns these into node builders and a child map. hgraph ranks,
allocates and runs the graph. The prototype's recorder calls back with an
integer trace. [Prepared-builder work][prepared] · [Keyed compiler fixture][keyed]

Keep the split between emitted composition and emitted hooks. A Rust
backend can consume the same lowering and supply its own planner, endpoint
storage and evaluator. Compile core's HGL recorder so its owned deltas,
stop hook and store write are observable on that path. [Core execution][run]

[hg]: https://github.com/hhenson/hgraph/tree/c9a70d5e001b1ae4a1b233eb8986e673c4fae068
[pins]: https://github.com/hhenson/hgl-compiler/tree/ce056c917666f2d7f5049e13672b6c6fcdff495b/spec
[design]: https://github.com/hhenson/hgl-runtime/blob/28b62bc30974ce8f1e8954c38113b1103a3bca88/docs/design/graph.md
[rank]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/src/hgraph/types/graph_wiring.cpp#L978-L1058
[graph]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/src/hgraph/runtime/graph.cpp
[data]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/src/hgraph/types/metadata/ts_data_plan_factory.cpp
[link]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/include/hgraph/types/time_series/ts_input/target_link.h
[clear]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/src/hgraph/types/time_series/ts_data/base_view.cpp#L541-L580
[slots]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/include/hgraph/runtime/nested_graph_storage.h
[stop]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/src/hgraph/runtime/graph.cpp#L1164-L1220
[expiry]: https://github.com/hhenson/hgraph/blob/c9a70d5e001b1ae4a1b233eb8986e673c4fae068/src/hgraph/runtime/window_expiry_service.cpp
[end]: https://github.com/hhenson/hgl_core/blob/40c3e6ff8391c4cfd2821e9fc5f2cffc3450ab68/spec/temporal-endpoints.md
[prepared]: https://github.com/hhenson/hgraph/issues/1824
[keyed]: https://github.com/hhenson/hgl-compiler/blob/ce056c917666f2d7f5049e13672b6c6fcdff495b/crates/hgl_hgraph/tests/fixtures/demo.graph_for.hgl
[run]: https://github.com/hhenson/hgl_core/blob/40c3e6ff8391c4cfd2821e9fc5f2cffc3450ab68/spec/execution.md
