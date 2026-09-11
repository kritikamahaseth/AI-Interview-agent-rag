from fastapi import FastAPI
from pydantic import BaseModel
import uuid

from questions import questions
from faiss_index import search_answer

app = FastAPI()

# Store multiple interview sessions
interview_sessions = {}


class AnswerRequest(BaseModel):
    session_id: str
    answer: str


def evaluate(score):

    if score < 0.5:
        return 10, "Excellent answer. Very close to the expected explanation."

    elif score < 1.5:
        return 6, "Partially correct answer but missing some key details."

    else:
        return 2, "Answer seems incorrect or unrelated to the concept."


@app.get("/")
def home():
    return {"message": "AI Interview Agent API Running"}


@app.get("/start")
def start_interview():

    session_id = str(uuid.uuid4())

    interview_sessions[session_id] = {
        "question_index": 0,
        "score": 0
    }

    first_question = questions[0]["question"]

    return {
        "session_id": session_id,
        "question": first_question
    }


@app.post("/answer")
def submit_answer(request: AnswerRequest):

    session_id = request.session_id
    user_answer = request.answer

    if session_id not in interview_sessions:
        return {"error": "Invalid session_id"}

    session = interview_sessions[session_id]

    reference_answer, similarity_score = search_answer(user_answer)

    marks, feedback = evaluate(similarity_score)

    session["score"] += marks
    session["question_index"] += 1

    response = {
        "reference_answer": reference_answer,
        "feedback": feedback,
        "score": marks
    }

    if session["question_index"] < len(questions):

        next_question = questions[session["question_index"]]["question"]
        response["next_question"] = next_question

    else:

        response["final_score"] = session["score"]
        response["message"] = "Interview completed."

    return response