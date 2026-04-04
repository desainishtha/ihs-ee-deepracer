# test_cases.py
# Sample test cases for Phase 1 reward function validation
# Each case represents a different driving scenario

TEST_CASES = [
    {
        "name": "ideal_centered_driving",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.0,
            "all_wheels_on_track": True,
            "speed": 2.0,
            "steering_angle": 0.0
        },
        "expected_outcome": "high reward"
    },
    {
        "name": "slightly_off_center_driving",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.12,
            "all_wheels_on_track": True,
            "speed": 2.0,
            "steering_angle": 5.0
        },
        "expected_outcome": "medium reward"
    },
    {
        "name": "moderately_off_center_driving",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.3,
            "all_wheels_on_track": True,
            "speed": 2.0,
            "steering_angle": 5.0
        },
        "expected_outcome": "low reward"
    },
    {
        "name": "near_edge_of_track",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.55,
            "all_wheels_on_track": True,
            "speed": 2.0,
            "steering_angle": 5.0
        },
        "expected_outcome": "low reward"
    },
    {
        "name": "all_wheels_off_track",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.6,
            "all_wheels_on_track": False,
            "speed": 2.0,
            "steering_angle": 25.0
        },
        "expected_outcome": "near-zero reward"
    },
    {
        "name": "centered_but_harsh_steering",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.05,
            "all_wheels_on_track": True,
            "speed": 2.0,
            "steering_angle": 20.0
        },
        "expected_outcome": "medium reward"
    },
    {
        "name": "off_center_with_harsh_steering",
        "params": {
            "track_width": 1.0,
            "distance_from_center": 0.3,
            "all_wheels_on_track": True,
            "speed": 2.0,
            "steering_angle": 20.0
        },
        "expected_outcome": "low reward"
    }
]