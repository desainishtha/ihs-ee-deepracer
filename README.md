# my-deepracer

AWS DeepRacer project scaffold.

## What is this repo for?

This repository is a starting point for developing and managing AWS DeepRacer code, including reward functions and helper scripts.

## Included files

- `reward_function.py` — starter AWS DeepRacer reward function template.
- `train.py` — local validation helper for reward function input.
- `requirements.txt` — dependency list for Python tooling.
- `.gitignore` — common ignores for Python and model files.

## Getting started

1. Install Python dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
2. Open this folder in your editor.
3. Edit `reward_function.py` with the policy you want to test.
4. Use the AWS DeepRacer console to create or update your model and paste your reward function there.
5. When you are ready, push this repo to GitHub and connect it to your DeepRacer workflow.

## Notes

- AWS DeepRacer reward functions are written in Python and executed by the AWS DeepRacer service.
- This repository is intentionally lightweight to keep focus on reward logic, evaluation, and deployment.
