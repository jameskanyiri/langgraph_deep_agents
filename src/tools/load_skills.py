from langchain.tools import tool
from pathlib import Path

LOAD_SKILLS_TOOL_DESCRIPTION = """
Load and manage reusable domain skills so the agent can use the right capabilities during planning and execution.

## What does a skill contain?
- Skills contains structured instruction, scripts, or resources that extends the agents base capabilities.

## When to use skills?
- Before, during, or after planning when the task likely needs domain expertise (e.g. brand writing, brand tone, specific document templates etc.)

## When to not use skills?
- When the task is not clear or not related to domain expertise or specific skills (e.g. "I need help with my project", "I need to write a report", etc.)

## Skill File Structure
- Each skill is a folder containing:
    - SKILL.md: Description, usage guidance and examples.
    
    
## Best Practices:
- Load only minimal required information per skill to stay efficient and focused.
- Compose compatible skills (e.g., research + brand_style); prune irrelevant ones

## Lifecycle:
- 1. Scan: Inspect available skills in the skills directory.
- 2. Match: Identify skills that are relevant to the current goal or user request.
- 3. Load: Retrieve and inject necessary context or scripts into the agent’s workspace.

## Parameters:
- skill_name: The name of the skill to load (e.g., "brand_writing_skill", "research_guidelines_skill")

## Returns:
- The full content of the skill's SKILL.md file with instructions and examples.
"""


@tool(description=LOAD_SKILLS_TOOL_DESCRIPTION)
def load_skills(skill_name: str) -> str:
    """
    Load and return the content of a skill's SKILL.md file.

    Args:
        skill_name: The name of the skill to load (e.g., "brand_writing_skill")

    Returns:
        The content of the SKILL.md file, or an error message if not found.
    """
    # Construct the path to the skill directory
    skills_base = Path("src/skills")
    skill_dir = skills_base / skill_name
    skill_md_path = skill_dir / "SKILL.md"

    # Check if skill directory exists
    if not skill_dir.exists():
        available_skills = (
            [d.name for d in skills_base.iterdir() if d.is_dir()]
            if skills_base.exists()
            else []
        )
        return f"Error: Skill '{skill_name}' not found. Available skills: {', '.join(available_skills)}"

    # Check if SKILL.md file exists
    if not skill_md_path.exists():
        return f"Error: SKILL.md file not found in skill '{skill_name}'"

    # Read and return the content
    try:
        content = skill_md_path.read_text(encoding="utf-8")
        return f"# Loaded Skill: {skill_name}\n\n{content}"
    except Exception as e:
        return f"Error reading SKILL.md for '{skill_name}': {str(e)}"
