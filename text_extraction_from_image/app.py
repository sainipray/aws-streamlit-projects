import streamlit as st

from .design import render_image_upload, render_text_extraction
from .logic import extract_text_from_image


def main():
    st.title("Text Extraction from Image")

    image = render_image_upload()
    if image:
        text = extract_text_from_image(image)
        render_text_extraction(text)
