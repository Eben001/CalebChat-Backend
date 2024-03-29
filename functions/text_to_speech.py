import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")


# Eleven Labs
# Convert Text to Speech

def convert_text_to_speech(message):
    # Define data (BODY)
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
            "use_speaker_boost": True
        }
    }

    voice_liam = "TX3LPaxmHKxFdv7VOQHJ"

    # Constructing Headers and Endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json",
               "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_liam}/stream"

    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx response codes
    except requests.exceptions.RequestException as e:
        # Handle request exceptions, e.g., network errors
        print("Request Exception:", e)
        return None
    except Exception as e:
        # Handle other unexpected exceptions
        print("Unexpected Exception:", e)
        return None

    if response.status_code == 200:
        return response.content
    else:
        print("Unexpected Status Code:", response.status_code)
        return None
