import itertools
from multiprocessing import Event
from multiprocessing import Process
from multiprocessing import synchronize

from spin_thread import main
from spin_thread import slow


def spin(msg: str, done: synchronize.Event):
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


def supervisor():
    done = Event()
    spinner = Process(target=spin, args=("thinking!", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


if __name__ == "__main__":
    main()
