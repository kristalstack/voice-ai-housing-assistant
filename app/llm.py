import os

from dotenv import load_dotenv
from openai import OpenAI
from app.knowledge import load_knowledge


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_response(question: str) -> str:
    knowledge = load_knowledge()
    response = client.responses.create(
        model="gpt-5.6-sol",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a voice AI assistant that explains U.S. affordable housing "
                    "programs clearly and accurately. Answer in natural spoken language. "
                    "Do not use markdown, headings, bullet points, asterisks, or formatting "
                    "that would sound unnatural when read aloud. Keep answers concise, warm, "
                    "and easy to follow. Use the knowledge provided below as your primary "
                    "source. If the answer is not supported by the provided knowledge, say "
                    "that you do not have enough information instead of guessing. "
                    "If information may vary by location or housing authority, say so clearly.\n\n"
                    f"KNOWLEDGE BASE:\n{knowledge}"
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.output_text