import os

import streamlit as st

from .design import render_upload_form, render_file_list
from .logic import list_files_in_s3, upload_file_to_s3


def main():
    st.title("S3 File Manager")

    s3_bucket_name = st.text_input("S3 Bucket Name", value=os.environ["S3_BUCKET_NAME"])

    # File upload form
    file = render_upload_form()

    if file and st.button("Upload to S3"):
        upload_file_to_s3(file, s3_bucket_name)
        st.success(f"File {file.name} uploaded successfully.")

    # List files in S3 bucket
    if st.button("List Files in S3"):
        files = list_files_in_s3(s3_bucket_name)
        render_file_list(files)
