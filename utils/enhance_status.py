from utils.llm_instance import llm

def enhance_ticket_status(department, ticket_id, issue, status) -> str:
    """
    Summarize ticket status into a user-friendly sentence.
    """
    prompt = f"""
    Write a friendly summary of the ticket based on the following data:
    - Department: {department}
    - Ticket ID: {ticket_id}
    - Issue: {issue}
    - Status: {status}

    Keep it short, helpful, and clear. Don't use technical terms.
    """
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Unable to summarize ticket right now. Error: {e}"
