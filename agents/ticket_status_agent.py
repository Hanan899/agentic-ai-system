from langchain.tools import BaseTool
from typing import Optional
from utils.db_utils import check_ticket_status
import re

class TicketStatusTool(BaseTool):
    name: str = "TicketStatusChecker"
    description: str = (
        "Checks the status of a ticket. "
        "Input should be a string containing ticket ID and department, e.g., 'ticket_id=4, department=hr'"
    )

    def _run(self, input: str) -> str:
        print(f"🛠️ [TicketStatusTool] Raw input: {input}")

        # Parse ticket_id and department
        ticket_match = re.search(r"ticket_id\s*=\s*(\d+)", input)
        dept_match = re.search(r"department\s*=\s*['\"]?(\w+)['\"]?", input)

        if not ticket_match or not dept_match:
            return "❌ Invalid input format. Expected 'ticket_id=4, department=hr'"

        ticket_id = int(ticket_match.group(1))
        department = dept_match.group(1).strip().lower()
        table_name = f"{department}_tickets"  # <-- ✅ key fix here

        print(f"✅ [TicketStatusTool] Parsed ticket_id={ticket_id}, table_name='{table_name}'")

        result = check_ticket_status(ticket_id, table_name)
        print(f"📤 [TicketStatusTool] Result: {result}")
        return result

    def _arun(self, *args, **kwargs) -> str:
        raise NotImplementedError("This tool does not support async")
    


