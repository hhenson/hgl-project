# Observing scalar invalidation in hgraph

An investigation of hgraph 0.9.1 and Alex Balabin's `hg_cpp` development
branch. The runtime probes used 0.9.1. A source comparison on November 18,
2026 confirmed the same scalar clear path on hgraph's main branch.

## What a receiving node can observe

Clearing a valid scalar gives hgraph the current evaluation time and wakes
active subscribers. The native mutation returns whether it cleared a value.
It then leaves both stored timestamps at `MIN_DT`. Clearing an already
invalid scalar produces no new notification. A direct input reads `MIN_DT`
while its target is invalid. Python also discards the native mutation's return
value. [Owned scalar](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/src/hgraph/types/time_series/ts_data/base_view.cpp#L533-L571)
· [Input observation](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/src/hgraph/types/time_series/ts_input/base_view.cpp#L148-L203)
· [Python binding](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/python/py_runtime.h#L678-L682)

A probe that wakes one cycle after a passive clear sees the same invalid value
as a probe that coincides with the clear. Remembering the previous sample
also misses a publication followed by a clear between samples. On 0.9.1, a
producer that started invalid and then wrote and cleared its output in one
evaluation woke its subscriber with an invalid value. Repeating just the clear
on the next cycle left the subscriber asleep. Raw input `.modified` can also
reflect binding notifications and gave different answers across two Python
callback paths on an active clear. [Callback selection](https://github.com/hhenson/hgraph/blob/cd5e6a49f073aa537aee8a1dee1b009dc14fed8d/python/py_nodes.cpp#L648-L670)

## What hg_cpp retains

On Alex's `merge-bg-smaller` branch, the endpoint stores the time and kind of
its latest change together. A valid-to-invalid transition records the clear
time. A repeated clear preserves it. The receiving view's `became_invalid()`
combines the change kind with a current-cycle observation. A probe of the
state implementation gave the following sequence. [Storage decision](https://github.com/abalabin-bamfunds/hg_cpp/blob/18a13c68247f9b6a285615f200a2c976ad2a4ca0/docs/development/decisions/0026-packed-time-series-state.md#L7-L23)
· [Owned output](https://github.com/abalabin-bamfunds/hg_cpp/blob/18a13c68247f9b6a285615f200a2c976ad2a4ca0/include/hg/time_series/details/output_state.hpp#L58-L88)
· [Input predicate](https://github.com/abalabin-bamfunds/hg_cpp/blob/18a13c68247f9b6a285615f200a2c976ad2a4ca0/include/hg/time_series/details/input_data.hpp#L20-L31)

| Observation | Never valid | Publish | Clear | Idle | Publish again |
| --- | --- | --- | --- | --- | --- |
| Invalidated this cycle | false | false | true | false | false |

## Proposed direction for hgraph

For an owned scalar or its directly bound input, retain the evaluation time
of an effective clear. A read-only query can check that the endpoint ends
invalid and the clear occurred in this cycle. That would detect a write
followed by a clear, even from an initially invalid state. A clear followed
by a publication would end valid. A passive input could answer the same query
on an independent wake. This is a proposed scalar contract.

hgraph already writes a second timestamp on scalar clear. Its two readers
use it for explicit empty list and bundle publications. For an owned scalar,
this word could hold the clear time when invalid. This would add zero bytes
to the record and replace one existing store. A directly bound input could
check validity and compare that timestamp to the evaluation time on demand.
No end-of-cycle sweep would be needed. A separate eight-byte timestamp
would instead grow the shared 64-bit tracking record from 48 to 56 bytes,
about 7.6 MiB per million records before alignment and allocator effects.
These are layout estimates. CPU time has not been benchmarked.
[Scalar clear](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/src/hgraph/types/time_series/ts_data/base_view.cpp#L564-L570)
· [Structural readers](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/src/hgraph/types/time_series/ts_delta.cpp#L695-L723)
· [Tracking layout](https://github.com/hhenson/hgraph/blob/55be4cde3afb32718a6d9fb07c940cf3a0c344f3/include/hgraph/types/time_series/ts_data/types.h#L346-L359)

A scalar implementation would need to preserve checkpoint semantics and the
existing meaning of that word on structural values. A reference follower can lose its
target while the producer stays valid, and a dictionary child can become
invalid while its key remains present. Extending the query to these cases
requires tracking the transition on the endpoint being observed.
[Layout assertion](https://github.com/hhenson/hgraph/blob/cd5e6a49f073aa537aee8a1dee1b009dc14fed8d/tests/cpp/test_type_erasure_layout.cpp#L106-L112)
· [Checkpoint implementation](https://github.com/hhenson/hgraph/blob/cd5e6a49f073aa537aee8a1dee1b009dc14fed8d/src/hgraph/types/time_series/ts_data/checkpoint.cpp#L25-L45)
· [Reference withdrawal](https://github.com/hhenson/hgraph/blob/cd5e6a49f073aa537aee8a1dee1b009dc14fed8d/python/tests/test_runtime_spec_conformance.py#L6-L119)
· [Child invalidation](https://github.com/hhenson/hgraph/blob/cd5e6a49f073aa537aee8a1dee1b009dc14fed8d/tests/cpp/test_ts_input.cpp#L2981-L2996)
