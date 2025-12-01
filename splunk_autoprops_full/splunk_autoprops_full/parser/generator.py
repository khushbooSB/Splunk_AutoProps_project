
from .detector import detect_timestamp

def generate_props(sourcetype, detection):
    lines = [f"[{sourcetype}]"]
    ts = detection.get("timestamp_examples", [])
    if ts:
        _, tf = detect_timestamp(ts[0])
        lines.append(f"TIME_FORMAT = {tf}")
        lines.append("TIME_PREFIX = ^")
    lines.append("SHOULD_LINEMERGE = false")
    return "\n".join(lines)

def generate_transforms(sourcetype, detection):
    return ""
