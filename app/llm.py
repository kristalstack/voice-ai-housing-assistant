import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_response(question: str) -> str:
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
                    "and easy to follow. If information may vary by location or housing "
                    "authority, say so clearly."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.output_text