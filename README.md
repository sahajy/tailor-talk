# 🧵 TailorTalk - AI Calendar Booking Assistant

TailorTalk is an AI-powered conversational assistant that helps users seamlessly book appointments using natural language. It integrates **LangGraph**, **FastAPI**, and **Google Calendar API**, and offers a clean interface via **Streamlit**.

---

## 🚀 Features

- 🤖 Conversational agent built using LangGraph & Langchain
- 📅 Real-time appointment creation on Google Calendar
- 🔐 Secure handling of service account credentials
- 🧠 LLM-backed dynamic response generation
- 🖥️ Streamlit frontend for smooth interaction
- ⚡ FastAPI backend for scalable deployment

---

## 🗂️ Project Structure

```

tailor-talk/
├── backend/
│   ├── **init**.py
│   ├── main.py              # FastAPI entry point
│   ├── agent.py             # LangGraph / agent logic
│   ├── gcal\_utils.py        # Google Calendar API helpers
│   ├── gcal\_setup.py        # Credential setup
├── frontend/
│   └── app.py               # Streamlit frontend UI
├── requirements.txt
└── .gitignore

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sahajy/tailor-talk.git
cd tailor-talk
````

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔐 Google Calendar API Setup

### 1. Enable Google Calendar API

* Go to [Google Cloud Console](https://console.cloud.google.com/)
* Enable the **Google Calendar API**
* Create a **Service Account**
* Download the JSON credentials file

### 2. Securely Add Service Account Credentials

* Don't commit the `service_account.json` file!
* On **Render**, add it as a **Secret File** with this name:

```
service_account.json
```

* Your code should load it like this:

```python
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file("/etc/secrets/service_account.json")
```

---

## ▶️ Running the App

### 1. Run FastAPI Backend

```bash
cd backend
uvicorn main:app --reload
```

### 2. Run Streamlit Frontend

```bash
cd ../frontend
streamlit run app.py
```

---

## ☁️ Deployment on Render

### Backend (FastAPI)

* Use Render Web Service
* Build Command: `pip install -r requirements.txt`
* Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port 8000`
* Python version: 3.11+

### Frontend (Streamlit)

* Use Render Web Service (or static site)
* Start Command: `streamlit run frontend/app.py --server.port 10000`

---

## 🧠 Technologies Used

* [LangGraph](https://www.langchain.com/langgraph) + Langchain
* [FastAPI](https://fastapi.tiangolo.com/)
* [Google Calendar API](https://developers.google.com/calendar)
* [Streamlit](https://streamlit.io/)
* [OpenAI or Together AI LLMs](https://platform.openai.com/)

---

## 🙋‍♂️ Author

**Sahaj Yadav**

* ✉️ [LinkedIn](https://www.linkedin.com/in/sahajyadav/)
* 💻 [GitHub](https://github.com/sahajy)

---
