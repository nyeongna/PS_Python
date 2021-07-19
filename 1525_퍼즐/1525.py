import sys
from collections import deque

graph = [ ''.join(input().split()) for _ in range(3) ]


Q = deque()
visited = dict()
for i in range(3):
    for j in range(3):
        if graph[i][j]=='0':
            Q.append([i*3+j,0, ''.join(graph)])
            visited[''.join(graph)] = 1

ans = '123456780'

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while len(Q) > 0:
    zero, dist, graph = Q.popleft()

    if graph==ans:
        print(dist)
        exit()

    x = zero // 3
    y = zero % 3
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx>= 0 and dx < 3 and dy >= 0 and dy < 3:
            pos = dx * 3 + dy
            strlst = list(graph)
            strlst[zero], strlst[pos] = strlst[pos], strlst[zero]
            converted = ''.join(strlst)
            if converted not in visited:
                visited[converted]=1
                Q.append([pos, dist+1, converted])

print(-1)