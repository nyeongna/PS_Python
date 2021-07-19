from sys import stdin
from collections import deque
import sys
# Python3 기준 1,000,000 성공
# pypy 기준 1,000,000 시간초과
sys.setrecursionlimit(100000)

n, m = map(int, stdin.readline().rstrip().split())
graph = [ list(map(str, stdin.readline().rstrip())) for _ in range(n) ]

# 방문여부 판단 visited
visited = [ [0]*m for _ in range(n) ]
# 해당 칸의 성공여부 판단 result
result = [ [0]*m for _ in range(n) ]
# 하지만 이차원 배열 1개만 있어도 된다.
# 왜냐하면, 어차피 한번 시작한 길은 끝이 무조건 나게 되어있으므로, 도중에 같은 칸으로 돌아온다면 0으로 하면된다
# 끝이 성공으로 끝나면 모두 1로 하면되는거고....

def DFS(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 1
    if visited[x][y]==1 and result[x][y] == 0:
        return -1
    if result[x][y] != 0:
        return result[x][y]

    visited[x][y]=1

    if graph[x][y] == 'D':
        result[x][y] = DFS(x+1,y)
        return result[x][y]
    if graph[x][y] == 'U':
        result[x][y] = DFS(x-1,y)
        return result[x][y]
    if graph[x][y] == 'L':
        result[x][y] = DFS(x, y-1)
        return result[x][y]
    if graph[x][y] == 'R':
        result[x][y] = DFS(x, y+1)
        return result[x][y]

for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            DFS(i,j) 

ans = 0
for i in range(n):
    for j in range(m):
        if result[i][j]==1:
            ans = ans + 1

print(ans)