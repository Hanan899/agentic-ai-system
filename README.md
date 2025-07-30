
markdown
Copy
Edit
# 🤖 Agentic AI System

An intelligent agent-based ticket classification and routing system built with **LangChain**, **Google Gemini**, and **Streamlit**, powered by a modular architecture. This app detects user intent (e.g., ticket request vs. general info), routes issues to appropriate domain-specific agents (HR, IT, Finance, Admin, Infra), and logs tickets into a local **SQLite** database.

---

## 🧠 Features

- ✅ Intent classification: "ticket" or "info"
- 🧭 Dynamic sub-agent routing (HR, IT, Finance, etc.)
- 🗃️ SQLite-based persistent ticket storage
- 🌐 Powered by Google Gemini LLM (via LangChain)
- 📊 Admin dashboard to view and filter all tickets
- 🖼️ Streamlit UI for interaction and testing

---

## 🏗️ Architecture

- 📝 User prompt → Intent classification
- 🔁 "ticket" → Routed to correct department agent
- 📦 Ticket stored in SQLite with metadata
- 🔍 "info" → Answered using LLM without logging
- 🔧 Modular agents (HR, IT, Finance, etc.) handle routing logic
- 📋 Streamlit dashboard for monitoring + testing DB

---

## 📁 Project Structure

Agentic-AI-System/
│
├── agents/ # Sub-agents by domain
│ ├── admin_agent.py
│ ├── finance_agent.py
│ ├── hr_agent.py
│ ├── infra_agent.py
│ └── it_agent.py
│
├── db/
│ └── system.db # SQLite database
│
├── frontend/ # Streamlit-based interface
│ ├── app.py # Main UI with intent classification
│ └── check_db.py # View saved ticket records
│
├── utils/
│ └── db_utils.py # DB connection, ticket saving/query logic
│
├── main.py # Entry point for LLM + routing logic
├── requirements.txt
├── .gitignore
└── README.md # You're reading it!

yaml
Copy
Edit

---

## 🚀 How It Works

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

## 🧪 Example Queries

| Query                                 | Intent   | Routed To     | Ticket |
|--------------------------------------|----------|----------------|--------|
| "I want to apply for medical leave"  | ticket   | HR Agent       | ✅     |
| "What is our holiday policy?"        | info     | —              | ❌     |
| "Projector is not working in Room 2" | ticket   | Infra Agent    | ✅     |
| "When is salary disbursed?"          | info     | —              | ❌     |
| "Can't access my email"              | ticket   | IT Agent       | ✅     |

---

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Agentic-AI-System.git
cd Agentic-AI-System
2. Create a virtual environment
bash
Copy
Edit
python -m venv .venv
# Activate it:
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set your Gemini API key (via .env or direct)
bash
Copy
Edit
export GOOGLE_API_KEY=your_gemini_api_key
5. Run the main interface
bash
Copy
Edit
streamlit run frontend/app.py
Or view stored tickets:

bash
Copy
Edit
streamlit run frontend/check_db.py
📦 Key Dependencies
langchain

google-generativeai (Gemini)

streamlit

sqlite3

python-dotenv (optional)

🛠️ Future Enhancements
 Add more detailed sub-intents (e.g., HR → Leave, Complaint, Onboarding)

 Integrate email or Slack notifications for tickets

 Add authentication layer

 Dashboard with filters and charts

 Support for voice input using speech_recognition

📄 License
This project is released under the MIT License.

👨‍💻 Author
Abdul Hanan
AI Intern @ Hazen Technologies
📧 a.hananwork4@gmail.com
🔗 LinkedIn

🤝 Contributions
Pull requests and forks are welcome!
If you’d like to extend this with:

🧠 More advanced agents

📊 Analytics dashboard

🐳 Docker deployment
Just fork it and submit a PR.

javascript
Copy
Edit

Would you like me to generate this `README.md` file and `.gitignore`, `requirements.txt` and zip them for you?








Ask ChatGPT
