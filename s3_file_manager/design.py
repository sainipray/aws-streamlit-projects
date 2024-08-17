import base64
import os

import boto3
import streamlit as st
from botocore.exceptions import NoCredentialsError

s3_client = boto3.client('s3')


def render_upload_form():
    file = st.file_uploader("Choose a file to upload", type=None)
    return file


def load_svg(file_path):
    # Load the SVG file and encode it in Base64
    with open(file_path, "r") as f:
        svg_content = f.read()
    encoded_svg = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{encoded_svg}"


def render_file_list(files):
    folder_structure = build_folder_structure(files)
    st.write("Files in S3 bucket:")
    # Start with the root folder
    render_folder(folder_structure)


def build_folder_structure(files):
    folder_structure = {}
    for file in files:
        parts = file.split('/')
        current = folder_structure
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
    return folder_structure


def generate_presigned_url(bucket_name, file_key):
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': file_key},
            ExpiresIn=3600  # URL expires in 1 hour
        )
        return response
    except NoCredentialsError:
        st.error("Credentials not available")
        return None
    except Exception as e:
        st.error(f"Failed to generate presigned URL: {e}")
        return None


def render_folder(folder, indent=0, parent_path=''):
    folder_icon = load_svg("data/folder.svg")
    for name, content in folder.items():
        if content:
            st.markdown(f'<div style="margin-left: {indent * 20}px; font-size: 16px;">'
                        f'<img src="{folder_icon}" width="16" height="16"> <b>{name}</b></div>',
                        unsafe_allow_html=True)
            # Expandable folder
            render_folder(content, indent + 1, parent_path + name + '/')
        else:
            file_key = parent_path + name
            file_url = generate_presigned_url(os.getenv('S3_BUCKET_NAME'), file_key)
            st.markdown(f'<div style="margin-left: {indent * 20}px; font-size: 14px;">'
                        f'📄 <a href="{file_url}" download>{name}</a></div>',
                        unsafe_allow_html=True)
