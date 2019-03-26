from collections import deque

# 创建队列
# q = deque()
# # 进队
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)
# # 出队
# print(q.popleft())

#            队列最大长度
# q = deque([],5)
# for i in range(6):
#     q.append(i)
#
# print(q.popleft())

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


def solve_maze_queue(x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1, -1))
    maze[x1][x2] = 2
    li = []
    while len(q) > 0:
        cur_node = q.popleft()
        li.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            path = []
            i = len(li) - 1
            while i >= 0:
                path.append(li[i][0:2])
                i = li[i][2]
            path.reverse()
            print(path)
            return
        for d in dirs:
            next_node = d(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                q.append((next_node[0], next_node[1], len(li) - 1))
                maze[next_node[0]][next_node[1]] = 2

    else:
        print("没有路")
        return

solve_maze_queue(1,1,8,8)