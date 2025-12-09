# config/kfk_config.py

# Danh sách bootstrap servers: 3 node Kafka
KAFKA_BOOTSTRAP_SERVERS = [
    "localhost:9093",
    "localhost:9094",
    "localhost:9095"
]

KAFKA_INTERNAL_BOOTSTRAP_SERVERS = [
    "kafka-1:19092",  # Broker 1 - INTERNAL
    "kafka-2:19092",  # Broker 2 - INTERNAL
    "kafka-3:19092"   # Broker 3 - INTERNAL
]

# Tên các topic sử dụng trong pipeline
ORG_TOPIC = "org"
STD_TOPIC = "std"

# Group ID cho consumer lắng nghe topic org
CONSUMER_GROUP = "org-listener-group"

# Một số cấu hình bổ sung (tuỳ chọn)
AUTO_OFFSET_RESET = "earliest"      # bắt đầu đọc từ đầu nếu chưa có offset
ENABLE_AUTO_COMMIT = True           # tự động commit offset
