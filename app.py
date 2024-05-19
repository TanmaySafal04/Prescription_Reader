from src.Prescription_Reader.pipeline.OCR import read_text_from_prescription,show_detection_with_score
import gradio as gr
import matplotlib.pyplot as plt
from src.Prescription_Reader.pipeline.text_to_audio import generate_audio
from src.Prescription_Reader.pipeline.refine_text_output import refined_output
import base64
import streamlit as st
from PIL import Image
import numpy as np

# Image input section
st.header("Image Uploader")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# extracted_text=""
# boxes=[]
# texts=[]
# scores=[]
# image_np=np.array(image_np)
if uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    #st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert image to numpy array
    image_np = np.array(image)
    #print(read_text_from_prescription(image_np))
    extracted_text,boxes,texts,scores = read_text_from_prescription(image_np)

    st.write(f"Recognized Text from Image: {extracted_text}" ) 

    annotated_img = show_detection_with_score(image_np,boxes,texts,scores) 
    st.image(annotated_img, caption="Uploaded Image", use_column_width=True) 
    print("*******************")
    print(extracted_text)
 
#extracted_text,boxes,texts,scores = read_text_from_prescription(image_np)


#st.image(im_show, caption='OCR Result', use_column_width=True)

# # Displays detcted texts
# bb_annotation = show_detection_with_score(image_np,boxes,texts,scores)
# plt.figure(figsize=(100,100))
# display_img = plt.imshow(bb_annotation)
# st.image(display_img, caption="Uploaded Image", use_column_width=True)

# #Converts the BytesIO audio data to a base64-encoded string.
# #Embeds the base64-encoded audio data in an HTML <audio> element and uses st.markdown to render it.

# def audio_player(audio_data):
#     audio_base64 = base64.b64encode(audio_data.read()).decode('utf-8')
#     audio_html = f'''
#         <audio controls>
#             <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
#         </audio>
#     '''
#     st.markdown(audio_html, unsafe_allow_html=True)


# if st.button("Generate and Play Audio"):
#         audio_io = generate_audio(text_input)
#         audio_player(audio_io)








