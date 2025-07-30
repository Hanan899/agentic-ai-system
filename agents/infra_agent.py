from utils.db_utils import insert_infra_ticket

def handle_infra_issue(prompt: str) -> str:
    return insert_infra_ticket(prompt)
