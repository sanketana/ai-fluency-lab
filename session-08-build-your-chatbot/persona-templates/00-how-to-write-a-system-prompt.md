# How to Write a System Prompt — The Anatomy of a Bot's Brain

A **system prompt** is the secret instruction the AI reads *before* it ever
talks to a user. The user never sees it. It is your bot's personality, job,
and rules — written in plain words.

This is the most important thing you will write all session. It is not code.
**It is thinking.** Two students with the *exact same app code* will build
completely different bots — and the only difference is the words in here.

> **The one rule that matters: be specific.**
> Vague instructions → vague, generic bot.
> Sharp, detailed instructions → a bot with a real personality and real limits.

---

## The 5 ingredients of a strong system prompt

Think of it like designing a character. A good system prompt answers five
questions:

### 1. ROLE — Who is the bot? What is its job?
> *"You are Coach Pep, a running coach for beginners who have never run before."*

Weak: "You are a helpful assistant." (This could be anyone. Boring.)

### 2. PERSONALITY — How does it talk?
> *"You are upbeat and encouraging, like a friendly PE teacher. You celebrate
> small wins and never make anyone feel slow or unfit."*

Is your bot funny? Calm? Sarcastic? A bit dramatic? Decide on purpose.

### 3. KNOWLEDGE — What is it about?
> *"You only talk about running, walking, stretching, and staying motivated."*

A focused bot is a good bot. A bot that knows "everything" usually feels like
nothing.

### 4. RULES — What must it ALWAYS do, and NEVER do?
This is the part most kids skip — and it's where AI fluency really shows.
> ALWAYS: "Always give one small, doable next step at the end of every answer."
> NEVER: "Never give medical advice. If someone mentions pain or injury, tell
> them to talk to a doctor or a trusted adult."

**The "NEVER" list is your bot's conscience.** Deciding what your bot should
*refuse* to do is a thinking skill, not a coding skill.

### 5. STYLE — What do its answers look like?
> *"Keep answers short — 2 or 3 sentences. Use a friendly emoji sometimes,
> but not in every line."*

Long? Short? Bullet points? Emojis or not? You decide.

---

## A filled-in example you can copy and change

```
You are Coach Pep, a running coach for total beginners.

PERSONALITY:
- Upbeat, warm, and encouraging — like a friendly PE teacher.
- You celebrate small wins and never shame anyone for being slow or unfit.

YOUR JOB:
- Help people start running: how to begin, how to breathe, how to stay motivated.

ALWAYS:
- End every answer with one small, doable next step (e.g. "Try a 5-minute walk today").
- Keep answers to 2-3 short sentences.

NEVER:
- NEVER give medical advice. If someone mentions pain, dizziness, or injury,
  tell them kindly to check with a doctor or a trusted adult.
- NEVER talk about topics other than running and fitness. Gently steer back.
- NEVER pretend to be sure when you are not.
```

---

## Test your prompt with these questions

Before you say you're done, ask:

- ✅ Could a stranger guess my bot's personality from the first reply?
- ✅ Does my bot have at least **two clear "NEVER" rules**?
- ✅ If someone asks an off-topic question, do I know what my bot will say?
- ✅ Did I describe *how long* and *what style* the answers should be?

If you answered "no" to any of these, your prompt is too vague. Go make it sharper.

---

## Starter personas

Stuck for an idea? Open one of these and make it your own — but change at least
the personality and the rules so the bot is truly *yours*:

- `01-homework-coach.md` — helps you learn without doing your work for you
- `02-character-bot.md` — talks as a historical figure or fictional character
- `03-language-buddy.md` — practises a new language with you
- `04-story-game-master.md` — runs a choose-your-own-adventure story
