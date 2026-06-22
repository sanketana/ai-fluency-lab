# Deployment Guide — Put Your Chatbot on the Internet (Free, Browser-Only)

This guide takes your chatbot from "a folder of files" to "a live website with
its own link that you can text to a friend." Everything happens in your web
browser. You do **not** install anything on your computer.

There are **three free accounts** in this journey, and three big steps:

```
  STEP A: Get a free AI key      (Google AI Studio)
  STEP B: Get your own copy      (GitHub)
  STEP C: Put it online          (Streamlit Community Cloud)
```

> ⏱️ First time through, this takes about 15 minutes with your teacher.
> After that, updating your bot takes about 30 seconds.

> 🧑‍🏫 **Age + accounts note for teachers/parents:** Google, GitHub, and
> Streamlit accounts generally require users to be 13+. For students under 13,
> a parent- or teacher-managed account should be used, with supervision. Decide
> the account plan **before** class (see the teacher prep in `classwork.md`).

---

## STEP A — Get your free Gemini API key 🔑

An **API key** is like a password that lets your app talk to Google's AI. It is
secret. You never paste it into your code or show it on screen.

1. Go to **[aistudio.google.com](https://aistudio.google.com)** and sign in with
   a Google account.
2. Click **Get API key** (usually top-left or under the menu).
3. Click **Create API key** → **Create API key in new project**.
4. A long string appears (it starts with `AIza...`). Click **Copy**.
5. Paste it somewhere safe for a few minutes (a private notes app). You'll need
   it in Step C.

> 🔒 **Golden rule:** Treat this key like a password. Never put it in your code,
> never post it in a chat, never show it in a screenshot. If it ever leaks,
> delete it in AI Studio and make a new one.

The free tier gives you about **1,500 messages a day** — plenty for this course.

---

## STEP B — Get your own copy of the chatbot 🐙

The code lives in a **GitHub repository** (a "repo" = an online folder for code).
You'll make your own copy so you can change it.

**If your teacher gave you a template repo link:**

1. Open the template repo link your teacher shared.
2. Click the green **Use this template** button → **Create a new repository**
   (or click **Fork** if that's what your teacher tells you).
3. Give it a name like `my-ai-chatbot`.
4. Make sure it is set to **Public** (Streamlit's free plan needs this).
5. Click **Create repository**. 🎉 You now own a copy of the code.

> ⚠️ Because your repo is **public**, anyone can read the files in it. That's
> exactly why the API key is **never** stored in the code — it goes in Step C
> instead, in a private secrets box.

---

## STEP C — Put it online with Streamlit ☁️

1. Go to **[share.streamlit.io](https://share.streamlit.io)** and click
   **Sign in with GitHub**. Approve the connection.
2. Click **Create app** → **Deploy a public app from GitHub**.
3. Fill in the boxes:
   - **Repository:** pick the repo you made in Step B
     (e.g. `your-name/my-ai-chatbot`)
   - **Branch:** `main`
   - **Main file path:** `chatbot-app/app.py`
4. **Before** you click Deploy, open **Advanced settings** → **Secrets**, and
   paste this line (with your real key from Step A):

   ```toml
   GEMINI_API_KEY = "AIza...your-real-key-here..."
   ```

5. Click **Deploy**. Wait 1–2 minutes while it installs and starts up. ☕
6. Your bot appears live, with a URL like
   `https://my-ai-chatbot.streamlit.app` — **that link is yours to share!**

---

## How to change your bot after it's live ✏️

This is the magic part. You don't re-deploy from scratch — you just edit one file.

1. Go to your repo on GitHub.
2. Open the folder `chatbot-app` → click **`bot_config.py`**.
3. Click the **pencil ✏️ (Edit)** button.
4. Change your bot's name, greeting, personality, or rules.
5. Scroll down → **Commit changes**.
6. Streamlit notices the change and **redeploys automatically** in about a
   minute. Refresh your bot's URL to see the new version.

> 💡 This is the loop you'll use all session: *edit `bot_config.py` → commit →
> refresh → test.* Small changes, tested often, beat one giant change.

---

## Troubleshooting 🔧

| Problem | What to check |
|---|---|
| **"No API key found"** on the live app | Your secret is missing or misnamed. In Streamlit: **Manage app → Settings → Secrets**. It must be exactly `GEMINI_API_KEY = "..."`. Then **Reboot app**. |
| App says "Error installing requirements" | Check that `chatbot-app/requirements.txt` exists and the **Main file path** is `chatbot-app/app.py`. |
| Bot replies with a quota or 429 error | You've hit the free daily limit (~1,500 messages) or are sending too fast. Wait a bit, or make a new key in a new project. |
| Changes to `bot_config.py` don't show up | Did you **Commit** the change on GitHub? Then wait ~1 min and **hard refresh** (Ctrl/Cmd+Shift+R). |
| "Model not found" error | The model name in `bot_config.py` may have changed. Try `gemini-2.0-flash` or ask your teacher for the current free model name. |

---

## Optional: run it on your own computer (for teachers / Senior cohort)

Not needed for class — the browser path above is enough. But if you want to run
it locally:

```bash
pip install -r chatbot-app/requirements.txt
# create chatbot-app/.streamlit/secrets.toml from the .example file, add your key
streamlit run chatbot-app/app.py
```
