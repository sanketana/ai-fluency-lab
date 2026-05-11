# Prompt Template: Exam Quiz Generator

**Purpose:** Generates a targeted quiz from YOUR actual textbook content (uploaded as image/PDF), then provides a gap analysis showing what you know vs. what you need to review
**When to use:** Exam preparation — when you want to test yourself on specific textbook material
**Best for:** Any subject where you have textbook chapters, class notes, or study material to upload

---

## The Prompt

### Step 1: Upload and Generate Quiz

First, upload your textbook chapter (photo or PDF) to Claude. Then use this prompt:

```
I've uploaded pages from my [SUBJECT] textbook, Chapter [X]: [CHAPTER TITLE].
I have an exam on this material on [DATE].

Please:
1. Read through the uploaded content carefully
2. Generate a 15-question quiz that covers ALL the key concepts from this material
3. Mix the question types:
   - 8 multiple choice questions (4 options each)
   - 4 short answer questions (1-2 sentence answers expected)
   - 3 application questions (apply the concept to a new scenario)
4. Order questions from basic recall to deeper understanding
5. Make this an interactive quiz artifact where I can answer each question and get immediate feedback

After I complete the quiz, provide:
- My score with percentage
- A breakdown of which topics I got right vs. wrong
- A "Gap Analysis" section that says: "You're strong on: [topics]. You need to review: [topics]."
- A suggested 30-minute revision plan focusing on my weak areas

Important: Base ALL questions strictly on the uploaded material — don't add content from outside this chapter.
```

---

### Step 2: Deep Dive on Weak Areas

After completing the quiz, use this follow-up:

```
Based on my quiz results, I scored poorly on [TOPICS FROM GAP ANALYSIS].

For each weak topic:
1. Give me a concise explanation (as if I'm learning it for the first time)
2. Create 3 more practice questions focused specifically on that topic
3. Show me one "exam-style" question with a model answer I can study

Keep everything based on the textbook content I uploaded.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Subject and chapter | Be specific about what you uploaded | "Physics Chapter 3: Light — Reflection and Refraction, NCERT Grade 10" |
| Number of questions | Adjust to match your exam format | "20 questions for a 1-hour exam" or "10 questions for a quick check" |
| Question types | Match your actual exam format | "My exam has MCQs and diagram-based questions — include both" |
| Exam date | Creates urgency context for the revision plan | "My exam is in 3 days" → tighter revision plan |

---

## What to Expect

**From the quiz:** An interactive assessment matching your textbook content with varied question types and instant feedback.

**From the gap analysis:** A clear picture of strong vs. weak areas, with a focused revision plan.

**Quality checks — critical for exam prep:**
- Verify every "correct answer" against your textbook — an incorrect answer key will teach you the wrong thing
- Check that questions actually come from your uploaded content, not AI's general knowledge (which may differ from your syllabus)
- If a question seems off-topic or too hard, it may be pulling from outside your material — flag it

---

## Tips for Best Results

- **Upload quality matters:** Clear, well-lit photos of textbook pages work better than blurry scans. Crop out margins and irrelevant content.
- **One chapter at a time:** Don't upload an entire textbook. Focus on one chapter per quiz session for accurate, relevant questions.
- **Take it seriously:** Answer honestly — if you guess and get lucky, the gap analysis won't be accurate. Mark questions you were unsure about even if you got them right.
- **Iterate:** After reviewing weak areas, generate a SECOND quiz focusing only on those topics. Keep going until you score 80%+.
