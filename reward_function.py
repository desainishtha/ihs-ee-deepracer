def reward_function(params):
    """
    AWS DeepRacer Reward Function for Phase 1: Lane Following.
    
    This function teaches the car to stay centered on the track.
    The car is rewarded for:
      - Staying close to the center line (main goal)
      - Smooth steering (not turning too hard)
    
    The car is punished for:
      - Going off-track (instant near-zero reward)
    
    Args:
        params: Dictionary with car telemetry from AWS DeepRacer service.
                Expected keys: track_width, distance_from_center,
                all_wheels_on_track, speed, steering_angle

    Returns:
        float: Reward value (higher is better). Range: [0, ~5]
    """

    # Read sensor data from the car
    track_width = params.get("track_width", 1.0)
    distance_from_center = params.get("distance_from_center", 0.0)
    all_wheels_on_track = params.get("all_wheels_on_track", True)
    speed = params.get("speed", 0.0)
    steering_angle = abs(params.get("steering_angle", 0.0))

    # ====== RULE 1: Off-track is bad =====
    # If any wheel leaves the track, give almost zero reward
    if not all_wheels_on_track:
        return 1e-3  # Very small reward (basically failure)

    # ====== RULE 2: Center-line is good =====
    # Define what "center" means (10% of track width from actual center)
    center_threshold = 0.1 * track_width

    if distance_from_center <= center_threshold:
        # Excellent: car is very close to center
        reward = 3.0
    elif distance_from_center <= 0.25 * track_width:
        # Good: car is reasonably close to center
        reward = 2.0
    elif distance_from_center <= 0.5 * track_width:
        # Okay: car is getting close to edge
        reward = 1.0
    else:
        # Bad: car is too close to edge (but still on track)
        reward = 0.5

    # ====== RULE 3: Smooth steering is better =====
    # Penalize harsh turns (steering angle > 15 degrees)
    if steering_angle > 15:
        reward *= 0.8  # Reduce reward by 20%

    # ====== RULE 4: Encourage reasonable speed =====
    # Add a small bonus for moving at a moderate pace while staying on track.
    if speed >= 2.0:
        reward += 0.5

    return float(reward)
