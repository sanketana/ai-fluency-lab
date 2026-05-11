# Prompt Template: Interactive Quiz

**Purpose:** Generates an MCQ quiz with instant feedback, scoring, and explanations as a Claude artifact
**When to use:** Self-assessment, exam practice, testing understanding after studying
**Best for subjects:** Any — especially effective for Science, Social Studies, Math concepts

---

## The Prompt

```
Create an interactive quiz app as an artifact with the following specs:

Topic: [YOUR TOPIC — e.g., "Photosynthesis and Respiration for Grade 10 Biology"]
Number of questions: [10-15]
Difficulty level: [Grade level — e.g., "CBSE Grade 10 board exam level"]
Question types: Multiple choice (4 options each)

Requirements:
- Show one question at a time with 4 options
- When I select an answer, immediately show if I'm correct or wrong
- If wrong, show the correct answer AND a brief explanation of WHY it's correct
- Track my score as I go (e.g., "7/10 correct")
- At the end, show a summary with:
  - Total score and percentage
  - List of questions I got wrong with the correct answers
  - A "Study these topics" recommendation based on what I missed
- Include a "Try Again" button to retake the quiz with shuffled question order
- Use green for correct and red for incorrect answers
- Make it visually clean and easy to read

Ensure all questions and answers are factually accurate for the specified curriculum and grade level.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Specific chapter/unit, not just a subject name | "Chapter 5: Acids, Bases and Salts — NCERT Grade 10" |
| Number of questions | 10 for a quick check, 15-20 for thorough assessment | Start with 10, then ask for more on weak areas |
| Difficulty level | Matches your actual exam standard | "ICSE board level" or "JEE Foundation level" |
| Question types | Can request different formats | "Include 5 MCQ + 3 true/false + 2 fill-in-the-blank" |

---

## What to Expect

A working quiz interface with:
- Clean question display with numbered progress
- Clickable answer options with instant visual feedback
- Explanation popups for wrong answers
- End-of-quiz summary with score and gap analysis

**Quality check:** For every question you get "wrong," verify the AI's "correct" answer against your textbook. AI-generated quizzes occasionally have incorrect answer keys — catching these is part of the learning.

---

## Iteration Prompts

If the first result isn't quite right, try:
- "Make the questions harder — these are too easy for someone who has studied the chapter"
- "Add more questions specifically about [sub-topic I got wrong]"
- "Question 4's answer is wrong — [correct info]. Fix it and review the others."
- "Add a timer — 30 seconds per question to simulate exam conditions"
- "Include diagram-based questions where I have to interpret a figure"
- "After the quiz, generate a mini study plan for the topics I scored below 50% on"
