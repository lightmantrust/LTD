from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="LTD Backend API",
    version="1.0.0",
    description="Backend API for LTD AI-Agent Platform"
)

# ------------------------------
# MODELS
# ------------------------------

class TaskRequest(BaseModel):
    task: str

class SimulationRequest(BaseModel):
    scenario: str

# ------------------------------
# HEALTH & SYSTEM ROUTES
# ------------------------------

@app.get("/health")
def healthcheck():
    return {"status": "ok", "timestamp": datetime.utcnow()}

@app.get("/metadata")
def metadata():
    return {
        "system": "LTD Platform",
        "version": "1.0",
        "agents": ["orchestrator", "connector", "simulation"]
    }

# ------------------------------
# AGENT ENDPOINTS
# ------------------------------

@app.post("/agent/orchestrator")
def run_orchestrator(data: TaskRequest):
    return {"agent": "orchestrator", "result": f"Processed task: {data.task}"}

@app.post("/agent/simulation")
def run_simulation(data: SimulationRequest):
    return {
        "agent": "simulation",
        "scenario": data.scenario,
        "outcome": "Scenario executed successfully"
    }

@app.get("/api/sample")
def sample():
    return {"data": "sample dataset ready"}
