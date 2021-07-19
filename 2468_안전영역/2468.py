import sys
from collections import deque
from itertools import combinations
from itertools import permutations
from sys import stdin
sys.setrecursionlimit(110000)

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]


max_height = 100
for i in range(n):
    for j in range(n):
        max_height = max(max_height, graph[i][j])

x_dir = [-1, 0, 1, 0]
y_dir = [0, 1, 0, -1]
ans = 1


def DFS(x, y, visited):
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx >= 0 and dx < n and dy >= 0 and dy < n and visited[dx][dy] == 0:
            visited[dx][dy] = 1
            DFS(dx, dy, visited)


for height in range(max_height+1):
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                visited[i][j] = 1
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == 0):
                cnt = cnt + 1
                visited[i][j] = 1
                DFS(i, j, visited)
    ans = max(ans, cnt)

print(ans)
