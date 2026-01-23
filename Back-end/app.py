from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import Chatbot  

app = FastAPI()
chatbot = Chatbot()


# ---------- Allow the frontend server to send requests to this API ----------
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://127.0.0.1:5000"],  
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class MessageCreate(BaseModel):
  content: str

class MessageResponse(BaseModel):
  reply: str


@app.post(
  "/api/v1/messages",
  response_model=MessageResponse,
  status_code=status.HTTP_201_CREATED
)
async def create_message(message: MessageCreate):
  reply = await chatbot.get_response(message.content)
  return MessageResponse(reply=str(reply))

@app.get("/api/v1/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "ok"}
