import boto3

# Initialize SQS client
sqs_client = boto3.client('sqs')


def list_queues():
    """List all SQS queues."""
    response = sqs_client.list_queues()
    return response.get('QueueUrls', [])


def create_queue(queue_name):
    """Create an SQS queue and return the queue URL."""
    response = sqs_client.create_queue(QueueName=queue_name)
    return response['QueueUrl']


def send_message(queue_url, message_body):
    """Send a message to the specified SQS queue."""
    response = sqs_client.send_message(QueueUrl=queue_url, MessageBody=message_body)
    return response['MessageId']


def receive_messages(queue_url):
    """Receive messages from the specified SQS queue."""
    response = sqs_client.receive_message(QueueUrl=queue_url)
    return response.get('Messages', [])


def delete_message(queue_url, receipt_handle):
    """Delete a specific message from the SQS queue."""
    sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)


def delete_queue(queue_url):
    """Delete the specified SQS queue."""
    sqs_client.delete_queue(QueueUrl=queue_url)
