# Session 8: Homework — Build & Deploy Your Own AI Chatbot

**Due before next session**

Your bot is alive on the internet. This homework makes it *better* — by putting it
in front of real people, watching it fail, and patching the holes. That loop —
**test → find the flaw → fix it** — is the whole skill.

---

## Task 1: Real-World Stress Test 🔨

Send your bot's live link to **two people** (family or friends) and watch what
happens — without coaching them. Real users break things in ways you never expect.

**For each person, write down:**
- One message they sent that your bot handled **well**
- One message that made your bot mess up, go off-topic, or break a rule

**Then patch it:**
1. Pick the worst failure you saw.
2. Open `bot_config.py` on GitHub and **strengthen the matching rule** in your
   system prompt (make it more specific, or add a new NEVER rule).
3. Commit the change, wait a minute, and **re-test** the same failing message.

**What to submit:**
1. Your bot's **live link**.
2. The **failure you found** + what you changed in your system prompt.
3. One sentence: did your fix hold when you re-tested?

**What we're looking for:** evidence that you tested, found a real flaw, and tried
to fix it — not a perfect bot.

---

## Task 2: The Jailbreak Challenge 🕵️

A "jailbreak" is a clever message that tricks a bot into breaking its own rules.
Companies pay people to find these before their AI ships. Your turn.

1. Write the **three trickiest messages** you can think of to get your own bot to
   break one of its NEVER rules. (Examples of tactics: pretending it's "just
   pretend," claiming you have permission, asking the same thing five different
   ways, or telling it the rule doesn't apply to you.)
2. Try each one.

**What to submit:**
- Your three jailbreak attempts.
- For each: did it work (you broke the bot) or did your rules hold?
- One sentence: which tactic was hardest for your bot to resist, and why do you
  think so?

---

## Task 3: Give It a Second Life (choose ONE) 🎭

Pick **one** of these:

**Option A — A totally new bot.** Change `bot_config.py` so your bot becomes
something completely different (a new persona from `persona-templates/`, or your
own idea). Same app, brand-new character. Submit the new live version's behaviour
in 2–3 sentences: who is it now, and what are its rules?

**Option B — The opposite bot.** Make a *deliberately vague* version (system
prompt = just "You are a helpful assistant") and compare it to your good one. Ask
both the same 3 questions. Submit: what was different, and what does that teach
you about system prompts?

---

## Bonus Challenge (Optional): Two-Bot Conversation 🤖↔️🤖

Open your bot in two browser tabs (or two different bots). Take a message from one
and paste it into the other, back and forth, like they're talking to each other.
Where does the conversation go? Does either bot break character or its rules?
Write 2–3 sentences about what happened.

---

## Submission Format

Share your work via the method your teacher specified (Google Classroom / WhatsApp
/ Email). Include:
- [ ] Task 1: Live link + failure found + fix + did it hold
- [ ] Task 2: Three jailbreak attempts + results + hardest tactic
- [ ] Task 3: Option A or B write-up
- [ ] Bonus (optional): Two-bot conversation notes

> 🔒 **Reminder:** Never put your API key in a message, a screenshot, or your code.
> Share the *bot's link*, never the key.
