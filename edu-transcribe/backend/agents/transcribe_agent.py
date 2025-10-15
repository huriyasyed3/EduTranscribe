from agents import function_tool
from services.openai_service import openai

@function_tool 
def transcribe_audio(audio_url : str) -> str:
     # Use OpenAI audio transcription API
     resp = openai.audio.transcriptions.create(
        file= audio_url,
        model = "whisper-1",

     )

     return = resp.text