from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import Chatbot  

app = FastAPI()
chatbot = Chatbot()


# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000"],  # frontend server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):  # this is like request = ChatRequest indirect way
    response_text = chatbot.get_response(request.message) # calling the function in chatboy.py
    return {"reply": response_text} 

@app.get("/health")
def health():
    return {"status": "ok"}
