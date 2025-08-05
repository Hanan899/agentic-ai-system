import os
import json
import importlib.util
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from utils.llm_instance import llm
from utils.db_utils import init_db
from utils.ticket_parser import extract_ticket_info_and_intent


init_db()

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'agents_config.json')
tools = []

with open(CONFIG_PATH, 'r') as f:
    agent_config = json.load(f)

for agent in agent_config:
    module_path = os.path.join(os.path.dirname(__file__), "agents", f"{agent['file']}.py")
    spec = importlib.util.spec_from_file_location(agent["file"], module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    func = getattr(module, agent["function"])
    tools.append(Tool(name=agent["name"], func=func, description=agent["description"]))


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def classify_intent(prompt: str) -> str:
    """
    Classify the user intent into:
    - "ticket": if the user is asking for support, status, or reporting an issue.
    - "info": if the message is informational or general.
    """
    intent_prompt = f"""
    Classify the intent of the following user message into one of these categories:
    - "ticket": if the user is reporting a problem, requesting support, or asking for ticket status.
    - "info": if the message doesn't relate to tickets or support.

    User message: "{prompt}"

    Only return one word: ticket or info.
    """
    try:
        result = llm.invoke(intent_prompt).content.strip().lower()
        return result if result in ("ticket", "info") else "info"
    except Exception as e:
        print(f"[Intent Classification Error] {e}")
        return "info"
