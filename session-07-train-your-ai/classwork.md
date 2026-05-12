# Session 7: How AI "Learns" — Train Your Own AI

**Duration:** 90 minutes
**Cohort:** Both (Junior 10–12 / Senior 13–16)
**Thinking Skills:** Mental Modeling + Ethical Reasoning
**Primary Tools:** Google Teachable Machine + Custom Game Template (browser-based)

---

## Session Overview

**Format:** 1:1 (one teacher, one student)

The student stops being a consumer of AI and becomes its creator. They train an image classifier to recognize Rock, Paper, and Scissors hand gestures using Google's Teachable Machine, then plug their trained model into a playable game. The core lesson: the shape of what goes in determines the shape of what comes out. When the student builds a model with their own hands and watches it succeed or fail based on their training choices, they deeply understand how AI works — and where bias comes from.

**Key message to reinforce throughout:** You don't just use AI — you shape it. And if the training data is limited, the AI is limited.

---

## Pre-Session Teacher Prep

### 1. Prepare a "Bad Model" for the Hook (10 min before class)

Go to [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) and train a deliberately terrible RPS model:
- Only 5–8 samples per class (not 50)
- All samples from the same angle, same distance, same background
- Train and export → Upload → Save the URL

This model will fail hilariously during your demo. That's the point.

### 2. Test the Game Template

- Open `game-templates/rps-game.html` in **Chrome** on the student's machine
- Paste your bad model URL and verify the game loads
- Verify webcam permission works (click "Allow" when Chrome asks)

### 3. Share Files with Student

Have `rps-game.html` ready on the student's machine (shared folder, email, or USB).

### 4. Checklist

- [ ] Chrome browser on both teacher and student machines with working webcams
- [ ] Internet access (for Teachable Machine + TensorFlow.js CDN)
- [ ] "Bad model" URL ready for the Hook demo
- [ ] `rps-game.html` accessible on student's machine
- [ ] Training guide ready to share (`training-guide/teachable-machine-steps.md`)
- [ ] Reflection sheet ready (`reflection-sheet.md`)

---

## Session Flow

### Phase 1: Think — The Broken AI (15 minutes)

#### The Hook: Play a Rigged Game (8 min)

**Teacher says:**
> "I built an AI that plays Rock Paper Scissors. It watches my hand through the webcam and figures out what I'm showing. Let's see how smart it is."

Open the RPS game template with your pre-trained *bad* model. Play 5–6 rounds live. The model should misclassify constantly — calling Rock "Scissors," confusing Paper with Rock, etc.

Ham it up: act frustrated. "What?! That was clearly Rock! Why does it think that's Scissors?"

After a few laughable rounds:
> "Okay, this AI is terrible. But here's the thing — I built this AI. So whose fault is it that it's bad?"

#### Discussion (5 min)

**Ask the student:**
- "Why do you think my AI was so bad at this?" (Let them hypothesize)
- "How many example photos do you think I used to train it?" (Reveal: only 5 per gesture)
- "What if all my photos were from the same angle? Same lighting? Same hand?"

**Teacher lands the concept:**
> "This is one of the most important ideas in AI: **garbage in, garbage out**. An AI can only be as good as the data it was trained on. If the training data is limited, biased, or sloppy — the AI will be limited, biased, and sloppy. Today, you're going to train your OWN AI, and make it good enough to actually win."

#### Quick Framing (2 min)

> "By the end of this session, you'll have:
> 1. Trained an AI with your own hands — literally
> 2. Plugged it into a real game and played against a computer
> 3. Discovered what happens when someone ELSE tries to use YOUR AI
>
> That third part is the most interesting. Let's go."

---

### Phase 2: Build — Train, Play, Break (45 minutes)

#### Step 1: Open Teachable Machine (3 min)

Open [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) in Chrome together.

**Walk through together:**
1. Click **Get Started**
2. Choose **Image Project** → **Standard image model**
3. You'll see two default classes — rename and add a third

> "Rename your classes to exactly: **Rock**, **Paper**, **Scissors**. Spelling and capitalization matter — the game needs to match these names."

