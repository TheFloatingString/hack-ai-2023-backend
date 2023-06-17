import os
import requests

def generate_audio(text_input, filepath):
    CHUNK_SIZE = 1024
    URL = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    HEADERS = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": os.getenv("ELEVEN_API_KEY")
    }

    data = {
        "text": text_input,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    resp = requests.post(URL, json=data, headers=HEADERS)

    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)