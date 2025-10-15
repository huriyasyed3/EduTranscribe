import asyncio
from services.openai_service import run_edu_agent
from services.firebase_service import store_results

async def process_lecture(audio_url: str, target_lang: str, user_id: str):
    # Prepare prompt input
    prompt_input = f"Audio URL: {audio_url}\nTarget language: {target_lang}\n"
    result = await run_edu_agent(prompt_input)
    # result expected JSON with transcription, translation, notes, audio_url
    # Store in Firebase
    await store_results(user_id, result)

if __name__ == "__main__":
    # test
    asyncio.run(process_lecture("https://someurl/video.mp3", "Urdu", "user123"))
