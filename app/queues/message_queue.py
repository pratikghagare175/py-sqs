from app.configs.sqs_config import sqs_client, queue_url

response = sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
messages = response.get('Messages', [])
if messages:
    for message in messages:
        print('Received message:', message['Body'])
        # Optionally, delete the message from the queue after processing
        sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])