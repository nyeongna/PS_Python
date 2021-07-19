import sys
from collections import deque

t = int(input())

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
while t > 0:
    t=t-1
    c, r = map(int, input().split())
    graph = [ list(map(str,input())) for _ in range(r) ]
    start=0
    fires=[]
    Q = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '@':
                start = [i,j,0,0]
            if graph[i][j] == '*':
                Q.append([i,j,0,1])
    
    Q.append(start)
    graph[start[0]][start[1]] = '@'

    found=False
    while len(Q) > 0:
        x, y, dist, status = Q.popleft()
        if status==0:
            if x==0 or x == r-1 or y==0 or y == c-1:
                found=True
                break
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if status==0 and dx >= 0 and dx < r and dy >= 0 and dy < c and graph[dx][dy]=='.':
                graph[dx][dy]='@'
                Q.append([dx,dy,dist+1,status])
            if status==1 and dx >= 0 and dx < r and dy >= 0 and dy < c and (graph[dx][dy]=='.' or graph[dx][dy]=='@'):
                graph[dx][dy]='*'
                Q.append([dx,dy,dist+1,status])

    if found:
        print(dist+1)
    else:
        print('IMPOSSIBLE')