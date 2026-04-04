import os
import sys

# Allow imports from the repo root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from reward_function import reward_function
from tests.test_cases import TEST_CASES

TOTAL_EPISODES = 10
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "simulation_results.txt")


def make_worse(params):
    """Return a worse version of the input parameters for early training."""
    distance = params["distance_from_center"]
    steering = params["steering_angle"]
    track_width = params.get("track_width", 1.0)

    worse_distance = min(distance + 0.30, track_width * 0.49)
    worse_steering = min(steering + 10.0, 30.0)

    return {
        "track_width": track_width,
        "distance_from_center": worse_distance,
        "all_wheels_on_track": params["all_wheels_on_track"],
        "speed": params.get("speed", 2.0),
        "steering_angle": worse_steering,
    }


def interpolate(start, end, fraction):
    return start + (end - start) * fraction


def simulate_params(params, episode):
    """Create simulated params for this episode."""
    final = params.copy()
    poor = make_worse(params)
    progress = episode / TOTAL_EPISODES

    return {
        "track_width": params.get("track_width", 1.0),
        "distance_from_center": interpolate(poor["distance_from_center"], final["distance_from_center"], progress),
        "all_wheels_on_track": final["all_wheels_on_track"],
        "speed": final.get("speed", 2.0),
        "steering_angle": interpolate(poor["steering_angle"], final["steering_angle"], progress),
    }


def run_simulation():
    lines = []
    lines.append("=== Phase 1 Training Simulation ===")
    lines.append("Showing how average reward improves over episodes.")
    lines.append("")
    lines.append(f"{'Episode':<10} {'Avg Reward':<12}")
    lines.append("" + "-" * 25)

    episode_results = []
    for episode in range(1, TOTAL_EPISODES + 1):
        rewards = []
        for case in TEST_CASES:
            sim_params = simulate_params(case["params"], episode)
            rewards.append(reward_function(sim_params))

        avg_reward = sum(rewards) / len(rewards)
        episode_results.append((episode, avg_reward))
        lines.append(f"Episode {episode:<3} → avg reward: {avg_reward:.3f}")

    lines.append("")
    lines.append("Summary:")
    lines.append(f"Episode 1 → avg reward: {episode_results[0][1]:.3f}")
    lines.append(f"Episode {TOTAL_EPISODES//2} → avg reward: {episode_results[TOTAL_EPISODES//2 - 1][1]:.3f}")
    lines.append(f"Episode {TOTAL_EPISODES} → avg reward: {episode_results[-1][1]:.3f}")
    lines.append("")
    lines.append("Training simulation complete.")

    output = "\n".join(lines)
    print(output)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output)
    print(f"\nSaved simulation output to: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_simulation()
