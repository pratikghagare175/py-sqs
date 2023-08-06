import boto3
from app.configs.env_config import AWS_ACCESS_KEY, AWS_ACCESS_SECRET

sqs_client = boto3.client(
"sqs", region_name="ap-south-1", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_ACCESS_SECRET
)

queue_name = 'my-queue'
response = sqs_client.create_queue(QueueName=queue_name)
queue_url = response['QueueUrl']
