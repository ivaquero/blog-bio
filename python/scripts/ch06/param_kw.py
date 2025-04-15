def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("Michael", 30)
# 也可先组装出一个 dict，再把该 dict 传进去：
extra = {"city": "Beijing", "job": "Engineer"}
person("Jack", 24, **extra)
