import streamlit as st
import speech_recognition as sr
from groq_ai import *
from TTS import *
import base64
import tempfile

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
           <audio controls autoplay="true">
           <source src ="data:audio/mp3;base64,{b64}" type="audio/mp3">
           </audio>
           """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        st.write("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        st.write("Listening...")
        audio = recognizer.listen(source)
    
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    
    return response

def main():
    st.title("Talking Assistant with Groq-AI")
    st.write("Click 'Speak' to start recording and 'Stop' to stop recording.")
    
    if 'listening' not in st.session_state:
        st.session_state.listening = False

    start_recording = st.button("Speak")
    stop_recording = st.button("Stop")

    if start_recording:
        st.session_state.listening = True
    
    if stop_recording:
        st.session_state.listening = False
    
    if st.session_state.listening:
        st.write("Recording...")
        speech_result = recognize_speech_from_microphone()
        
        if speech_result["transcription"]:
            st.write(f"You said: {speech_result['transcription']}")
            response = generate_response(speech_result["transcription"])
            file = TTS(response)
            autoplay_audio(file)
        elif speech_result["error"]:
            st.write(f"Error: {speech_result['error']}")

if __name__ == "__main__":
    main()
