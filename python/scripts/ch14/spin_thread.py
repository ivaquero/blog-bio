import itertools
import time
from threading import Event
from threading import Thread


def spin(msg: str, done: Event):
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


def supervisor():
    done = Event()
    spinner = Thread(target=spin, args=("thinking!", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def slow():
    time.sleep(3)
    return 42


def main():
    result = supervisor()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
