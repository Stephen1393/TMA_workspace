from main import app
from fastapi.testclient import TestClient
from database import get_connection, get_answers
import pytest

client = TestClient(app)

@pytest.fixture
def test_database(tmp_path):
    database_path = tmp_path / "test.db"
    con = get_connection(str(database_path))
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE answers (
    id INTEGER PRIMARY KEY,
    question_id INTEGER UNIQUE,
    answer TEXT

            )
        """) 

    cur.execute(
            "INSERT INTO answers (question_id, answer) VALUES (?, ?)",
            (101, "The answer is 42")
            )

    cur.execute(
            "INSERT INTO answers(question_id, answer) VALUES (?,?)",
            (102, "The answer is 100")
            )
    
    con.commit()
    con.close()

    return database_path



def test_answers(test_database, monkeypatch):

    monkeypatch.setattr(
            "main.get_answers",
            lambda: get_answers(str(test_database))
            )
                
    response = client.get('/answers')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0][2] == "The answer is 42" 
    assert response.json()[1][2] == "The answer is 100"

