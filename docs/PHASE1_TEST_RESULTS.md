# Phase 1 Test Results

## Purpose of Testing
These tests validate that the Phase 1 reward function works correctly. They check that the car gets higher rewards for better driving behavior.

## How to Run the Validation
```bash
cd /path/to/your/repo
python3 tests/run_phase1_validation.py
```

## What is Being Checked
- Reward function returns numeric, non-negative values
- Centered driving gets higher rewards than off-center driving
- Off-track driving gets near-zero rewards
- Harsh steering reduces rewards
- Logical consistency across all scenarios

## Test Results
(Paste the output from running the validation here)

## How to Interpret Results
- **PASSED**: Reward function is working correctly
- **FAILED**: Check the reward function code for logic errors
- Look at the reward values to see if they make sense for each scenario