from langchain.agents import AgentState
from src.schema import Todo
from typing import NotRequired


class DeepAgentState(AgentState):
    """
    A structured state for the deep agent.
    """
    
    todos: NotRequired[list[Todo]]
