"""Validate existing documentation navigation and JSON without external writes."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs.json").read_text())
errors = []
assert manifest.get("icons", {}).get("library") == "lucide", "Lucide must remain the configured icon family"

def check_pages(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "pages":
                for page in child:
                    if isinstance(page, str) and not page.startswith(("https://", "http://")):
                        if not (ROOT / (page + ".mdx")).is_file():
                            errors.append("Missing navigation document: " + page)
            check_pages(child)
    elif isinstance(value, list):
        for child in value:
            check_pages(child)

check_pages(manifest.get("navigation", []))
for path in ROOT.rglob("*.json"):
    if ".git" not in path.parts:
        json.loads(path.read_text())
if errors:
    raise SystemExit("\n".join(errors))
print("Documentation navigation and JSON contracts passed")

# Authored card icons are pinned canonical SVG assets; provider shell stays Lucide.
import hashlib
import re
icons = json.loads((ROOT / "LUCIDE_PROVENANCE.json").read_text())
for file, expected in icons["files"].items():
    data = (ROOT / file).read_bytes()
    assert hashlib.sha256(data).hexdigest() == expected, file
    assert b'stroke-width="1.75"' in data, file
for page in ROOT.rglob("*.mdx"):
    for icon in re.findall(r'icon="([^"]+)"', page.read_text()):
        assert icon.lstrip("/") in icons["files"], (page, icon)
print("Canonical Lucide card assets and all authored icon references passed")

# A generated contract prevents the hosted docs navbar from drifting.
nav = json.loads((ROOT / "NAVIGATION_PROVENANCE.json").read_text())
assert manifest["navbar"]["links"] == nav["links"], "Regenerate public links from the Alpha design system"
canonical = json.dumps(nav["links"], separators=(",", ":"), ensure_ascii=False)
assert hashlib.sha256(canonical.encode()).hexdigest() == nav["sha256"]
assert [link["label"] for link in nav["links"]] == ["Platform", "Institute", "Council", "Events", "Company"]
print("Shared Alpha public navigation projection passed")
