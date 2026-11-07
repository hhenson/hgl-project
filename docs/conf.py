"""Build the public specification from the wrapper's pinned member sources."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hgl_docs import prepare_sources, setup  # noqa: E402,F401

prepare_sources(Path(__file__).resolve().parent)

project = "HGL specification"
author = "HGL contributors"
copyright = "2026, HGL contributors"
language = "en"
root_doc = "index"
source_suffix = {".md": "markdown"}
extensions = ["myst_parser", "sphinxcontrib.mermaid"]
myst_heading_anchors = 6
exclude_patterns = ["publishing.md"]
html_theme = "furo"
html_title = "HGL specification"
html_static_path = ["_static"]
html_css_files = ["hgl.css"]
html_show_sourcelink = False
html_theme_options = {"navigation_with_keys": True}
mermaid_version = "11.12.1"
nitpicky = True
