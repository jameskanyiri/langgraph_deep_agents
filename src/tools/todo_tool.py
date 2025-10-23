from typing import Annotated
from langchain.tools import InjectedToolCallId, tool
from src.schema import Todo
from langgraph.types import Command
from langchain_core.messages import ToolMessage

TODO_TOOL_DESCRIPTION = """
Create and manage structured task list for tracking progress through complex workflows.

## When to use?
- Multi-step or non-trivial tasks requiring coordination
- When user provides multiple tasks or explicit requests todo list.
- Avoid for single, trivial actions.

## Structure
- Maintain one list containing multiple todo objects (content, status, id)
- Use clear, actionable content descriptions.
- Status must be: pending, in_progress or completed.

## Best practices
- Only one in_progress task at a time.
- Mark completed immediately when task is fully done.
- Always send the full updated list when making changes.
- Prune irrelevant items to keep list focused.

## Progress Updates
- Call TodoWrite again to change task status or edit content.
- Reflect real-time progress; do not batch completions.
- If blocked, keep in_progress and add new task describing blocker.


# Parameters
- todos: List of TODO items with content and status field.

Returns:
Updates agent state with new todos list.

"""


@tool(description=TODO_TOOL_DESCRIPTION)
def write_todo(
    todos: list[Todo], tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """
    Create or update the agents TODO list for task planning and tracking.

    Args:
        todos (list[Todo]): List of TODO items with content and status field.
        tool_call_id (Annotated[str, InjectedToolCallId]): The tool call id.

    Returns:
        Command: A command to update the agent's state with the new todos list.
    """
    return Command(
        update={
            "todos": todos,
            "messages": [
                ToolMessage(
                    content=f"Updated todos list to: {todos}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )
