import streamlit as st
from PIL import ImageDraw


def render_image_upload():
    return st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


def render_faces(image, faces):
    # Create an ImageDraw object from a PIL image
    draw = ImageDraw.Draw(image)

    for face in faces:
        left, top, right, bottom = face
        # Draw a rectangle around the face
        draw.rectangle([(left, top), (right, bottom)], outline="red", width=3)

    # Display the image with the drawn rectangles
    st.image(image, caption="Detected Faces", use_column_width=True)
