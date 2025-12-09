# # main.py
#
# import sys
#
# from producer.fake_data_producer import start_producer
# from consumer.org_listener import start_listener
#
#
# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python main.py [producer|consumer]")
#         sys.exit(1)
#
#     mode = sys.argv[1].lower()
#
#     if mode == "producer":
#         print("[INFO] Starting Fake Data Producer...")
#         start_producer()
#     elif mode == "consumer":
#         print("[INFO] Starting Org Listener...")
#         start_listener()
#     else:
#         print("Invalid mode. Use 'producer' or 'consumer'.")
#
#
# if __name__ == "__main__":
#     main()


# main.py

import sys
import threading

from producer.fake_data_producer import start_producer
from consumer.org_listener import start_org_consumer
from consumer.std_listener import start_std_consumer


def run_consumers():
    # Thread 1: consumer org
    t1 = threading.Thread(target=start_org_consumer, daemon=True)

    # Thread 2: consumer std
    t2 = threading.Thread(target=start_std_consumer, daemon=True)

    t1.start()
    t2.start()

    print("[INFO] Both consumers (ORG + STD) are running...")

    t1.join()
    t2.join()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [producer|consumer]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "producer":
        print("[INFO] Starting Fake Data Producer...")
        start_producer()

    elif mode == "consumer":
        print("[INFO] Starting ALL Consumers (ORG + STD)...")
        run_consumers()

    else:
        print("Invalid mode. Use 'producer' or 'consumer'.")


if __name__ == "__main__":
    main()
