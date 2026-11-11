from fastapi import FastAPI
from SQLite import get_answers

app = FastAPI()

@app.get("/questions")

def get_questions():
    
    questions = [ 
                 {"number": 1, "text": "Calculate the area of a circle"},

                 {"number": 2, "text": "What is square root of 25?"},

                 {"number": 3, "text": "Find the height of this triangle"}

                 ]
                

    return questions



@app.get('/answers')

def read_anwsers():
    return get_answers()
