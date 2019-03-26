# and  如果and前面是个false 那么久直接跳出 是个布尔运算的短路

# 不用if写个判断

a = 3


def func():
    print("hello")


a > 0 and func()
