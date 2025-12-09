# main.py

import sys

from producer.fake_data_producer import start_producer
from consumer.org_listener import start_listener


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [producer|consumer]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "producer":
        print("[INFO] Starting Fake Data Producer...")
        start_producer()
    elif mode == "consumer":
        print("[INFO] Starting Org Listener...")
        start_listener()
    else:
        print("Invalid mode. Use 'producer' or 'consumer'.")


if __name__ == "__main__":
    main()
