# LangGraph Deep Agent

A deep research agent built with LangGraph that dynamically loads skills to complete specialized tasks.

## What is This?

This is a **deep agent** - an AI agent that can dynamically load and use **skills** to improve its performance on specialized tasks.

### What are Skills?

Skills are folders of instructions, scripts, and resources that the agent loads dynamically to improve performance on specialized tasks. Skills teach the agent how to complete specific tasks in a repeatable way, whether that's:

- Creating documents with specific brand guidelines
- Analyzing data using specific workflows
- Following research methodologies
- Automating domain-specific tasks

## Current Features

### ✅ Skills System

- **List Skills**: Discover available skills without loading them
- **Load Skills**: Dynamically load specific skills when needed
- **Modular Design**: Each skill is a self-contained folder with instructions and examples

### Skills Included

1. **Brand Writing** - Guidelines for maintaining consistent brand voice and formatting
2. **Research Guidelines** - Structured approach to research with citation standards

## Upcoming Features

- 🔄 **Planning**: Advanced task planning and decomposition
- 💾 **Context Offloading**: Efficient memory management for long-running tasks
- 🤖 **Sub Agents**: Spawn specialized sub-agents for complex tasks

## Quick Start

### Prerequisites

- Python 3.13+
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd langgraph_deep_agent

# Install dependencies
uv sync

# Set up environment
echo "OPENAI_API_KEY=your_key_here" > .env
```

### Run the Agent

```bash
# Start with LangGraph CLI
langgraph dev
```

Or use programmatically:

```python
from src.graph import agent

result = agent.invoke({
    "messages": [("user", "Your task here")]
})
```

## How It Works

1. **User makes a request** → Agent receives the task
2. **Agent lists available skills** → Discovers what capabilities exist
3. **Agent loads relevant skills** → Loads only what's needed for the task
4. **Agent executes with skills** → Uses loaded instructions to complete the task

## Project Structure

```
langgraph_deep_agent/
├── src/
│   ├── graph.py              # Agent configuration
│   ├── prompt.py             # Agent instructions
│   ├── tools/
│   │   ├── list_skills.py    # Discover skills
│   │   └── load_skills.py    # Load skills
│   └── skills/               # Skills directory
│       ├── brand_writing_skill/
│       │   ├── SKILL.yaml    # Metadata
│       │   └── SKILL.md      # Instructions
│       └── research_guidelines_skill/
│           ├── SKILL.yaml
│           └── SKILL.md
├── langgraph.json            # LangGraph config
└── pyproject.toml            # Dependencies
```

## Creating a New Skill

1. **Create a folder** in `src/skills/`:

   ```bash
   mkdir src/skills/my_skill
   ```

2. **Add SKILL.yaml**:

   ```yaml
   name: my_skill
   purpose: What this skill does
   ```

3. **Add SKILL.md** with instructions:

   ```markdown
   # Skill: My Skill

   ## Purpose

   What this skill helps with

   ## When to Use

   - Scenario 1
   - Scenario 2

   ## Instructions

   Step-by-step guidance for the agent

   ## Examples

   Concrete examples
   ```

4. **Agent auto-discovers it** - No code changes needed!

## Example Usage

**Listing Skills:**

```
User: "What skills do you have?"
Agent: Lists all available skills with their purposes
```

**Research Task:**

```
User: "Research webhook security best practices"
Agent:
  → Lists skills
  → Loads research_guidelines_skill
  → Conducts structured research with citations
  → Returns findings
```

**Writing Task:**

```
User: "Write a product update announcement"
Agent:
  → Loads brand_writing_skill
  → Applies brand guidelines
  → Produces on-brand content
```

## Configuration

### Change the Model

Edit `src/graph.py`:

```python
model = init_chat_model(model="openai:gpt-4o", temperature=0)
```

### Customize Prompts

Edit `src/prompt.py` to change agent behavior and instructions.

## Dependencies

- `langchain` - LLM framework
- `langchain-openai` - OpenAI integration
- `langgraph` - Agent orchestration
- `langgraph-cli` - Development tools

## Troubleshooting

**Skills not loading?**

- Check that `SKILL.yaml` and `SKILL.md` exist in the skill folder
- Verify file encoding is UTF-8

**API errors?**

- Confirm `OPENAI_API_KEY` is set in `.env`
- Check your API quota

**Import errors?**

- Ensure Python 3.13+ is installed
- Run `uv sync` to install dependencies

## Why Skills?

Traditional agents have all their knowledge baked in, making them:

- ❌ Hard to maintain
- ❌ Difficult to customize
- ❌ Expensive (loading unused context)

Skills make agents:

- ✅ Modular and maintainable
- ✅ Easy to customize
- ✅ Efficient (load only what's needed)
- ✅ Shareable across teams

## Contributing

Add new skills, improve existing ones, or enhance the agent's core capabilities. Pull requests welcome!

## License

[Add your license here]

---

Built with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph)
