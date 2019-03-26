import random
import time


# def cal_time(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         end_time = time.time()
#         print("花费了%f" % (end_time - start_time))
#         return res
#
#     return inner

# @cal_time
def choose_sort(li):
    for i in range(len(li) - 1):
        min_pos = i  # min_pos用来当最小值的位置 假设目前i最小
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        # 然后最小值与i互换位置
        li[min_pos], li[i] = li[i], li[min_pos]


li = list(range(10))
random.shuffle(li)
choose_sort(li)