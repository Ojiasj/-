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


def insert_sort_gap(li, gap):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - gap  # j是插入前的最后一个数 比如 列表是2,9,1  要插入3  1就是j
        while j >= 0 and li[j] > tmp:  # j小于0表示tmp是最小的
            # 所有数字往后挪
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp

@cal_time
def shell_sort(li):
    d = len(li)//2
    while d>0:
        insert_sort_gap(li,d)
        d=d//2

li = list(range(1000000))
random.shuffle(li)
shell_sort(li)
print(li)
