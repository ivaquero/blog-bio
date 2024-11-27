from threading import Thread
from threading import current_thread
from threading import local

# 创建全局 ThreadLocal 对象：
local_school = local()


def process_student():
    # 获取当前线程关联的 student:
    std = local_school.student
    print(f"Hello, {std} (in {current_thread().name})")


def process_thread(name):
    # 绑定 ThreadLocal 的 student:
    local_school.student = name
    process_student()


t1 = Thread(target=process_thread, args=("Alice",), name="Thread-A")
t2 = Thread(target=process_thread, args=("Bob",), name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()
