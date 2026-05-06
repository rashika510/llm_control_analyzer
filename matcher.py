import json
import os
from openai import OpenAI

def llm_match(incident_text, controls):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    prompt = {
        "incident": incident_text,
        "controls": controls,
        "instruction": "Return JSON with control_id, confidence (0-1), and explanation. Choose the best matching control only."
    }
    resp = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        input=json.dumps(prompt)
    )
    return resp.output_text
