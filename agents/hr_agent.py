from utils.db_utils import insert_hr_ticket

def handle_hr_issue(prompt: str) -> str:
    return insert_hr_ticket(prompt)
