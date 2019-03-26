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
def bin_sort(li, min_num=0, max_num=99, bin_num=10):
    """
    :param li: 列表
    :param min_num: 最小值
    :param max_num: 最大值
    :param bin_sort: 桶的个数
    :return:
    """
    bin = [[] for i in range(bin_num)]
    for num in li:
        n = (max_num - min_num + 1) // bin_num
        i = num // n
        bin[i].append(num)
        # 维护桶有序
        i = len(bin[int(num // n)]) - 1
        li = bin[int(num // n)]
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j -= 1

        li[j + 1] = num

    res = []
    for l in bin:
        res.extend(l)

    return res

li = [random.randint(0,99) for i in range(100000)]
new_li = bin_sort(li)
print(new_li)