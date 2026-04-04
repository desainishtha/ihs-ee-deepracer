# run_phase1_validation.py
# Phase 1 validation runner
# Runs all tests and provides clear results

import sys
import os
sys.path.append(os.path.dirname(__file__))

from test_reward_function import test_reward_function
from test_cases import TEST_CASES

def classify_reward(reward):
    """Classify reward value into categories."""
    if reward > 3.0:
        return "high"
    elif reward > 2.0:
        return "medium"
    elif reward > 0.01:
        return "low"
    else:
        return "near-zero"

def print_summary_table(results, output_file=None):
    """Print a readable table of test results."""
    lines = []
    lines.append("\n" + "="*80)
    lines.append("PHASE 1 VALIDATION RESULTS")
    lines.append("="*80)
    lines.append(f"{'Scenario':<25} {'Distance':<10} {'Steering':<10} {'Reward':<8} {'Class'}")
    lines.append("-" * 80)

    for case in TEST_CASES:
        name = case["name"].replace("_", " ").title()
        params = case["params"]
        distance = params["distance_from_center"]
        steering = params["steering_angle"]
        reward = results[case["name"]]
        reward_class = classify_reward(reward)
        lines.append(f"{name:<25} {distance:<10.2f} {steering:<10.1f} {reward:<8.3f} {reward_class}")

    lines.append("="*80)

    output = "\n".join(lines)
    print(output)

    if output_file:
        with open(output_file, "w") as f:
            f.write(output)
        print(f"\nOutput saved to: {output_file}")

def save_markdown(results, md_file):
    """Save results as markdown table."""
    lines = []
    lines.append("# Phase 1 Validation Results\n")
    lines.append("| Scenario | Distance | Steering | Reward | Class |")
    lines.append("|----------|----------|----------|--------|-------|")

    for case in TEST_CASES:
        name = case["name"].replace("_", " ").title()
        params = case["params"]
        distance = params["distance_from_center"]
        steering = params["steering_angle"]
        reward = results[case["name"]]
        reward_class = classify_reward(reward)
        lines.append(f"| {name} | {distance:.2f} | {steering:.1f} | {reward:.3f} | {reward_class} |")

    with open(md_file, "w") as f:
        f.write("\n".join(lines))
    print(f"Markdown output saved to: {md_file}")

def main():
    print("Running Phase 1 validation...")
    print("Testing reward function logic and consistency.")

    try:
        results = test_reward_function()
        print("✓ All validation checks passed!")
        print_summary_table(results, "tests/phase1_test_output.txt")
        save_markdown(results, "tests/phase1_test_output.md")
        print("\n" + "="*80)
        print("Phase 1 validation PASSED")
        print("Reward function is working correctly.")
        print("="*80)
        return 0
    except AssertionError as e:
        print("✗ Validation failed!")
        print(f"Error: {e}")
        print("\n" + "="*80)
        print("Phase 1 validation FAILED")
        print("Please check the reward function logic.")
        print("="*80)
        return 1

if __name__ == "__main__":
    sys.exit(main())