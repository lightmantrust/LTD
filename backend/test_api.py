import pytest
from backend.api.app import app  # Assuming FastAPI or Flask app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_sample_endpoint():
    response = client.get("/api/sample")
    assert response.status_code == 200
    assert "data" in response.json()
