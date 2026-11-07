# HGL project

HGL is a language for temporal computation. This workspace brings its
specification, mandatory core, and standard library together.

| Repository | Owns |
| --- | --- |
| [hgl_spec](https://github.com/hhenson/hgl_spec) | Language, runtime concepts, and testing specifications; explanations |
| [hgl_core](https://github.com/hhenson/hgl_core) | Mandatory core API, runtime contract, HGL code, and runtime conformance |
| [hgl_std](https://github.com/hhenson/hgl_std) | Optional standard-library contracts, HGL code, and tests |

Start with the [foundation charter](FOUNDATION.md). Historical context stays
in [existing work](context/existing-work.md); member repositories stand alone.
Track [open decisions](https://github.com/hhenson/hgl-project/issues/2) in issues.
The [language baseline review](context/language-baseline-review.md) summarizes
the initial thirteen-chapter specification and its improvement priorities.

## Checkout and CLion

```sh
git clone --recurse-submodules https://github.com/hhenson/hgl-project.git
cmake -S hgl-project -B hgl-project/build
```

Open `hgl-project` in CLion and load its root `CMakeLists.txt`. The CMake target
lists workspace files; it builds no compiler or runtime. Each submodule pins
one reviewed revision. Commit member changes in their owning repository,
then update the wrapper's pins.

The language chapters contain the initial reviewed baseline and labelled
proposals. The workspace supplies no executable core or conformance runner yet.
Practical examples and core cases will refine the contracts.

## Documentation site

The Read the Docs configuration builds one specification site from this wrapper's
pinned member documents. [Publishing and local preview](docs/publishing.md)
describes the configuration and account setup. Generated pages are not committed;
edit each document in its owning repository.
