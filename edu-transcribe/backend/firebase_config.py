import firebase_admin
from firebase_admin import credentials, firestore, storage, auth

# Service account credentials load karo
cred = credentials.Certificate("config/firebase-service.json")

# Firebase app initialize karo
firebase_admin.initialize_app(cred, {
    'storageBucket': 'YOUR_PROJECT_ID.appspot.com'
})

# Firestore client
db = firestore.client()

# Storage bucket
bucket = storage.bucket()
