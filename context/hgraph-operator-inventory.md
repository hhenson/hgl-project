# hgraph operators against core

Status: context only. A name-level inventory; no contract was compared and
no row is a decision about `hgl_std`.

Sources: hgraph `5749e59` (the 189 public names of
`python/hgraph/_operator_docs.py`, grouped as in
`include/hgraph/lib/std/operators/`), `hgl_core` `c47f1a7`, `hgl_spec`
`bff597b`.

| Coverage | Count | Meaning |
| --- | --- | --- |
| Core | 32 | Core declares an identity or native function for the need in `hgl/` |
| Core contract | 2 | A core specification gives the contract; `hgl/` declares nothing |
| Language | 16 | A language construct or core facility serves the need; no operator of that name |
| None | 139 | Neither core nor the language specification covers it |

A hgraph operator is a graph node over time-series. A core row often meets
the need another way: an endpoint read inside a node, a value function the
language lifts, or syntax. Equal names do not show equal behavior.

## Core

| hgraph | Core | Note |
| --- | --- | --- |
| `add_` `sub_` `mul_` `div_` `floordiv_` `mod_` `neg_` | Same identities | Numeric, scalar, temporal and tenor candidates; no collection broadcasting |
| `eq_` `ne_` `lt_` `le_` `gt_` `ge_` | Same identities | |
| `cmp_` | `compare_`, `CmpResult` | Core adds `unordered` |
| `and_` `or_` `not_` `all_` `any_` | Same identities | `bool` only; no truth semantics of other types |
| `convert` | `convert<T>` | Scalar, enum and text conversions (OPS-4, OPS-6); no collection reshaping |
| `str_` | `convert<str>` | |
| `map_` `reduce` | `map`, `reduce` | MAP-1 to MAP-10, RED-1 to RED-7 |
| `keys_` | `keys` | |
| `format_` `debug_print` | `format`, `debug_print` | |
| `print_` | `write` with `format` | |
| `log_` | `log`, `log_debug` … `log_error` | Through the `Logger` capability |
| `valid` `modified` `last_modified_time` | `valid`, `modified`, `last_modified` | Endpoint reads in a node, not graph nodes |
| `join` | `join` | Text only; hgraph's frame join has no counterpart |

## Core contract

| hgraph | Core | Note |
| --- | --- | --- |
| `union` `intersection` | SET-1, SET-2 in `spec/mapping.md` | Two sets; hgraph's take any number |

## Language

| hgraph | Language or core facility | Note |
| --- | --- | --- |
| `getitem_` `getattr_` | Named by the operator table (generics and operators) | No declaration in core's `hgl/` |
| `switch_` `if_then_else` | Temporal `switch` and `if` (CTRL-2, CTRL-15) | Only the selected child runs; hgraph's `if_then_else` wires both |
| `try_except` | `capture` (ERR-7) | |
| `nothing` | A temporal `if` without `else` (CTRL-3) | No standalone never-ticking source |
| `type_` | `type(e)` (TYPE-18) | The type the program's text gives |
| `window` `to_window` | `rolling_window<V, Max, Min>` (TYPE-11, END-9) | |
| `record` `replay` | Eval's replay and recording (CEVAL-2 to CEVAL-4) | Test execution only; no recording backend |
| `const` `schedule` | A source with `yield` (SOURCE-1); the `Scheduler` capability | Core's `schedule` asks for a wake and is not this operator |
| `dereference` | `ref` mode (TYPE-12, END-10) | |
| `null_sink` | An example function in the temporal model | |
| `len_` | `len(values)` appears in one language example | Declared nowhere |

## None

