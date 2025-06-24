# Real-time Notifications with WebSockets

This project implements **real-time notifications** using **WebSockets** in FastAPI.
Implements a WebSocket-based real-time notification system to send instant alerts to users.

```bash
event-microservices/
│── producer/
│   ├── main.py
│   ├── config.py
│── consumer/
│   ├── main.py
│   ├── config.py
│── Dockerfile
│── docker-compose.yml
│── .env
│── requirements.txt
│── README.md
```

## 🚀 Features
- Real-time push notifications via WebSockets

## 📌 Installation
```bash
cd 10_real_time_notifications
pip install -r requirements.txt
```

## 🏃 Running the API
```bash
uvicorn app.main:app --reload
```

## 🔍 WebSocket Example

- Connect to ws://localhost:8000/notify

- Send a message

- Receive a real-time update


---
## steps

### Step 1: Install Dependencies

```bash
pip install fastapi uvicorn confluent-kafka python-dotenv
```
### Step 2: Configure Kafka

```bash
KAFKA_BROKER=localhost:9092
KAFKA_TOPIC=test-topic
```
Load these environment variables in config.py:

### Step 3: Run Kafka, API, and Test

Start Kafka using Docker:
```bash
docker-compose up -d
```

Run the Producer API:

```bash
uvicorn producer.main:app --host 0.0.0.0 --port 8001 --reload

```
Run the Consumer API:

```bash
uvicorn consumer.main:app --host 0.0.0.0 --port 8002 --reload

```

#### Test Kafka Messaging
Send a Message
```bash
curl -X POST "http://localhost:8001/produce/" -H "Content-Type: application/json" -d '{"message": "Hello, Kafka!"}'

```
Retrieve a Message
```bash
curl -X GET "http://localhost:8002/consume/"

```
