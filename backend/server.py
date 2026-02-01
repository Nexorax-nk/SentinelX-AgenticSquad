from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any
import json
from datetime import datetime

# --- IMPORT YOUR TOOLS ---
# Ensure these function names match exactly what is in sentinel_tools.py
from sentinel_tools import analyze_login_event, judge_threat_level, execute_enforcement, generate_compliance_report, DATABASE

app = FastAPI()

# --- CRITICAL FIX: ENABLE CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 1. GLOBAL MEMORY FOR FRONTEND LOGS (Fixes the 404 issue) ---
EVENT_LOGS = []

def add_log(stage: str, data: Any):
    """Save the agent's result so the Frontend can see it"""
    log_entry = {
        "stage": stage, 
        "data": data,
        "timestamp": datetime.now().isoformat()
    }
    # Add to top of list
    EVENT_LOGS.insert(0, log_entry)
    # Keep only last 20 logs to save memory
    if len(EVENT_LOGS) > 20: 
        EVENT_LOGS.pop()

# --- INPUT MODELS ---
class DetectiveInput(BaseModel):
    log_json: str

class JudgeInput(BaseModel):
    risk_score: int
    anomalies: List[str]

class EnforcerInput(BaseModel):
    user_id: str
    verdict: str

class ClerkInput(BaseModel):
    user_id: str
    enforcement_status: str

# --- ENDPOINTS ---

@app.post("/detective/analyze")
async def api_detective(data: DetectiveInput):
    print(f"🕵️ DETECTIVE: Analyzing input...")
    # Call the tool
    result = analyze_login_event(data.log_json)
    # Save to logs for Frontend
    add_log("DETECTIVE", result)
    return result

@app.post("/judge/evaluate")
async def api_judge(data: JudgeInput):
    print(f"⚖️ JUDGE: Evaluating Risk Score {data.risk_score}")
    result = judge_threat_level(data.risk_score, data.anomalies)
    add_log("JUDGE", result)
    return result

@app.post("/enforcer/execute")
async def api_enforcer(data: EnforcerInput):
    print(f"👮 ENFORCER: Action on {data.user_id} -> {data.verdict}")
    result = execute_enforcement(data.user_id, data.verdict)
    add_log("ENFORCER", result)
    return result

@app.post("/clerk/report")
async def api_clerk(data: ClerkInput):
    print(f"📝 CLERK: Filing report for {data.user_id}")
    result = generate_compliance_report(data.user_id, data.enforcement_status)
    add_log("CLERK", result)
    return result

# --- CRITICAL FIX: THE MISSING ENDPOINT ---
@app.get("/events")
async def get_events():
    """Frontend calls this to get the latest animations"""
    return EVENT_LOGS

@app.get("/status/{user_id}")
async def api_status(user_id: str):
    clean_id = user_id.strip().lower()
    user_data = DATABASE.get(clean_id, {"status": "UNKNOWN"})
    print(f"🔍 STATUS CHECK: {clean_id} is currently {user_data.get('status')}")
    return user_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)