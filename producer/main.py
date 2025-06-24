from fastapi import FastAPI
from confluent_kafka import Producer
from .config import KAFKA_BROKER, KAFKA_TOPIC

app = FastAPI()
producer = Producer({"bootstrap.servers": KAFKA_BROKER})

@app.post("/produce/")
def produce_message(message: str):
    producer.produce(KAFKA_TOPIC, message.encode("utf-8"))
    producer.flush()
    return {"status": "Message sent", "message": message}
