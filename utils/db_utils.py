import sqlite3
import re

def init_db():
    conn = sqlite3.connect("db/system.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS infra_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hr_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS it_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS finance_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def insert_infra_ticket(issue: str) -> str:
    return _insert_ticket("infra_tickets", "issue", issue)

def insert_it_ticket(issue: str) -> str:
    return _insert_ticket("it_tickets", "issue", issue)

def insert_finance_ticket(query: str) -> str:
    return _insert_ticket("finance_tickets", "query", query)

def insert_hr_ticket(issue: str) -> str:
    return _insert_ticket("hr_tickets", "issue", issue)

def insert_admin_ticket(issue: str) -> str:
    return _insert_ticket("admin_tickets", "issue", issue)

def _insert_ticket(table, column, value):
    conn = sqlite3.connect("db/system.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} ({column}) VALUES (?)", (value,))
    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()
    print(f"🐛 Inserted into {table} with ID {ticket_id} and value '{value}'")
    return f"{table.replace('_', ' ').title()} ticket #{ticket_id} created for: '{value}'"

def fetch_all_tickets():
    conn = sqlite3.connect("db/system.db")
    cursor = conn.cursor()

    tables = {
        "Infra ": ("infra_tickets", "issue"),
        "IT ": ("it_tickets", "issue"),
        "HR ": ("hr_tickets", "issue"),
        "Finance ": ("finance_tickets", "query"),
        "Admin ": ("admin_tickets", "issue")
    }

    all_data = {}
    for label, (table, col) in tables.items():
        cursor.execute(f"SELECT id, {col}, status, created_at FROM {table}")
        all_data[label] = cursor.fetchall()

    conn.close()
    print("🐛 Fetched all ticket data from all tables.")
    return all_data

def check_ticket_status(ticket_id: int, table_name: str) -> str:
    conn = sqlite3.connect("db/system.db")
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT status FROM {table_name} WHERE id=?", (ticket_id,))
        result = cursor.fetchone()
        if result:
            return f"The status of your ticket #{ticket_id} in {table_name.replace('_tickets', '').upper()} is: {result[0]}"
        else:
            return f"No ticket found with ID {ticket_id} in {table_name.replace('_tickets', '').upper()} department."
    except Exception as e:
        return f"Error checking ticket status: {str(e)}"
    finally:
        conn.close()
