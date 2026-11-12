from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_ask_questions():
    response = client.get("/questions")

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["text"] == "Calculate the area of a circle"



