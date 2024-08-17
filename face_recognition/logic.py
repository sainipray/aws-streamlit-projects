import io

import boto3
from PIL import Image

rekognition_client = boto3.client('rekognition')


def detect_faces(image):
    # Convert the image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')  # Ensure the format is compatible with Rekognition
    img_bytes = img_bytes.getvalue()

    response = rekognition_client.detect_faces(
        Image={'Bytes': img_bytes},
        Attributes=['ALL']
    )

    # Reopen the image using PIL to calculate dimensions
    img = Image.open(io.BytesIO(img_bytes))
    width, height = img.size

    face_locations = []
    for faceDetail in response['FaceDetails']:
        box = faceDetail['BoundingBox']
        left = int(box['Left'] * width)
        top = int(box['Top'] * height)
        right = int((box['Left'] + box['Width']) * width)
        bottom = int((box['Top'] + box['Height']) * height)
        face_locations.append((left, top, right, bottom))  # Corrected the order

    return face_locations, img
