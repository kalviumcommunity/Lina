# 📌 Lina – AI Agent for Automated LinkedIn Posting

## 🚀 Overview

**Lina** is an AI-powered agent that automates LinkedIn posting.
It supports:

* **Prompting** → Dynamic prompt design for generating content.
* **RAG (Retrieval-Augmented Generation)** → Enhances posts with context from your knowledge base.
* **Structured Output** → Ensures AI-generated posts follow LinkedIn formatting guidelines.
* **Function Calling** → Handles scheduling, post creation, and publishing automatically.

The project follows a **frontend + backend architecture** for modularity and scalability.


## 🏗️ Project Structure

```
Lina/
│── frontend/                  # React (or Next.js) app for UI
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── pages/             # Pages (Dashboard, Scheduler, Post Creator)
│   │   ├── services/          # API calls to backend
│   │   ├── styles/            # Tailwind / CSS files
│   │   └── App.js             # Main entry
│   ├── package.json           # Frontend dependencies
│
│── backend/                   # Flask (Python) backend
│   ├── app/                   
│   │   ├── api/               # API routes (auth, posts, scheduling)
│   │   ├── services/          # AI services (Prompting, RAG, etc.)
│   │   ├── utils/             # Helper functions (LinkedIn API integration)
│   │   ├── models/            # Database models (User, Posts, Schedule)
│   │   └── __init__.py
│   ├── tests/                 # Unit & integration tests
│   ├── requirements.txt       # Backend dependencies
│   └── wsgi.py                # Entry point
│
│── docs/                      # Documentation
│── .gitignore
│── README.md
```



## ⚡ Tech Stack

### Frontend

* **React.js** or **Next.js** → UI
* **TailwindCSS** → Styling
* **Axios/Fetch** → API calls
* **React Query / Zustand / Redux** → State management

### Backend

* **Flask (Python)** → REST API
* **LangChain / LlamaIndex** → RAG, Prompting, Structured Output
* **PostgreSQL / MongoDB** → Database for scheduling & posts
* **Celery + Redis** → Task queue for scheduled posts
* **LinkedIn API** → Post publishing



## 🔑 Features

✅ AI-generated LinkedIn posts with proper structure
✅ Schedule posts at specific times
✅ Store drafts and history of posts
✅ Integration with LinkedIn API for publishing
✅ Knowledge base support via RAG
✅ Modular architecture (easy to extend for Twitter, Instagram later)



## ⚙️ Installation

### Clone the repo

```bash
git clone https://github.com/kalviumcommunity/Lina.git
cd Lina
```

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
flask run
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev   # For React / Next.js
```


## 📌 Usage

1. Start backend → Flask will serve API at `http://127.0.0.1:5000/`
2. Start frontend → Visit `http://localhost:3000/`
3. Login with LinkedIn
4. Generate post using AI
5. Schedule or publish instantly



## 🎯 Roadmap

* [ ] MVP: Generate & publish LinkedIn posts
* [ ] Add RAG with custom knowledge sources
* [ ] Scheduling system with Celery & Redis
* [ ] Support for multiple platforms (Twitter, IG, etc.)
* [ ] Analytics dashboard for engagement



## 🤝 Contributing

1. Fork the repo
2. Create a feature branch → `git checkout -b feature-name`
3. Commit changes → `git commit -m "Add new feature"`
4. Push → `git push origin feature-name`
5. Open a Pull Request

