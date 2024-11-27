import os
import random
import time
from multiprocessing import Process
from multiprocessing import Queue


# 写数据进程执行的代码：
def write(q):
    print(f"Process to write: {os.getpid()}")
    for value in ["A", "B", "C"]:
        print(f"Put {value} to queue...")
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码：
def read(q):
    print(f"Process to read: {os.getpid()}")
    while True:
        value = q.get(True)
        print(f"Get {value} from queue.")


if __name__ == "__main__":
    # 父进程创建 Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw，写入：
    pw.start()
    # 启动子进程 pr，读取：
    pr.start()
    # 等待 pw 结束：
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()
