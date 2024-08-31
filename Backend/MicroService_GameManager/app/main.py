from fastapi import FastAPI, HTTPException
from app.trivia_service import TriviaService
from app.data_handler import DataHandler
from pydantic import BaseModel


class QuestionModel(BaseModel):
    question_id: str
    question: str
    choices: list
    correct_answer: str


app = FastAPI()
trivia_service = TriviaService
data_handler = DataHandler


@app.post("/questions/")
def create_question(question: QuestionModel):
    if not question.choices or len(question.choices) < 2:
        raise HTTPException(status_code=400, detail="At least two choices are required")
    if question.correct_answer not in question.choices:
        raise HTTPException(status_code=400, detail="Correct answer must be one of the choices ")
    data_handler.add_question(question.dict())
    return {"msg": "Question added"}


@app.get("/questions/")
def get_question():
    question = data_handler.get_random_question()
    if not question:
        raise HTTPException(status_code=400, detail="No question available")


@app.post("/answer/")
def check_answer(question_id: str, answer: str):
    if not trivia_service.is_valid_answer(question_id, answer):
        raise HTTPException(status_code=400, detail="Invalid answer.")
    correct = trivia_service.check_answer(question_id, answer)
    return {"correct", correct}


@app.get("/score/{user_id}")
def get_score(user_id: str):
    score = trivia_service.get_score(user_id)
    if not score:
        raise HTTPException(status_code=400, detail="Problem with score fetching")
    return {"Score": score}


@app.post("/score/{user_id}")
def update_score(user_id: str, score: int):
    if score < 0:
        raise HTTPException(status_code=400, detail="score cannot be be negative.")
    trivia_service.set_score(user_id, score)
    return {"msg", "Score updated."}
