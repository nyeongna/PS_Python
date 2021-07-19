from collections import deque

t = int(input())

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

for num in range(t):
    m, n, k = map(int, input().split())
    graph = [ [0]*m for _ in range(n) ]
    visited = [ [0]*m for _ in range(n) ]
    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                graph[i][j]=2
                cnt += 1
                visited[i][j] =1
                Q = deque()
                Q.append((i,j))
                while len(Q) > 0:
                    x, y = Q.popleft()
                    for k in range(4):
                        dx = x + x_dir[k]
                        dy = y + y_dir[k]
                        if 0 <= dx < n and 0 <= dy < m and graph[dx][dy]==1:
                            graph[dx][dy]=2
                            Q.append((dx,dy))
    print(cnt)

