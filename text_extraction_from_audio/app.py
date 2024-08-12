import streamlit as st

from .design import render_audio_upload, render_text_extraction
from .logic import extract_text_from_audio


def main():
    st.title("Text Extraction from Audio Files")

    audio = render_audio_upload()
    if audio:
        text = extract_text_from_audio(audio)
        render_text_extraction(text)
