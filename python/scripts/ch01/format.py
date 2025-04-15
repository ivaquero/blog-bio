key = "my_var"
value = 1.234

# 常用
print(f"{key} = {value}")  # my_var = 1.234

# 对齐
text = "python"
n = 10

print(f"{text:>{n}}")  # 右对齐
print(f"{text:<{n}}")  # 左对齐
print(f"{text:^{n}}")  # 居中对齐
print(f"{text:*^{n}}")  # 居中对齐，用*补齐空白
"""
    python
python
  python
**python**
"""

# 多行输出
a = 1
b = 2
c = 3
s = f"{a = }\n" f"{b = }\n" f"{c = }\n"
print(s)
"""
a = 1
b = 2
c = 3
"""
