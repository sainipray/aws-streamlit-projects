import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# Define project directories
PROJECTS = {
    "Text Extraction from Image": "text_extraction_from_image.app",
    "Text Extraction from Audio Files": "text_extraction_from_audio.app",
    "Face Recognition": "face_recognition.app",
    "S3 File Manager": "s3_file_manager.app",
    "SQS Messages": "sqs_messages.app",
    "Lambda API": "lambda_api.app"
}

# Sidebar for navigation
st.sidebar.title("Navigation")
project_selection = st.sidebar.radio("Select a Project", list(PROJECTS.keys()))

# Load and display the selected project
if project_selection:
    module = PROJECTS[project_selection]
    exec(f"from {module} import main as project_main")
    project_main()
