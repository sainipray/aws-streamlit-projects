# AWS Streamlit Projects

## Overview

This repository contains various projects leveraging AWS and machine learning services to address different use cases. The central entry point allows you to navigate between the projects: Face Recognition, Text Extraction from Audio, Text Extraction from Images, SQS Manager, Lambda Function Manager, and S3 Manager.

## Projects

### 1. Face Recognition

**Description:**
Detect and recognize faces in images for various applications, such as security, identity verification, or user interaction enhancements.

**Key Features:**

- Face detection and recognition using AWS Rekognition.
- Integration with a web interface for image upload and face detection.
- Ability to identify and label known individuals from a database of faces.

**Technology Stack:**

- AWS Rekognition
- Streamlit
- PIL (Python Imaging Library)
- Boto3 (AWS SDK for Python)

### 2. Text Extraction from Audio

**Description:**
Convert spoken content from audio files into text for transcription services, content indexing, accessibility improvements, and more.

**Key Features:**

- Audio file upload and processing.
- Transcription of audio using AWS Transcribe.
- Retrieval and display of transcripts from AWS S3.
- Real-time transcription capabilities.

**Technology Stack:**

- AWS Transcribe
- AWS S3
- Streamlit
- Requests library for HTTP requests
- Boto3

### 3. Text Extraction from Images

**Description:**
Extract text from images using Optical Character Recognition (OCR) to digitize printed or handwritten text for further processing, analysis, or archival purposes.

**Key Features:**

- Image upload and text extraction via the web interface.
- Utilization of AWS Textract for accurate OCR.
- Support for various image formats (JPG, PNG, etc.).

**Technology Stack:**

- AWS Textract
- Streamlit
- PIL (Python Imaging Library)
- Boto3

### 4. S3 Manager

**Description:**
Manage files in your AWS S3 buckets directly from the web interface. This includes uploading, listing, and generating presigned URLs for files.

**Key Features:**

- Upload files to your S3 bucket.
- Display and navigate the folder structure of your S3 bucket.
- Generate presigned URLs for secure access to files.
- Download files directly via presigned URLs.

**Technology Stack:**

- AWS S3
- Streamlit
- Boto3
- Base64 for encoding SVG images (for folder icons)

### 5. SQS Manager

**Description:**
Manage AWS Simple Queue Service (SQS) queues directly from the web interface. This includes creating, listing, sending messages, and deleting queues.

**Key Features:**

- List all SQS queues in your AWS account.
- Create new queues and delete existing ones.
- Send and receive messages from SQS queues.
- Ability to delete individual messages from a queue.

**Technology Stack:**

- AWS SQS
- Streamlit
- Boto3

### 6. Lambda Function Manager

**Description:**
Create and manage AWS Lambda functions using a user-friendly interface. This feature allows you to deploy serverless functions directly from the application.

**Key Features:**

- Create Lambda functions with custom Python code.
- Automated IAM role creation with basic Lambda execution permissions.
- Real-time function deployment and testing.
- Retrieve and manage function configurations.

**Technology Stack:**

- AWS Lambda
- AWS IAM
- Streamlit
- Boto3

## Getting Started

### Prerequisites

- Python 3.9 or higher
- AWS account with appropriate permissions for S3, SQS, Lambda, and IAM services
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
   Create a `.env` file in the root directory with the following content:
   ```dotenv
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_DEFAULT_REGION=your_default_region
   S3_BUCKET_NAME=your_s3_bucket_name
   IAM_ROLE_NAME=lambda-role # we need role name that have lambda access
   ```
   Replace the placeholder values with your actual AWS credentials and S3 bucket name.

4. **Run the Projects:**
   Use the central `main.py` to navigate and run the projects. In the root directory, run:
   ```bash
   streamlit run main.py
   ```
   You will see a sidebar where you can select which project to run: "Face Recognition", "Text Extraction from Image", "Text Extraction from Audio Files", "SQS Manager", "Lambda Function Manager", or "S3 Manager".

## Usage

For detailed instructions on using each project, refer to the individual project directories:

- **Text Extraction from Image**: `text_extraction_from_image/`
- **Text Extraction from Audio**: `text_extraction_from_audio/`
- **Face Recognition**: `face_recognition/`
- **SQS Manager**: `sqs_messages/`
- **Lambda Function Manager**: `lambda_api/`
- **S3 Manager**: `s3_file_manager/`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

