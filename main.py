from services.IA import IAService

from fastapi import FastAPI

app = FastAPI()

ia_service = IAService()

@app.get("/roadmap/{topic}")
def read_item(topic: str):
    return ia_service.create_roadmap(topic)