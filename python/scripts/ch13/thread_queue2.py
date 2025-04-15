from queue import Queue
from threading import Thread

in_queue = Queue()


def consumer():
    print("Consumer waiting")
    in_queue.get()  # Runs 2nd
    print("Consumer working")
    print("Consumer done")
    in_queue.task_done()  # Runs 3rd


thread = Thread(target=consumer)
thread.start()

print("Producer putting")
in_queue.put(object())  # Runs 1st
print("Producer waiting")
in_queue.join()  # Runs 4th
print("Producer done")
thread.join()
