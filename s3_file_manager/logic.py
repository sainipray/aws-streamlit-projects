import boto3
import streamlit as st

s3_client = boto3.client('s3')


def list_files_in_s3(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            return [obj['Key'] for obj in response['Contents']]
        else:
            return []
    except Exception as e:
        st.error(f"Failed to list files: {e}")
        return []


def upload_file_to_s3(file, bucket_name):
    try:
        s3_client.upload_fileobj(file, bucket_name, file.name)
    except Exception as e:
        st.error(f"Failed to upload file: {e}")
