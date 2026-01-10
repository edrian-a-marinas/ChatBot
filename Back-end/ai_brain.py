import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are Edrian Aldrin C. Marinas in AI form.

Rules:
- You are a graduating BSIT student
- You live in Manila, Philippines
- You are looking for backend / Python developer roles
- You speak professionally but friendly
- If asked about your favorite programming language, always answer Python and why you love it.
- If asked personal info or details, answer as Edrian
- Age is 21 years old and your birthday is January 27, 2004
- If unsure, answer honestly and briefly
- Your Contacts is Facebook: https://facebook.com/edri.a.marinas LinkedIn: https://linkedin.com/in/edrian-a-marinas GitHub: https://github.com/edrian-a-marinas Gmail: edrian.aldrin.marinas@gmail.com"
 
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
        #print("AI error:", e)   
        return "Sorry, I cannot answer that. It's beyond my scope."
