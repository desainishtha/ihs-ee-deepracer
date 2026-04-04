# Project Presentation Script

## Introduction
This project is about teaching AWS DeepRacer how to drive itself. We built a simple system that uses code to tell the car what good driving looks like.

## What problem we are solving
The problem is how to teach a self-driving car to stay on a track. We need to define what "good driving" means so the car can learn it.

## Our approach (phased)
- Phase 1: Build basic lane-following behavior and test it locally.
- Phase 2: Improve the reward logic and make driving smarter.
- Phase 3: Add more advanced driving strategies later.

## What we built in Phase 1
- `reward_function.py`: the lane-following logic.
- `train.py`: local testing tool.
- test cases and validation script: to check the reward function.
- training simulation: shows reward improving over time.

## Challenge we faced
We could not access the AWS DeepRacer console. That meant we could not run real AWS training at the moment.

## How we solved it
We built a local simulation instead. The simulation reuses our reward function and test cases. It shows how reward values get better over episodes.

## Results
- The reward function gave higher scores for better driving.
- Early episodes were lower reward.
- Later episodes showed improved reward.
- This shows the reward function is guiding learning.

## Conclusion
We proved the Phase 1 system works in a local setup. We showed the reward function, testing, validation, and a training simulation. Next, we can improve the driving logic and move toward Phase 2.
