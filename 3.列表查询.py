li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import time


# print(li.index(5))

def cal_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("花费了%f" % (start_time - end_time))
        return res

    return inner


# 正常操作
@cal_time
def binary_search(li, val):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid < val:
            low = mid + 1
        elif mid > val:
            high = mid - 1
        else:
            return mid
    return None


@cal_time
def bin_search_rec(data_set, val, low, high):
    if low <= high:
        mid = (low + high) // 2
        if mid < val:
            bin_search_rec(data_set, val, mid + 1, high)
        elif mid > val:
            bin_search_rec(data_set, val, low, mid - 1)
        else:
            return mid
    else:
        return None


lis = list(range(10000))
s1 = binary_search(lis, 696)
s2 = bin_search_rec(lis, 696, 0, len(lis) - 1)

# print(s1)
print(s2)
