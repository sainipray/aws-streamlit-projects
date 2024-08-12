import io
import os

import boto3
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    'textract',
    region_name=os.getenv('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def extract_text_from_image(image):
    # If the image is not a file-like object, skip opening it again
    if not isinstance(image, Image.Image):
        img = Image.open(image)
    else:
        img = image

    # Convert the image to RGB if it has an alpha channel (RGBA)
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Convert the image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    # Call AWS Textract to extract text from the image
    client = boto3.client('textract')

    response = client.detect_document_text(
        Document={'Bytes': img_bytes}
    )

    # Process the response as needed
    extracted_text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + '\n'

    return extracted_text
