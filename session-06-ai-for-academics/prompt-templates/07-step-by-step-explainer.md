# Prompt Template: Step-by-Step Explainer

**Purpose:** Generates a walkthrough that explains a concept one step at a time with visuals and examples
**When to use:** Understanding complex procedures, mathematical proofs, algorithms, multi-step processes
**Best for subjects:** Math (solving equations, geometric proofs), Physics (problem-solving methods), Chemistry (balancing equations, reaction mechanisms), Computer Science (algorithms)

---

## The Prompt

```
Create an interactive step-by-step explainer as an artifact for:

Topic: [YOUR TOPIC — e.g., "How to solve quadratic equations using the quadratic formula"]
Level: [Grade level — e.g., "Grade 10 ICSE Mathematics"]

Requirements:
- Break the concept into clear numbered steps (typically 5-10 steps)
- Show ONE step at a time with a "Next Step" button — don't overwhelm with everything at once
- Each step should have:
  - A clear heading (what this step does)
  - A visual or worked example showing the step in action
  - A brief explanation of WHY this step works (not just what to do)
- Include a progress bar showing which step I'm on
- After all steps, show a complete worked example that applies every step together
- Add a "Practice" section at the end with 2-3 problems for me to try, with hidden solutions I can reveal
- Use color highlighting to show what changes at each step
- Include common mistakes to avoid at relevant steps

Ensure mathematical/scientific accuracy for the specified curriculum.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Describe the specific procedure or method | "Long division of polynomials" not just "polynomial division" |
| Level | Controls complexity and notation used | "Grade 9 — basic method" vs "Grade 11 — include complex number solutions" |
| Starting point | Specify what the student already knows | "Assume I already know how to factor simple expressions" |
| Practice problems | Request specific types | "Include 1 easy, 1 medium, and 1 hard practice problem" |

---

## What to Expect

An interactive tutorial with:
- Step-by-step progression with navigation controls
- Visual examples at each step with highlighted changes
- "Why this works" explanations alongside the procedure
- Practice problems with revealable solutions
- Progress tracking

**Quality check:** Work through the example manually alongside the explainer. Verify:
- Is each step mathematically/scientifically correct?
- Does the sequence make sense, or are steps out of order?
- Are the practice problem solutions correct?
- Does the explanation match what your teacher taught? (methods can vary)

---

## Iteration Prompts

If the first result isn't quite right, try:
- "Step 3 needs more explanation — I don't understand why [specific part]"
- "Add an alternative method for step [X] — my teacher taught it differently using [method]"
- "The solution to practice problem 2 is wrong — show me the correct working"
- "Add a step between step 2 and step 3 — I'm getting lost at that transition"
- "Make it more visual — add a diagram at step [X] showing [what you need to see]"
- "Add 3 more practice problems that are harder than the current ones"
- "Include a 'Common mistakes' warning at step [X] — I keep getting that part wrong"
