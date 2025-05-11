# 🧠 Inspectra – AI-Powered GitHub Repo Insight Tool

Inspectra is an AI-native web application that ingests a GitHub repository and enables intelligent Q\&A over its codebase using Google's Gemini model, LangChain, ChromaDB, and FastAPI. Just paste a repo link, and Inspectra transforms it into an interactive, searchable knowledge source.

![image](https://github.com/user-attachments/assets/7044bfbd-b85a-4f5b-bed3-eb05f862baca)


---

## 🚀 Features

* 🔗 **GitHub Repo Ingestion** – Extract and embed code from any public repo.
* 💬 **Natural Language Chat** – Ask high-level or low-level questions about the repo.
* 🧠 **Memory-Backed Conversations** – Contextual follow-up questions supported.
* ⚡ **Gemini + LangChain** – Smart responses powered by state-of-the-art LLMs.
* 🗂️ **ChromaDB Vector Store** – Persistent semantic search across repo files.
* 🎯 **Optimized Search** – MMR-based retrieval for diverse and relevant context.

---

## 🛠️ Tech Stack

| Layer      | Technology                                  |
| ---------- | ------------------------------------------- |
| Framework  | FastAPI, Jinja2                             |
| LLM        | Gemini 1.5 Pro via `langchain_google_genai` |
| Embeddings | Google Embeddings                           |
| Vector DB  | ChromaDB (LangChain 0.2+ compatible)        |
| Memory     | ConversationSummaryMemory                   |
| Frontend   | HTML, CSS, JavaScript                       |
| Deployment | Uvicorn with live reload                    |

---

## 📦 Installation

```bash
git clone https://github.com/Phoenixarjun/Inspectra
cd Inspectra
pip install -r requirements.txt
```

> ⚠️ Ensure you have a `.env` file with your Google API Key:

```
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the App

```bash
uvicorn app:app --reload
```

Navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Usage

1. Paste a public GitHub repository URL into the form.
2. Submit to trigger ingestion and vector embedding.
3. Ask natural language questions like:

   * “What is the repo about?”
   * “Explain the SpamFilter class.”
   * “How is error handling done?”
4. Type `clear` to reset context.

---

---

## 🧠 How It Works

* Downloads code from GitHub.
* Splits source files using LangChain's text splitter.
* Embeds chunks with Google’s embedding model.
* Stores vectors in ChromaDB.
* On user query, retrieves relevant chunks via MMR.
* Feeds results to Gemini with memory-enabled Q\&A chain.

---

## 🛡️ License

This project is open-sourced under the [MIT License](LICENSE).

---

## ✍️ Created By

**Naresh B A** – Reimagining developer experiences with AI.
*Connect with me on [LinkedIn]((www.linkedin.com/in/naresh-b-a-1b5331243)) or explore more on [GitHub]((https://github.com/Phoenixarjun)).*


