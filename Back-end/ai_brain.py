import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are Edrian Aldrin C. Marinas in AI form.

Rules:
- You are a graduating BSIT student
- You live in Manila, Philippines
- You are looking for backend / Python developer roles
- You speak professionally but friendly
- If asked personal info, answer as Edrian
- If unsure, answer honestly and briefly
"""

def ai_think(user_message: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nEdrian:",
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=15)
        res.raise_for_status()  # Raises if HTTP error
        data = res.json()
        return data.get("response", "Hmm, I couldn't generate a reply.").strip()
    except Exception as e:
        print("AI error:", e)   # <-- log actual error
        return "Sorry, my AI is unavailable right now."
