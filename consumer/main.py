from fastapi import FastAPI
from confluent_kafka import Consumer
from .config import KAFKA_BROKER, KAFKA_TOPIC

app = FastAPI()

consumer = Consumer({
    "bootstrap.servers": KAFKA_BROKER,
    "group.id": "consumer-group",
    "auto.offset.reset": "earliest"
})
consumer.subscribe([KAFKA_TOPIC])

@app.get("/consume/")
def consume_message():
    msg = consumer.poll(1.0)
    if msg is None:
        return {"message": "No messages available"}
    elif msg.error():
        return {"error": msg.error().str()}
    else:
        return {"message": msg.value().decode("utf-8")}
