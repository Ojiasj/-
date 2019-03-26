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


def merge(li, low, mid, high):
    """
    low-mid 有序, mid+1-high 有序
    :param li:
    :param low:起始位置
    :param mid:中间最大数字位置
    :param high:len(li)-1
    :return:
    """
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1

    li[low:high + 1] = ltmp


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        # 合并
        merge(li, low, mid, high)


li = [6, 7, 1, 2]
merge_sort(li, 0, len(li)-1)
print(li)
