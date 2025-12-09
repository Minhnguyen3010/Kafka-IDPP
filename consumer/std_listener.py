# consumer/std_consumer.py

from kafka import KafkaConsumer
import json
import redis
from config.kfk_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    STD_TOPIC,
    AUTO_OFFSET_RESET,
)

# Khởi tạo Redis client (tự sửa host nếu Docker)
redis_client = redis.Redis(host="localhost", port=6379, db=0)


def start_std_consumer():
    consumer = KafkaConsumer(
        STD_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset=AUTO_OFFSET_RESET,
        enable_auto_commit=True,
        group_id="std-consumer-group",
    )

    print(f"[INFO] STD Consumer is listening on topic '{STD_TOPIC}'...")

    for message in consumer:
        std_data = message.value
        print(f"[STD RECEIVED] {std_data}")

        # --- Đẩy vào Redis ---
        # Ví dụ: Key = TAG_ID ; Value = JSON
        tag_id = std_data.get("TAG_ID", "unknown")
        redis_client.set(f"TAG:{tag_id}", json.dumps(std_data))

        print(f"[REDIS SAVED] TAG:{tag_id} -> {std_data}")
