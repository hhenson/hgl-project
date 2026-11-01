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

## Checkout and CLion

```sh
git clone --recurse-submodules https://github.com/hhenson/hgl-project.git
cmake -S hgl-project -B hgl-project/build
```

Open `hgl-project` in CLion and load its root `CMakeLists.txt`. The CMake target
lists workspace files; it builds no compiler or runtime. Each submodule pins
one reviewed revision. Commit member changes in their owning repository,
then update the wrapper's pins.

This is the foundation scaffold. It supplies no executable core or conformance
runner yet. Practical examples will refine the proposed contracts.
