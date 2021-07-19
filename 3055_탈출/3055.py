import sys
from collections import deque

r, c = map(int, input().split())
graph = [ list(map(str,input())) for _ in range(r) ]
#print(graph)
Q = deque()
start = list()
goal = list()
for i in range(r):
    for j in range(c):
        if graph[i][j]=='S':
            start=[i,j,0,0]
        if graph[i][j]=='*':
            Q.append([i,j,0,1])
        if graph[i][j]=='D':
            goal = [i, j]
Q.append(start)

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

found = 0
while len(Q) > 0:
    x, y, dist, status = Q.popleft()

    if x==goal[0] and y==goal[1]:
        found=1
        break
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        # hedgedog
        if dx>=0 and dx < r and dy>=0 and dy < c and status==0 and (graph[dx][dy]=='.' or graph[dx][dy]=='D'):
            graph[dx][dy]='S'
            Q.append([dx,dy,dist+1,status])
        # water spreading
        if dx>=0 and dx <r and dy>=0 and dy < c and status==1 and (graph[dx][dy]=='.' or graph[dx][dy]=='S'):
            graph[dx][dy]='*'
            Q.append([dx,dy,dist+1,status])

if found:
    print(dist)
else:
    print('KAKTUS')
