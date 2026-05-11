# Prompt Template: Simulator

**Purpose:** Generates an interactive simulation where students can change inputs and see results in real time
**When to use:** Understanding mathematical relationships, physics principles, chemical reactions — anything where changing one variable affects others
**Best for subjects:** Physics (motion, optics, electricity), Math (functions, geometry, graphing), Chemistry (reactions, equilibrium)

---

## The Prompt

```
Create an interactive simulator as an artifact for:

Topic: [YOUR TOPIC — e.g., "Projectile motion — how launch angle and velocity affect range and height"]
Level: [Grade level — e.g., "Grade 10 Physics, ICSE"]

Requirements:
- Build a visual simulation where I can adjust input variables using sliders or input fields
- Show the result visually in real time as I change inputs (graph, animation, or both)
- Display the relevant formula(s) alongside the simulation
- Show calculated output values updating live as inputs change
- Include preset examples (e.g., "Try this: set angle to 45° and velocity to 20 m/s")
- Add labels and units to all values
- Use a clean layout with controls on one side and visualization on the other
- Include a brief explanation of the physics/math principle being demonstrated

Ensure formulas and calculations are correct for the specified grade level.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Describe the specific relationship being explored | "Ohm's Law — how voltage, current, and resistance relate" |
| Level | Controls formula complexity and which variables to include | "Grade 9 — basic formula only" vs "Grade 11 — include friction and air resistance" |
| Variables | Specify which inputs you want to control | "Let me adjust mass, velocity, and height" |
| Visualization | Describe what you want to see | "Show a real-time graph of position vs time" |

---

## What to Expect

An interactive panel with:
- Sliders/input fields for adjustable variables
- Live-updating visualization (graph, animation, or diagram)
- Displayed formulas with current values substituted in
- Calculated results updating in real time

**Quality check:** Try known values from your textbook's solved examples. Plug them into the simulator and verify the output matches. If the simulator gives different answers, the formula implementation may be wrong.

---

## Iteration Prompts

If the first result isn't quite right, try:
- "Add a [variable] slider — I want to see how it affects the result too"
- "The formula used is wrong — it should be [correct formula]. Please fix the calculations."
- "Add a second graph showing [another relationship] alongside the first"
- "Include 3 preset scenarios from my textbook that I can load with one click"
- "Add a 'Challenge Mode' where the simulator gives me a target output and I have to find the right inputs"
- "Show the step-by-step calculation breakdown when I click on the answer"
