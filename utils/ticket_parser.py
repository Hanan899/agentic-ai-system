from utils.llm_instance import llm

def extract_ticket_info_and_intent(prompt: str) -> dict:
    """
    Extract ticket_id, department, and intent (check/close) from the user prompt.

    Returns:
        A dict like:
        {'ticket_id': 3, 'department': 'finance', 'intent': 'close'}
        OR
        {'ticket_id': None, 'department': None, 'intent': 'missing'}
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
            return {
                "ticket_id": int(parts.get("ticket_id", "0")) or None,
                "department": parts.get("department"),
                "intent": parts.get("intent"),
            }
        else:
            # Uniform fallback
            return {"ticket_id": None, "department": None, "intent": "missing"}

    except Exception as e:
        print(f"[Ticket Extraction Error] {e}")
        return {"ticket_id": None, "department": None, "intent": "missing"}
