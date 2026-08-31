# Voice AI Housing Assistant

A Voice AI assistant that helps users understand U.S. affordable housing programs through natural spoken conversation.

The application accepts a user's voice question, transcribes the audio, generates a grounded AI response, and converts that response back into speech.

## How It Works

Voice input → Speech-to-Text → Grounded LLM Response → Text-to-Speech → Voice response

## Current Features

- Voice question transcription
- AI-generated affordable housing responses
- Grounding with a local housing knowledge base
- Hallucination mitigation for unsupported questions
- Voice-optimized conversational responses
- Text-to-speech generation
- End-to-end voice interaction through FastAPI
- Interactive API documentation with Swagger UI
- Evaluation test cases and rubric

## Architecture

The project is organized into separate modules:

- `app/main.py` — FastAPI endpoints
- `app/llm.py` — LLM response generation
- `app/speech.py` — speech-to-text and text-to-speech
- `app/knowledge.py` — knowledge base loading
- `data/section8_basics.md` — grounded housing information
- `evals/` — evaluation cases, rubric, and runner

## Example

A user asks by voice:

> What is Section 8 and how do I apply?

The system:

1. Transcribes the audio.
2. Uses the housing knowledge base to generate a grounded response.
3. Avoids unsupported claims when information is missing.
4. Converts the response into spoken audio.

## Setup

Clone the repository and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and add your OpenAI API key:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Then open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Evaluation

The `evals/` directory contains test cases and a rubric focused on:

- Accuracy
- Grounding
- Clarity
- Voice suitability
- Safety and uncertainty

Run the evaluation cases with:

```bash
python -m evals.run_evals
```

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Speech-to-Text
- Text-to-Speech
- Swagger UI
- Git and GitHub