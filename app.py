from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from models import ChatRequest
from agent import stream_response

app = FastAPI()

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "message": "AI Agent Running"
    }

@app.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(
        stream_response(request.prompt),
        media_type="text/plain"
    )