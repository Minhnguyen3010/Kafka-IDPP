🌀 Giới thiệu

IDPP-Flow là một hệ thống mô phỏng dòng dữ liệu sử dụng Kafka và Redis. Dự án bao gồm:

Producer: Tạo dữ liệu giả và gửi lên Kafka.

Consumers: Nhận dữ liệu từ Kafka và xử lý theo từng loại (ORG, STD).

Redis: Lưu trữ dữ liệu đã xử lý.

Kafka UI: Giao diện quản lý Kafka Cluster.

📦 Clone dự án

git clone https://github.com/your-username/IDPP-Flow.git
cd IDPP-Flow

🐳 Khởi chạy Docker

Dự án sử dụng Docker Compose để khởi tạo các dịch vụ:

Zookeeper

Kafka (3 brokers)

Redis

Kafka UI

Bước chạy:

docker-compose -f docker/kafka-compose.yml -f docker/redis-compose.yml up -d

Sau khi chạy xong:

Kafka UI truy cập tại http://localhost:8080

Redis hoạt động tại localhost:6379

📜 Cài đặt thư viện Python

Kích hoạt môi trường ảo .venv nếu có, hoặc tạo mới:

python -m venv .venv
source .venv/bin/activate  # hoặc .venv\Scripts\activate trên Windows
pip install -r requirements.txt

🚀 Chạy chương trình chính

File utils/main.py cho phép chạy producer hoặc consumer:

Chạy Producer:

python utils/main.py producer

Chạy Consumers:

python utils/main.py consumer

Sau khi chạy consumer, bạn sẽ thấy log:

[INFO] Both consumers (ORG + STD) are running...

🔍 Kiểm tra dữ liệu

Truy cập Kafka UI tại http://localhost:8080 để kiểm tra các topic và message.

Sử dụng Redis CLI hoặc công cụ như RedisInsight để kiểm tra dữ liệu đã được lưu:

redis-cli
> keys *
> get <key>

📁 Cấu trúc thư mục

IDPP-Flow/
├── config/
│   └── kfk_config.py
├── consumer/
│   ├── org_listener.py
│   └── std_listener.py
├── docker/
│   ├── kafka-compose.yml
│   └── redis-compose.yml
├── producer/
│   └── fake_data_producer.py
├── utils/
│   ├── data_converter.py
│   └── main.py
├── requirements.txt
└── .venv/

📌 Ghi chú

Đảm bảo Docker đã được cài đặt và chạy ổn định.

Kafka cần thời gian khởi động, hãy đợi vài giây trước khi chạy producer/consumer.

Redis sẽ lưu dữ liệu theo định dạng được xử lý trong data_converter.py.

Chúc bạn triển khai thành công hệ thống mô phỏng dữ liệu với IDPP-Flow!
