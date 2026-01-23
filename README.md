# Personal Chatbot using FastApi and React (REST API) 🤖

A personal AI chatbot powered by **Edrian's AI form (Ollama)**.  
Ask about Edrian’s skills, details, background, or just chat for fun!

---

## Click to Watch Demo


<a href="https://drive.google.com/file/d/1QnFidwca1VCwhxpipPuqP6FI_3ptGXBt/view?usp=sharing" target="_blank">
  <img src="https://drive.google.com/uc?export=view&id=1bHPrK90a0bKDiNV69AzrUYx5ieCgxRZt" alt="Demo Video" width="400" />
</a>

---

## ⚠️ About Response Speed

You might notice that the AI takes a bit longer to respond in the demo video.  

This is because the chatbot runs entirely **locally** on my laptop, which has **entry-level specs** (CPU-Intel i3 1005G1 , GPU-NVIDIA MX330 , RAM-8GB)  at the same  time recording it.  

Thank you for your patience, and I hope you still enjoy chatting with Edrian’s AI! 🤖

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



