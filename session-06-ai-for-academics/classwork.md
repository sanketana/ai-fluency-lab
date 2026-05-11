# Session 6: AI for Academics — Your AI Study Buddy

**Duration:** 90 minutes
**Cohort:** Senior (Age 13-16)
**Thinking Skills:** Intentional Direction + Critical Evaluation
**Primary Tool:** Claude (claude.ai) — Artifacts feature

---

## Session Overview

Students discover how to use AI as a powerful academic tool across three real scenarios they face every week: understanding concepts, tackling assignments, and preparing for exams. The primary hands-on focus is building interactive explainers using Claude artifacts. Students leave with a working study tool they built themselves — and the judgment to know when it's accurate and when it's not.

**Key message to reinforce throughout:** AI is your study *partner*, not your answer machine. The goal is to understand better, not to skip the thinking.

---

## Session Flow

### Phase 1: Hook (5 minutes)

**Teacher says:**
> "Quick show of hands — how many of you have an exam or an assignment due this week?"
> "Now, how many of you have used AI to help you study? Be honest."
> "Today we're going to turn AI into something way more useful than just asking it for answers. By the end of this class, you'll have built your own interactive study tool — flashcards, quizzes, animated diagrams, whatever fits YOUR subject. And you'll know exactly when to trust it and when not to."

**Frame the three academic scenarios:**
1. "I need to actually understand this concept" → Interactive Explainers
2. "I have an assignment due" → Assignment Clarifier
3. "I have an exam coming up" → Exam Prep & Quiz Generator

Tell students: "We're going deep on #1 today. You'll get a taste of #2 and #3, and your homework will let you explore those further."

---

### Phase 2: Demo — Interactive Explainers (15 minutes)

Teacher live-demos three different explainer types in Claude, showing the full prompt → artifact → iterate cycle.

#### Demo 2a: Flashcard App (5 min)

1. Open Claude and type the flashcard prompt (see `prompt-templates/01-flashcard-app.md`)
2. Show the artifact appearing — a working flip-card app right in the browser
3. Click through a few cards, show the shuffle feature
4. **Key teaching moment:** "Notice how I told Claude exactly what subject, what grade level, and how many cards. If I just said 'make me flashcards,' I'd get something generic and useless."

#### Demo 2b: Concept Visualizer (5 min)

1. Use the concept visualizer prompt (see `prompt-templates/03-concept-visualizer.md`) for a biology topic like "how the heart pumps blood"
2. Show the animated/interactive diagram that appears
3. **Key teaching moment:** "Look — this is an interactive diagram I can explore. But here's the critical question: is the biology actually correct? Let me check this against what the textbook says."
4. Deliberately point out one thing to verify (e.g., the order of blood flow through chambers)

#### Demo 2c: Interactive Quiz (5 min)

1. Use the interactive quiz prompt (see `prompt-templates/02-interactive-quiz.md`)
2. Take the quiz live — answer a couple questions, show instant feedback
3. Show the score at the end
4. **Key teaching moment:** "I can build a quiz for ANY topic in 30 seconds. But — and this is important — I need to check that the answers are actually correct. AI can be confidently wrong."

**Transition:** "Now it's your turn. Pick a subject you're actually studying right now, and build your own explainer."

---

### Phase 3: Student Build — Create Your Explainer (30 minutes)

#### Setup (2 min)
- Each student opens Claude (claude.ai)
- They pick a **real topic** from their current schoolwork — something they have an upcoming test or assignment on
- They choose one explainer type to build (refer them to the prompt templates)

#### Explainer Types Available
| Type | Best For | Prompt Template |
|------|----------|-----------------|
| Flashcard App | Memorizing terms, definitions, vocabulary | `01-flashcard-app.md` |
| Interactive Quiz | Testing understanding, self-assessment | `02-interactive-quiz.md` |
| Concept Visualizer | Understanding processes, systems, flows | `03-concept-visualizer.md` |
| Simulator | Math functions, physics, chemistry reactions | `04-simulator.md` |
| Timeline | History, sequences, evolution of ideas | `05-timeline.md` |
| Mindmap | Connecting related concepts, big-picture view | `06-mindmap.md` |
| Step-by-Step Explainer | Complex procedures, proofs, algorithms | `07-step-by-step-explainer.md` |

