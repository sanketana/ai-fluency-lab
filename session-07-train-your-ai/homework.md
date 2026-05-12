# Session 7: Homework — Train Your Own AI

**Due before next session**

---

## Task 1: Improve Your RPS Model

Your Rock Paper Scissors model from class probably wasn't perfect. Time to make it better.

**Steps:**
1. Open your Teachable Machine project (go to teachablemachine.withgoogle.com — your project should still be there if you used the same browser)
2. Ask **two family members or friends** to play your RPS game
3. For each person, record:
   - Did the AI recognize their gestures? (Yes / Mostly / Not really)
   - Which gesture failed the most?
4. Now go back to Teachable Machine and **add training samples from those other people's hands**
5. Retrain and re-export your model
6. Test again — did it improve?

**What to submit:**
1. Your **new model URL** (after retraining)
2. A short paragraph (3–5 sentences): What failed when other people tried your model? What did you change? Did it improve?

**What we're looking for:** Evidence that you tested, diagnosed a problem, and tried to fix it — not a perfect model.

---

## Task 2: Build a Gesture Invaders Game

You've trained an AI to recognize Rock, Paper, Scissors. Now train a completely **new** model with **your own creative gestures** and plug it into a different game.

### The Game: Gesture Invaders

Aliens fall from the sky. Each alien is labelled with one of your trained gestures. Show the matching gesture to your camera to destroy the alien before it reaches the bottom. You have 3 lives — don't let any through!

### Steps:

1. **Choose 4 or more creative gestures.** These are YOUR choice — be inventive! Ideas:
   - Thumbs up, peace sign, wave, finger point
   - Open hand, fist, high-five, OK sign
   - Heart shape with hands, salute, clap, shrug
   - Or anything else — the more distinct the better

2. **Train a new Teachable Machine model** with your chosen gestures
   - New Image Project (don't reuse your RPS one)
   - Name each class after the gesture (e.g., "Thumbs Up", "Peace", "Wave", "Point")
   - At least 50 samples per class, with variation

3. **Export and upload** your model — copy the URL

4. **Open `gesture-invaders.html`** in Chrome
   - Paste your model URL → Load
   - Review your detected gesture classes
   - Click **Start Game**
   - Survive as long as you can!

5. **Play at least 3 full games** and record your best score

### What to submit:
1. Your **model URL**
2. A **list of your chosen gestures** and why you picked them
3. Your **best score** and what level you reached
4. **One sentence:** Which gesture did the game say your AI struggled with most? (The game tells you at the end!)

### Pro Tips:
- Gestures that look very different from each other are easier for the AI to tell apart
- If two gestures are similar (e.g., open hand vs. high-five), the AI will confuse them and you'll lose lives
- More training data = better recognition = higher score
- Try playing in different lighting to see how robust your model is

---

## Bonus Challenge (Optional)

**The Family Invaders Tournament**

1. After training your model, challenge a family member to play Gesture Invaders using YOUR gestures
2. They'll probably struggle because the AI was trained on YOUR hands
3. Now add training samples of THEIR hands to your model and retrain
4. Let them play again — did their score improve?

Write 2–3 sentences about what happened and why.

---

## Submission Format

Share your work via the method your teacher specified (Google Classroom / WhatsApp / Email). Include:
- [ ] Task 1: New model URL + improvement paragraph
- [ ] Task 2: Model URL + gesture list + best score + struggle sentence
- [ ] Bonus (optional): Family tournament results + explanation
