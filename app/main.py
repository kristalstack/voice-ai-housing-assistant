from fastapi import FastAPI

app = FastAPI(
    title="Voice AI Housing Assistant",
    description="A Voice AI agent that helps users understand affordable housing programs.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Voice AI Housing Assistant is running."}

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": "This is a placeholder response."
    }