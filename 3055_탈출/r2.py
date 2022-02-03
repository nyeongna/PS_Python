from collections import deque

r, c = map(int, input().split())
graph = list()
for _ in range(r):
    row = list(map(str, input()))
    graph.append(row)
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
bx, by = None, None
hhx, hhy = None, None

# Q에는 물먼저 다 넣고, 마지막에 고슴도치를 넣어준다.
# 물이 채워질 위치에는 고슴도치가 못 움직이기때문
Q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'D':
            bx, by = i, j
        elif graph[i][j] == 'S':
            hhx, hhy = i,j
        elif graph[i][j] == '*':
            Q.append((i,j,'*', 0))
Q.append((hhx, hhy, 'S', 0))

# bfs 탐색
visited = [ [0]*c for _ in range(r) ]
while len(Q) > 0:
    x, y, status, dist = Q.popleft()
    if x==bx and y==by and status=='S':
        print(dist)
        exit()
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<r and 0<=dy<c and visited[dx][dy]==0:
            # 물일경우
            if status=='*' and graph[dx][dy]!='X' and graph[dx][dy]!='D':
                visited[dx][dy]=1
                Q.append((dx,dy,status,dist+1))
            # 고슴도치일경우
            elif status=='S' and (graph[dx][dy]=='.' or graph[dx][dy]=='D'):
                visited[dx][dy]=1
                Q.append((dx,dy,status,dist+1))
print('KAKTUS')
    
    