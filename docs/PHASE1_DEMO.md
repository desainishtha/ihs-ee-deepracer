# Phase 1 Demo Guide: Lane Following

This guide explains how to demo your Phase 1 AWS DeepRacer project to judges, teachers, and peers at the Engineering Expo.

---

## What the Demo Will Show

### The Three Parts

**Part 1: The Idea (30 seconds)**
- Show the code
- Explain what a reward function is

**Part 2: Local Testing (1 minute)**
- Run `python3 train.py` on your laptop
- Show how we test locally before AWS
- Explain what the output means

**Part 3: The Result (2 minutes)**
- Show a video/recording of the trained car completing a lap
- Explain what the car learned

---

## How to Explain the Reward Function (Simply)

### For Non-Technical Judges/Teachers

**Simple Version:**
> "We teach the car what good driving looks like by giving it rewards. If the car stays in the middle of the track, we say 'good job!' with points. If it goes off the track, we say 'oops' with negative points. The car tries thousands of different behaviors and learns which ones earn the most points. This is like how video game scores work—the car wants to maximize its score."

**Analogy:**
> "It's like training a dog. We reward the dog with treats for behaviors we like (staying centered) and don't reward it for bad behaviors (going off track). After many tries, the dog learns what behavior earns rewards."

### For Students/Tech-Savvy Audience

**Technical Version:**
> "This is a reward function—a Python function that scores driving behavior. It takes sensor data (distance from center line, speed, steering angle) and returns a score from 0 to 10. AWS DeepRacer uses this score to optimize a neural network. After 10,000+ training steps, the car learns to drive autonomously by maximizing cumulative reward."

---

## How to Explain What the Car is Learning

### The Car's Learning Process

1. **Random Start** — Car makes random steering decisions at first
2. **Calculate Reward** — We score each decision using our reward function
3. **Update Model** — Car's neural network gets updated based on results
4. **Repeat** — Thousands of times, car improves
5. **Result** — Car learns to stay centered and move forward

### Simple Explanation for Judges

> "When the car first starts training, it drives randomly—left, right, off the track. After each action, we calculate a score using our reward function. The car notices patterns: 'Centering gives +2 points, off-track gives -5 points.' Over thousands of repetitions, it learns to repeat the behaviors that earn the most points. By the end, it automatically steers to stay centered."

### Why This Matters

> "This demonstrates reinforcement learning—a fundamental AI technique used in robotics, game AI, and autonomous vehicles. Once the car learns, it doesn't need our help anymore; it drives by itself."

---

## Talking Points for Your Audience

### For the Expo (General Public)

1. **"We taught a car to drive itself using machine learning"**
   - This is real AI; it's not pre-programmed turns
   - The car learned by trial and error
   - After training, it drives completely autonomously

2. **"We defined what 'good driving' means, and the car learned to do it"**
   - We wrote a reward function (like a scorecard)
   - The car tries to get the highest score
   - This is how real autonomous vehicles learn

3. **"We test on a laptop before uploading to AWS"**
   - Local testing is fast
   - AWS training is the real deal (takes hours)
   - This workflow mirrors professional ML development

4. **"The car completes a whole lap without any human intervention"**
   - Show video of the car driving
   - Explain it learned from zero—no pre-programmed route
   - Emphasize this is fully autonomous after training

5. **"This is the 'Hello World' of autonomous driving"**
   - Simplest meaningful demo
   - Foundation for more complex behaviors
   - Real AI, not just a script

### For Teachers

- **Connectedness to curriculum:** Demonstrates feedback loops, optimization, and algorithmic thinking
- **Real-world application:** Autonomous vehicles, robotics, game AI—all use this technique
- **STEM integration:** Python coding + math (reward functions) + physics (car dynamics) + AI
- **Career relevance:** This is foundational knowledge for robotics engineers, ML engineers

### For Judges

- **Engineering rigor:** Systematic approach (scope → design → test → deploy → demo)
- **Reproducibility:** Code is on GitHub, anyone can replicate
- **Scalability:** Phase 1 is simple; Phase 2 adds complexity (proven pathway)
- **Innovation:** Using AWS cutting-edge tech; applying ML to robotics

---

## Real-World Relevance

### Why This Matters in the Real World

**Autonomous Vehicles:**
> Similar reward functions train actual self-driving cars. Instead of "stay centered," we might reward "follow traffic laws and avoid collisions." It's the same principle, scaled up.

**Robotics:**
> Robots in factories use reinforcement learning to optimize tasks. A robot might be rewarded for "completing assembly in minimum time." After training, it becomes faster and more efficient.

**Game AI:**
> Video game AI uses reward functions to learn winning strategies. AlphaGo (the program that beat world chess/Go champions) uses advanced reward functions.

