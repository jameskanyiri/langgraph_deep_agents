# LangGraph Deep Agent

A deep research agent built with LangGraph that conducts thorough, multi-layered research through dynamic skill loading, intelligent planning, context management, and task delegation.

## What is a Deep Research Agent?

A **deep research agent** is an AI system that can conduct comprehensive research by breaking down complex queries into manageable parts, delegating work to specialized sub-agents, and dynamically loading domain expertise as needed.

This agent has four core components:

1. **✅ Skill Loading** (Implemented) - Dynamically loads domain expertise
2. **🔄 Planning** (Coming Soon) - Breaks down complex research into structured plans
3. **🔄 Context Offloading** (Coming Soon) - Manages memory efficiently for long research sessions
4. **🔄 Sub Agents** (Coming Soon) - Delegates specialized research to focused sub-agents

## What are Skills?

Skills are folders of instructions, scripts, and resources that the agent loads dynamically to improve performance on specialized tasks. Skills teach the agent how to complete specific tasks in a repeatable way, whether that's:

- Creating documents with specific brand guidelines
- Analyzing data using specific workflows
- Following research methodologies
- Automating domain-specific tasks

## Current Implementation

### ✅ Skill Loading System

The first component is fully implemented, enabling the agent to:

- **List Skills**: Discover available skills without loading them
- **Load Skills**: Dynamically load specific skills when needed
- **Modular Design**: Each skill is a self-contained folder with instructions

**Available Skills:**

- **Brand Writing** - Guidelines for maintaining consistent brand voice and formatting
- **Research Guidelines** - Structured approach to research with citation standards

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Deep Research Agent                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ Skill Loading      → Load domain expertise on-demand    │
│  🔄 Planning           → Decompose research into tasks      │
│  🔄 Context Offloading → Manage long-term memory           │
│  🔄 Sub Agents         → Delegate specialized research      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### How Deep Research Will Work (When Complete)

1. **User asks a complex research question**
2. **Planning**: Agent creates a structured research plan
3. **Skill Loading**: Loads relevant domain expertise
4. **Sub Agents**: Spawns specialized agents for different research aspects
5. **Context Offloading**: Manages information efficiently across long sessions
6. **Synthesis**: Combines findings into comprehensive results

## Quick Start

### Prerequisites

- Python 3.13+
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/jameskanyiri/langgraph_deep_agents.git
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
    "messages": [("user", "Your research question here")]
})
```

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

## Example Usage (Current)

**Listing Skills:**

```
User: "What skills do you have?"
Agent: Lists all available skills with their purposes
```

**Research with Guidelines:**

```
User: "Research webhook security best practices"
Agent:
  → Lists available skills
  → Loads research_guidelines_skill
  → Conducts structured research with citations
  → Returns findings
```

**Brand-Compliant Writing:**

```
User: "Write a product update announcement"
Agent:
  → Loads brand_writing_skill
  → Applies brand guidelines
  → Produces on-brand content
```

## Roadmap

### Phase 1: Skill Loading ✅ Complete

- [x] Skill discovery system
- [x] Dynamic skill loading
- [x] Basic research and writing skills

### Phase 2: Planning 🔄 In Progress

- [ ] Task decomposition
- [ ] Research plan generation
- [ ] Query analysis and breakdown
- [ ] Structured thinking steps

### Phase 3: Context Offloading 🔄 Planned

- [ ] Memory management system
- [ ] Context compression
- [ ] Long-term information storage
- [ ] Retrieval mechanisms

### Phase 4: Sub Agents 🔄 Planned

- [ ] Sub-agent spawning
- [ ] Task delegation
- [ ] Parallel research execution
- [ ] Result aggregation

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

## Why Deep Research?

Traditional research agents have limitations:

- ❌ Can't handle complex, multi-faceted queries
- ❌ Run out of context on long research sessions
- ❌ Lack specialized domain knowledge
- ❌ Can't work in parallel on sub-tasks

Deep research agents solve this:

- ✅ Break down complex queries systematically
- ✅ Manage context efficiently across long sessions
- ✅ Load domain expertise on-demand
- ✅ Delegate work to specialized sub-agents
- ✅ Synthesize findings comprehensively

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

## Contributing

We're actively building the remaining components! Contributions welcome for:

- New skills
- Planning system implementation
- Context management strategies
- Sub-agent architectures

Pull requests welcome!

## License

[Add your license here]

---

Built with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph)
