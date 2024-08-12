import streamlit as st


def render_audio_upload():
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])
    if uploaded_file:
        st.audio(uploaded_file, format='audio/wav')
        return uploaded_file
    return None


def render_text_extraction(text):
    st.subheader("Extracted Text")
    st.text_area("Text from Audio", value=text, height=300)
