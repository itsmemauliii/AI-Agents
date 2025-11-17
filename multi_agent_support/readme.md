# 💬 Multi-Agent Customer Support System

A **local, fully offline multi-agent AI support system** built with **LangGraph + Ollama**, wrapped in a **Streamlit chat interface**.  
Users can type queries, and messages are dynamically routed to specialized agents:

- **Billing Agent** 💳  
- **Technical Support Agent** 🛠️  
- **General Agent** ☀️  

This is ideal for testing AI customer support locally or creating a deployable MVP.

---

## Features

- Fully local and offline, no cloud required.
- Multi-agent system with conditional routing.
- Clean, interactive chat UI via Streamlit.
- Persistent session chat history.
- Lightweight, no subscription needed.

---

## Requirements

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [LangGraph](https://pypi.org/project/langgraph/)
- [LangChain Ollama](https://pypi.org/project/langchain-ollama/)
- Ollama local LLM installed (e.g., Llama3)

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/itsmemauliii/AI-Agents.git
cd multi_agent_support
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Ensure Ollama is installed and working locally:

```bash
ollama --version
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run multi_agent.py
```

* Type your message in the input box.
* Click **Send**.
* The system will route your message to the appropriate agent and display the response.
* Chat history is maintained during the session.

---

## Folder Structure

```
multi_agent_support/
│
├─ multi_agent.py      # Streamlit chat app
├─ requirements.txt           # Dependencies
└─ README.md                  # Project overview
```

---

## Notes

* Currently designed for **local testing**.
* LLM responses are generated using your local Ollama model (Llama3).
* Can be extended to add more specialized agents or personality-based replies.

---

## License

This project is private. All rights reserved by the creator.

---
