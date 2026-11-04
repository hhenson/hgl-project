# Project rules

- Before every push, check the branch's PR state on GitHub. If its previous PR
  is merged, fetch `origin/main`, start a fresh `codex/` branch from it, and carry
  forward only the new changes. Do not push follow-up commits to a merged PR's
  branch; open a new PR for the fresh branch.
- Keep documents, discussions, issues, and reviews terse. Avoid extended dialogue.
- Read [FOUNDATION.md](FOUNDATION.md); preserve its agreed/proposed/open labels.
- Keep open questions and decision checklists in the owning repository's issue
  tracker, outside specification and explanation documents.
- Keep historical knowledge in this wrapper. Member projects must be usable alone.
- Reuse reviewed ideas. Existing behavior does not silently become a rule.
- Member repositories own their contracts and files. Update submodule pins after
  member commits; never edit generated copies of their sources.
- Spec documents contain rules, example code/APIs, and diagrams where useful.
  Explanations justify complex concepts only when needed. Executable HGL and
  required native implementation code live in core or library repositories.
- Mark required native surfaces explicitly. Do not invent a native API or HGL
  spelling to fill an open decision.
- Report validation with its scope. A workspace configuration is not conformance.
- Keep host details, credentials, local paths, and private projects out of commits.
