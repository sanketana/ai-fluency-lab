# Prompt Template: Mindmap

**Purpose:** Generates a visual concept map linking related ideas, showing how topics connect to each other
**When to use:** Getting a big-picture view of a topic, understanding relationships between concepts, revision before exams
**Best for subjects:** Any subject — especially useful for Biology (classification, systems), Social Studies (governance, economics), Literature (themes, character relationships), Science (interconnected concepts)

---

## The Prompt

```
Create an interactive mindmap as an artifact for:

Topic: [YOUR TOPIC — e.g., "Ecosystem and its components — Grade 10 Biology"]
Level: [Grade level — e.g., "ICSE Grade 10"]

Requirements:
- Central node with the main topic
- Branch into major subtopics (4-6 main branches)
- Each subtopic branches further into specific concepts (2-4 sub-branches each)
- Use color coding — each main branch and its children share a color
- Clicking on any node shows a brief explanation (2-3 sentences)
- Show relationship lines between related concepts across different branches (with dotted lines or arrows)
- Include a "Collapse/Expand" feature so I can focus on one branch at a time
- Make nodes draggable so I can rearrange the layout
- Use clear, readable text with varying font sizes (larger for main topics, smaller for details)

Ensure all concepts and relationships are accurate for the specified curriculum.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Define scope clearly | "The Indian Constitution — Fundamental Rights and Duties" not just "Indian Constitution" |
| Level | Controls how many sub-branches and how deep | Grade 8 = 3 main branches; Grade 11 = 6 branches with sub-sub-branches |
| Branches | Pre-specify if you know what the main categories should be | "Main branches: producers, consumers, decomposers, abiotic factors, energy flow" |
| Cross-links | Specify connections you want highlighted | "Show how energy flow connects to food chains and food webs" |

---

## What to Expect

An interactive visual mindmap with:
- Central topic node with radiating branches
- Color-coded branch families
- Clickable nodes with explanation popups
- Cross-branch relationship lines
- Expand/collapse functionality

**Quality check:** Compare the mindmap's structure against your textbook's chapter headings and your class notes. Ask yourself:
- Are any major concepts missing?
- Are concepts placed under the right parent branch?
- Do the cross-links make sense, or has the AI drawn a false connection?

---

## Iteration Prompts

If the first result isn't quite right, try:
- "Add a branch for [missing subtopic] under [parent topic]"
- "[Concept X] is under the wrong branch — it should be under [correct branch]"
- "Add a cross-link between [concept A] and [concept B] — they're related because [reason]"
- "Make this more detailed — add sub-branches under [specific branch]"
- "Add a 'Study Mode' that hides the leaf nodes and lets me fill them in from memory"
- "Convert this into a printable version I can stick on my wall"
