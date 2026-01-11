# Personal Chatbot REST FastApi and React 🤖

A personal AI chatbot powered by **Edrian's AI form (Ollama)**.  
Ask about Edrian’s skills, details, background, or just chat for fun!

---

## Demo

📹 [![Demo Video](https://drive.google.com/file/d/1bHPrK90a0bKDiNV69AzrUYx5ieCgxRZt/view?usp=sharing)](https://drive.google.com/file/d/17lLGOz7Ig4iCePseYQrqKlRB1pm2hn0a/view?usp=sharing)


---

## Features

- Ask about **personal details, skills, hobbies, and contacts**.  
- Handles **complex queries** via Ollama AI backend.  
- Fast predefined responses for common questions (greetings, age, favorite things).  
- Server health monitoring and auto-reconnect notifications.  

---

## Project Structure
```
ChatBot/
├─ Front-end/
│ ├─ index.html
│ ├─ JS/Chatbot.jsx
│ └─ CSS/Chatbot.css
│ └─ CSS/Images/user.png && bot.png
└─ Back-end/
├─ app.py
├─ chatbot.py
└─ ai_brain.py
```


---

## How to Run

**Front-end:**
```
bash
cd Front-end
python -m http.server 5000
```
**Back-end:**
```
bash
cd Back-end
uvicorn app:app --reload
```
Make sure too that Ollama is installed and running
```
Frontend URL: http://127.0.0.1:5000
Backend URL: http://127.0.0.1:8000
```
Then start chatting with me AI form! 🎉