**Our Project:**
> We're building the simplest version: "stay centered." But we're using the exact same technique that powers billion-dollar industries.

---

## Demo Walkthrough Script

### Setup (30 seconds before demo)
- Have your laptop ready with `reward_function.py` open
- Have a terminal window ready to run `python3 train.py`
- Have a video/GIF of trained model (or screenshot of AWS job) ready

### Part 1: The Code (30 seconds)

**Show screen with `reward_function.py` open**

> "This is our reward function. It defines what 'good driving' means. 
>
> If the car stays in the center of the track, it gets +1 to +2 points.  
> If it goes off track, it gets -5 points.  
> Harsh steering gets a penalty.  
> Fast, smooth driving gets a bonus.
>
> The car tries thousands of behaviors and learns which ones maximize points."

**Point to key lines:**
- Center-line reward
- Off-track penalty
- Speed bonus

### Part 2: Local Testing (1 minute)

**Run `python3 train.py`**

```bash
$ python3 train.py

Sample input:
{
  "track_width": 1.0,
  "distance_from_center": 0.05,
  "all_wheels_on_track": true,
  "speed": 2.5,
  "steering_angle": 5.0
}
Reward: 4.25
```

> "This test simulates the car perfectly centered, moving at 2.5 m/s, with gentle steering. It gets a reward of 4.25. This is how we validate locally before uploading to AWS."

*Run it a few times with different inputs to show variance.*

### Part 3: The Result (2 minutes)

**Show video or screenshot of trained model**

> "After AWS trains on this reward function for several hours, the car learns. Here's the result—the car completing a lap, staying mostly centered, moving smoothly. It learned this by trial and error, maximizing the reward score.
>
> This entire car is autonomous—no human steering, no pre-programmed route. Just learned behavior from reward signals."

**Pause for questions:**
> "Questions?"

---

## Tips for Success

### Before Demo Day
- [ ] Practice the demo 3+ times
- [ ] Time it (should be 3–5 minutes total)
- [ ] Have phone with video backup ready
- [ ] Test laptop screen share/projection
- [ ] Prepare for tech failures (have screenshots)

### During Demo
- [ ] Speak clearly, make eye contact
- [ ] Pause for questions
- [ ] Don't rush; take time to explain
- [ ] Show enthusiasm! (This is cool stuff)
- [ ] Have your Mentor present for credibility

### If Something Breaks
- [ ] Have a 30-second video of the car driving
- [ ] Have screenshots of AWS training job
- [ ] Have printed handout with reward function code
- [ ] Fallback: "Let me show you the video from when we tested this yesterday"

---

## Q&A Preparation

**Q: "How long did the car take to learn?"**  
A: "AWS training takes about 2–4 hours. We don't watch; we just wait for completion."

**Q: "Could the car learn a different strategy, like zigzagging?"**  
A: "Yes! If we changed the reward function to reward aggressive steering, it would learn differently. The reward function completely defines what the car learns."

**Q: "Is this the same as real self-driving cars?"**  
A: "The principles are the same, but real cars use many more sensors and much more complex reward functions. We're learning the basics."

**Q: "Could it learn to cheat somehow?"**  
A: "Great question! In real deployments, engineers have to be very careful the reward function doesn't incentivize cheating. For example, a poorly designed function might reward going backwards fast. We have to think through unintended behaviors."

**Q: "What happens next?"**  
A: "Phase 2 will train on multiple tracks. Phase 3 will compete against other teams' models."

---

## Success Indicators

Your demo was successful if:
- ✅ Audience understood the concept
- ✅ You explained why this matters
- ✅ You answered questions confidently
- ✅ The demo ran without major errors
- ✅ Judges asked follow-up questions (shows interest)

---

## Follow-Up Materials to Have Ready

Print or have digital copies of:
- [ ] GitHub repo URL
- [ ] This guide (PHASE1_DEMO.md)
- [ ] Reward function code (printed)
- [ ] Phase roadmap (what's next)
- [ ] Team member contact info

---

## Timeline for Demo Prep

| Task | Deadline |
|------|----------|
| Part 1: Write demo script | April 10 |
| Part 2: Practice 1st time | April 12 |
| Part 3: Record video/screenshots | April 13 |
| Part 4: Practice 2nd time | April 15 |
| Part 5: Practice with full team | April 18 |
| Part 6: Final refinement | April 20 |
| Demo day | April 25 |

---

## Additional Resources

- AWS DeepRacer console: https://console.aws.amazon.com/deepracer
- GitHub repo: https://github.com/desainishtha/ihs-ee-deepracer
- Mentor support available for last-minute issues
