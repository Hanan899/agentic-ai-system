# Agentic AI System

An intelligent agent-based system built with **LangChain**, **Agents**, **Google Gemini**, and **Streamlit**, powered by a modular architecture. This system detects user intent (e.g., ticket request vs. general info), routes issues to appropriate domain-specific agents (HR, IT, Finance, Admin, Infra), and logs tickets into a local **SQLite** database. It also handles general informational queries without logging tickets.

---

## Features


- **Intent Classification**: Automatically determines whether the user is requesting information or raising a support ticket.
- **Domain-Specific Agents**:
  - **ITAgent**: Software/hardware technical issues.
  - **FinanceAgent**: Salary, reimbursement, or payment-related queries.
  - **HRAgent**: HR issues like leave, complaints, and policies.
  - **InfraAgent**: Wi-Fi, power, or device-related infrastructure problems.
  - **AdminAgent**: General admin or logistics requests.
- **SQLite Ticket Logging**: Only ticket-type prompts are stored in the local database.
- **Streamlit Frontend**: Simple UI for chat interaction and database checking.
- **Google Gemini LLM**: Handles understanding and routing of queries using `gemini-2.0-flash`.

---

## Tech Stack

| Component     | Technology               |
|---------------|---------------------------|
| LLM           | Google Gemini (`gemini-2.0-flash`) |
| Framework     | LangChain Agents          |
| Backend       | Python (FastAPI-style logic) |
| Frontend      | Streamlit                 |
| Database      | SQLite (via `sqlite3`)    |

---


## Project Structure

```text
Agentic-AI-System/
│
├── agents/ # Sub-agents by domain
│   ├── admin_agent.py
│   ├── finance_agent.py
│   ├── hr_agent.py
│   ├── infra_agent.py
│   └── it_agent.py
│
├── db/
│   └── system.db # SQLite database
│
├── frontend/ # Streamlit-based interface
│   ├── app.py # Main UI with intent classification
│   └── check_db.py # View saved ticket records
│
├── utils/
│   └── db_utils.py # DB connection, ticket saving/query logic
│
├── main.py # Entry point for LLM + routing logic
└── requirements.txt

```

---

## Architecture

1. **User** enters a query (e.g., "My laptop is not working")
2. **LLM** classifies the intent as either:
   - `"ticket"` → routed to correct sub-agent
   - `"info"` → answered using LLM knowledge
3. **Sub-agents** respond based on domain:
   - HR: leave, complaints
   - IT: hardware/software
   - Finance: salary, reimbursement
   - Admin: general tasks
   - Infra: power, WiFi, etc.
4. **Ticket data** saved to local `system.db` with timestamp, status, etc.
5. **Admins** view tickets from the Streamlit dashboard (`check_db.py`)

---

## Example Queries

| Query                                 | Intent   | Routed To     | Ticket |
|--------------------------------------|----------|----------------|--------|
| "I want to apply for medical leave"  | ticket   | HR Agent       | ✅     |
| "What is our holiday policy?"        | info     | —              | ❌     |
| "Projector is not working in Room 2" | ticket   | Infra Agent    | ✅     |
| "When is salary disbursed?"          | info     | —              | ❌     |
| "Can't access my email"              | ticket   | IT Agent       | ✅     |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Agentic-AI-System.git
cd Agentic-AI-System
```
### 2. Create a virtual environment & install dependencie

```bash
python -m venv .venv
source .venv/bin/activate     # For Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set your Gemini API key (via .env or direct)

```bash
export GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the main interface

```bash
streamlit run frontend/app.py
```

### Or view stored tickets:

```bash
streamlit run frontend/check_db.py
```

### Key Dependencies

 - **langchain**

- **google-generativeai (Gemini)**

- **streamlit**

- **sqlite3**

- **python-dotenv (optional)**

### Future Enhancements

 - Add more detailed sub-intents (e.g., HR → Leave, Complaint, Onboarding)

 - Integrate email or Slack notifications for tickets

 - Add authentication layer

 - Dashboard with filters and charts

 - Support for voice input using speech_recognition

---

### Author
Abdul Hanan  
AI Intern @ Hazen Technologies  
LinkedIn: [LinkedIn](https://www.linkedin.com/in/abdul-hanan-2003-)  
Gmail: a.hananwork4@gmail.com

---

### Contributions
Pull requests and forks are welcome!
If you’d like to extend this with:

- More advanced agents

- Analytics dashboard

- Docker deployment
  
Just fork it and submit a PR.
