import threading
import random
import time

BUFFER_SIZE = 5

class Semaphore:
    def __init__(self, initial):
        self.lock = threading.Condition()
        self.value = initial

    def acquire(self):
        with self.lock:
            while self.value <= 0:
                self.lock.wait()
            self.value -= 1

    def release(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

def producer(buffer, semaphore):
    while True:
        if len(buffer) < BUFFER_SIZE:
            item = random.randint(1, 200)
            semaphore.acquire()
            time.sleep(random.randint(2,4))
            buffer.append(item)
            print(f"Produced {item}. Buffer: {buffer}")
        else:
            print("Producer is waiting, buffer is full")
            time.sleep(1)
            continue
        semaphore.release()

def consumer(buffer, semaphore):
    while True:
        if len(buffer) > 0:
            semaphore.acquire()
            item = buffer.pop(0)
            time.sleep(random.randint(2,4))
            print(f"Consumed {item}. Buffer: {buffer}")
        else:
            print("Consumer is waiting, buffer is empty")
            time.sleep(1)
            continue
        semaphore.release()

def main():
    buffer = []
    semaphore = Semaphore(BUFFER_SIZE)
    producer_thread = threading.Thread(target=producer, args=(buffer, semaphore))
    consumer_thread = threading.Thread(target=consumer, args=(buffer, semaphore))
    producer_thread.setDaemon(True)
    consumer_thread.setDaemon(True)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()
    print("Terminating program")
if __name__ == "__main__":
    main()