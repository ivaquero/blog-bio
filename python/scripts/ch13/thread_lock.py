from threading import Lock
from threading import Thread


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from the sensor
        counter.increment(1)


def thread_run():
    for i in range(5):
        thread = Thread(target=worker, args=(i, how_many, counter))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    expected = how_many * 5
    found = counter.count
    print(f"Counter should be {expected}, got {found}")


how_many = 10**5
threads = []


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


counter = Counter()
thread_run()


class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


counter = LockingCounter()
thread_run()
