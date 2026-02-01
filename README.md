# 🛡️ SentinelX: Agentic Enforcement Squad for Security Operations
### **Built for IBM "AI Demystified" Hackathon 2026**

SentinelX is an autonomous multi-agent SOC enforcement system built on IBM watsonx Orchestrate.
It detects security anomalies, issues breach verdicts, and executes real-time containment actions.
Unlike advisory copilots, SentinelX has true enforcement authority — lockdown, revoke, block.
Every incident is automatically closed with compliance audit proof and Jira ticketing.

---

[![IBM Watsonx](https://img.shields.io/badge/AI-IBM%20Watsonx-blue)](https://www.ibm.com/watsonx)
[![Python](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-Next.js-red)](https://nextjs.org/)

> **"Not another SOC dashboard — SentinelX is enforcement authority in action."**

## 🎥 Project Demo
<a href="https://youtu.be/zVxtBcSR8k4" target="_blank">
 <img src="https://img.youtube.com/vi/zVxtBcSR8k4/maxresdefault.jpg" alt="Watch the Video" width="60%" />
</a>

---

## 🚧 The Problem: The "Mean Time to Respond" Gap
Large enterprises continuously face security threats such as:

- Unauthorized authentication attempts
- Geo-location anomalies and impossible travel logins
- SQL injection attack payloads
- Leaked API key exploitation
- Insider-driven mass data extraction

In current SOC practice, these alerts require manual investigation by analysts, leading to:

- Average incident response times of 4–8 hours
- High operational workload and alert fatigue
- Delayed containment and escalation into breaches
- Compliance risk due to slow documentation and audit closure

**The critical gap is not detection capability — it is enforcement latency.**

Enterprises require autonomous enforcement workflows, not only monitoring systems.


---

## 💡 The Solution: Agentic Security Orchestration
SentinelX is a governed multi-agent enforcement workflow implemented with IBM watsonx Orchestrate.

Rather than functioning as a single assistant, SentinelX operates as an orchestrated SOC squad where specialized agents collaborate to execute the full incident lifecycle:

- Evidence extraction
- Threat classification
- Automated containment enforcement
- Compliance documentation and closure

SentinelX is designed to demonstrate enforcement authority in security operations, reducing response time from hours to seconds.


---


## ☁️ Role of IBM watsonx Orchestrate

SentinelX is enabled by IBM watsonx Orchestrate's core enterprise capabilities:

- Multi-agent orchestration within a governed runtime
- Tool execution integrated directly into agent workflows
- Delegation and structured handoff between specialized agents
- Autonomous workflow enforcement with traceability and audit readiness

watsonx Orchestrate serves as the execution layer that allows SentinelX to move beyond text-based reasoning into operational security action.

---

## 🕵🏻 Multi-Agent Architecture

SentinelX is implemented as a structured five-agent SOC enforcement squad:

### 1. Sentinel Detective — Evidence Extraction Agent

Responsible for ingesting raw security logs and producing:

- Risk score (0–100)
- Detected anomalies
- Target user identity

This agent provides forensic evidence without enforcement authority.

### 2. Threat Judge — Verdict Classification Agent

Receives structured evidence and issues an official operational verdict via tool-based evaluation:

- CLEARED
- ESCALATION WATCH
- LOCKDOWN AUTHORIZED

This removes subjective interpretation and ensures binding classification.

### 3. Enforcement Officer — Autonomous Containment Agent

Executes enforcement actions only when breach-level authorization is issued, including:

- Account lockdown
- Token revocation
- Hostile IP blacklisting
- Session termination

SentinelX enforces containment rather than recommending remediation.

### 4. Compliance Clerk — Governance Closure Agent

Generates audit-ready compliance artifacts immediately after enforcement:

- Jira security incident ticket
- Audit evidence record
- Compliance closure confirmation

This ensures every action is documented and traceable.

### 5. SentinelX Commander — Orchestration Control Agent

Acts as the central coordinator, delegating each stage end-to-end:

- Dispatch investigation
- Route evidence to verdict
- Trigger enforcement when authorized
- Close incidents with governance documentation

This demonstrates true multi-agent orchestration rather than single-agent Q&A.

---

## 🍁 Agentic Enforcement Workflow

SentinelX follows a complete agentic security lifecycle:

**Sense → Investigate → Decide → Enforce → Document**

Operational execution flow:

1. Security evidence is ingested
2. Anomalies and risk are extracted
3. A binding verdict is issued
4. Enforcement is triggered autonomously when authorized
5. Compliance closure is generated immediately

This forms a closed-loop enforcement workflow suitable for enterprise SOC environments.

---

## 🛠️ Tooling and Orchestrate Integration

SentinelX integrates custom operational tools into IBM watsonx Orchestrate via OpenAPI specifications and a Python FastAPI backend.

Key tools include:

- `analyze_login_event()` — anomaly extraction and scoring
- `judge_threat_level()` — verdict issuance
- `execute_enforcement()` — real-time lockdown authority
- `generate_compliance_report()` — audit + Jira closure

These tools enable agents to perform operational actions beyond conversational output.

## 🔗 Supported Incident Scenarios

SentinelX supports real-world enforcement cases such as:

- Impossible travel authentication anomalies
- SQL injection breach signatures
- Abnormal API key request bursts
- Insider-driven mass record downloads

Each scenario results in autonomous enforcement execution and governance closure.

--- 

## 🏗️ Architecture
SentinelX is built on a **Multi-Agent System (MAS)** architecture using IBM Watsonx.ai (Llama-3-90b) for reasoning and Python (FastAPI) for tool execution.

<img src="./screenshots/architecture.png" alt="Attack View" width="600px" />

---

## ⚡Repository Structure

The project is organized as follows:

```
SENTINELX-SOC-COPILOT/
│
├── backend/                        # 🐍 Agent Logic & Tool Server
│   ├── sentinel_tools.py           # Core functions (detect, judge, enforce, audit)
│   ├── sentinel-openapi.yaml       # OpenAPI spec for IBM Watsonx Orchestrate
│   ├── server.py                   # FastAPI server exposing tools to Watsonx
│   └── requirements.txt            # Python dependencies (FastAPI, Uvicorn, etc.)
│
├── frontend/                       # ⚛️ Autonomous SOC Dashboard
│   ├── app/
│   │   ├── globals.css             # Global styling (Tailwind CSS)
│   │   ├── layout.tsx              # Root application layout
│   │   └── page.tsx                # Main dashboard UI (Live Attack View)
│   ├── public/                     # Static assets
│   ├── next.config.ts              # Next.js configuration
│   ├── package.json                # Frontend dependencies
│   ├── postcss.config.mjs          # PostCSS config
│   ├── tsconfig.json               # TypeScript configuration
│
├── screenshots/                    # 📸 Assets for README
│   ├── 4 agents.png
│   ├── architecture.png
│   ├── chat.png
│   ├── commander.png
│   ├── dashboard.png
│   └── steps.png
│
├── SentinelX.pdf                   # Project Documentation / Slide Deck
└── README.md                       # Main project documentation
```

---
## 📸 Screenshots

### 1. The IBM watsonx Orchestrate Console
<img src="./screenshots/commander.png" alt="Dashboard" width="600px" />

### 2. The Attack Simulation
<img src="./screenshots/chat.png" alt="Attack View" width="600px" />

---

## 🚀 How to Run Locally

### Prerequisites
* Python 3.9+
* Node.js 16+
* IBM Watsonx API Key

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sentinelx.git
cd sentinelx
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python server.py
# Server running at http://localhost:8000
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
# Dashboard running at http://localhost:3000
```
--- 

## 💥 Impact

SentinelX demonstrates measurable enterprise security value:

- Incident response reduced from hours → seconds
- Automated enforcement prevents escalation
- Governance and audit closure generated instantly
- SOC analysts relieved from repetitive manual investigation
- Enforcement actions remain fully traceable and compliant

## 📤 Hackathon Submission

This project was developed for the IBM Dev Day AI Demystified Hackathon - Feb 2026 , showcasing IBM watsonx Orchestrate as a deployable platform for agentic AI enforcement workflows.
