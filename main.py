import os
import json
import importlib.util
from langchain.agents import Tool, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType
from utils.db_utils import init_db

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

os.environ["GOOGLE_API_KEY"] = "API_Key_Here"
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def classify_intent(prompt: str) -> str:
    """
    Classify the user intent from their prompt.
    Categories: ticket, info
    """
    intent_prompt = f"""
    Classify the intent of the following user message into one of these categories:
    - "ticket": if the user is reporting a problem or requesting support.
    - "info": if the message doesn't fit any of the above.

    User message: "{prompt}"

    Just return the category label (ticket, info).
    """
    result = llm.invoke(intent_prompt).content.strip().lower()
    return result
