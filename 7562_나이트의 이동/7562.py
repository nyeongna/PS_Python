import sys
from collections import deque

t = int(input())

x_dir = [ -1, -2, -2, -1, 1, 2, 2, 1]
y_dir = [ -2, -1, 1, 2, -2, -1, 1, 2]
while t>0:
    t=t-1
    size = int(input())
    x, y = map(int, input().split())
    dx,dy = map(int, input().split())
    graph = [ [ 0 for _ in range(size) ] for _ in range(size) ]
    
    Q = deque()
    Q.append([x,y,0])
    graph[x][y]=1

    while len(Q)>0:
        cur_x = Q[0][0]
        cur_y = Q[0][1]
        dist = Q[0][2]
        Q.popleft()

        if cur_x == dx and cur_y == dy:
            print(dist)
            break

        for i in range(8):
            dxx = cur_x + x_dir[i]
            dyy = cur_y + y_dir[i]
            if (dxx >= 0 and dxx < size and dyy >=0 and dyy < size and graph[dxx][dyy] == 0):
                graph[dxx][dyy]=1
                Q.append([dxx,dyy,dist+1])


