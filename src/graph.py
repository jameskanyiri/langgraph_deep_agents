from langchain.agents import create_agent
from src.prompt import AGENT_PROMPT
from langchain.chat_models import init_chat_model
from src.utils.utils import get_today_str
from src.state import DeepAgentState

from src.tools.load_skills import load_skills
from src.tools.list_skills import list_skills
from src.tools.todo_tool import write_todo
from src.tools.read_todo import read_todo

model = init_chat_model(model="openai:gpt-4.1", temperature=0)

tools = [load_skills, list_skills, write_todo, read_todo]

agent = create_agent(
    model=model,
    tools=tools,
    prompt=AGENT_PROMPT.format(date=get_today_str()),
    state_schema=DeepAgentState,
).with_config({"recursion_limit": 50})
