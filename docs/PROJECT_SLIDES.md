# Project Slides

## Slide 1: Title
- IHS DeepRacer Project
- Student: [Your Name]
- Teaching a Car to Drive Using AI

## Slide 2: What is DeepRacer?
- A small autonomous race car
- Uses AI to learn how to drive
- Learns from rewards, not instructions

## Slide 3: Problem
- How do we teach a car to drive?
- How does it know what “good driving” is?
- We need a system to guide its behavior

## Slide 4: Our Approach (Phases)
- Phase 1 → Basic lane-following
- Phase 2 → Smarter driving behavior
- Phase 3 → Training & real deployment

## Slide 5: Phase 1 Breakdown
- Reward function (defines good driving)
- Local testing (different scenarios)
- Validation (checking correctness)
- Simulation (mimics training)

## Slide 6: System Flow
ChatGPT → Prompt → Copilot → Code → Test → Simulation

## Slide 7: How Learning Happens
Bad Driving → Low Reward  
Better Driving → Higher Reward  
More Reward → Learning Improves

## Slide 8: Results
- Episode 1 → Lower reward
- Episode 5 → Improved reward
- Episode 10 → Higher reward
- Shows learning over time

## Slide 9: Challenge
- AWS DeepRacer console not accessible
- Could not run real cloud training

## Slide 10: Our Solution
- Built our own training simulation
- Reused reward function and test cases
- Demonstrated learning locally

## Slide 11: What We Learned
- Reward function controls behavior
- Testing ensures correctness
- Learning can be simulated

## Slide 12: Next Steps
- Improve reward logic (Phase 2)
- Add smarter driving rules
- Prepare for real deployment
