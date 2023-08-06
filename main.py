from fastapi import FastAPI
from app.routes.message_route import router as message_router
import app.queues.message_queue
app = FastAPI()

@app.get("/_healthz")
async def health_check():
    return {"ok":True}

app.include_router(message_router)