# backend/server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# Import your actual logic
from sentinel_tools import analyze_login_risk, execute_lockdown, get_audit_status

app = FastAPI(title="SentinelX API")

# Allow the frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATA MODELS (Ensures IBM sends the right data) ---
class AnalyzeRequest(BaseModel):
    ip_address: str
    location: str
    user_id: str

class LockdownRequest(BaseModel):
    user_id: str
    reason: str

# --- API ENDPOINTS (These match your YAML) ---

@app.post("/analyze")
async def api_analyze(request: AnalyzeRequest):
    """Watsonx calls this to check for threats."""
    result = analyze_login_risk(request.ip_address, request.location, request.user_id)
    return result

@app.post("/lockdown")
async def api_lockdown(request: LockdownRequest):
    """Watsonx calls this to EXECUTE the kill switch."""
    result = execute_lockdown(request.user_id, request.reason)
    return result

@app.get("/status/{user_id}")
async def api_status(user_id: str):
    """Frontend Dashboard calls this to check if 'RED ALERT' is active."""
    return get_audit_status(user_id)

if __name__ == "__main__":
    import uvicorn
    # Runs the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)