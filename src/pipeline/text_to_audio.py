import streamlit as st
from gtts import gTTS
from io import BytesIO

# This function generates audio from the given text using gTTS and returns a BytesIO object containing the audio data.
def generate_audio(text, lang='en'):

    tts = gTTS(text=text, lang=lang)
    
    audio_io = BytesIO()
    
    tts.write_to_fp(audio_io)
    
    audio_io.seek(0)
    
    return audio_io

