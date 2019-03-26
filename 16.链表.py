class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
#
# print(a.next.next.item)

# 头插法
def create_linklist(li):
    head = None
    for num in li:
        p = Node(num)
        p.next = head
        head = p
    return head


# 尾插法
def create_linklist_tail(li):
    if len(li) > 0:
        head = Node(li[0])
        tail = head
        for num in li[1:]:
            p = Node()
            tail.next = p
            tail = p
        return head
    else:
        return None


link = create_linklist([1, 2, 3, 4, 5])

p = link
while p != None:
    print(p.item)
    p = p.next
