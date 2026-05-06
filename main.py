import json
from pathlib import Path
from matcher import llm_match

BASE = Path(__file__).resolve().parent
with open(BASE / "sample_data.json", "r") as f:
    data = json.load(f)

for incident in data["incidents"]:
    result = llm_match(incident["description"], data["controls"])
    print(f"Incident: {incident['id']}")
    print(result)
    print()
