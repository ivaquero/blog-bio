# a^2 + b^2 + c^2 + ……
# 计算的对象数目不确定
def calc(*numbers):
    return sum(n * n for n in numbers)


# 也可先组装一个 list，再将该 list 传进去
nums = [1, 2, 3]
print(calc(*nums))
