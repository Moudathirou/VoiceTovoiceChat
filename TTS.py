
"""def TTS(text):
    try:
        # STEP 1: Create a ElevenLabs client using the API key from environment variables
        elevenlabs = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        # STEP 2: Configure the voice settings
        voice = Voice(
            voice_id='aQROLel5sQbj1vuIVi6B',  # Replace with your desired voice ID
            settings=VoiceSettings(stability=0.5, similarity_boost=0.75, style=0.0, use_speaker_boost=True)
        )

        # STEP 3: Generate the audio from the text
        audio = elevenlabs.generate(
            text=text,
            voice=voice,
            model="eleven_multilingual_v2"
        )

        # STEP 4: Save the audio to a file
        filename = "static/output.wav"
        save(audio, filename)
      

        return filename
    except Exception as e:
        print(f"Exception: {e}")
        return None"""

import os
from dotenv import load_dotenv
from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs

load_dotenv()

def TTS(text):
    try:
        elevenlabs = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        voice = Voice(
            voice_id='aQROLel5sQbj1vuIVi6B',  # Replace with your desired voice ID
            settings=VoiceSettings(stability=0.5, similarity_boost=0.75, style=0.0, use_speaker_boost=True)
        )

        audio = elevenlabs.generate(
            text=text,
            voice=voice,
            model="eleven_multilingual_v2"
        )

        filename = "output.wav"
        filepath = os.path.join("static", filename)
        save(audio, filepath)

        return filename
    except Exception as e:
        print(f"Exception: {e}")
        return None








