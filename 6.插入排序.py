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

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1  # j是插入前的最后一个数 比如 列表是2,9,1  要插入3  1就是j
        while j >= 0 and li[j] > tmp:  # j小于0表示tmp是最小的
            # 所有数字往后挪
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp

li = list(range(10))
random.shuffle(li)
insert_sort(li)
print(li)