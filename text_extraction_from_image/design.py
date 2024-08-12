import streamlit as st
from PIL import Image


def render_image_upload():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        return image
    return None


def render_text_extraction(text):
    st.subheader("Extracted Text")
    st.text_area("Text from Image", value=text, height=300)
