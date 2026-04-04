# run_phase1_validation.py
# Phase 1 validation runner
# Runs all tests and provides clear results

import sys
import os
sys.path.append(os.path.dirname(__file__))

from test_reward_function import test_reward_function

def print_summary_table(results):
    """Print a readable table of test results."""
    print("\n" + "="*60)
    print("PHASE 1 VALIDATION RESULTS")
    print("="*60)
    print(f"{'Scenario':<30} {'Reward':<10} {'Expected'}")
    print("-" * 60)

    for case in TEST_CASES:
        name = case["name"].replace("_", " ").title()
        reward = results[case["name"]]
        expected = case["expected_outcome"]
        print(f"{name:<30} {reward:<10.3f} {expected}")

def main():
    print("Running Phase 1 validation...")
    print("Testing reward function logic and consistency.")

    try:
        results = test_reward_function()
        print("✓ All validation checks passed!")
        print_summary_table(results)
        print("\n" + "="*60)
        print("Phase 1 validation PASSED")
        print("Reward function is working correctly.")
        print("="*60)
        return 0
    except AssertionError as e:
        print("✗ Validation failed!")
        print(f"Error: {e}")
        print("\n" + "="*60)
        print("Phase 1 validation FAILED")
        print("Please check the reward function logic.")
        print("="*60)
        return 1

if __name__ == "__main__":
    # Import test cases for summary
    from test_cases import TEST_CASES
    sys.exit(main())