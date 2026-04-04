def reward_function(params):
    """AWS DeepRacer reward function template.

    The function receives a dictionary of track and car state values from DeepRacer.
    Return a floating-point reward value; higher values encourage the desired behavior.
    """

    # Read input values from parameters
    track_width = params.get("track_width", 1.0)
    distance_from_center = params.get("distance_from_center", 0.0)
    all_wheels_on_track = params.get("all_wheels_on_track", True)
    speed = params.get("speed", 0.0)
    steering_angle = abs(params.get("steering_angle", 0.0))

    # Start with a base reward
    reward = 1.0

    # Penalize if the car goes off track
    if not all_wheels_on_track:
        return 1e-3

    # Reward staying near the center line
    marker = 0.1 * track_width
    if distance_from_center <= marker:
        reward += 1.0
    elif distance_from_center <= 0.25 * track_width:
        reward += 0.5
    else:
        reward += 0.1

    # Reward faster speeds
    reward += speed * 0.5

    # Penalize harsh steering
    if steering_angle > 15:
        reward *= 0.8

    return float(reward)
