from src.pipeline.OCR import read_text_from_prescription,show_detection_with_score
from src.pipeline.refine_text_output import refined_output
import matplotlib.pyplot as plt
from src.pipeline.text_to_audio import generate_audio
from src.pipeline.refine_text_output import refined_output
from src.pipeline.cvt_to_RGB import convert_to_rgb
import base64
import streamlit as st
from PIL import Image
import numpy as np
#from dotenv import load_dotenv
#load_dotenv()

# Image input section
st.header("Upload Prescription Here")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Store uploaded image for further operation
    image = Image.open(uploaded_image)

    # Convert image to numpy array
    image_np = np.array(image)
    converted_img = convert_to_rgb(image_np)
   
    extracted_text,boxes,texts,scores = read_text_from_prescription(converted_img)

    st.write(f"Recognized Text from Image:\n {extracted_text}" ) 

    annotated_img = show_detection_with_score(converted_img,boxes,texts,scores) 

    im_show = Image.fromarray(annotated_img)
    st.image(im_show, caption="Uploaded Image", use_column_width=True)
    refined_text = refined_output(extracted_text) 

    st.write(f"Important information from the prescription:\n {refined_text}" )
    # print("*******************")
    # print(extracted_text)
 

# #Converts the BytesIO audio data to a base64-encoded string.
# #Embeds the base64-encoded audio data in an HTML <audio> element and uses st.markdown to render it.

    def audio_player(audio_data):
        audio_base64 = base64.b64encode(audio_data.read()).decode('utf-8')
        audio_html = f'''
            <audio controls>
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            </audio>
        '''
        st.markdown(audio_html, unsafe_allow_html=True)


    if st.button("Play Audio"):
            audio_io = generate_audio(refined_text)
            audio_player(audio_io)








