import time
from queue import Queue
from threading import Thread

my_queue = Queue(1)  # Buffer size of 1


def consumer():
    time.sleep(0.1)  # Wait
    my_queue.get()  # Runs second
    print("Consumer got 1")
    my_queue.get()  # Runs fourth
    print("Consumer got 2")
    print("Consumer done")


thread = Thread(target=consumer)
thread.start()

my_queue.put(object())  # Runs first
print("Producer put 1")
my_queue.put(object())  # Runs third
print("Producer put 2")
print("Producer done")
thread.join()
