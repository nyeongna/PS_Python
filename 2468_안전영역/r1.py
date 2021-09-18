
from collections import deque

ans = 1
n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]
max_height = 0
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        max_height = max(max_height, graph[i][j])

for height in range(1, max_height+1, 1):
    tmp_graph = [ [0]*n for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                tmp_graph[i][j] = 1
    cnt = 0
    # print(height)
    # for k in tmp_graph:
    #     print(k)
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 0:
                cnt = cnt + 1
                Q = deque()
                Q.append((i,j))
                while len(Q) > 0:
                    x, y = Q.popleft()
                    tmp_graph[x][y]=1
                    for k in range(4):
                        dx = x + x_dir[k]
                        dy = y + y_dir[k]
                        if 0<=dx<n and 0<=dy<n and tmp_graph[dx][dy]==0:
                            #이게 필요한게 그래야 나중에
                            tmp_graph[dx][dy]=1
                            Q.append((dx,dy))
    #print(f'cnt={cnt}')
    ans = max(ans, cnt)

print(ans)
