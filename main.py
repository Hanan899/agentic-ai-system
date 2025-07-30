from langchain.agents import Tool, initialize_agent
from agents.infra_agent import handle_infra_issue
from agents.hr_agent import handle_hr_issue
from agents.it_agent import handle_it_issue
from agents.finance_agent import handle_finance_issue
from agents.admin_agent import handle_admin_issue
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.db_utils import init_db
import os

init_db()

tools = [
    Tool(name="InfraAgent", func=handle_infra_issue,
         description="Useful for handling infrastructure issues such as WiFi problems, power outages, or hardware malfunctions."),
    Tool(name="HRAgent", func=handle_hr_issue,
         description="Useful for HR-related concerns like leave applications, salary queries, complaints, and resignations."),
    Tool(name="ITAgent", func=handle_it_issue,
         description="Useful for technical support related to software, hardware, and login issues."),
    Tool(name="FinanceAgent", func=handle_finance_issue,
         description="Useful for financial queries including reimbursements, salary problems, or payment delays."),
    Tool(name="AdminAgent", func=handle_admin_issue,
         description="Useful for administrative issues such as logistics, access requests, office supplies, or general support."),
]

os.environ["GOOGLE_API_KEY"] = "AIzaSyBhTaT29mORqPhmnPyGEYdpVRTswmzSxgU"

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
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
