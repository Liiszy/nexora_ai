# Nexora AI

**A local AI assistant built with Python, Ollama, and SQLite.**

Nexora AI is a personal AI assistant project designed to explore the development of intelligent applications using Large Language Models (LLMs), local AI inference, and persistent data storage.

The project integrates a locally running language model with a Python application, allowing users to interact with the assistant through a conversational interface.

## Features

- **AI-powered conversations:** Generates responses using a locally hosted language model through Ollama.
- **Conversation history:** Stores previous interactions using SQLite.
- **Persistent memory:** Saves user information, such as their name, and retrieves it across sessions.
- **Local execution:** Runs the AI model locally instead of relying on a cloud-based AI API.

## Technologies

- Python
- Ollama
- Qwen 2.5 (3B)
- SQLite
- Requests
- Git & GitHub

## Project Structure

```text
nexora-ai/
├── data/
├── src/
│   ├── database/
│   ├── modules/
│   └── main.py
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.12+
- Ollama
- Git

### Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd nexora-ai
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install requests
```

5. Download the model:

```bash
ollama pull qwen2.5:3b
```

6. Run the application:

```bash
python src/main.py
```

Make sure Ollama is running before starting the application.

## Development Goals

Nexora AI is an ongoing learning and development project. Planned improvements include:

- More flexible memory management.
- Improved conversation context.
- Integration with external APIs and tools.
- Retrieval-Augmented Generation (RAG).
- Semantic search using embeddings.
- Automated tests and improved documentation.

## Author

Developed as a personal project to study Artificial Intelligence, Python development, and LLM-based applications.
