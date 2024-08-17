import streamlit as st


def styled_header(text):
    """Display a styled header for the Streamlit app."""
    st.markdown(f"### {text}", unsafe_allow_html=True)


def styled_subheader(text):
    """Display a styled subheader for the Streamlit app."""
    st.markdown(f"#### {text}", unsafe_allow_html=True)


def divider():
    """Insert a horizontal line for separation."""
    st.markdown("---")
