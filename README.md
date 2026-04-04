# IHS - DeepRacer project for Engineering Expo 2026

## What is AWS DeepRacer?

AWS DeepRacer is a **machine learning racing car** that learns to drive itself. Instead of manually programming every steering decision, we teach it a **reward function**—a simple set of rules that tell the car what good driving looks like. The car then learns through trial and error to follow those rules.

This project is your introduction to building smart autonomous systems.

---

## What is This Repository?

This repository contains the code and documentation to build your first AWS DeepRacer model. 

**Phase 1** focuses on the simplest, most teachable goal: **teach the car to stay centered on a racing track** (lane following).

By completing Phase 1, you'll understand:
- How reward functions guide AI behavior
- How to test your code locally before deploying to AWS
- How to train your first model and see it in action
- How machine learning works in robotics

---

## Phase 1: Lane Following "Hello World"

**Phase 1 is your first milestone.** Think of it like a "Hello World" program—simple, clear, and proof that everything works.

### Phase 1 Success Criteria

After Phase 1, you should be able to:

- ✅ **Clone and run** this repository locally in under 2 minutes
- ✅ **Understand** every line of the reward function
- ✅ **Modify and test** the reward function on your laptop
- ✅ **Deploy to AWS** and start a training job
- ✅ **Explain the demo** to a teacher or expo judge in 1–2 minutes
- ✅ **See your car** complete a lap staying mostly centered on the track

---

## Repository Structure

```
ihs-ee-deepracer/
│
├── README.md                     ← You are here
├── requirements.txt              ← Python dependencies
│
├── reward_function.py            ← The AI "brain" (what we teach the car)
├── train.py                      ← Local testing tool
│
├── docs/
│   ├── PHASE1_SCOPE.md          ← What's in Phase 1 (and what's not)
│   ├── PHASE1_DEMO.md           ← How to demo your project
│   └── PROJECT_ROADMAP.md       ← What comes after Phase 1
│
└── examples/
    └── (sample test cases coming soon)
```

---

## How to Get Started

### Step 1: Clone and Install (1 minute)

```bash
git clone https://github.com/desainishtha/ihs-ee-deepracer.git
cd ihs-ee-deepracer
python3 -m pip install -r requirements.txt
```

### Step 2: Test Locally (1 minute)

```bash
python3 train.py
```

This runs your reward function with sample data and shows you what score it gets. **This is how you test before uploading to AWS.**

### Step 3: Understand the Code (5 minutes)

Open `reward_function.py` and read the comments. Each line explains what it does.

### Step 4: Deploy to AWS (5 minutes)

1. Go to [AWS DeepRacer Console](https://console.aws.amazon.com/deepracer)
2. Create a new training job
3. Copy your `reward_function.py` code and paste it into the console
4. Start training
5. Watch your car learn to drive!

For detailed instructions, see `docs/PHASE1_DEMO.md`.

---

## How to Test Locally

Use `train.py` to validate your reward function before uploading to AWS.

```bash
python3 train.py
```

**What happens:**
- Loads your `reward_function.py`
- Runs it with sample car telemetry (simulated sensor data)
- Prints the reward score
- Repeats with different scenarios

This is **much faster** than training on AWS. Use this to quickly test ideas.

---

## File Descriptions

| File | Purpose |
|------|---------|
| `reward_function.py` | Defines how the car learns—the "brain" of the project |
| `train.py` | Local test runner; validates your reward function |
| `requirements.txt` | Python dependencies (numpy, pytest) |
| `docs/PHASE1_SCOPE.md` | Detailed Phase 1 scope and deliverables |
| `docs/PHASE1_DEMO.md` | How to explain and demo your project |
| `docs/PROJECT_ROADMAP.md` | Vision for Phase 2 and Phase 3 |

---

## What is Phase 1 About?

**Phase 1 Goal:** Build a lane-following car.

**In Scope:**
- Simple center-line reward logic (stay in the middle of the track)
- Local testing with `train.py`
- AWS console training (manual)
- Basic student-friendly documentation

**Out of Scope (coming in later phases):**
- Advanced strategies (multi-objective rewards)
- Automated AWS integration
- Model versioning and tracking
- Real car deployment

For the full scope, see `docs/PHASE1_SCOPE.md`.

---

## Next Phases

**Phase 2** (Coming Later):
- Build faster lane-following strategies
- Integrate with AWS programmatically
- Track model versions

**Phase 3** (Coming Later):
- Multi-track strategies
- Winning techniques
- Performance optimization

See `docs/PROJECT_ROADMAP.md` for details.

---

## Key Concepts Explained Simply

### What is a Reward Function?

A **reward function** is a set of rules that score how well the car is driving.

```
If car stays centered:      +10 points ✅ (good!)
If car goes off-track:       -5 points ❌ (bad!)
If car turns too hard:       -2 points ⚠️  (not ideal)
```

The car tries thousands of different behaviors and learns which ones get the highest scores.

### How Does the Car Learn?

1. Car makes a random steering decision
2. We calculate the reward using our reward function
3. Car remembers: "This behavior got X points"
4. After many tries, car learns the best behaviors

This is called **reinforcement learning**—the car learns from rewards.

---

## Getting Help

- **Understanding the code:** Read inline comments in `reward_function.py`
- **Demo planning:** See `docs/PHASE1_DEMO.md`
- **AWS setup:** See AWS console instructions in the demo guide
- **Errors:** Check for typos in your edited reward function

---

## Project Ownership

**Author:** IHS Engineering Club  
**Project:** AWS DeepRacer for Engineering Expo 2026  
**Repository:** https://github.com/desainishtha/ihs-ee-deepracer

---

## License

This project is open source and meant for educational use.

---

## Questions?

Refer to:
1. `docs/PHASE1_SCOPE.md` — What we're building
2. `docs/PHASE1_DEMO.md` — How to explain it
3. `docs/PROJECT_ROADMAP.md` — What comes next
