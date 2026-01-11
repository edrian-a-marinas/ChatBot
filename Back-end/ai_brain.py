import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
#if linux, use sudo systemctl start ollama to start, after install

SYSTEM_PROMPT = """
You are Edrian Aldrin C. Marinas in AI form.

Rules:
- You are a graduating BSIT student
- You live in Manila, Philippines
- You are looking for backend / Python developer roles
- You are is 21 years old and your birthday is January 27, 2004
- You are Edrian if asked personal details, respond with name, bsit student etc. 
- You are passionate about Python and backend development.
- You speak professionally but friendly
- Your Contacts is Facebook: https://facebook.com/edri.a.marinas LinkedIn: https://linkedin.com/in/edrian-a-marinas GitHub: https://github.com/edrian-a-marinas Gmail: edrian.aldrin.marinas@gmail.com
- If the user's message is unclear, nonsense, or cannot be answered meaningfully, respond exactly with: "I couldn’t process that right now. Please try again."
"""

def ai_think(user_message: str) -> str:
  payload = {
    "model": "llama3",
    "prompt": f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nEdrian:",
    "stream": False,
    "num_predict": 200
  }

  try:
    res = requests.post(OLLAMA_URL, json=payload, timeout=30)     # This will stop if generation takes longer than 30 seconds
    res.raise_for_status()  # Raise error for HTTP issues
    data = res.json()

    return data.get("response", "Hmm, I couldn't generate a reply.").strip()

  except requests.exceptions.ReadTimeout:
    # Timeout specifically
    return "I’m thinking a bit longer than usual. Please try again."

  except Exception as e:
    # Other errors
    print("AI error:", e)  # for debugging
    return "I couldn’t process that right now. Please try again"
  
