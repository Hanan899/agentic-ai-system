# Agentic AI System

An intelligent agent-based system built with **LangChain**, **Agents**, **Google Gemini**, and **Streamlit**, powered by a modular architecture.This system detects user intent (e.g., ticket status request, ticket closing, or raising new tickets), routes issues to appropriate domain-specific agents (HR, IT, Finance, Admin, Infra), and logs tickets into a local  **SQLite** database. It also handles general informational queries without logging tickets.

---

## Features


- **Intent Classification**: Automatically determines whether the user is requesting information, checking ticket status, closing a ticket, or raising a new support ticket.
- **Domain-Specific Agents**:
  - **ITAgent**: Software/hardware technical issues.
  - **FinanceAgent**: Salary, reimbursement, or payment-related queries.
  - **HRAgent**: HR issues like leave, complaints, and policies.
  - **InfraAgent**: Wi-Fi, power, or device-related infrastructure problems.
  - **AdminAgent**: General admin or logistics requests.
- **Ticket Status + Closing Support**: Users can check ticket statuses or explicitly close them *(e.g., "Please close ticket 3 from finance")*.
- **SQLite Ticket Logging**: Only ticket-type prompts are stored in the local database, with Open or Closed status.
- **Streamlit Frontend**: Simple UI for chat interaction and database checking.
- **Google Gemini LLM**:Handles user understanding, ticket intent classification, and dynamic prompting using gemini-2.0-flash.

---

## Tech Stack

| Component     | Technology               |
|---------------|---------------------------|
| LLM           | Google Gemini (`gemini-2.0-flash`) |
| Framework     | LangChain Agents          |
| Backend       | Python (LangChain logic) |
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
│   ├── it_agent.py
│   └── ticket_status_agent.py
│
├── db/
│   └── system.db # SQLite database
│
├── frontend/ # Streamlit-based interface
│   ├── app.py 
│   └── check_db.py 
│
├── utils/
│   ├── enhance_status.py
│   ├── llm_instance.py
│   ├── ticket_parser.py
│   └── db_utils.py
│
├── agents_config.json
├── main.py # Entry point for LLM + routing logic
└── requirements.txt

```

---

## Architecture

1. **User** enters a query (e.g., "My laptop is not working")
2. **Intent Extraction** via Gemini + LangChain:
   - `"info"` → answered using LLM knowledge (no ticket)
   - `"ticket"` → new issue created
   - `"status"` → fetch status from DB
   - `"close"` → mark ticket as closed
3. **Sub-agents** respond based on domain:
   - HR: leave, complaints
   - IT: hardware/software
   - Finance: salary, reimbursement
   - Admin: general tasks
   - Infra: power, WiFi, etc.
4. **Ticket Details** extracted: `department`, `ticket_id`, `issue summary`
5. **Agent Routing**: Based on department, ticket is passed to the respective agent
6. **Ticket** is created, closed, or queried via SQLite
7. **Streamlit Frontend** displays interaction and tracks updates

---

## Example Queries

| Query                                     | Intent | Routed To     | Ticket | Action       |
| ----------------------------------------- | ------ | ------------- | ------ | ------------ |
| "I want to apply for medical leave"       | ticket | HR Agent      | ✅      | Create       |
| "What is our holiday policy?"             | info   | —             | ❌      | LLM Reply    |
| "Projector is not working in Room 2"      | ticket | Infra Agent   | ✅      | Create       |
| "When is salary disbursed?"               | info   | —             | ❌      | LLM Reply    |
| "Can't access my email"                   | ticket | IT Agent      | ✅      | Create       |
| "What is the status of ticket 2 from IT?" | status | IT Agent      | ❓      | Fetch Status |
| "Please close ticket 3 from finance"      | close  | Finance Agent | ✅      | Close        |


---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Hanan899/agentic-ai-system.git

cd agentic-ai-system
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

 - Add more detailed sub-intents (`leave_balance`, `salary_issue`, `hardware_fix`)

 - Integrate email or Slack notifications for tickets

 - Add user authentication (`basic login`)

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
