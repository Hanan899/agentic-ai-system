import re
import sqlite3
from utils.enhance_status import enhance_ticket_status
from utils.ticket_parser import extract_ticket_info_and_intent

def check_ticket_status(query: str) -> str:
    # Extract ticket number
    if "ticket_id=" in query and "department=" in query:
        try:
            parts = dict(item.strip().split("=") for item in query.split(","))
            ticket_id = int(parts["ticket_id"])
            department = parts["department"]
        except Exception:
            return "❌ Failed to parse structured ticket info."
    else:
        # Fallback to legacy regex logic
        ticket_id_match = re.search(r'ticket\s*#?(\d+)', query, re.IGNORECASE)
        if not ticket_id_match:
            return "Please provide a ticket number like 'ticket #3'."
        ticket_id = int(ticket_id_match.group(1))
        department = None

    # Try to find department from the query
    department_map = {
        "it": ("it_tickets", "issue"),
        "infra": ("infra_tickets", "issue"),
        "infrastructure": ("infra_tickets", "issue"),
        "hr": ("hr_tickets", "issue"),
        "finance": ("finance_tickets", "query"),
        "admin": ("admin_tickets", "issue"),
    }

    query_lower = query.lower()
    selected_table = None

    for keyword, (table, column) in department_map.items():
        if keyword in query_lower:
            selected_table = (table, column)
            break

    conn = sqlite3.connect("db/system.db")
    cursor = conn.cursor()

    # If department is identified, search only in that table
    if selected_table:
        table, column = selected_table
        cursor.execute(f"SELECT id, {column}, status FROM {table} WHERE id = ?", (ticket_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return enhance_ticket_status(keyword.upper(), row[0], row[1], row[2])
        else:
            return f"No {keyword.upper()} ticket found with ID #{ticket_id}."
    else:
        # Otherwise, search all tables
        for table, column in department_map.values():
            cursor.execute(f"SELECT id, {column}, status FROM {table} WHERE id = ?", (ticket_id,))
            row = cursor.fetchone()
            if row:
                conn.close()
                return enhance_ticket_status(table.split("_")[0].upper(), row[0], row[1], row[2])
        
        conn.close()
        return f"Ticket ID #{ticket_id} not found in any department."

def close_ticket_status(query: str) -> str:
    info = extract_ticket_info_and_intent(query)
    
    if info == "missing" or not isinstance(info, dict):
        return "❌ Could not extract ticket info. Please specify both ID and department."

    try:
        ticket_id = int(info["ticket_id"])
        department = info["department"]
    except Exception as e:
        return f"❌ Error parsing extracted info: {e}"

    department_map = {
        "it": ("it_tickets", "issue"),
        "infra": ("infra_tickets", "issue"),
        "hr": ("hr_tickets", "issue"),
        "finance": ("finance_tickets", "query"),
        "admin": ("admin_tickets", "issue"),
    }

    if department not in department_map:
        return f"❌ Unknown department: {department}"

    table, col = department_map[department]
    conn = sqlite3.connect("db/system.db")
    cursor = conn.cursor()

    # Check current status
    cursor.execute(f"SELECT status FROM {table} WHERE id = ?", (ticket_id,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return f"❌ Ticket #{ticket_id} not found in {department.title()} department."

    current_status = result[0]
    if current_status.lower() == "closed":
        conn.close()
        return f"✅ Ticket #{ticket_id} is already closed."

    # Update status to Closed
    cursor.execute(f"UPDATE {table} SET status = 'Closed' WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()
    return f"✅ Ticket #{ticket_id} in {department.title()} department has been marked as Closed."


def handle_ticket_status(query: str) -> str:
    info = extract_ticket_info_and_intent(query)
    
    if info == "missing" or not isinstance(info, dict):
        return "❌ Could not understand the ticket details. Please include ticket ID and department."

    intent = info.get("intent")
    if not intent:
        return "❌ Could not detect intent ('check' or 'close')."

    if intent == "check":
        return check_ticket_status(query)
    elif intent == "close":
        return close_ticket_status(query)
    else:
        return "❌ Unknown intent. Please specify if you want to 'check' or 'close' a ticket."
