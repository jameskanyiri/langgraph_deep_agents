from typing import Annotated, Literal, NotRequired, TypedDict


class Todo(TypedDict):
    """
    A structured task item for tracking progress through complex workflows.
    
    Attributes:
        content: Short, specific description of the task.
        status: Current state - pending, in_progress, completed
    """
    
    content: str
    status: Literal["pending", "in_progress", "completed"]