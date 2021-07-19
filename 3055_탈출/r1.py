from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())
graph = [ list(map(str, stdin.readline().rstrip())) for _ in range(n) ]

hx, hy = 0, 0
wx, wy = 0, 0
visited = [ [0]*m for _ in range(n) ]
Q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            hx, hy = i, j
            visited[i][j]=1
        if graph[i][j] == '*':
            Q.append((i,j,0, 'water'))
            visited[i][j]=1

Q.append((hx,hy, 0,'h'))

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while len(Q) > 0:
    x, y, dist, status = Q.popleft()
    if graph[x][y]=='D' and status =='h':
        print(dist)
        exit()
    
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0 <= dx < n and 0 <= dy < m and visited[dx][dy]==0 and (graph[dx][dy] == '.' or graph[dx][dy] == 'D'):
            if status=='water' and graph[dx][dy]=='D':
                continue
            visited[dx][dy]=dist+1
            Q.append((dx,dy,dist+1,status))
print('KAKTUS')
