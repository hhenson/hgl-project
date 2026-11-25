# HGL project

HGL is a language for temporal computation. This workspace brings its
specification, mandatory core, standard library, compiler, and Rust runtime together.

| Repository | Owns |
| --- | --- |
| [hgl_spec](https://github.com/hhenson/hgl_spec) | Language, runtime concepts, and testing specifications; explanations |
| [hgl_core](https://github.com/hhenson/hgl_core) | Mandatory core API, runtime contract, HGL code, and runtime conformance |
| [hgl_std](https://github.com/hhenson/hgl_std) | Optional standard-library contracts, HGL code, and tests |
| [hgl-compiler](https://github.com/hhenson/hgl-compiler) | Compiler implementation, CLI, and implementation tests |
| [hgl-runtime](https://github.com/hhenson/hgl-runtime) | Rust graph execution engine and native support for HGL core |
| [hgl-ai](https://github.com/hhenson/hgl-ai) | Multi-host agent coordination bus, MCP server, and worker bridge |

Start with the [foundation charter](FOUNDATION.md). Historical context stays
in [existing work](context/existing-work.md); member repositories stand alone.
Track [open decisions](https://github.com/hhenson/hgl-project/issues/2) in issues.
The [language baseline review](context/language-baseline-review.md) summarizes
the initial thirteen-chapter specification and its improvement priorities.

On Apple silicon with macOS 26.0 or later, install the compiler and its SDK with
`brew install hhenson/hgraph/hgl`.

## Checkout and CLion

```sh
git clone --recurse-submodules https://github.com/hhenson/hgl-project.git
cmake -S hgl-project -B hgl-project/build
```

Open `hgl-project` in CLion and load its root `CMakeLists.txt`. The CMake target
lists workspace files; it builds no compiler or runtime. Each submodule pins
one reviewed revision. Commit member changes in their owning repository,
then update the wrapper's pins.

For an existing checkout, run `git submodule update --init --recursive` to
populate member checkouts, including the compiler's nested specification and
core. The wrapper's specification and core pins match those nested pins.

The compiler's Cargo workspace is `hgl-compiler/Cargo.toml`; its
[README](hgl-compiler/README.md) describes the build and CLI commands.
The pinned compiler's C++ target uses the hgraph 0.9.23 SDK in CI.
The language chapters preserve agreed rules and labelled proposals; compiler
implementation status does not establish runtime conformance.

The [runtime design drafts](hgl-runtime) cover graph execution,
endpoint storage and the first porting slice. The [native engine review](context/rust-runtime-port.md)
records the C++ mechanisms that informed those proposals.

## Documentation site

The Read the Docs configuration builds one specification site from this wrapper's
pinned member documents. [Publishing and local preview](docs/publishing.md)
describes the configuration and account setup. Generated pages are not committed;
edit each document in its owning repository.
