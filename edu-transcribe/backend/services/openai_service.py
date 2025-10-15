from agents import Agent , Runner
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

openai = OpenAI()
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
      return result.final_output