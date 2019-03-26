import random
import time


def cal_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("花费了%f" % (end_time - start_time))
        return res

    return inner


#################未优化########################
@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):  # 这个代表第几次循环
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


#################优化########################
# 如果一趟下来没有进行变化的话  就代表已经有序了
@cal_time
def bubble_sort2(li):
    exchange = False
    for i in range(len(li) - 1):  # 这个代表第几次循环
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


@cal_time
def ssort(li):
    li.sort()


li = list(range(100))
random.shuffle(li)
bubble_sort(li)
ssort(li)
