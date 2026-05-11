# Prompt Template: Flashcard App

**Purpose:** Generates an interactive flip-card study tool as a Claude artifact
**When to use:** Memorizing terms, definitions, vocabulary, formulas, key facts
**Best for subjects:** Biology, History, Languages, Chemistry, Geography

---

## The Prompt

```
Create an interactive flashcard app as an artifact with the following specs:

Topic: [YOUR TOPIC — e.g., "Cell organelles and their functions for Grade 10 Biology"]
Number of cards: [10-20]
Difficulty level: [Grade level or exam level — e.g., "ICSE Grade 10"]

Requirements:
- Each card has a front (question/term) and a back (answer/explanation)
- Clicking a card flips it to reveal the answer
- Include a "Shuffle" button to randomize card order
- Include a progress tracker showing how many cards reviewed
- Add a "Mark as Known" feature so I can focus on cards I haven't mastered
- Use clean, readable fonts and good contrast
- Make it visually appealing with colors relevant to the subject

Make sure all facts are accurate for the specified grade level and curriculum.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Must be specific, not just "Biology" | "Periodic table — first 20 elements, atomic number and symbol" |
| Number of cards | 10-15 for focused review, 20+ for comprehensive | 12 cards for a single chapter, 25 for an entire unit |
| Difficulty level | Ensures content matches your actual curriculum | "CBSE Grade 9" vs "ICSE Grade 10" vs "IB MYP Year 4" |
| Additional requirements | Add what matters for YOUR study style | "Include mnemonics" or "Add a hint button" |

---

## What to Expect

A working web app inside Claude's artifact panel with:
- Clickable cards that flip with animation
- Navigation between cards (previous/next)
- Shuffle functionality
- Progress indicator

**Quality check:** Open your textbook and verify at least 5 cards. AI can get definitions subtly wrong — especially for science terms where precision matters.

---

## Iteration Prompts

If the first result isn't quite right, try:
- "Add a hint button that shows the first letter of the answer"
- "Make the cards bigger and increase the font size"
- "Add 5 more cards focusing specifically on [sub-topic]"
- "The answer on card 3 is incorrect — [correct information]. Please fix it and double-check the others."
- "Add a 'Test Me' mode where I type the answer and it checks if I'm right"
