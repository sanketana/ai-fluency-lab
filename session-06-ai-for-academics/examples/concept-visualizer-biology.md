# Example: Concept Visualizer — The Human Heart & Circulatory System

**Explainer type:** Concept Visualizer
**Subject:** Biology — How the Heart Pumps Blood (Cardiac Cycle)
**Level:** Grade 10 ICSE
**What makes this a good example:** Animated step-by-step process, clickable parts, color-coded blood flow, and a built-in self-test

---

## Prompt Used

```
Create an interactive concept visualizer as an artifact that explains:

Topic: How the human heart pumps blood — the complete cardiac cycle, including double circulation
Level: Grade 10 ICSE Biology

Requirements:
- Draw a simplified but anatomically correct diagram of the heart with all 4 chambers labeled: Left Atrium, Right Atrium, Left Ventricle, Right Ventricle
- Show the major blood vessels: Aorta, Pulmonary Artery, Pulmonary Vein, Superior/Inferior Vena Cava
- Animate the blood flow path using:
  - RED for oxygenated blood
  - BLUE for deoxygenated blood
- Create a step-by-step walkthrough with "Next Step" and "Previous Step" buttons:
  - Step 1: Deoxygenated blood enters Right Atrium from Vena Cava
  - Step 2: Right Atrium contracts, blood flows to Right Ventricle through tricuspid valve
  - Step 3: Right Ventricle contracts, blood pumped to lungs via Pulmonary Artery
  - Step 4: Blood gets oxygenated in lungs
  - Step 5: Oxygenated blood returns to Left Atrium via Pulmonary Veins
  - Step 6: Left Atrium contracts, blood flows to Left Ventricle through mitral valve
  - Step 7: Left Ventricle contracts, blood pumped to body via Aorta
  - Step 8: Blood delivers oxygen to body, becomes deoxygenated, returns to heart
- At each step, highlight the active part of the heart and dim the rest
- Include a text panel on the right side explaining what's happening at the current step
- Clicking on any chamber or vessel shows a popup with its name and function
- After all steps, show a "Double Circulation" summary explaining why blood passes through the heart twice

Add a "Test Yourself" mode at the end where the labels are hidden and I have to click on the correct chamber/vessel when prompted.
```

---

## What the Output Looks Like

The artifact generates an interactive heart diagram with:
- **Visual heart diagram** — simplified cross-section with 4 labeled chambers and major vessels
- **Animated blood flow** — red and blue particles/arrows moving through the correct path
- **Step controls** — "Previous" and "Next" buttons with a step counter (Step 3 of 8)
- **Active highlighting** — the current chamber glows/pulses while others dim
- **Info panel** — right side shows: step title, what's happening, which valve opens, direction of flow
- **Clickable parts** — clicking "Pulmonary Artery" shows: "Carries deoxygenated blood FROM the heart TO the lungs. The only artery that carries deoxygenated blood."
- **Test mode** — labels disappear, prompts like "Click on the chamber that receives oxygenated blood from the lungs" appear, student clicks, gets immediate feedback

---

## Quality Check Results

Verified against ICSE Grade 10 Biology textbook (Selina Publishers):

| Step | AI's Description | Textbook Check | Accurate? |
|------|-----------------|----------------|-----------|
| Blood flow direction | Right Atrium → Right Ventricle → Lungs → Left Atrium → Left Ventricle → Body | Matches textbook diagram exactly | Yes |
| Valve names | Tricuspid (right), Mitral/Bicuspid (left) | Textbook uses "Bicuspid" not "Mitral" | Minor — both terms correct, but ICSE uses "Bicuspid" more |
| Pulmonary Artery description | "Only artery carrying deoxygenated blood" | Matches | Yes |
| Double circulation explanation | Blood passes through heart twice per circuit | Matches textbook's definition | Yes |
| Left Ventricle wall thickness | Not mentioned | Textbook emphasizes: "Left ventricle has the thickest walls because it pumps blood to the entire body" | Missing — added via follow-up prompt |

**Action taken:** 
1. Asked Claude to use "Bicuspid valve" instead of "Mitral valve" to match ICSE terminology
2. Added a note about left ventricle wall thickness at Step 7

---

## Why This Example Works

1. **Pre-specified the steps** — didn't just say "show the cardiac cycle," laid out the exact sequence so the AI couldn't skip or misorient steps
2. **Color coding with meaning** — red/blue for oxygenated/deoxygenated is standard and prevents confusion
3. **Interactive elements** — clickable parts make it exploratory, not just a passive animation
4. **Self-test built in** — the "Test Yourself" mode turns the learning tool into an assessment tool
5. **Caught real inaccuracies** — "Mitral vs Bicuspid" is exactly the kind of subtle terminology difference that matters for board exams
