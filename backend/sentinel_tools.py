import json
from datetime import datetime

# --- MOCK DATABASE (Keys are now all lowercase for safety) ---
DATABASE = {
    "user_101": {"name": "Alice Admin", "status": "ACTIVE", "role": "admin"},
    "user_404": {"name": "John Doe", "status": "ACTIVE", "role": "viewer"},
    "blocked_ips": []
}

# --- THE TOOLS ---

def analyze_login_risk(ip_address: str, location: str, user_id: str):
    """
    Analyzes a login attempt for risk factors.
    """
    # FIX: Convert to lowercase to match database
    clean_user_id = user_id.strip().lower() 
    
    print(f"🕵️ SENTINEL DETECTIVE: Analyzing login for {clean_user_id} ({user_id}) from {location}...")
    
    # Simulation Logic
    if location.lower() in ["russia", "north korea"] or ip_address.startswith("192.168.66"):
        return {
            "risk_score": 95,
            "risk_level": "CRITICAL",
            "reason": "Geo-fencing violation (Restricted Country)",
            "recommendation": "IMMEDIATE_LOCKDOWN"
        }
    
    return {"risk_score": 10, "risk_level": "LOW", "status": "Safe"}

def execute_lockdown(user_id: str, reason: str):
    """
    ENFORCEMENT TOOL: Locks the user account.
    """
    # FIX: Convert to lowercase to match database
    clean_user_id = user_id.strip().lower()
    
    print(f"🚨 SENTINEL ENFORCER: Initiating LOCKDOWN for {clean_user_id}...")
    
    if clean_user_id in DATABASE:
        DATABASE[clean_user_id]["status"] = "LOCKED"
        
        ticket_id = f"JIRA-{int(datetime.now().timestamp())}"
        
        return {
            "status": "SUCCESS",
            "action_taken": f"User {clean_user_id} account LOCKED. Session Killed.",
            "audit_ticket": ticket_id,
            "timestamp": datetime.now().isoformat()
        }
    else:
        # Debugging print to see what went wrong
        print(f"❌ ERROR: User ID '{clean_user_id}' not found in DB keys: {list(DATABASE.keys())}")
        return {"status": "ERROR", "message": f"User ID {clean_user_id} not found."}

def get_audit_status(user_id: str):
    # FIX: Convert to lowercase
    return DATABASE.get(user_id.strip().lower(), {"status": "UNKNOWN"})

if __name__ == "__main__":
    # Test
    print(execute_lockdown("User_404", "Test"))