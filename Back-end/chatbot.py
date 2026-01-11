import random
import requests
from datetime import datetime
from ai_brain import ai_think


class Chatbot:
  def __init__(self):
    self.default_responses = {
      "introduce yourself": self.introduce,
      "your name": self.fullName,
      "nickname": lambda: "Call me Ian for short",
      "degree": lambda: "I'm currently holding a BS in Information Technology from Our Lady of Fatima.",

      "hello": self.random_greeting,
      "hi": self.random_greeting,
      "how are you": self.random_status,
      "thank you": lambda: "No problem! Let me know if you need anything else.",

      "age": lambda: f"I'm {self.age()}",
      "when is your birthday": lambda: "January 27, 2004",
      "where do you live": self.whereLive,
      "hobbies": lambda: "I enjoy coding and listening to music.",
      "skills": lambda: "Python, JavaScript, SQL, and HTML/CSS.",
      "gender": lambda: "Male",

      "favorite movie": lambda: "My favorite movie is Knives Out.",
      "favorite show": lambda: "My favorite show is Breaking Bad.",
      "favorite anime": lambda: "One Piece is my favorite anime.",
      "favorite language": lambda: "My favorite programming language is Python.",
      

      "status": self.jobHunt,
      "do you job": self.jobHunt,
      "employed": self.jobHunt,

      "social": self.my_contacts,

      "date today": self.date_today,
      "tell me a joke": self.get_joke,
    }


  # ---------- Identity ----------
  def introduce(self):
    return f"I'm {self.fullName()}, {self.age()} {self.whereLive()} {self.jobHunt()}"
  
  def age(self):
    return "21 years old."

  def fullName(self):
    return "Edrian Aldrin C. Marinas"

  def whereLive(self):
    return "I live in Manila, Philippines."

  def jobHunt(self):
    return "I'm currently looking for backend or Python developer roles."

  def my_contacts(self):
    return (
      "Facebook: https://facebook.com/edri.a.marinas\n"
      "LinkedIn: https://linkedin.com/in/edrian-a-marinas\n"
      "GitHub: https://github.com/edrian-a-marinas\n"
      "Gmail: edrian.aldrin.marinas@gmail.com"
    )
  

  # ---------- Random greetings and status ----------
  def random_status(self):
    return random.choice([
      "I’m doing great—thanks for asking! What would you like to know about Edrian?",
      "All systems running smoothly 😄 What can I help you with?",
      "Doing well! How can I assist you today?"
    ])
  
  def random_greeting(self):
    return random.choice([
      "Hello! I’m Edrian’s bot 🤖 What would you like to know about him?",
      "Hi there! 👋 I’m Edrian’s bot. Ask me anything about him!",
      "Yoo! I can tell you jokes, answer math and todays date, aside from Edrian's details!",
      "Hey! I’m Edrian’s AI assistant. How can I help you today?"
    ])


  # ----------  Quick utility response ----------
  def date_today(self):
    now = datetime.now()
    return now.strftime("Today is %B %d, %Y")

  def get_joke(self):
    try:
      res = requests.get(
        "https://official-joke-api.appspot.com/jokes/random",
        timeout=5
      )
      data = res.json()
      return f"{data['setup']} — {data['punchline']}"
    except Exception:
      return "I couldn't fetch a joke right now."


  # ---------- Utilities / Helper functions ----------
  def compare_two_strings(self, a: str, b: str) -> float:
    a, b = a.replace(" ", ""), b.replace(" ", "")
    if len(a) < 2 or len(b) < 2:
      return 0.0

    bigrams = {}
    for i in range(len(a) - 1):
      bg = a[i:i+2]
      bigrams[bg] = bigrams.get(bg, 0) + 1

    intersection = 0
    for i in range(len(b) - 1):
      bg = b[i:i+2]
      if bigrams.get(bg, 0) > 0:
        bigrams[bg] -= 1
        intersection += 1

    return (2 * intersection) / (len(a) + len(b) - 2)


  # ---------- Main logic / Fast response ----------
  def get_response(self, message: str):
    message = message.lower().strip()

    # ----  For fast and accurate response  ----
    if "favorite language" in message:
      return "My favorite programming language is Python."
            
    if any(word in message for word in ["name", "who are you"]):
      return self.fullName()

    if any(word in message for word in ["age", "old are you"]):
      return "I'm 21 years old."

    if any(word in message for word in ["hello", "hi", "hey"]):
      return self.random_greeting()
    
  
    best_match = None
    best_score = 0.0

    for key in self.default_responses:
      score = self.compare_two_strings(message, key)
      if score > best_score:
        best_score = score
        best_match = key

    if best_score >= 0.6 and best_match:
      response = self.default_responses[best_match]
      return response() if callable(response) else response


    # ---- AI THINKING FALLBACK / Longer response ----
    return ai_think(message)
