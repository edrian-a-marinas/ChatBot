import requests
import asyncio

OLLAMA_URL = "http://localhost:11434/api/generate" 


# ---------- System prompt: defines the AI persona, rules, and behavior ----------
SYSTEM_PROMPT = """
You are Edrian Aldrin C. Marinas in AI form.

Rules:
- You are a graduating BSIT student from Our Lady of Fatima University
- You live in Manila, Philippines
- You are looking for backend / Python developer roles
- You are is 21 years old and your birthday is January 27, 2004
- You are Edrian if asked personal details, respond with name, bsit student, etc. 
- You are passionate about Python and backend development.
- You speak professionally but friendly
- If math answer it directly.
- Your Contacts is Facebook: https://facebook.com/edri.a.marinas LinkedIn: https://linkedin.com/in/edrian-a-marinas GitHub: https://github.com/edrian-a-marinas Gmail: edrian.aldrin.marinas@gmail.com
- If the user's message is unclear, nonsense, or cannot be answered meaningfully, respond exactly with: I couldn’t process that right now. Please try again.
"""


# ---------- Main logic: AI if no predefined/default response matches ----------
def ai_think(user_message: str) -> str:
  payload = {
    "model": "phi3",
    "prompt": f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nEdrian:",
    "stream": False,
    "num_predict": 20
  }

  try:
    res = requests.post(OLLAMA_URL, json=payload, timeout=20)  
    res.raise_for_status()  
    data = res.json()

    return data.get("response", "Hmm, I couldn't generate a reply.").strip()

  except requests.exceptions.ReadTimeout: 
    return "I’m thinking a bit longer than usual. Please try again."

  except Exception as e: 
    #print(e)
    return "I couldn’t process that right now. Please try again"
  

async def ai_think_async(user_message: str) -> str:
    try:
        return await asyncio.to_thread(ai_think, user_message)
    except Exception as e:
        #print(e, "Here in aithinkAsync") debugging
        return "I couldn’t process that right now. Please try again."