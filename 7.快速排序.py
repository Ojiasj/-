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


def partition(li, left, right):
    randi = random.randint(left, right)
    li[randi], li[left] = li[left], li[randi]
    tmp = li[left]
    while left < right:
        while left < right and li[right] > tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp  # 把tmp写到两个箭头指的位置
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@cal_time 
def quick_sort(li):
    return _quick_sort(li, 0, len(li) - 1)


li = list(range(1000000))
random.shuffle(li)
# quick_sort(li, 0, len(li) - 1)
quick_sort(li)


