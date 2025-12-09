IDPP-Flow – Real-time Kafka → STD → Redis Pipeline

Hệ thống gồm 3 thành phần chính:

Kafka Producer – sinh dữ liệu thô (ORG data)

Kafka STD Consumer – nhận ORG → chuẩn hóa → đẩy STD data lên Kafka

Redis Writer – nhận STD data → lưu vào Redis theo dạng key = TAG:{TAG_ID}

🚀 1. Chuẩn bị môi trường
Python virtual environment
python -m venv .venv
.\.venv\Scripts\activate     # Windows
source .venv/bin/activate   # Linux/Mac

Cài đặt thư viện
pip install -r requirements.txt

🐳 2. Chạy Redis bằng Docker

File docker: docker/redis-compose.yml

services:
  redis:
    image: redis:7
    container_name: redis-server
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: ["redis-server", "--appendonly", "yes"]

volumes:
  redis_data:

Chạy Redis
docker compose -f docker/redis-compose.yml up -d

Kiểm tra Redis đã chạy
docker ps
redis-cli PING
# -> PONG

🧩 3. Cấu trúc thư mục
IDPP-Flow/
│
├── docker/
│   └── redis-compose.yml
│
├── main.py
├── producer/
│   └── producer_org.py
├── consumer/
│   ├── org_consumer.py
│   └── std_consumer.py
│
├── redis/
│   └── redis_client.py
│
├── utils/
│   └── tag_mapping.py
│
└── README.md

🔄 4. Luồng xử lý dữ liệu
Luồng tổng thể
[ORG PRODUCER] → topic org
       ↓
[ORG CONSUMER] → chuẩn hóa → thêm STD_ID + Plant_CD
       ↓
→ đẩy vào topic std
       ↓
[STD CONSUMER] → lưu vào Redis

Redis được dùng để làm gì?

Redis lưu dữ liệu dạng:

KEY: TAG:{TAG_ID}
VALUE: {
  "TAG_ID": 67,
  "Org_Time": 1765264850.618498,
  "Col_Time": 1765264850.618498,
  "Value": 36.69,
  "STD_ID": "STD_67",
  "Plant_CD": "PLANT01"
}

📌 5. Chạy từng thành phần
1) Chạy Kafka Producer (ORG producer)
python main.py producer


Sinh dữ liệu test vào topic org.

2) Chạy STD Consumer

Chạy consumer chuẩn hóa dữ liệu:

python main.py std


STD consumer sẽ:

Nhận dữ liệu ORG

Thêm STD_ID & Plant_CD

Đẩy lên topic std

3) Chạy Redis Writer

Có 2 cách:

Cách 1 — Tích hợp trong STD consumer (recommend)

STD consumer của bạn đã có log:

[REDIS SAVED] TAG:75 -> {...}


=> nghĩa là Redis writer chạy trong cùng consumer.

4) Kiểm tra dữ liệu trên Redis
redis-cli
keys *
get TAG:75


Hoặc xem dạng đẹp:

redis-cli --raw GET TAG:75
