from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().strip().split())
hx, hy = map(int, stdin.readline().strip().split())
ex, ey = map(int, stdin.readline().strip().split())
hx -= 1
hy -= 1
ex -= 1
ey -= 1
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range(n) ]
visited = [ [[0]*m for _ in range(n)] for _ in range(2) ]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

Q = deque()
Q.append((hx,hy,0,0))
visited[0][hx][hy] = 1

while len(Q) > 0:
    x, y, dist, status = Q.popleft()
    if x == ex and y == ey:
        print(dist)
        exit()
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        # 다음 칸이 빈 칸(0) 인 경우, status가 1이든 0이든 상관없이 안가본 곳이라면 진행.
        if dx>=0 and dx < n and dy>=0 and dy < m and visited[status][dx][dy]==0 and graph[dx][dy]==0:
            visited[status][dx][dy]=1
            Q.append((dx,dy,dist+1,status))
        # 다음 칸이 돌(1) 인 경우, status가 1이어야함.
        elif status ==0 and dx>=0 and dx < n and dy>=0 and dy < m and visited[1][dx][dy]==0 and graph[dx][dy]==1:
            visited[1][dx][dy]=1
            Q.append((dx,dy,dist+1,1))
print(-1)





