from agents import function_tool
from services.openai_service import openai
from services.firebase_service import upload_audio_file  # to store TTS output

@function_tool
def text_to_speech(text: str, lang: str) -> str:
    resp = openai.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    # Save the audio content to storage
    audio_bytes = resp.audio
    audio_url = upload_audio_file(audio_bytes, lang)
    return audio_url
