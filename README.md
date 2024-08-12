# AWS Streamlit Projects

## Overview

This repository contains various projects utilizing AWS and machine learning services to address different use cases. The central entry point allows you to navigate between the projects: Face Recognition, Text Extraction from Audio, and Text Extraction from Images.

## Projects

### 1. Face Recognition

**Description:**
Detect and recognize faces in images for applications.

**Key Features:**
- Face detection and recognition using AWS Rekognition.
- Integration with a web interface for image upload and face detection.

**Technology Stack:**
- AWS Rekognition
- Streamlit
- PIL (Python Imaging Library)

### 2. Text Extraction from Audio

**Description:**
Convert spoken content from audio files into text for transcription services, content indexing, or accessibility improvements.

**Key Features:**
- Audio file upload and processing.
- Transcription of audio using AWS Transcribe.
- Retrieval of transcripts from AWS S3.

**Technology Stack:**
- AWS Transcribe
- AWS S3
- Requests library for HTTP requests

### 3. Text Extraction from Images

**Description:**
Extract text from images using Optical Character Recognition (OCR) to digitize printed or handwritten text for further processing and analysis.

**Key Features:**
- Image upload and text extraction.
- Utilization of AWS Textract for OCR.

**Technology Stack:**
- AWS Textract
- Streamlit for UI

## Getting Started

### Prerequisites

- Python 3.9 or higher
- AWS account with appropriate permissions
- Required Python libraries (installed via `pip`)
- .env file with AWS credentials and configuration

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sainipray/aws-streamlit-projects.git
   cd aws-streamlit-projects
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials:**
   Create a .env file in the root directory with the following content:
   ```dotenv
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_DEFAULT_REGION=your_default_region
   S3_BUCKET_NAME=your_s3_bucket_name
   ```

4. **Run the Projects:**
   Use the central `main.py` to navigate and run the projects. In the root directory, run:
   ```bash
   streamlit run main.py
   ```
   You will see a sidebar where you can select which project to run: "Text Extraction from Image", "Text Extraction from Audio Files", or "Face Recognition".

## Usage

For detailed instructions on using each project, refer to the individual project directories:
- **Text Extraction from Image**: text_extraction_from_image/
- **Text Extraction from Audio**: text_extraction_from_audio/
- **Face Recognition**: face_recognition/

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
