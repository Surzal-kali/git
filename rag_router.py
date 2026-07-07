import json
from typing import List, Dict, Any

import chromadb
import ollama
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel


app = FastAPI()

# Open WebUI API endpoint (adjust host/port as needed)
OPENWEBUI_API_URL = "http://localhost:3000/api/chat"


class ChatRequest(BaseModel):
    messages: List[Dict[str, Any]]
    stream: bool = False


def format_sse(data: str) -> str:
    return f"data: {data}\n\n"


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        if request.stream:
            def event_generator():
                for message in request.messages:
                    resp = requests.post(
                        OPENWEBUI_API_URL,
                        json={
                            "model": "dexter:latest",
                            "messages": [{"role": "user", "content": message["content"]}],
                            "stream": True,
                        },
                        stream=True,
                    )
                    for line in resp.iter_lines():
                        if line:
                            yield format_sse(line.decode("utf-8"))
            return StreamingResponse(event_generator(), media_type="text/event-stream")
        else:
            responses = []
            for message in request.messages:
                resp = requests.post(
                    OPENWEBUI_API_URL,
                    json={
                        "model": "dexter:latest",
                        "messages": [{"role": "user", "content": message["content"]}],
                        "stream": False,
                    },
                )
                responses.append(resp.json())
            return {"responses": responses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_chroma_client():
    return chromadb.EphemeralClient()


def create_collection(client: chromadb.Client, name: str):
    return client.create_collection(name)


def add_documents(collection, documents: List[str]):
    ids = [str(i) for i in range(len(documents))]
    collection.add(documents=documents, ids=ids)


def query_collection(collection, query: str):
    return collection.query(query_texts=[query])


def split_text(text: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)


if __name__ == "__main__":
    # ChromaDB example
    client = get_chroma_client()
    collection = create_collection(client, "my_collection")
    documents = ["This is a sample document.", "Another document goes here."]
    add_documents(collection, documents)
    results = query_collection(collection, "sample")
    print(results)

    # HTTP test client (uncomment to run manually):
    # import requests
    # response = requests.post(
    #     "http://127.0.0.1:8000/chat",
    #     json={
    #         "messages": [
    #             {"content": "Hello, how are you?"},
    #         ],
    #         "stream": True,
    #     },
    # )
    # for line in response.iter_lines():
    #     if line:
    #         print(line.decode("utf-8"))

    # HTTP test client with OpenWebUI
    # import requests
    # response = requests.post(
    #     "http://your-openwebui-host/api/chat",
    #     json={
    #         "model": "dexter:latest",
    #         "messages": [{"role": "user", "content": message["content"]}],
    #         "stream": True,
    #     },
    # )
    # for line in response.iter_lines():
    #     if line:
    #         print(line.decode("utf-8"))
