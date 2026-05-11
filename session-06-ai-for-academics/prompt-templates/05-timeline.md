# Prompt Template: Timeline

**Purpose:** Generates an interactive chronological visualization of events, processes, or evolution of ideas
**When to use:** Understanding historical sequences, cause-and-effect chains, development of concepts over time
**Best for subjects:** History, Political Science, Literature (author/movement timelines), Science (discovery timelines), Biology (evolutionary sequences)

---

## The Prompt

```
Create an interactive timeline as an artifact for:

Topic: [YOUR TOPIC — e.g., "Key events of the Indian Independence Movement, 1857-1947"]
Level: [Grade level — e.g., "Grade 10 ICSE History"]

Requirements:
- Create a horizontal scrollable timeline with events placed chronologically
- Each event should show: date, title, and a brief description (2-3 sentences)
- Use color coding to categorize events (e.g., political events, social movements, key figures, legislative acts)
- Clicking on an event expands it to show more detail and significance
- Include a legend explaining the color categories
- Add a "cause and effect" connection: show how earlier events led to later ones with connecting arrows or lines
- Include [15-25] key events — not every detail, but the ones essential for understanding the narrative
- At the bottom, include a 3-sentence summary of the overall arc

Ensure dates and facts are historically accurate for the specified curriculum.
```

---

## Customization Notes

| What to change | Why | Example |
|----------------|-----|---------|
| Topic | Define the specific period and scope | "French Revolution 1789-1799" not just "French Revolution" |
| Level | Controls depth and which events are included | Grade 8 = major events only; Grade 11 = includes political analysis |
| Number of events | Controls density | 10-15 for overview, 20-30 for detailed study |
| Categories | Specify how you want events grouped | "Color code by: economic, political, social, military" |

---

## What to Expect

An interactive horizontal timeline with:
- Scrollable view of events placed along a time axis
- Color-coded event markers with category legend
- Expandable event cards showing details on click
- Visual connections showing cause-effect relationships

**Quality check:** Cross-reference dates and event descriptions with your textbook. Pay special attention to:
- Are the dates correct? (AI sometimes gets dates off by a year)
- Are events attributed to the right people?
- Is the cause-effect narrative accurate, or has the AI oversimplified?

---

## Iteration Prompts

If the first result isn't quite right, try:
- "Add the following events that are missing: [event 1, event 2]"
- "The date for [event] is wrong — it was [correct date], not [AI's date]"
- "Add a 'Quiz Mode' where the timeline is blank and I have to place events in the right order"
- "Add a second parallel timeline showing [related events in another country/domain] for comparison"
- "Include key figures — show a brief bio popup for important people mentioned"
- "Add a 'Zoom' feature to focus on a specific decade/period in detail"
