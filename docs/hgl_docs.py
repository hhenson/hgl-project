"""Stage published Markdown without changing the owning repositories."""

from pathlib import Path
import posixpath
import re
import shutil
import subprocess

from pygments.lexers import TextLexer


MEMBERS = ("hgl_spec", "hgl_core", "hgl_std")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
GITHUB = re.compile(
    r"https://github\.com/hhenson/(hgl_spec|hgl_core|hgl_std)"
    r"(?:/blob/[^/]+/([^\s)#]+)(#[^\s)]+)?)?(?=[\s)]|$)"
)


def revision(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repository), "rev-parse", "HEAD"], text=True
    ).strip()


def local_links(text: str, destination: Path, site: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        member, document, fragment = match.groups()
        target = site / "reference" / member / (document or "README.md")
        if not target.is_file():
            return match.group(0)
        relative = posixpath.relpath(target.as_posix(), destination.parent.as_posix())
        return relative + (fragment or "")

    return GITHUB.sub(replace, text)


def children(index: Path, candidates: list[Path]) -> list[Path]:
    """Use each repository's link order, then include new documents by name."""
    available = {p.resolve(): p for p in candidates}
    ordered = []
    for target in LINK.findall(index.read_text(encoding="utf-8")):
        if "://" in target:
            continue
        candidate = (index.parent / target.split("#", 1)[0]).resolve()
        if candidate in available and candidate not in ordered:
            ordered.append(candidate)
    ordered += sorted(set(available) - set(ordered))
    return [available[p] for p in ordered]


def append_navigation(index: Path, entries: list[Path]) -> None:
    if not entries:
        return
    paths = [posixpath.relpath(p.as_posix(), index.parent.as_posix()) for p in entries]
    with index.open("a", encoding="utf-8") as stream:
        stream.write("\n\n```{toctree}\n:hidden:\n:maxdepth: 2\n\n")
        stream.write("\n".join(paths))
        stream.write("\n```\n")


def prepare_sources(site: Path) -> None:
    root = site.parent
    destination = site / "reference"
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir()
    sources = [(root / "FOUNDATION.md", destination / "FOUNDATION.md", root)]
    for name in MEMBERS:
        member = root / name
        if not (member / "README.md").is_file():
            raise RuntimeError(f"Missing {name}; run git submodule update --init --recursive")
        paths = [member / "README.md"]
        for directory in ("spec", "explanations"):
            folder = member / directory
            if folder.is_dir():
                paths.extend(
                    p for p in folder.rglob("*")
                    if p.is_file() and p.name != "AGENTS.md"
                )
        for source in paths:
            target = destination / name / source.relative_to(member)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            if source.suffix == ".md":
                sources.append((source, target, member))
    shutil.copyfile(root / "FOUNDATION.md", destination / "FOUNDATION.md")
    revisions = {repository: revision(repository) for repository in {p[2] for p in sources}}
    for source, target, repository in sources:
        text = source.read_text(encoding="utf-8")
        text = local_links(text, target, site)
        text = re.sub(r"^```mermaid\s*$", "```{mermaid}", text, flags=re.MULTILINE)
        repository_name = "hgl-project" if repository == root else repository.name
        source_path = source.relative_to(repository).as_posix()
        source_url = (
            f"https://github.com/hhenson/{repository_name}/blob/"
            f"{revisions[repository]}/{source_path}"
        )
        target.write_text(text + f"\n\n---\n\n[Repository source]({source_url}).\n", encoding="utf-8")
    for name in MEMBERS:
        member = destination / name
        index = member / "README.md"
        candidates = list((member / "spec").rglob("*.md"))
        language_index = member / "spec" / "language" / "README.md"
        if language_index.is_file():
            candidates = [
                p for p in candidates
                if not p.is_relative_to(language_index.parent) or p == language_index
            ]
            chapters = [p for p in language_index.parent.rglob("*.md") if p != language_index]
            append_navigation(language_index, children(language_index, chapters))
        for folder in (member / "explanations",):
            if folder.is_dir():
                candidates.extend(folder.rglob("*.md"))
        append_navigation(index, children(index, candidates))


def setup(app):
    # Preserve illustrative HGL/EBNF as written; no compiler is involved.
    app.add_lexer("hgl", TextLexer)
    app.add_lexer("ebnf", TextLexer)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
