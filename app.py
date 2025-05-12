from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain

from src.helper import load_embedding, repo_ingestion
from dotenv import load_dotenv
from pathlib import Path

import os
import uvicorn

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY



app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Set up templates directory
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


# Vector DB + Embeddings
embeddings = load_embedding()
persist_directory = "db"
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# LLM and memory chain
llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY, temperature=0.5)
memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(
    llm, retriever=vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 8}), memory=memory
)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chatbot")
async def git_repo(question: str = Form(...)):
    repo_ingestion(question)
    os.system("python store_index.py")
    return JSONResponse(content={"response": question})

@app.post("/get")
async def chat(msg: str = Form(...)):
    if msg.strip().lower() == "clear":
        os.system("rm -rf repo")
    result = qa(msg)
    return result["answer"]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
