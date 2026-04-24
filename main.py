# import sys
# import threading

# from producer.fake_data_producer import start_producer
# from consumer.org_listener import start_org_consumer
# from consumer.std_listener import start_std_consumer


# def run_consumers():
#     # Thread 1: consumer org
#     t1 = threading.Thread(target=start_org_consumer, daemon=True)

#     # Thread 2: consumer std
#     t2 = threading.Thread(target=start_std_consumer, daemon=True)

#     t1.start()
#     t2.start()

#     print("[INFO] Both consumers (ORG + STD) are running...")

#     t1.join()
#     t2.join()


# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python main.py [producer|consumer]")
#         sys.exit(1)

#     mode = sys.argv[1].lower()

#     if mode == "producer":
#         print("[INFO] Starting Fake Data Producer...")
#         start_producer()

#     elif mode == "consumer":
#         print("[INFO] Starting ALL Consumers (ORG + STD)...")
#         run_consumers()

#     else:
#         print("Invalid mode. Use 'producer' or 'consumer'.")


# if __name__ == "__main__":
#     main()


# main.py

import sys
import threading
import signal
import time

from producer.fake_data_producer import start_producer
from consumer.org_listener import start_org_consumer
from consumer.std_listener import start_std_consumer


# =========================
# RUN ALL (Producer + Consumers)
# =========================
def run_all():
    print("[INFO] Starting ALL services (Producer + ORG + STD)...")

    threads = []

    # Producer
    t_producer = threading.Thread(
        target=start_producer,
        name="ProducerThread",
        daemon=True
    )
    threads.append(t_producer)

    # ORG Consumer
    t_org = threading.Thread(
        target=start_org_consumer,
        name="OrgConsumerThread",
        daemon=True
    )
    threads.append(t_org)

    # STD Consumer
    t_std = threading.Thread(
        target=start_std_consumer,
        name="StdConsumerThread",
        daemon=True
    )
    threads.append(t_std)

    # Start all threads
    for t in threads:
        t.start()
        print(f"[INFO] Started {t.name}")

    print("[INFO] All services are running... (Ctrl+C to stop)")

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down gracefully...")


# =========================
# RUN ONLY CONSUMERS
# =========================
def run_consumers():
    print("[INFO] Starting Consumers (ORG + STD)...")

    threads = []

    t_org = threading.Thread(
        target=start_org_consumer,
        name="OrgConsumerThread",
        daemon=True
    )

    t_std = threading.Thread(
        target=start_std_consumer,
        name="StdConsumerThread",
        daemon=True
    )

    threads.extend([t_org, t_std])

    for t in threads:
        t.start()
        print(f"[INFO] Started {t.name}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Consumers stopped.")


# =========================
# MAIN
# =========================
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [producer|consumer|all]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "producer":
        print("[INFO] Starting Producer...")
        start_producer()

    elif mode == "consumer":
        run_consumers()

    elif mode == "all":
        run_all()

    else:
        print("Invalid mode. Use 'producer', 'consumer', or 'all'.")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()