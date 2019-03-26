# li = []
#
# # 进栈
# li.append(1)
# li.append(2)
# li.append(3)
# # 出栈
# print(li.pop())
# # 查看第一位
# print(li[-1])


def check_brace(s):
    match = {"}": "{", "]": "[", ")": "("}
    li = []
    for ch in s:
        if ch in ["(", "[", "{"]:
            li.append(ch)
        elif len(li) == 0:
            print("缺少%s" % match[ch])
            return False
        elif li[-1] != match[ch]:
            print("不匹配")
            return False
        else:
            li.pop()

    if len(li) > 0:
        print("存在多余的%s" % li[-1])
        return False
    else:
        print("匹配成功")
        return True


# print(check_brace("([]"))


# def A():
#     print("A")
#     B()
#
# def B():
#     C()
#     print("B")
#
# def C():
#     print("C")
#
# A()

# def A(x):
#     if x == 0:
#         print("终止条件")
#     else:
#         print(x)
#         A(x-1)
#
# A(5)


###############################################
# 迷宫问题
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y - 1),  # 左
    lambda x, y: (x, y + 1),  # 右

]


def solve_maze(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    maze[x1][y1] = 2  # 2代表走过了
    while len(stack) > 0:  # 栈不空时循环
        cur_node = stack[-1]
        if cur_node == (x2, y2):  # 到达终点
            # 结束
            print(stack)
            return
        for d in dirs:
            next_node = d(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            stack.pop()
    else:
        print("没有路")

solve_maze(1,1,8,8)