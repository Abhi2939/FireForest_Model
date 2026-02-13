from detection import detect_fire
from severity import compute_severity
from spread import compute_spread_radius

def analyze_fire(image_path):

    fire_event = detect_fire(image_path)

    if fire_event is None:
        return {"message": "No fire detected"}

    features = [
    fire_event["brightness"],
    fire_event["bright_t31"],
    fire_event["scan"],
    fire_event["track"],
    fire_event["latitude"],
    fire_event["longitude"],
    fire_event["confidence"]
]
    severity = compute_severity(features)

    radius = compute_spread_radius(
        severity,
        wind_speed = 18,
        vegetation_density = 0.7
    )

    return {
        "severity": severity,
        "radius_meters": radius,
        "location": fire_event["location"]
    }
