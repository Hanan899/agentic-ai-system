from utils.llm_instance import llm

def extract_ticket_info_and_intent(prompt: str) -> dict:
    """
    Extract ticket info and intent from prompt.
    Returns a dictionary like:
    {'ticket_id': 3, 'department': 'finance', 'intent': 'close'}
    or
    {'status': 'missing'}
    """
    extract_prompt = f"""
    From the following user message, extract:
    - ticket_id (as a number)
    - department (like it, hr, finance, etc.)
    - intent (check or close)

    Return format (lowercase, no punctuation):
    ticket_id=3, department=finance, intent=close

    If anything is missing or unclear, return: missing

    User message: "{prompt}"
    """
    try:
        response = llm.invoke(extract_prompt).content.strip().lower()
        if "ticket_id" in response and "department" in response and "intent" in response:
            parts = dict(part.strip().split("=") for part in response.split(","))
            return parts
        else:
            return {"status": "missing"}
    except Exception as e:
        print(f"[Ticket Extraction Error] {e}")
        return {"status": "missing"}