
import re
from typing import Dict
from dateutil import parser as dateparser

TS_PATTERNS = [
    (r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}", "%Y-%m-%d %H:%M:%S,%3N")
]

def detect_timestamp(line: str):
    for rx, tf in TS_PATTERNS:
        m = re.search(rx, line)
        if m:
            try: dateparser.parse(m.group())
            except: continue
            return m.group(), tf
    return None, None

def detect_structure(sample: str) -> Dict:
    lines = sample.splitlines()
    timestamps = [detect_timestamp(l)[0] for l in lines if detect_timestamp(l)[0]]
    return {
        "timestamp_examples": timestamps,
        "multiline": False,
        "is_json": sample.strip().startswith("{")
    }

def get_expected_event_count(sample: str) -> int:
    lines = sample.splitlines()
    count = 0
    for ln in lines:
        ts,_ = detect_timestamp(ln)
        if ts and ln.startswith(ts):
            count += 1
    return count or len([l for l in lines if l.strip()])
