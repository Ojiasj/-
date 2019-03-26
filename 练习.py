import random
#################################2.22#############################################################
def hanni(n,A,B,C):
	hanni(n-1,A,C,B)
	print("")
	hanni(n-1,B,A,C)

# 冒泡排序
def bubble_sort(li):
	for i in range(len(li)-1):
		exchange = False
		for j in range(len(li)-i-1):
			if li[j+1]<li[i]:
				li[j],li[j+1] = li[j+1],li[j]
				exchange = True
		if not exchange:
			return
#################################2.22#############################################################

#################################2.24############################################################
# 冒泡排序
def bubble_sort_1(li):
	for i in range(len(li)-1): # 因为100的话就是 0-99
		for j in range(len(li)-i-1):
			if li[j]>li[j+1]:
				li[j],li[j+1] = li[j+1],li[j]
li = list(range(100))
random.shuffle(li)
bubble_sort_1(li)
print(li)

# 选择排序
def choose_sort(li):
	for i in range(len(li)-1):
		min_pros = i
		for j in range(i+1,len(li)):
			if li[min_pros]>li[j]:
				min_pros = j
		li[min_pros],li[i] = li[i],li[min_pros]

li2 = list(range(100))
random.shuffle(li2)
choose_sort(li2)
print(li2)
#################################2.26############################################################
# 冒泡排序
def bubble_sort_2(li):
	for i in range(len(li)-1):
		for j in range(len(li)-i-1):
			if li[j]>li[j+1]:
				li[j+1],li[j]=li[j],li[j+1]

li = list(range(100))
random.shuffle(li)
bubble_sort_2(li)
print(li)

# 选择排序
def choose_sort_2(li):
	for i in range(len(li)-1):
		min_pros = i
		for j in range(i+1,len(li)):
			if li[min_pros]>li[j]:
				min_pros=j
		li[min_pros],li[i] = li[i],li[min_pros]

li = list(range(100))
random.shuffle(li)
choose_sort_2(li)
print(li)
#################################2.27############################################################
# 插入排序
def insert_sort(li):
	for i in range(1,len(li)):
		tmp = li[i]
		j = i-1
		while j>=0 and li[j]>tmp:
			li[j+1] = li[j]
			j-=1
		li[j+1]=tmp

li1 = list(range(100))
random.shuffle(li1)
insert_sort(li1)
print(li1)

#################################3.6############################################################
# 快速排序
def quick_sort(li,left,right):
	randi = random.randit(left,right)
	