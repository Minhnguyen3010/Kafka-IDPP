# producer/fake_data_producer.py

from kafka import KafkaProducer
import json
import time
import random
from config.kfk_config import KAFKA_BOOTSTRAP_SERVERS, ORG_TOPIC


def start_producer():
    # Khởi tạo Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    print(f"[INFO] Producer started, sending to topic '{ORG_TOPIC}'...")

    while True:
        # Sinh dữ liệu giả
        fake_data = {
            "TAG_ID": random.randint(1, 100),
            "Org_Time": time.time(),
            "Col_Time": time.time(),
            "Value": round(random.uniform(0, 100), 2),
        }

        # Gửi vào Kafka topic 'org'
        producer.send(ORG_TOPIC, fake_data)
        print(f"[SENT] {fake_data}")

        # Delay để mô phỏng dữ liệu streaming
        time.sleep(2)


if __name__ == "__main__":
    start_producer()