#### During Build Time — Teacher Circulates
Watch for and coach on:
- **Vague prompts:** "Make me flashcards about science" → help them be specific: subject, topic, grade level, number of items, difficulty
- **Blind trust:** Student accepts output without checking → ask "How do you know this is correct? Open your textbook and verify."
- **First-draft acceptance:** Student takes the first output → encourage iteration: "What would make this better? Ask Claude to change it."
- **Wrong explainer choice:** Student picked a format that doesn't fit the content → guide them to a better match (e.g., timeline for a topic that's really about processes → suggest a visualizer instead)

#### Quality Checkpoints (announce at 15 min and 25 min)
- **At 15 min:** "If you haven't verified at least 3 facts in your explainer against your notes or textbook, do that now."
- **At 25 min:** "Start wrapping up. Make sure your explainer is in a state you'd be proud to show the class."

---

### Phase 4: Demo — Assignment Helper (10 minutes)

**Teacher says:**
> "Scenario two: you have an assignment due and you're staring at the brief thinking 'what do they actually want from me?'"

#### Live Demo
1. Pull up a sample assignment brief (use a real-looking one — e.g., "Write a 1000-word essay on the causes and consequences of the French Revolution. Include primary sources. Due Friday.")
2. Paste it into Claude with the assignment clarifier prompt (see `prompt-templates/08-assignment-clarifier.md`)
3. Show how Claude breaks down:
   - What the assignment is actually asking for
   - Likely grading criteria
   - A suggested approach/structure
   - What "primary sources" means and how to find them

**Critical ethical moment — say this clearly:**
> "Notice what I did NOT do. I did not ask Claude to WRITE the essay. I asked it to help me UNDERSTAND what my teacher wants. There's a massive difference. Using AI to understand the assignment is smart. Using AI to do the assignment is cheating — and your teacher WILL be able to tell."

**Quick student exercise (2 min):** "Think of an assignment you have right now. In your head, what's the one part of the brief you're most confused about? That's exactly where this technique helps."

---

### Phase 5: Demo — Exam Prep & Quiz Generator (10 minutes)

**Teacher says:**
> "Scenario three: you have an exam next week and you need to figure out what you actually know vs. what you think you know."

#### Live Demo
1. Show uploading a textbook chapter (photo/PDF) to Claude
2. Use the exam quiz generator prompt (see `prompt-templates/09-exam-quiz-generator.md`)
3. Walk through the generated quiz — take 3-4 questions live
4. Show the gap analysis: "Based on your answers, here are your strong areas and here's what you should review"

**Key teaching moments:**
- "The quiz is only as good as the material you feed it. Give it your actual textbook, not random internet content."
- "The gap analysis is a starting point, not gospel. It tells you where to focus your revision — but you still have to do the revision."
- "This is NOT a replacement for actually studying. It's a tool to study SMARTER."

---

### Phase 6: Share + Reflect (20 minutes)

#### Student Demos (12 min)
- 3-4 volunteers share their explainers with the class
- For each demo, the presenter answers:
  1. "What topic did you build this for?"
  2. "Which explainer type did you pick and why?"
  3. "Did the AI get anything wrong? How did you catch it?"

#### Group Discussion (3 min)
**Teacher asks the class:**
- "Who found a factual error in their explainer? What was it?"
- "Who had to re-prompt Claude to get a better result? What did you change?"
- "Would you actually use what you built to study for a real exam?"

#### Reflection Sheet (5 min)
Hand out the reflection sheet (see `reflection-sheet.md`). Students fill it in before leaving.

---

## Materials Checklist

- [ ] Claude accounts — all students logged into claude.ai
- [ ] Prompt templates printed or shared digitally (all 9 templates)
- [ ] Sample assignment brief for Demo 2 (prepare something realistic for this age group)
- [ ] Textbook chapter photo/PDF for Demo 3 (pick a subject most students are studying)
- [ ] Reflection sheets — printed or digital
- [ ] Timer visible to class (for build phase checkpoints)

## Teacher Notes

- **Most common issue:** Students will want to use AI to generate homework answers, not study tools. Redirect firmly but without shaming — frame it as "you're selling yourself short if you just get answers."
- **If a student finishes early:** Challenge them to build a SECOND explainer in a different format, or ask them to try breaking their first one (find errors, edge cases).
- **If a student is stuck choosing a topic:** Ask "What's the next test you have? What subject?" — anchor it in their real academic life.
- **Artifact troubleshooting:** If Claude doesn't generate an artifact, the student may need to explicitly say "Create an interactive artifact" or "Build this as a React component." Sometimes rephrasing helps.
