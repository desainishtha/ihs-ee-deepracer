import json
from reward_function import reward_function


def print_test_scenario(scenario_name, params):
    """
    Run a single test scenario and print the result.
    
    Args:
        scenario_name: Human-readable name of this test case
        params: Dictionary of car telemetry parameters
    """
    reward = reward_function(params)
    print(f"\n[{scenario_name}]")
    print(f"  Distance from center: {params.get('distance_from_center', 0):.2f}m")
    print(f"  Steering angle: {params.get('steering_angle', 0):.1f}°")
    print(f"  All wheels on track: {params.get('all_wheels_on_track', True)}")
    print(f"  → Reward: {reward:.2f}")
    return reward


def main():
    print("="*60)
    print("AWS DeepRacer Phase 1: Lane Following Test Harness")
    print("Testing reward function with various driving scenarios")
    print("="*60)

    # Define test scenarios
    # Each scenario represents a different driving situation
    test_cases = [
        {
            "name": "IDEAL: Perfectly centered, gentle steering",
            "params": {
                "track_width": 1.0,
                "distance_from_center": 0.0,      # Dead center
                "all_wheels_on_track": True,
                "speed": 2.0,
                "steering_angle": 0.0,            # No turning
            },
        },
        {
            "name": "GOOD: Slightly off-center, smooth steering",
            "params": {
                "track_width": 1.0,
                "distance_from_center": 0.08,     # Close to center
                "all_wheels_on_track": True,
                "speed": 2.0,
                "steering_angle": 5.0,            # Gentle turn
            },
        },
        {
            "name": "OKAY: Approaching edge, gentle steering",
            "params": {
                "track_width": 1.0,
                "distance_from_center": 0.35,     # Getting close to edge
                "all_wheels_on_track": True,
                "speed": 2.0,
                "steering_angle": 5.0,
            },
        },
        {
            "name": "BAD: Very close to edge, harsh steering",
            "params": {
                "track_width": 1.0,
                "distance_from_center": 0.45,     # Very close to edge
                "all_wheels_on_track": True,
                "speed": 2.0,
                "steering_angle": 20.0,           # Hard turn
            },
        },
        {
            "name": "CRITICAL: Off-track",
            "params": {
                "track_width": 1.0,
                "distance_from_center": 0.6,      # Beyond edge
                "all_wheels_on_track": False,     # CRASHED
                "speed": 2.0,
                "steering_angle": 25.0,
            },
        },
        {
            "name": "SMOOTH: Centered with aggressive steering",
            "params": {
                "track_width": 1.0,
                "distance_from_center": 0.05,     # Well centered
                "all_wheels_on_track": True,
                "speed": 2.0,
                "steering_angle": 25.0,           # Hard turn (penalty)
            },
        },
    ]

    # Run all test scenarios
    print("\nRunning test scenarios...\n")
    results = []
    for test_case in test_cases:
        reward = print_test_scenario(test_case["name"], test_case["params"])
        results.append((test_case["name"], reward))

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print("\nExpected behavior:")
    print("  ✓ Centered driving: HIGH reward (3.0)")
    print("  ✓ Near-center driving: MEDIUM reward (2.0)")
    print("  ✓ Edge driving: LOW reward (0.5-1.0)")
    print("  ✗ Off-track: CRITICAL (≈0)")
    print("  ✓ Harsh steering: PENALTY (×0.8)\n")

    print("Results:")
    for name, reward in results:
        if reward >= 2.5:
            status = "✓ EXCELLENT"
        elif reward >= 2.0:
            status = "✓ GOOD"
        elif reward >= 1.0:
            status = "⚠ OKAY"
        elif reward > 0.001:
            status = "✗ BAD"
        else:
            status = "✗ CRITICAL"
        print(f"  {status:15} {name}: {reward:.3f}")

    print("\n" + "="*60)
    print("Local test complete! Ready to deploy to AWS DeepRacer.")
    print("="*60)


if __name__ == "__main__":
    main()