Share the training guide (`training-guide/teachable-machine-steps.md`) for reference.

#### Step 2: Record Training Samples (15 min)

**Teacher demonstrates with Rock first:**
1. Click **Webcam** under the Rock class
2. Hold down the **Record** button and show the Rock gesture (fist)
3. While recording, slowly vary: angle, distance from camera, background position, slight rotation

> "Watch me — I'm not holding perfectly still. I'm tilting my hand, moving closer and further, shifting left and right. This teaches the AI to recognize Rock in MANY situations, not just one."

**Student records their own samples.** Minimum targets:

| Class | Minimum Samples | Key Instruction |
|-------|----------------|-----------------|
| Rock | 50+ | Vary angle, distance, and background |
| Paper | 50+ | Show palm from different positions |
| Scissors | 50+ | Both left and right hand if possible |

**Watch for and coach on:**
- **Too few samples:** "You've only got 15 photos. That's like studying one paragraph for a whole exam — add more!"
- **No variation:** "All your photos look identical. Move your hand around, change the distance. Teach the AI that Rock can look different."
- **Messy background:** "If you have a lot of stuff behind you, the AI might learn to recognize your bookshelf instead of your hand. Try to keep the background simple."

#### Step 3: Train the Model (3 min)

> "Click **Train Model**. This takes 30–60 seconds. While it trains, watch the progress — you're literally watching a neural network learn from your examples."

**While training, explain simply:**
> "Right now, the computer is looking at all your photos and figuring out patterns. 'When I see a closed fist shape, that's probably Rock. When I see spread fingers, that's probably Paper.' The MORE examples you gave it, and the MORE varied those examples were, the better it gets at this."

#### Step 4: Test in Preview (2 min)

> "On the right side, you'll see a Preview panel. Turn it on. Show your gestures to the camera. Do you see the confidence bars moving?"

Quick checkpoint:
- Does Rock show >80% confidence? Paper? Scissors?
- If any gesture is weak, add more samples and retrain

#### Step 5: Export and Load Into Game (3 min)

1. Click **Export Model**
2. Click the **Upload** tab
3. Click **Upload my model**
4. Wait for upload → Copy the shareable link
5. Open `rps-game.html` in a new browser tab
6. Paste the URL → Click **Load My AI**

> "You should see your webcam appear and live prediction bars at the bottom. Wave your hands — make sure the AI is responding before you start playing."

#### Step 6: Play! (9 min)

> "Click **Play Round** and show your gesture when the countdown says SHOW. Best of 10 rounds. Let's see if your AI can beat the computer!"

Let the student play a full game. Coach as they go:
- If AI keeps misreading: "Look at the confidence bars. Which gestures is it confusing? You might need to go back and add more training data."
- If student wins easily: "Great training! Now here comes the real test..."

#### Step 7: The Bias Experiment (10 min)

**This is the most important part of the session.**

**Teacher says:**
> "Your AI was trained on YOUR hands. Let's see what happens when someone else tries to use it."

**Round 1 — Teacher tries the student's model (4 min):**
The teacher plays the RPS game using the student's trained model. The teacher's hands will likely be a different size, skin tone, and angle than what the model learned.

> "Watch — I'm showing Rock, but your AI thinks it's Paper. Why? Because it only learned what YOUR Rock looks like, not mine."

Let the student observe the model struggling with the teacher's hands. Play 3–4 rounds so the pattern is clear.

