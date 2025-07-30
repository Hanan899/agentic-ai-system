from utils.db_utils import insert_admin_ticket

def handle_admin_issue(prompt: str) -> str:
    return insert_admin_ticket(prompt)
