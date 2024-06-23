import queue
import threading
import time
import random

# Create a queue for requests
request_queue = queue.Queue()

# Request counter for unique request IDs
request_counter = 0

def generate_request():
    global request_counter
    while True:
        # Simulate time delay between request generation
        time.sleep(random.uniform(0.5, 2.0))
        request_counter += 1
        request_id = f"Request - {request_counter}"
        request_queue.put(request_id)
        print(f"Generated: {request_id}")


def process_request():
    while True:
        try:
            # Simulate time delay in processing
            time.sleep(random.uniform(1.0, 3.0))
            if not request_queue.empty():
                request_id = request_queue.get()
                print(f"Processing: {request_id}")
                request_queue.task_done()
            else:
                print("Queue is empty, waiting for new requests...")
        except Exception as e:
            print(f"Error processing request: {e}")

def main():
    # Start the request generation thread
    generator_thread = threading.Thread(target=generate_request)
    generator_thread.daemon = True
    generator_thread.start()

    # Start the request processing thread
    processor_thread = threading.Thread(target=process_request)
    processor_thread.daemon = True
    processor_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting program...")

if __name__ == "__main__":
    main()