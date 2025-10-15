import os
import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET")
})

db = firestore.client()
bucket = storage.bucket()

async def upload_audio_file(audio_bytes: bytes, lang: str) -> str:
    blob = bucket.blob(f"audios/{lang}/{blob_name_here}.mp3")
    blob.upload_from_string(audio_bytes, content_type="audio/mp3")
    return blob.public_url

async def store_results(user_id: str, result: dict):
    doc_ref = db.collection("lectures").document(user_id)
    doc_ref.set({
        "transcription": result.get("transcription"),
        "translation": result.get("translation"),
        "notes": result.get("notes"),
        "audio_url": result.get("audio_url")
    })
