# Phase 1 Scope: Lane Following "Hello World"

## Project Objective

Build a **lane-following AWS DeepRacer model** that demonstrates how machine learning can teach a car to drive autonomously.

Phase 1 is a minimal, teachable milestone suitable for student understanding and an engineering expo demo.

---

## Why Phase 1 Matters

- **Proves the concept** — Shows that we can write code to teach a car to drive
- **Student-friendly** — Logic is simple enough to understand in 1–2 hours
- **Demo-ready** — Exciting to watch; easy to explain to judges and teachers
- **Foundation** — Base case for advanced strategies in later phases
- **Time-boxed** — Achievable within a school project timeline

---

## In Scope

### Reward Function Design
- ✅ Lane following (center-line reward logic)
- ✅ Off-track penalty (car learns not to crash)
- ✅ Speed reward (encourages forward movement)
- ✅ Smooth steering behavior (penalizes harsh turns)
- ✅ Simple, commented code (easy for students to understand)

### Testing & Validation
- ✅ Local Python testing (`train.py`) — no AWS required
- ✅ Sample test cases (edge cases: tight corners, straight sections)
- ✅ Basic output validation (reward scores are sensible)

### Documentation
- ✅ Student-friendly README
- ✅ Reward function explanation
- ✅ Local testing guide
- ✅ AWS console walkthrough (text + screenshots)
- ✅ Demo talking points

### Deployment
- ✅ Manual paste into AWS DeepRacer console
- ✅ Single training job on default track
- ✅ Observation of trained model behavior

---

## Out of Scope (Phase 1)

### ❌ Advanced AI Techniques
- Multi-objective reward functions (Pareto optimization)
- Hyperparameter tuning
- Custom loss functions
- Imitation learning

### ❌ AWS Automation
- Automated job submission (CLI)
- Model versioning in S3
- CI/CD pipelines
- SageMaker integration

### ❌ Multi-Track Strategies
- Track-specific tuning
- Adaptive strategies per circuit
- Performance benchmarking

### ❌ Real-World Deployment
- Physical car programming
- Sensor calibration
- Real-time adjustments

### ❌ Advanced Monitoring
- Training analytics dashboards
- Reward function live plotting
- Meta-analysis of learning curves

---

## Deliverables

### Documentation (4 files)
- [ ] README.md (updated)
- [ ] docs/PHASE1_SCOPE.md (this file)
- [ ] docs/PHASE1_DEMO.md
- [ ] docs/PROJECT_ROADMAP.md

### Code (no changes in Phase 1)
- [x] reward_function.py (already working, will add comments in Phase 1b)
- [x] train.py (already works, will enhance in Phase 1b)

### Examples & Resources
- [ ] examples/test_cases.json (sample data)
- [ ] examples/aws_walkthrough.md (AWS console steps)

---

## Assumptions

1. **Students have Python 3.7+** — installed and working
2. **AWS account exists** — students can access AWS DeepRacer console
3. **Single track** — training on AWS DeepRacer default track only
4. **Manual workflow** — no automation scripts; focus on understanding
5. **No model persistence** — don't worry about saving/loading models in Phase 1

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Students don't understand reward function | High | Add detailed inline comments and separate explanation doc |
| Car doesn't complete a lap | High | Pre-test reward logic; ensure values are sensible |
| AWS console changes | Medium | Document current workflow; update as needed |
| Local test doesn't match AWS behavior | Medium | Note in documentation that approximation != perfect |
| Students modify code and break it | Medium | Keep baseline simple; provide rolling back instructions |
| Demo fails on expo day | High | Practice multiple times; have backup demo video |

---

## Success Criteria

### Functional Success ✅
- Reward function is syntactically valid Python
- Local test runs without errors
- AWS training job starts successfully
- Car completes majority of track (doesn't crash immediately)

### Educational Success ✅
- Every student can explain what the reward function does
- Every student can run `train.py` and interpret results
- Every student can identify why a specific reward value makes sense

### Demo Success ✅
- Demo is repeatable (same input = same behavior)
- Explanation takes < 2 minutes
- Judges/teachers understand lane-following concept
- Interesting to watch (car makes sensible driving decisions)

### Project Success ✅
- All documentation complete
- No broken links or typos
- Code is clean and commented
- Ready for Phase 2 planning

---

## Demo Plan

### What We'll Show
1. **The code** — Show `reward_function.py` on screen
2. **Local test** — Run `train.py` and show output
3. **The training** — Show AWS training job in progress (or completed model)
4. **The result** — Play video of trained car completing a lap

### How Long
- Total: 3–5 minutes
- Explanation: 1–2 minutes
- Live demo: 2–3 minutes (or video playback)

### Talking Points
1. "This reward function teaches the car what good driving looks like"
2. "We test locally first with `train.py`, before uploading to AWS"
3. "AWS handles the machine learning; we just define the rules"
4. "The car learned this behavior by trying thousands of times and learning which behaviors earned rewards"

### Audience
- Engineering expo judges
- Teachers
- Peers
- General public (non-technical)

---

## Timeline

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Phase 1 scope approved | April 4, 2026 | ✅ |
| Documentation complete | April 5, 2026 | 🔄 |
| Code comments added | April 6, 2026 | 📋 |
| Local testing works | April 7, 2026 | 📋 |
| AWS training complete | April 10, 2026 | 📋 |
| Demo ready | April 15, 2026 | 📋 |
| Expo day demo | April 25, 2026 | 📋 |

---

## Next Steps

1. ✅ Approve Phase 1 scope (done)
2. 🔄 Complete documentation files
3. 📋 Add code comments to `reward_function.py`
4. 📋 Enhance `train.py` with multiple test scenarios
5. 📋 Create sample test cases in `examples/`
6. 📋 Conduct internal demo and refinement
7. 📋 Plan Phase 2

---

## Sign-Off

**Phase 1 Scope:** APPROVED  
**Project Lead:** [Student Name]  
**Mentor:** [Mentor Name]  
**Date:** April 4, 2026
