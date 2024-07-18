# Example filename: main.py
import os
import httpx
from dotenv import load_dotenv
import threading

from deepgram import (
    DeepgramClient,
    LiveTranscriptionEvents,
    LiveOptions,
)

load_dotenv()

# URL for the realtime streaming audio you would like to transcribe
"""URL = "http://stream.live.vc.bbcmedia.co.uk/bbc_world_service"

API_KEY = os.getenv("DG_API_KEY")


def main():
    try:
        # STEP 1: Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        # STEP 2: Create a websocket connection to Deepgram
        dg_connection = deepgram.listen.live.v("1")

        # STEP 3: Define the event handlers for the connection
        def on_message(self, result, **kwargs):
            sentence = result.channel.alternatives[0].transcript
            if len(sentence) == 0:
                return
            print(f"speaker: {sentence}")

        def on_metadata(self, metadata, **kwargs):
            print(f"\n\n{metadata}\n\n")

        def on_error(self, error, **kwargs):
            print(f"\n\n{error}\n\n")

        # STEP 4: Register the event handlers
        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        dg_connection.on(LiveTranscriptionEvents.Metadata, on_metadata)
        dg_connection.on(LiveTranscriptionEvents.Error, on_error)

        # STEP 5: Configure Deepgram options for live transcription
        options = LiveOptions(
            model="nova-2", 
            language="en-US", 
            smart_format=True,
            )
        
        # STEP 6: Start the connection
        dg_connection.start(options)

        # STEP 7: Create a lock and a flag for thread synchronization
        lock_exit = threading.Lock()
        exit = False

        # STEP 8: Define a thread that streams the audio and sends it to Deepgram
        def myThread():
            with httpx.stream("GET", URL) as r:
                for data in r.iter_bytes():
                    lock_exit.acquire()
                    if exit:
                        break
                    lock_exit.release()

                    dg_connection.send(data)

        # STEP 9: Start the thread
        myHttp = threading.Thread(target=myThread)
        myHttp.start()

        # STEP 10: Wait for user input to stop recording
        input("Press Enter to stop recording...\n\n")

        # STEP 11: Set the exit flag to True to stop the thread
        lock_exit.acquire()
        exit = True
        lock_exit.release()

        # STEP 12: Wait for the thread to finish
        myHttp.join()

        # STEP 13: Close the connection to Deepgram
        dg_connection.finish()

        print("Finished")

    except Exception as e:
        print(f"Could not open socket: {e}")
        return"""

# Example filename: main.py
"""import os
import pyaudio
import threading
import time
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    LiveTranscriptionEvents,
    LiveOptions,
)

load_dotenv()

API_KEY = os.getenv("DG_API_KEY")

# Audio stream parameters
CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (Hz)

def main():
    while True:
        try:
            # STEP 1: Create a Deepgram client using the API key
            deepgram = DeepgramClient(API_KEY)

            # STEP 2: Create a websocket connection to Deepgram
            dg_connection = deepgram.listen.live.v("1")

            # STEP 3: Define the event handlers for the connection
            def on_message(self, result, **kwargs):
                sentence = result["channel"]["alternatives"][0]["transcript"]
                if len(sentence) == 0:
                    return
                print(f"speaker: {sentence}")

            def on_metadata(self, metadata, **kwargs):
                print(f"\n\n{metadata}\n\n")

            def on_error(self, error, **kwargs):
                print(f"\n\n{error}\n\n")

            # STEP 4: Register the event handlers
            dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
            dg_connection.on(LiveTranscriptionEvents.Metadata, on_metadata)
            dg_connection.on(LiveTranscriptionEvents.Error, on_error)

            # STEP 5: Configure Deepgram options for live transcription
            options = LiveOptions(
                model="nova-2",
                language="en-US",
                smart_format=True,
            )

            # STEP 6: Start the connection
            dg_connection.start(options)

            # STEP 7: Create a lock and a flag for thread synchronization
            lock_exit = threading.Lock()
            exit_flag = False

            # STEP 8: Define a thread that streams the audio from the microphone and sends it to Deepgram
            def myThread():
                p = pyaudio.PyAudio()
                stream = p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)

                while True:
                    lock_exit.acquire()
                    if exit_flag:
                        break
                    lock_exit.release()

                    data = stream.read(CHUNK)
                    dg_connection.send(data)

                stream.stop_stream()
                stream.close()
                p.terminate()

            # STEP 9: Start the thread
            myHttp = threading.Thread(target=myThread)
            myHttp.start()

            # STEP 10: Wait for user input to stop recording
            input("Press Enter to stop recording...\n\n")

            # STEP 11: Set the exit flag to True to stop the thread
            lock_exit.acquire()
            exit_flag = True
            lock_exit.release()

            # STEP 12: Wait for the thread to finish
            myHttp.join()

            # STEP 13: Close the connection to Deepgram
            dg_connection.finish()

            print("Finished")
            break

        except Exception as e:
            print(f"Error: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    main()"""

import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import os
from dotenv import load_dotenv
from deepgram import DeepgramClient, SpeakOptions

load_dotenv()
filename = "output.wav"

def TTS(text):
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        # STEP 3: Call the save method on the speak property
        response = deepgram.speak.v1.save(filename, SPEAK_OPTIONS, options)
        return filename
    except Exception as e:
        print(f"Exception: {e}")
        return filename

if __name__ == "__main__":
    TTS("Hello this is a test")




