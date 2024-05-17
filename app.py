from src.Prescription_Reader.pipeline.OCR import read_text_from_prescription,show_detection_with_score
import gradio as gr
import matplotlib.pyplot as plt
from src.Prescription_Reader.pipeline.text_to_audio import generate_audio
import base64
import streamlit as st



text_input =

def audio_player(audio_data):
    audio_base64 = base64.b64encode(audio_data.read()).decode('utf-8')
    audio_html = f'''
        <audio controls>
            <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
        </audio>
    '''
    st.markdown(audio_html, unsafe_allow_html=True)


if st.button("Generate and Play Audio"):
        audio_io = generate_audio(text_input)
        audio_player(audio_io)








