import pytest
from ai_agents.orchestrator.example_agent import ExampleAgent

@pytest.fixture
def agent():
    return ExampleAgent(name="OrchestratorAgent")

def test_task_execution(agent):
    task_input = "Process incoming data"
    result = agent.run_task(task_input)
    assert "Processed" in result
    assert agent.status == "idle"
