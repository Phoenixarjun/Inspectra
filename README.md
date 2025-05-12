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




AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 339712989651.dkr.ecr.ap-south-1.amazonaws.com/inspectra
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
GOOGLE_API_KEY