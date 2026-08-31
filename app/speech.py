from pathlib import Path

from openai import OpenAI

client = OpenAI()


def text_to_speech(text: str, output_path: str = "speech.mp3") -> str:
    speech_file_path = Path(output_path)

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
    ) as response:
        response.stream_to_file(speech_file_path)

    return str(speech_file_path)