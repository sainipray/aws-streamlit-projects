import os
import time

import boto3
import requests
from dotenv import load_dotenv

load_dotenv()

transcribe_client = boto3.client(
    'transcribe',
    region_name=os.getenv('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def extract_text_from_audio(audio_file):
    audio_file.seek(0)
    job_name = str(int(time.time()))
    job_uri = upload_audio_to_s3(audio_file, job_name)

    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='en-US',
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        OutputBucketName=os.getenv('S3_BUCKET_NAME')
    )

    while True:
        status = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        time.sleep(30)

    transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    transcript_text = download_transcript_from_s3(transcript_uri)

    return transcript_text


def upload_audio_to_s3(audio_file, job_name):
    import boto3
    s3_client = boto3.client('s3')
    bucket_name = os.getenv('S3_BUCKET_NAME')
    s3_key = f'audio/{job_name}.mp3'
    s3_client.upload_fileobj(audio_file, bucket_name, s3_key)
    return f's3://{bucket_name}/{s3_key}'


def download_transcript_from_s3(transcript_uri):
    response = requests.get(transcript_uri)
    if response.status_code == 200:
        if response.content:  # Ensure content is present
            try:
                transcript_json = response.json()
                return transcript_json
            except ValueError as e:
                print("Error decoding JSON:", e)
                print("Response content:", response.content.decode('utf-8'))  # Print content for debugging
                return None
        else:
            print("Empty response content")
            return None
    else:
        print(f"Failed to download transcript. Status code: {response.status_code}")
        return None
