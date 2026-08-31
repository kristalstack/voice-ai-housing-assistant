from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from app.llm import get_ai_response
from app.speech import text_to_speech, speech_to_text

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
    answer = get_ai_response(request.question)

    return {
        "question": request.question,
        "answer": answer
    }

@app.post("/speak")
def speak_text(request: QuestionRequest):
    audio_path = text_to_speech(request.question)

    return {
        "text": request.question,
        "audio_file": audio_path
    }

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())

    transcription = speech_to_text(temp_path)

    return {
        "filename": file.filename,
        "transcription": transcription
    }