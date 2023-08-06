from fastapi import APIRouter
from pydantic import BaseModel
from app.configs.sqs_config import sqs_client, queue_url

router = APIRouter()

class SetBody(BaseModel):
    message: str

@router.post("/message/send")
async def produce_message(body: SetBody):
    sqs_client.send_message(QueueUrl=queue_url, MessageBody=body.message);
    return {"message":"Sent Successfully"}
