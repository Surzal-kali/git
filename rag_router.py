import os 
import json
import chromadb
import ollama
import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict, Any

app = FastAPI()

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
                    response = ollama.chat(message["content"])
                    yield format_sse(json.dumps({"message": response}))
            return StreamingResponse(event_generator(), media_type="text/event-stream")
        else:
            responses = []
            for message in request.messages:
                response = ollama.chat(message["content"])
                responses.append(response)
            return {"responses": responses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

response = requests.post("http://100.67.21.37:8000/chat", json={
    "messages": [
        {"content": "Hello, how are you?"},
        {"content": "What is the weather like today?"}
    ],
    "stream": True
})
for line in response.iter_lines():
    if line:
        print(line.decode("utf-8"))

def get_chroma_client():
    return chromadb.Client()

def create_collection(client, name):
    return client.create_collection(name)

def add_documents(collection, documents):
    collection.add(documents)

def query_collection(collection, query):
    return collection.query(query)

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)

# Example usage
if __name__ == "__main__":
    client = get_chroma_client()
    collection = create_collection(client, "my_collection")
    documents = ["This is a sample document.", "Another document goes here."]
    add_documents(collection, documents)
    results = query_collection(collection, {"query": "sample"})
    print(results)