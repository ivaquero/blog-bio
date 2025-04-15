def consumer():
    print("[CONSUMER] start")
    r = "start"
    while True:
        n = yield r
        if not n:
            print("n is empty")
            continue
        print(f"[CONSUMER] Consumer is consuming {n}")
        r = "200 ok"


def producer(c):
    # 启动生成器
    start_value = c.send(None)
    print(start_value)
    for n in range(1, 4):
        print(f"[PRODUCER] Producer is producing {n}")
        r = c.send(n)
        print(f"[PRODUCER] Consumer return: {r}")
    # 关闭生成器
    c.close()


# 创建生成器
c = consumer()
# 传入生成器
producer(c)
