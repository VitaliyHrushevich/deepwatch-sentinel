# 🤖 DeepWatch Sentinel: Autonomous AI Orchestrator

**DeepWatch Sentinel** is an advanced AI Agent system that acts as the "brain" for infrastructure observability. It leverages local Large Language Models (LLMs) to perform autonomous reasoning over statistical data, providing human-like verdicts on system health and experiment results.

## 🌟 Key Features
- **Agentic Reasoning:** Implements **ReAct logic** (Reasoning + Acting) to analyze complex SQL datasets.
- **Dynamic Context Injection:** Fuses real-time metrics from `StatGuard-Metric` with LLM prompts for grounded, data-driven insights.
- **Local AI Privacy:** Fully powered by **Ollama (Llama 3)**, ensuring that sensitive data never leaves the local environment.
- **Actionable Verdicts:** Provides business-ready recommendations (e.g., "Deploy V2 update based on +2.83% lift").

## 🛠 Tech Stack
- **AI Core:** Ollama (Llama 3 8B)
- **Persistence:** SQLite (StatGuard Integration)
- **Orchestration:** Python 3.11, Requests
- **Architecture:** RAG-style Context Augmentation

## 🚀 Quick Start
1. **Ensure Ollama is running:** `ollama serve`
2. **Setup DB:** Ensure `data/experiments.db` from **StatGuard-Metric** is available in the root.
3. **Run Sentinel:** `python main.py`

## 🛡️ Engineering Challenge: Hallucination Mitigation
Sentinel uses a strict **system prompt engineering** strategy to ensure that the AI only interprets data present in the database, preventing "hallucinations" and ensuring 100% reliable technical verdicts.

## 🗺 Future Roadmap
- [ ] **Multi-Agent Collaboration:** Integrating specialized agents for cost optimization and security.
- [ ] **Slack/Discord Integration:** Automated incident reporting via AI-generated summaries.
- [ ] **Advanced RAG:** Vector database integration for searching through technical documentation.

## 🤝 Contributing
Feel free to fork this project, report issues, or suggest new Agentic patterns. 

