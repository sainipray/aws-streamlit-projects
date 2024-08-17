import json
import os
import time

import boto3

transcribe_client = boto3.client('transcribe')


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


def download_transcript_from_s3(job_name):
    s3_client = boto3.client('s3')
    bucket_name = os.getenv('S3_BUCKET_NAME')
    s3_key = f'{job_name}.json'  # Assuming the transcript is saved as a JSON file in S3

    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
        transcript_data = response['Body'].read().decode('utf-8')
        transcript_json = json.loads(transcript_data)
        return transcript_json
    except Exception as e:
        print(f"Failed to download transcript: {e}")
        return None
