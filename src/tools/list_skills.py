from pathlib import Path
from typing import List, Dict
from langchain.tools import tool
import yaml

LIST_SKILLS_TOOL_DESCRIPTION = """
List all available skills

## When to Use
- Before planning, when the agent needs to know which skills exist.
- To display available domain skills to a user or planner.
- Use this instead of load_skills when you just want discovery, not activation.

## Returns
- A list of skills with their name, path, and first few lines of the SKILL.md file.
"""


def _read_skill_yaml(skill_dir: Path) -> Dict:
    y = skill_dir / "SKILL.yaml"
    if not y.exists():
        return {}
    data = yaml.safe_load(y.read_text(encoding="utf-8")) or {}
    # basic normalization & inference
    name = str(data.get("name") or skill_dir.name)
    purpose = str(data.get("purpose") or "").strip()
    return {"name": name, "purpose": purpose}


@tool(description=LIST_SKILLS_TOOL_DESCRIPTION)
def list_skills() -> List[Dict]:
    """
    Scan skill_root for subfolders with SKILL.yaml and return minimal metadata.
    """
    base = Path("src/skills")
    if not base.exists():
        return [{"error": f"No skills directory found at {base.resolve()}"}]

    items: List[Dict] = []
    for entry in base.iterdir():
        if entry.is_dir():
            meta = _read_skill_yaml(entry)
            if meta:
                items.append(meta)

    # Stable, predictable order
    items.sort(key=lambda x: x.get("name", ""))
    return items
