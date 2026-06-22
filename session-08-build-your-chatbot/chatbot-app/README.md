# 🤖 My AI Chatbot — AI Fluency Lab

This is a real chatbot, powered by Google's Gemini AI, that you can put on the
internet for free and share with anyone.

## The only file you edit

👉 **`bot_config.py`** — this is where your bot's name, personality, and rules
live. Everything that makes your bot *yours* is in that one file.

You do **not** need to touch `app.py`. That's the engine.

## The two-minute mental model

```
  bot_config.py   →   app.py   →   Google Gemini AI   →   a real chat window
  (YOUR thinking)     (the         (the brain that        (what people see
                       engine)      writes replies)         and use)
```

## How do I put it online?

Follow **`../deployment-guide.md`** — it walks you through it step by step,
all in your web browser. No installing anything.

## Files in here

| File | What it is |
|------|-----------|
| `bot_config.py` | ⭐ Your bot's personality and rules. **Edit this.** |
| `app.py` | The engine. Don't edit. |
| `requirements.txt` | The list of tools the app needs. Don't edit. |
| `.streamlit/secrets.toml.example` | Shows how the secret API key is stored. |
| `.gitignore` | Keeps your real API key off the internet. |
