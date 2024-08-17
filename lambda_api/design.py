import streamlit as st


def styled_header(text):
    st.markdown(f"### {text}")


def styled_subheader(text):
    st.markdown(f"**{text}**")


def divider():
    st.markdown("---")
