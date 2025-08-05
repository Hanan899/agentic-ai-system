from utils.llm_instance import llm

def enhance_ticket_status(department, ticket_id, issue, status) -> str:
    prompt = f"""
    Rephrase the following ticket status in a natural and helpful way like a human support assistant.

    Ticket Information:
    - Department: {department}
    - Ticket ID: {ticket_id}
    - Issue: {issue}
    - Status: {status}

    Structure your response like this:

    Thought: [A short sentence about what you did]
    Final Answer: [A human-friendly, clear summary of the ticket status]

    Respond only in that format.
    """

    result = llm.invoke(prompt).content.strip()
    return result