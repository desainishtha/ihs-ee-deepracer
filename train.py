import json
from reward_function import reward_function


def main():
    sample_input = {
        "track_width": 1.0,
        "distance_from_center": 0.05,
        "all_wheels_on_track": True,
        "speed": 2.5,
        "steering_angle": 5.0,
    }
    reward = reward_function(sample_input)
    print("Sample input:")
    print(json.dumps(sample_input, indent=2))
    print("Reward:", reward)


if __name__ == "__main__":
    main()
