import streamlit as st
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
print(uploaded_image)
print(type(uploaded_image))
