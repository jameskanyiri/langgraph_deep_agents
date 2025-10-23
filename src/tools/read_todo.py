from langchain.tools import tool,InjectedToolCallId
from langchain.tools import InjectedState
from src.state import DeepAgentState
from typing import Annotated
from langgraph.types import Command
from langchain_core.messages import ToolMessage

READ_TODO_TOOL_DESCRIPTION = """
Read the agents TODO list for task planning and tracking.

## When to use?
- When you need to know what tasks are currently being worked on.
- When you need to know what tasks are pending.
- When you need to know what tasks are completed.

## Returns:
- The current TODO list.
"""


@tool(description=READ_TODO_TOOL_DESCRIPTION)
def read_todo(
    state: Annotated[DeepAgentState, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId]
)->Command:
    """
    Read the agents TODO list for task planning and tracking.

    Returns:
        list[Todo]: The current TODO list.
    """
    #Get todos from the state
    todos = state.get("todos", [])
    
    if not todos:
        return "No todos found in the list"
    
    result = "Current TODO Lists: \n"
    
    for i, todo in enumerate(todos):
        status_emoji = {"pending": "🔴", "in_progress": "🟡", "completed": "🟢"}
        
        emoji = status_emoji.get(todo["status"], "?")
        result += f"{i}. {emoji} {todo['content']} ({todo['status']})\n"
    
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content=result.strip(),
                    tool_call_id=tool_call_id,
                )
            ]
        }
    )