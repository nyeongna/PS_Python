import sys
from collections import deque

r, c = map(int, input().split())
graph = list()
for _ in range(r):
    line = list(map(int, input()))
    graph.append(line)

visited = [  [ [ 0 for _ in range(c) ] for _ in range(r) ] for _ in range(2) ]

Q = deque()
# x y dist status
Q.append([0,0,1,0])
visited[0][0][0] = 1

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

a= 3
while len(Q) > 0:
    x = Q[0][0]
    y = Q[0][1]
    dist = Q[0][2]
    status = Q[0][3]
    #print(Q[0])
    Q.popleft()

    if x==r-1 and y==c-1:
        print(dist)
        a=4
        break
    
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx>=0 and dx < r and dy>=0 and dy < c:
            # no break yet, no break
            if status==0 and graph[dx][dy]==0 and visited[0][dx][dy]==0:
                visited[0][dx][dy]=1
                Q.append([dx,dy,dist+1,0])

            # no break yet, will break
            if status==0 and graph[dx][dy]==1 and visited[1][dx][dy]==0:
                visited[1][dx][dy]=1
                Q.append([dx,dy,dist+1,1])

            # break, no break
            if status==1 and graph[dx][dy]==0 and visited[1][dx][dy]==0:
                visited[1][dx][dy]=1
                Q.append([dx,dy,dist+1,1])
        
if a==3:
    print(-1)