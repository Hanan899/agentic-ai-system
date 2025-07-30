from utils.db_utils import insert_it_ticket

def handle_it_issue(prompt: str) -> str:
    return insert_it_ticket(prompt)
