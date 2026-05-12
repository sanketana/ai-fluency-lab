# Teachable Machine — Step-by-Step Training Guide

This guide walks you through training a Rock Paper Scissors image classifier and connecting it to the game.

---

## Part 1: Create Your Project

1. Open **Chrome** and go to [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com)
2. Click **Get Started**
3. Choose **Image Project**
4. Choose **Standard image model**

You'll see a page with two default classes (Class 1, Class 2).

---

## Part 2: Set Up Your Classes

1. Click the pencil icon on **Class 1** and rename it to exactly: **Rock**
2. Click the pencil icon on **Class 2** and rename it to exactly: **Paper**
3. Click **Add a class** and name it: **Scissors**

**Important:** The game matches these names, so spell them exactly as shown — capital first letter, rest lowercase.

---

## Part 3: Record Training Samples

For each class, you'll record webcam samples. Here's how to get the best results:

### Recording Rock (closed fist)

1. Click **Webcam** under the Rock class
2. Hold down the **Record** button
3. While recording, slowly do ALL of these:
   - Tilt your fist left and right
   - Move closer to and further from the camera
   - Shift your hand to different parts of the frame (center, left, right)
   - Slightly rotate your wrist
4. Aim for **at least 50 samples**

### Recording Paper (open palm)

1. Click **Webcam** under the Paper class
2. Hold down **Record** and show your open palm
3. Vary the same way: angle, distance, position in frame
4. Aim for **at least 50 samples**

### Recording Scissors (two fingers)

1. Click **Webcam** under the Scissors class
2. Hold down **Record** and show two fingers in a V shape
3. Vary angle, distance, position
4. Aim for **at least 50 samples**

### Tips for Better Training Data

| Do This | Don't Do This |
|---------|---------------|
| Move your hand while recording | Hold perfectly still |
| Vary the distance from camera | Keep the same distance every time |
| Record from multiple angles | Record from only one angle |
| Use 50+ samples per class | Use fewer than 20 samples |
| Keep the background relatively simple | Have a very cluttered background |

---

## Part 4: Train Your Model

1. Click the **Train Model** button (center of the page)
2. Wait 30–60 seconds while the model trains
3. You'll see a progress indicator — when it finishes, the Preview panel activates

---

## Part 5: Test Your Model

1. The **Preview** panel on the right should show your webcam
2. Show each gesture and check the confidence bars:
   - Rock should show high confidence (>80%) for the Rock bar
   - Paper should show high confidence for Paper
   - Scissors should show high confidence for Scissors
3. If any gesture is being confused with another:
   - Go back and add **more samples** for the confused gestures
   - Make the gestures **more distinct** (spread fingers wider for Paper, tighter fist for Rock)
   - Click **Train Model** again

---

## Part 6: Export Your Model

1. Click **Export Model** (above the Preview panel)
2. In the popup, click the **Upload** tab
3. Click **Upload my model**
4. Wait for the upload to complete (takes a few seconds)
5. You'll see a link like: `https://teachablemachine.withgoogle.com/models/abc123/`
6. **Copy this link** — you'll paste it into the game

---

## Part 7: Play the Game

1. Open the game file (`rps-game.html`) in Chrome
2. Paste your model URL into the text box
3. Click **Load My AI**
4. Allow camera access when Chrome asks
5. You should see your webcam and live prediction bars
6. Click **Play Round** to start!

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Could not load model" error | Make sure you copied the FULL URL including the trailing `/` |
| Webcam not showing | Click the camera icon in Chrome's address bar → Allow |
| Model keeps confusing two gestures | Add more training samples for those gestures, make them more distinct |
| Very slow loading | The first load downloads the AI library (~5MB). It's faster after the first time |
| Game says wrong class names | Your classes must be named exactly "Rock", "Paper", "Scissors" |
