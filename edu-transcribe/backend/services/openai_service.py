from agents import Agent , Runner
from dotenv import load_dotenv
from openai import OpenAI
import asyncio
import os
load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
edu_agent = Agent(
    name = "EduTranscribeAgent",
    instructions="""
    You are EduTranscribe Agent. Your job is to:
    1. Transcribe audio/video input to text.
    2. Translate the text to a user-specified language.
    3. Summarize into structured notes.
    4. (Optionally) Generate voice via TTS.
    5. Return a JSON object with fields: transcription, translation, notes, audio_url (if TTS).
    """,
)


async def run_edu_agent(prompt_input: str):
 # prompt_input might include video URL, target language, etc.
      result = await Runner.run(edu_agent , prompt_input)
      return print(result.final_output)
      print("hello")

asyncio.run(run_edu_agent("https://youtu.be/vD0E3EUb8-8?si=ED0wc52vVx1OGkw1"))