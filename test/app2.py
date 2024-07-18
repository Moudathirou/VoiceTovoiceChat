import streamlit as st
from groq_ai import generate_response
from TTS import TTS
from audio_utils import autoplay_audio
from STT import create_stt_button, get_speech_text

def main():
    st.title("Talking Assistant with Groq-AI")
    st.write("Click 'Speak' to start recording and 'Stop' to stop recording.")

    # Create and display the STT button
    stt_button = create_stt_button()
    st.bokeh_chart(stt_button)

    # Get the speech text
    speech_text = get_speech_text(stt_button)

    if speech_text:
        response = generate_response(speech_text)
        file = TTS(response)
        autoplay_audio(file)

if __name__ == "__main__":
    main()
