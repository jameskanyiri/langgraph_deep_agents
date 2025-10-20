from langchain.agents import create_agent
from src.tools.load_skills import load_skills
from src.tools.list_skills import list_skills
from src.prompt import AGENT_PROMPT
from langchain.chat_models import init_chat_model
from src.utils.utils import get_today_str

model = init_chat_model(model="openai:gpt-4.1", temperature=0)

tools = [load_skills, list_skills]

agent = create_agent(
    model=model,
    tools=tools,
    prompt=AGENT_PROMPT.format(date=get_today_str()),
).with_config({"recursion_limit": 50})
