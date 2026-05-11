# Example: Biology Flashcard App — Cell Organelles

**Explainer type:** Flashcard App
**Subject:** Biology — Cell Organelles and Their Functions
**Level:** Grade 10 ICSE
**What makes this a good example:** Specific topic, correct grade level, includes a "Mark as Known" feature for spaced repetition, and asks for visual cues

---

## Prompt Used

```
Create an interactive flashcard app as an artifact with the following specs:

Topic: Cell organelles and their functions for Grade 10 ICSE Biology
Number of cards: 12
Difficulty level: ICSE Grade 10

Requirements:
- Each card has a front (organelle name) and a back (function + one key fact)
- Clicking a card flips it with a smooth animation to reveal the answer
- Include a "Shuffle" button to randomize card order
- Include a progress tracker showing how many cards reviewed out of total
- Add a "Mark as Known" feature — known cards turn green, unknown stay orange
- At the end, show how many I marked as "Known" vs how many I need to review
- Use a biology-themed color scheme (greens and blues)
- On the front of each card, include a simple emoji or icon representing the organelle

Cover these organelles: Nucleus, Cell Membrane, Mitochondria, Ribosomes, Endoplasmic Reticulum (Rough & Smooth), Golgi Apparatus, Lysosomes, Vacuole, Chloroplast (plant cells), Cell Wall (plant cells), Centrosome, Cytoplasm
```

---

## What the Output Looks Like

The artifact generates a fully working flashcard app with:
- **12 cards** arranged in a deck, each showing an organelle name with an icon on the front
- **Flip animation** — clicking reveals the function and one key fact (e.g., Mitochondria: "Powerhouse of the cell. Generates ATP through cellular respiration. Has its own DNA.")
- **Progress bar** at the top: "4 of 12 reviewed"
- **Two buttons per card:** "I Know This" (moves to green pile) and "Review Again" (stays in orange pile)
- **End screen:** "You know 8/12 organelles! Review these 4: Golgi Apparatus, Endoplasmic Reticulum (Smooth), Centrosome, Lysosomes"
- **Shuffle button** to restart in a new order

---

## Quality Check Results

After generating, we verified against the ICSE Grade 10 Biology textbook:

| Card | AI Said | Textbook Says | Accurate? |
|------|---------|---------------|-----------|
| Nucleus | Controls cell activities, contains DNA | Controls cell activities, contains genetic material (DNA) | Yes |
| Mitochondria | Powerhouse of cell, generates ATP | Site of cellular respiration, produces ATP | Yes |
| Golgi Apparatus | Packages and ships proteins | Packages, modifies, and dispatches proteins and lipids | Partially — missing "modifies" and "lipids" |
| Lysosomes | Digestive system of the cell | Contains digestive enzymes, breaks down waste material | Yes |
| Smooth ER | Lipid synthesis and detoxification | Synthesis of lipids and steroids, detoxification | Yes — close enough for Grade 10 |

**Action taken:** Asked Claude to update the Golgi Apparatus card to include "modifies" and "lipids" — this is the kind of correction students should learn to make.

---

## Why This Example Works

1. **Specific prompt** — listed exact organelles, didn't just say "cell organelles"
2. **Grade-appropriate** — asked for ICSE Grade 10 level, not generic biology
3. **Study-functional** — the "Mark as Known" feature makes it actually useful for revision, not just a demo
4. **Verifiable** — each card's content can be checked against the textbook
5. **Iterable** — easy to ask for corrections or additions
