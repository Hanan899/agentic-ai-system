from utils.db_utils import insert_finance_ticket

def handle_finance_issue(prompt: str) -> str:
    return insert_finance_ticket(prompt)
