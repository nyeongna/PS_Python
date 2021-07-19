import sys
from collections import deque
from itertools import combinations

r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]

x_dir = [-1, 0, 1, 0]
y_dir = [0, 1, 0, -1]

sheep_list = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            sheep_list.append((i, j))

# 늑대 방어 불가능
for x, y in sheep_list:
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx >= 0 and dx < r and dy >= 0 and dy < c and graph[dx][dy] == 'W':
            print(0)
            exit()

# 늑대 방어 가능
for x, y in sheep_list:
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx >= 0 and dx < r and dy >= 0 and dy < c and graph[dx][dy] != 'S':
            graph[dx][dy] = 'D'
print(1)
for i in range(r):
    for j in range(c):
        print(graph[i][j], end='')
    print()
