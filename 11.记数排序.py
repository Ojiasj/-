import random
import time
import sys

sys.setrecursionlimit(20000)


def cal_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("花费了%f" % (end_time - start_time))
        return res

    return inner

@cal_time
def count_sort(li, max_num=100):
    # 一个列表中的数字范围都在0到100之间 设计时间复杂度为O(n)的算法
    count = [0 for i in range(max_num + 1)]
    for num in li:
        count[num] += 1
    li.clear()
    for i, j in enumerate(count):
        for k in range(j):
            li.append(i)

li = [random.randint(0,100) for i in range(1000000)]
count_sort(li)
# print(li)


# enumerate(count)
# (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
