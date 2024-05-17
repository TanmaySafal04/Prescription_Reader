import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

def generate_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_io = BytesIO()
    tts.write_to_fp(audio_io)
    audio_io.seek(0)
    return audio_io

def audio_player(audio_data):
    audio_base64 = base64.b64encode(audio_data.read()).decode('utf-8')
    audio_html = f'''
        <audio controls>
            <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
        </audio>
    '''
    st.markdown(audio_html, unsafe_allow_html=True)

st.title("Text to Speech with gTTS and Streamlit")

text_input = st.text_area("Enter text to convert to speech", "Hello, how are you today?")
language = st.selectbox("Select language", ("en", "fr", "es"))

if st.button("Generate and Play Audio"):
    audio_io = generate_audio(text_input, language)
    audio_player(audio_io)
