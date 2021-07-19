import sys
from collections import deque

c, r = map(int, input().split())
graph = [ list(map(int,input().split())) for _ in range(r) ]

tomato=list()
all_tomato=1
Q = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j]==1:
            Q.append([i,j,0])
        if graph[i][j]==0:
            all_tomato=0

if all_tomato:
    print(0)
    exit()

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]


ans=0
while len(Q) > 0:
    x, y, d = Q.popleft()
    ans = max(ans, d)
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx >= 0 and dx < r and dy>=0 and dy < c and graph[dx][dy]==0:
            graph[dx][dy]=d+1
            Q.append([dx,dy,d+1])

for i in range(r):
    for j in range(c):
        if graph[i][j]==0:
            print(-1)
            exit()
print(ans)

