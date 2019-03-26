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


# 调整函数
def sift(li, low, high):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= high:  # 退出条件2 i 是叶子的子节点 j的位置超过了high
        if j + 1 <= high and li[j + 1] >= li[j]:
            j = j + 1  # 如果右孩子比左孩子大  指针指向右边
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:  # 退出条件1 tmp的值大于两个孩子的值
            break
    li[i] = tmp


@cal_time
def heap_sort(li):
    # 1.建堆
    n = len(li)
    for i in range(n // 2 - 1, -1, -1):
        # i是建堆时要调整的子树的根的下标
        sift(li, i, n - 1)
    # 出数
    for i in range(n - 1, -1, -1):  # i表示当前的high值 也表示棋子的位置
        li[i], li[0] = li[0], li[i]
        # 堆的范围是0~i-1
        sift(li, 0, i - 1)


# li = list(range(10000))
# random.shuffle(li)
# heap_sort(li)

# 内置模块  堆排序
import heapq

li = list(range(1000000))
random.shuffle(li)
heapq.heapify(li)
print(li)
