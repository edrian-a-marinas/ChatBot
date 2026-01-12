from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import Chatbot  

app = FastAPI()
chatbot = Chatbot()


# ---------- Allow the frontend server to send requests to this API ----------
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://127.0.0.1:5500"],  
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class ChatRequest(BaseModel):
  message: str

class ChatResponse(BaseModel):
  reply: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):  # this is like request = ChatRequest indirect way for pydantic
  response_text = await chatbot.get_response(request.message) 
  return {"reply": response_text} 

@app.get("/health")
def health():
  return {"status": "ok"}
