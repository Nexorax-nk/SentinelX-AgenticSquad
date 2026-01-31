from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any
import json
from sentinel_tools import analyze_login_event, judge_threat_level, execute_enforcement, generate_compliance_report, DATABASE

app = FastAPI()

# --- CRITICAL FIX: ENABLE CORS ---
# This allows your React Frontend (localhost:3000) to talk to this Server (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

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
    return analyze_login_event(data.log_json)

@app.post("/judge/evaluate")
async def api_judge(data: JudgeInput):
    return judge_threat_level(data.risk_score, data.anomalies)

@app.post("/enforcer/execute")
async def api_enforcer(data: EnforcerInput):
    return execute_enforcement(data.user_id, data.verdict)

@app.post("/clerk/report")
async def api_clerk(data: ClerkInput):
    return generate_compliance_report(data.user_id, data.enforcement_status)

@app.get("/status/{user_id}")
async def api_status(user_id: str):
    clean_id = user_id.strip().lower()
    user_data = DATABASE.get(clean_id, {"status": "UNKNOWN"})
    
    # --- DEBUG PRINT: WATCH THIS IN YOUR TERMINAL ---
    # This will tell you if the database actually updated to "LOCKED"
    print(f"🔍 STATUS CHECK: {clean_id} is currently {user_data.get('status')}")
    
    return user_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)