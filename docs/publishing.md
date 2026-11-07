# Publishing the specification

Read the Docs builds the public specification from `hhenson/hgl-project`.
The wrapper pins `hgl_spec`, `hgl_core`, and `hgl_std`; member Markdown remains
authoritative. Build configuration and generated navigation live in this
wrapper, so member repositories need no publishing code.

## Local preview

```sh
git submodule update --init --recursive
python3 -m venv .venv-docs
.venv-docs/bin/python -m pip install -r docs/requirements.txt
.venv-docs/bin/python -m sphinx -n -W --keep-going docs build/docs/html
python3 -m http.server --directory build/docs/html 8000
```

Open `http://localhost:8000`. `docs/reference/` is generated from the member
checkouts, with local cross-repository links and navigation. Do not edit or
commit it. History, audit material, agent rules, and wrapper context are excluded.

## Read the Docs project

1. Sign in to [Read the Docs Community](https://app.readthedocs.org/dashboard/).
2. Import `https://github.com/hhenson/hgl-project`; use project slug `hgl-project`
   if available. Connect the GitHub repository integration.
3. Keep `main` as the intended default branch and use `.readthedocs.yaml` at
   the repository root. The configuration installs the documentation tools and
   checks out the pinned public submodules.
4. Before the documentation PR is merged, build its branch as described below.
   A build of `main` cannot use configuration that exists only on the PR branch.
5. Under **Settings → Pull request builds**, verify **Build pull requests for
   this project** is enabled and click **Update** if changed. An existing PR
   needs a new push after integration is enabled to trigger its first preview.
6. Confirm the hosted language/core pages, search, cross-links, and diagrams.

## Initial build before merge

The initial documentation configuration is on `codex/checked-division` in
wrapper PR #6. Until that PR is merged, the automatic initial `main` build may
fail because `main` does not yet contain `.readthedocs.yaml`.

In the project **Versions** tab, locate `codex/checked-division` under
**Activate a version**, click **Activate**, select **Active**, and save.
Activation triggers a build for that branch. Follow the version URL shown by
Read the Docs; its slug is generated from the branch name. This is a temporary
documentation preview, not a change to the intended `main` default.

After the member and wrapper PRs merge, trigger the `latest` build for `main`
and verify it succeeds. The temporary branch version can then be deactivated.
The `latest` version remains the project's default.

The project URL is confirmed after import; no account credentials or tokens
belong in this repository. Publishing a member change requires committing that
member revision and updating the wrapper pin.

Reference: [Read the Docs configuration](https://docs.readthedocs.com/platform/stable/config-file/v2.html).
See also [version activation](https://docs.readthedocs.com/platform/stable/versions.html)
and [pull-request builds](https://docs.readthedocs.com/platform/stable/guides/pull-requests.html).
