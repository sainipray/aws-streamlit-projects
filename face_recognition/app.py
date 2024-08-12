import streamlit as st
from PIL import Image

from .design import render_image_upload, render_faces
from .logic import detect_faces


def main():
    st.title("Face Recognition from Image")

    uploaded_file = render_image_upload()
    if uploaded_file is not None:
        # Convert the uploaded file to a PIL Image
        image = Image.open(uploaded_file)

        # Detect faces
        faces, processed_image = detect_faces(image)

        # Render faces on the image
        render_faces(processed_image, faces)
