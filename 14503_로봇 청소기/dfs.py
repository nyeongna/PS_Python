from sys import stdin
from collections import deque

n, m = map(int, input().split())
rx, ry, rd = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
visited = [ [0]*m for _ in range(n) ]

direction = [
    [-1, 0],
    [0,  1],
    [1,  0],
    [0, -1]
]
back_direction = [
    [1,  0],
    [0, -1],
    [-1, 0],
    [0,  1]
]
cnt = 0
def DFS(x, y, dir):
    global cnt
    for i in range(3, -1, -1):
        nd = (dir+i)%4
        dx = x + direction[nd][0]
        dy = y + direction[nd][1]
        if 0 <= dx < n and 0 <= dy < m and visited[dx][dy]==0 and graph[dx][dy]==0:
            cnt = cnt + 1
            visited[dx][dy]=1
            DFS(dx, dy, nd)
    bx = x + back_direction[dir][0]
    by = y + back_direction[dir][1]
    if bx < 0 or bx >= n or by < 0 or by >= m or graph[bx][by]==1:
        print(cnt)
        exit()
    DFS(bx, by, dir)

cnt += 1
visited[rx][ry]=1
DFS(rx, ry, rd)