| Family | hgraph operators |
| --- | --- |
| Arithmetic | `abs_` `divmod_` `ln` `pos_` `pow_` `round_` `sign` |
| Aggregates | `max_` `mean` `min_` `sum_` |
| Bitwise | `bit_and` `bit_or` `bit_xor` `invert_` `lshift_` `rshift_` |
| Sets | `difference` `symmetric_difference` |
| Containers | `contains_` `index_of` `is_empty` `setattr_` `values_` |
| Dictionary reshaping | `collapse_keys` `filter_by` `flip` `flip_keys` `make_tsd` `partition` `rekey` `uncollapse_keys` `unpartition` |
| Construction | `collect` `combine` `default` `downcast_` `downcast_ref` `emit` `zero` |
| Selection and routing | `dispatch_` `if_` `if_cmp` `if_true` `merge` `mesh_` `race` `reduce_tsd_of_bundles_with_race` `reduce_tsd_with_race` `route_by_index` |
| Stream shaping | `batch` `dedup` `drop` `filter_` `freeze` `gate` `lag` `request_id` `sample` `slice_` `step` `take` `throttle` `until_true` |
| Text | `match_` `replace` `split` `substr` |
| Runtime and callables | `apply` `assert_` `call` `compare` `stop_engine` |
| Date and time parts | `datepart` `day` `day_of_month` `days` `explode` `hour` `isoformat` `isoweekday` `microsecond` `microseconds` `minute` `month` `month_of_year` `second` `seconds` `timestamp` `total_seconds` `weekday` `year` |
| Engine time | `evaluation_time_in_range` `last_modified_date` `last_modified_wall_clock_time` |
| Time zones | `at_zone` `convert_zone` `resolve_civil` `to_civil` `to_instant` |
| Temporal ranges | `range_adjacent` `range_contains` `range_difference` `range_extent` `range_hull` `range_intersection` `range_merge` `range_mergeable` `range_overlaps` `range_shift` `range_touches` `range_union` |
| Temporal rounding | `temporal_bucket` `temporal_ceil` `temporal_floor` `temporal_round` |
| JSON | `from_json` `json_as_bool` `json_as_float` `json_as_int` `json_as_str` `json_decode` `json_encode` `to_json` |
| Tables | `from_table` `from_table_const` `table_schema` `to_table` |
| Frames | `concat` `filter_cs` `filter_frame` `from_data_frame` `from_data_frame_batches` `group_by` `replay_data_frame` `sorted_` `to_data_frame` `ungroup` `with_columns` |

## Projection in a graph

hgraph already has the graph-level behaviour that `hgl_spec` GEN-19 to
GEN-21 give the four projection identities. The correspondence, from
hgraph's operator documentation at the snapshot above:

| hgraph | Behaviour there | HGL rule |
| --- | --- | --- |
| `getattr_(ts, attr)` | The field name is fixed when the graph is wired, since it decides the output schema; `port.field` delegates to it | GEN-19, GEN-21: a member's name stays a constant |
| `getitem_(ts, key)` | `ts[key]` wires it; the key may be a scalar or a time-series, and a live key retargets the output when it changes; a list takes a time-series index | GEN-21: a key or an index may be a connection |
| `setattr_(ts, attr, value)` | Returns a structure of the same schema with the field replaced | GEN-20, GEN-21: the graph's `var` is rebound to the candidate's result |
| `make_tsd(key, value)` | A key change removes the old entry and publishes the value under the new key | GEN-21: a write by a ticking key reverts the key it left |

hgraph has no `setitem_`. HGL's write by a ticking key into an existing
dictionary follows `make_tsd`'s treatment of the key it left; nothing in
hgraph was compared for it beyond that.

## Observations

- The time-zone types are language types (TYPE-2) with no operation in core.
  The language has no temporal range type; its `a..<b` is a range of `i64`.
- JSON, tables and frames need value types neither the language nor core has.
- `stop_engine` has no rule: core's execution contract says a stop a node
  asks for is undefined.
- Core has no counterpart in this list for `roll`, `business_day` and tenor
  arithmetic, `append` and `extend`, the global store's `get`, `has` and
  `put`, or `delta_value`, `removed_value`, `invalidate`, `activate` and
  `passivate`.
- Not inventoried: hgraph's adaptors, services, analytics, and the testing
  helpers under `include/hgraph/lib/testing`.
