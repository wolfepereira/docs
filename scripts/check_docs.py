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
