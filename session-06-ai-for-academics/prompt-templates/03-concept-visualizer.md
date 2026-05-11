# Prompt Template: Concept Visualizer

**Purpose:** Generates an animated/interactive diagram explaining a process or system as a Claude artifact
**When to use:** Understanding processes, systems, cycles, flows — anything that benefits from visual explanation
**Best for subjects:** Biology (body systems, cell processes), Physics (circuits, forces), Chemistry (reactions, bonding), Geography (water cycle, plate tectonics)

---

## The Prompt

```
Create an interactive concept visualizer as an artifact that explains:

Topic: [YOUR TOPIC — e.g., "How the human heart pumps blood — the cardiac cycle"]
Level: [Grade level — e.g., "Grade 10 ICSE Biology"]

Requirements:
- Create an animated, interactive diagram that visually explains the concept step by step
- Use labels, arrows, and color coding to show different parts and their roles
- Include a "Play/Pause" control so I can step through the process at my own pace
- Add clickable elements — when I click on a part, show a brief explanation of what it does
- Use a "Step 1, Step 2, Step 3..." progression so I can follow the sequence
- Include a text panel alongside the diagram that explains what's happening at each step
- Use accurate terminology appropriate for the specified grade level
- Make colors meaningful (e.g., red for oxygenated blood, blue for deoxygenated)

Prioritize scientific accuracy. This will be used for exam preparation.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Must describe the specific process, not just the subject | "How photosynthesis converts CO2 and water into glucose" not just "photosynthesis" |
| Level | Controls terminology complexity | "Grade 8 simplified" vs "Grade 11 detailed with equations" |
| Specific focus | Narrow to what you need | "Focus on the light-dependent reactions only" |
| Additional features | Add what helps you learn | "Include a mini quiz at the end testing each step" |

---

## What to Expect

An interactive visual artifact with:
- Animated diagram showing the process in motion
- Step-by-step controls to move through the process
- Clickable labels with popup explanations
- Color-coded elements for clarity

**Quality check:** Compare the diagram's sequence and labels against your textbook diagram. Pay special attention to:
- Are the steps in the correct order?
- Are the labels using the right scientific terms?
- Are the cause-effect relationships shown accurately?

---

## Iteration Prompts

If the first result isn't quite right, try:
- "The diagram is too simple — add [specific detail] that my textbook includes"
- "Add a comparison view showing [normal process] vs [when it goes wrong]"
- "Make the animation slower and add more intermediate steps"
- "The label for [X] is incorrect — it should be [correct term]"
- "Add a 'Test Yourself' section where I label a blank version of the diagram"
- "Include the chemical equation alongside the visual"
