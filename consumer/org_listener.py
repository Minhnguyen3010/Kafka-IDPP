# consumer/org_listener.py

from kafka import KafkaConsumer, KafkaProducer
import json
from config.kfk_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    ORG_TOPIC,
    STD_TOPIC,
    CONSUMER_GROUP,
    AUTO_OFFSET_RESET,
    ENABLE_AUTO_COMMIT,
)
from utils.data_converter import convert_data


def start_listener():
    # Khởi tạo consumer lắng nghe topic 'org'
    consumer = KafkaConsumer(
        ORG_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset=AUTO_OFFSET_RESET,
        enable_auto_commit=ENABLE_AUTO_COMMIT,
        group_id=CONSUMER_GROUP,
    )

    # Khởi tạo producer để đẩy dữ liệu đã convert sang topic 'std'
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    print(f"[INFO] Listening on topic '{ORG_TOPIC}'...")

    # Vòng lặp liên tục: mỗi khi có message mới thì xử lý
    for message in consumer:
        org_data = message.value
        print(f"[RECEIVED] {org_data}")

        # Convert dữ liệu
        std_data = convert_data(org_data)

        # Đẩy sang topic 'std'
        producer.send(STD_TOPIC, std_data)
        print(f"[SENT] {std_data}")


if __name__ == "__main__":
    start_listener()
