from sys import stdin
from collections import deque
from copy import deepcopy

n, m = map(int, stdin.readline().rstrip().split())
graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range(n) ]

wall_list = []
virus_list = []

# '벽을 세울 수 있는 빈 칸의 위치'와
# '바이러스의 위치'를 미리 파악해서 list에 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall_list.append((i,j))
        if graph[i][j] == 2:
            virus_list.append((i,j))
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

def BFS():
    Q = deque()
    visited = [ [0]*m for _ in range(n) ]
    for vx,vy in virus_list:
        Q.append((vx,vy))
        visited[vx][vy]=1

    while len(Q)>0:
        x, y = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if dx>=0 and dx<n and dy>=0 and dy<m and graph[dx][dy]==0 and visited[dx][dy]==0:
                visited[dx][dy]=1
                Q.append((dx,dy))

    # print('virus map')
    # for i in visited:
    #     print(i)
    # print()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0 and visited[i][j]==0:
                cnt += 1
    return cnt
    
ans = float('-inf')

def DFS(s, wall_cnt):
    global ans
    if wall_cnt == 3:
        # for i in graph:
        #     print(i)
        # print()
        ans = max(ans, BFS())
        return
    for i in range(s, len(wall_list), 1):
        x, y = wall_list[i][0], wall_list[i][1]
        graph[x][y] = 1
        DFS(i+1, wall_cnt+1)
        graph[x][y] = 0

#   벽 조합 시작위치, 벽 갯수)
DFS(0,0)
print(ans)
