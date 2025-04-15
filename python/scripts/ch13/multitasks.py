import os
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print(f"Run child process {name} ({os.getpid()})...")


if __name__ == "__main__":
    print(f"Parent process {os.getpid()}.")
    p = Process(target=run_proc, args=("test",))
    print("Child process will start.")
    p.start()
    p.join()
    print("Child process end.")
