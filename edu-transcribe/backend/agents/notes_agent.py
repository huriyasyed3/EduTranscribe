from agents import function_tool
from services.openai_service import openai

@function_tool
def generate_notes(text: str) -> str:
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Generate structured lecture notes with bullet points."},
            {"role": "user", "content": text}
        ]
    )
    return resp.choices[0].message.content
