# def fun1(x):
#     if x > 0:
#         fun1(x-1)
#         print(x)
#
# fun1(5)

def fun2(x):
    if x > 0:
        print("抱起", end="")
        fun2(x - 1)
        print("的我", end="")
    if x == 0:
        print("我的小鲤鱼", end="")


fun2(5)
