
from fastapi import FastAPI, UploadFile, File, Form
from parser.detector import detect_structure, get_expected_event_count
from parser.generator import generate_props, generate_transforms

app = FastAPI()

@app.post("/analyze")
async def analyze(sample: UploadFile=File(...), sourcetype: str=Form(...)):
    text = (await sample.read()).decode("utf-8","ignore")
    detection = detect_structure(text)
    expected = get_expected_event_count(text)
    props = generate_props(sourcetype,detection)
    transforms = generate_transforms(sourcetype,detection)

    return {
        "sourcetype": sourcetype,
        "expected_event_count": expected,
        "props_conf": props,
        "transforms_conf": transforms,
        "detection": detection
    }
