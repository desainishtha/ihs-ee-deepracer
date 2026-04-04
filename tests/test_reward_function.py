# test_reward_function.py
# Unit tests for Phase 1 reward function
# Validates logical consistency of reward values

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from reward_function import reward_function
from test_cases import TEST_CASES

def test_reward_function():
    """Run reward function against all test cases and validate consistency."""
    results = {}
    for case in TEST_CASES:
        reward = reward_function(case["params"])
        results[case["name"]] = reward

        # Basic checks
        assert isinstance(reward, (int, float)), f"Reward must be numeric for {case['name']}"
        assert reward >= 0, f"Reward must be non-negative for {case['name']}"

    # Logical consistency checks
    assert results["ideal_centered_driving"] > results["slightly_off_center_driving"], \
        "Ideal centered should have higher reward than slightly off-center"

    assert results["slightly_off_center_driving"] > results["moderately_off_center_driving"], \
        "Slightly off-center should have higher reward than moderately off-center"

    assert results["moderately_off_center_driving"] > results["near_edge_of_track"], \
        "Moderately off-center should have higher reward than near edge"

    assert results["all_wheels_off_track"] < 0.01, \
        "Off-track should have near-zero reward"

    # Harsh steering penalty checks
    assert results["centered_but_harsh_steering"] < results["ideal_centered_driving"], \
        "Harsh steering should reduce reward even when centered"

    assert results["off_center_with_harsh_steering"] < results["moderately_off_center_driving"], \
        "Harsh steering should reduce reward when off-center"

    return results

if __name__ == "__main__":
    try:
        results = test_reward_function()
        print("All reward function tests passed!")
        for name, reward in results.items():
            print(f"  {name}: {reward:.3f}")
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)