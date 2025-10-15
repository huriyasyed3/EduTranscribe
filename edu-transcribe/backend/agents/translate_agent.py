from agent import function_tool
from services.openai_service import openai

@function_tool
def translate_text(text: str , target_lang : str) -> str:
     # Use OpenAI chat completion for translation
     resp = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"system","content":f"Translate into {target_lang}."}
            {"role":"user", "content":text}
        ]
     )
     return resp.choices[0].messages.content