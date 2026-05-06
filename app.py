import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.matcher import llm_match # Ensure this import is correct

app = FastAPI(title="Incident-to-Control Mapping Demo")

class MatchRequest(BaseModel):
    incident: str

@app.post("/match")
def match(req: MatchRequest):
    # 1. Check if the environment variable is MISSING or set to the placeholder
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key or api_key == "your_actual_key_here":
        #  This runs if NO key or the PLACEHOLDER key is found
        return {
            "incident": req.incident, 
            "result": "MOCK RESPONSE: Control RC-002 selected. This incident maps to Data Loss Prevention because it involves sensitive data export."
        }
    
    # 2. Run this if a real key is detected
    try:
        result = llm_match(req.incident, DATA["controls"])
        return {"incident": req.incident, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))