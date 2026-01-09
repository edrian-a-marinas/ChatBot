import random
from datetime import datetime
import requests

class Chatbot:
  def __init__(self):
    self.default_responses = {
      "Tell me about yourself, Introduce": f"I'm {self.fullName()}, {self.whereLive()} Currently  {self.jobHunt()} ",
      "name": f"Hello! I'm {self.fullName}",
      "nickname" : "Call me Ian for short",
      "degree":"I'm Currently holding B.S Information Technology from Our Lady of Fatima",

      "hello hi hey": "Hello! How can I help you?",
      "how are": "I'm doing great! How can I help you?",   #Actually looking for job?
      "thank": "No problem! Let me know if you need help with anything else!",
      "How old are you, your age?": "I'm 21 Years old",
      "when birthday": "January 27, 2004",
      "where do you live": f"{self.whereLive()}",
      "hobbies hobby": "I enjoy coding, and listening to music.",
      "skills, programming languages": "Python, Javascript, SQL and HTML/CSS",
      "passionate, passion,": "I'm Passionate at Python and back-end development",
      "favorite movies": "My favorite is Knives out",
      "favorite show": "My Favorite show is breaking bad.",
      "favorite anime": "One piece is my favorite anime",
      "favorite language": "My Favorite language is Python.",
      "status, doing, current":" I am currently a graduating student at Our Lady of Fatima, looking for job opportunities, internships, or OJT placements to gain experience and contribute.",
      "social, reach you, contacts, gmail": lambda: (
        "Here’s how to reach me!"
        "Facebook: https://facebook.com/edri.a.marinas "
        "LinkedIn: https://linkedin.com/in/edrian-a-marinas "
        "Github: https://github.com/edrian-a-marinas "
        "Gmail: edrian.aldrin.marinas@gmail.com "
        "Contact Number: 09854703444"
      ),
      "single relationship you taken": "I'm currently in relationship since August 22, 2019",
      "married": "Not married yet, just planning on it.",
      "do you do, employed,": self.jobHunt(),
      "employed":f"Not currently employed. {self.jobHunt()}",
      "looking for job": self.jobHunt,      
      "flip a coin": self.flip_coin,
      "roll a dice": self.roll_dice,
      "what is the date today, year": self.date_today,
      "Tell me a joke": self.get_joke,
      "Quote": self.get_quote
      

    }

    self.additional_responses = {}
    self.unsuccessful_response = (
      "Sorry, I didn't quite understand that. I can tell you joke if you want to!"
    )

  # --- Response functions ---
  def my_contacts(self):
    return "Facebook: https://facebook.com/edri.a.marinas Linkedin: https://linkedin.com/in/edrian-a-marinas Github: https://github.com/edrian-a-marinas Gmail: edrian.aldrin.marinas@gmail.com ContactNumber: 09854703444 "

  def whereLive(self):
    return "I live in Manila Philippines."

  def fullName(self):
    return "Edrian Aldrin C. Marinas"

  def jobHunt (self):
    return "I'm looking for jobs as a Software/Web developer focused on backend."

  def flip_coin(self):
    return "Sure! You got heads" if random.random() < 0.5 else "Sure! You got tails"

  def roll_dice(self):
    return f"Sure! You got {random.randint(1,6)}"

  def date_today(self):
    now = datetime.now()
    month = now.strftime("%B")
    day = now.day
    year = now.year
    return f"Today is {month} {day}, {year}"
  
    # --- Random joke ---
  def get_joke(self):
    try:
      res = requests.get("https://official-joke-api.appspot.com/jokes/random", timeout=5)
      data = res.json()
      return f"{data['setup']} ... {data['punchline']}"
    except Exception as e:
      return "Sorry, I couldn't fetch a joke right now."

  # --- Random quote ---
  def get_quote(self):
    try:
      res = requests.get("https://api.quotable.io/random", timeout=5)
      data = res.json()
      return f"\"{data['content']}\" — {data['author']}"
    except Exception as e:
      return "Sorry, I couldn't fetch a quote right now."



  # --- Add additional responses ---
  def add_responses(self, responses: dict):
    self.additional_responses.update(responses)

  # --- Compute similarity ---
  def compare_two_strings(self, first: str, second: str) -> float:
    first = first.replace(" ", "")
    second = second.replace(" ", "")

    if first == second:
      return 1.0
    if len(first) < 2 or len(second) < 2:
      return 0.0

    # Build bigrams
    first_bigrams = {}
    for i in range(len(first) - 1):
      bigram = first[i:i+2]
      first_bigrams[bigram] = first_bigrams.get(bigram, 0) + 1

    # Count intersection
    intersection_size = 0
    for i in range(len(second) - 1):
      bigram = second[i:i+2]
      if first_bigrams.get(bigram, 0) > 0:
        first_bigrams[bigram] -= 1
        intersection_size += 1

    return (2.0 * intersection_size) / (len(first) + len(second) - 2)

  def string_similarity(self, main_string: str, target_strings: list):
    ratings = []
    best_match_index = 0

    for i, target in enumerate(target_strings):
      rating = self.compare_two_strings(main_string, target)
      ratings.append({"target": target, "rating": rating})
      if rating > ratings[best_match_index]["rating"]:
        best_match_index = i

    return {
      "ratings": ratings,
      "best_match_index": best_match_index,
      "best_match": ratings[best_match_index]
    }

  # --- Get response ---
  def get_response(self, message: str):

    responses = {**self.default_responses, **self.additional_responses}

    similarity_data = self.string_similarity(message.lower(), list(responses.keys()))
    best_match_index = similarity_data["best_match_index"]
    best_match_rating = similarity_data["ratings"][best_match_index]["rating"]
    best_match_key = similarity_data["ratings"][best_match_index]["target"]

    response = responses[best_match_key]

    if best_match_rating <= 0.3:
      return self.unsuccessful_response

    # Call if function
    if callable(response):
      return response()
    return response