**Round 2 — Student tries the teacher's model (3 min):**
If you prepared your own well-trained model beforehand, let the student try playing YOUR model. Does it work for them? (If you trained only with your own hands, it probably won't.)

**Discussion (3 min):**
> "Your model was trained on one person's hands. It works for you, but not for me. Now think about this: if a real company built a facial recognition AI and only trained it on photos of one type of face, what would happen?"

> "This is exactly what has happened in the real world. Voice assistants that don't understand certain accents. Face filters that don't work on darker skin tones. Hiring AI that rejects qualified people. The AI isn't choosing to be biased — it's reflecting the limits of its training data."

Let this sink in. This is the bridge to real-world AI bias.

---

### Phase 3: Reflect (15 minutes)

#### Written Reflection (8 min)

Give the student the reflection sheet (`reflection-sheet.md`) and let them fill it in. The act of writing solidifies the learning — resist the urge to talk through it for them.

Key questions they'll answer:
- What happened when the teacher used your model?
- What training data was missing?
- How is this like real-world AI bias?

#### 1:1 Discussion (7 min)

Once the student finishes writing, talk through their answers together. Use the reflection sheet as a conversation starter, not a quiz.

**Real-world connection to share:**
> "Amazon built a hiring AI trained mostly on resumes from men — it learned to reject women's resumes. Facial recognition systems trained mostly on lighter skin tones fail on darker skin tones. The AI isn't choosing to be biased — it's reflecting the bias in its training data. That's what 'garbage in, garbage out' really means."

**Age Differentiation:**

**Junior (10–12):** Focus on the concrete experience: "What happened? What was missing?" Keep real-world examples simple and relatable (voice assistants not understanding some accents, face filters not working for everyone).

**Senior (13–16):** Push for deeper analysis: "Who's responsible for fixing AI bias? The engineers? The company? The government? What if biased AI is used to decide who gets a loan or who gets arrested?"

---

### Phase 4: Share + Challenge (15 minutes)

#### Student Explains Their Model (5 min)

Have the student walk you through their work as if presenting to a parent:
1. Show the model in action (play 2–3 rounds)
2. "What was the hardest gesture for your AI to learn? Why?"
3. "What would you do differently if you trained it again?"

#### Teacher vs Student Challenge (7 min)

Now both train models and compete! Teacher quickly trains a model of their own (or uses the pre-made one, improved). Play 5 rounds each on the same computer — who gets a higher win rate against the computer?

Alternatively: challenge the student to **improve their model in 3 minutes** (add more samples, retrain) and see if their win rate goes up. This reinforces that more/better data = better AI.

#### Wrap-Up (3 min)

> "Today you went from AI users to AI creators. You saw firsthand that AI doesn't think — it reflects. It reflects whatever data you give it, including the limitations and biases in that data."
>
> "Here's the takeaway: every time you use an AI product — a search engine, a recommendation algorithm, a face filter — remember that someone chose what training data to use. And that choice shapes what the AI can and can't do, who it works for and who it doesn't."
>
> "You now understand something that most adults don't: AI is only as fair as the data it's trained on."

---

## Materials Checklist

- [ ] Chrome browser on student's machine with working webcam
- [ ] Internet access (for Teachable Machine + TensorFlow.js CDN)
- [ ] Pre-trained "bad model" URL for teacher demo
- [ ] `rps-game.html` on student's machine
- [ ] Training guide ready to share (`training-guide/teachable-machine-steps.md`)
- [ ] Reflection sheet — printed or digital (`reflection-sheet.md`)

---

## Teacher Notes

- **Most common issue:** The model confuses two gestures (usually Paper and Scissors). Fix: add more samples with clearer distinction, or have the student exaggerate the difference (spread fingers wide for Paper, only two fingers for Scissors).

- **Webcam permission:** If Chrome blocks the webcam, click the camera icon in the address bar and select "Allow."

- **"Model won't load in the game":** Check that the student copied the FULL URL (including the trailing slash). The URL should look like `https://teachablemachine.withgoogle.com/models/abc123/`.

- **Slow internet:** Model training happens locally in the browser (no upload needed). Only the export step requires good internet. If internet is very slow, test models directly in Teachable Machine's Preview panel instead of the game template.

- **If the student finishes early:** Challenge them to improve their model's accuracy to 95%+ on all three gestures, or to make their model work for both teacher and student without retraining.

- **Privacy note:** Teachable Machine processes all images locally in the browser. No photos are uploaded to Google's servers during training. The only upload happens when the student exports the model (which contains the trained weights, not the original photos).

- **The bias experiment is the emotional peak.** Protect this time. If you're running behind, cut Step 6 (play time) down to 5 minutes rather than cutting the bias experiment. The game is fun, but the bias discovery is the real lesson.
