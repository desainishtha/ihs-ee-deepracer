# Phase 1 Demo Script

## What is AWS DeepRacer?
AWS DeepRacer is a toy car that learns to drive itself using machine learning. Instead of programming every turn, we teach it what good driving looks like.

## What Problem Are We Solving in Phase 1?
In Phase 1, we're teaching the car to stay in the middle of the track. This is like the "Hello World" of autonomous driving—simple but shows the basics work.

## What is a Reward Function?
A reward function is like a scorecard for driving. It gives points for good behavior and takes points away for bad behavior. The car tries to get the highest score.

## What Does Our Reward Function Do?
Our reward function encourages lane-following:
- +3 points for staying very close to the center
- +2 points for being reasonably close
- +1 point for approaching the edge
- -5 points for going off-track
- Penalty for harsh steering

## How Did We Test It Locally?
We built a test script called `train.py` that simulates different driving situations. It runs our reward function with sample data and shows the scores.

## What Results Did We Get?
The tests show:
- Perfect center driving: 3.5 points
- Close to center: 2.5 points
- Near edge: 1.5 points
- Off-track: almost 0 points

This means the car learns to drive in the center and steer smoothly.

## Why Does This Matter in the Real World?
This is the foundation of autonomous vehicles. Real self-driving cars use similar reward functions to learn safe driving. We're building the basics of robotics and AI.

## Demo Flow
**Step 1: Show the code**  
Open `reward_function.py` and point to the rules.

**Step 2: Run the test**  
Run `python3 train.py` to see the scores.

**Step 3: Explain the output**  
Show how higher scores mean better driving.
