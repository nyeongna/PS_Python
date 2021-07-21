from sys import stdin
from collections import deque

n, L, R = map(int, input().split())
graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range(n) ]
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
ans = 0
while True:
    flag=0
    visited= [ [0]*n for _ in range(n) ]
    for r in range(n):
        for c in range(n):
            if visited[r][c]==0:
                visit_list = [ (r,c,graph[r][c]) ]
                visited[r][c] = 1
                Q = deque()
                Q.append((r,c,graph[r][c]))
                while len(Q) > 0:
                    x, y, val = Q.popleft()
                    for i in range(4):
                        dx = x + x_dir[i]
                        dy = y + y_dir[i]
                        if 0 <= dx < n and 0 <= dy < n and visited[dx][dy]==0 and L <= abs(val-graph[dx][dy]) <= R:
                            visited[dx][dy] = 1
                            Q.append((dx,dy,graph[dx][dy]))
                            visit_list.append((dx,dy,graph[dx][dy]))
                if len(visit_list) >= 2:
                    flag = 1
                tmp_sum=0
                for (x,y,val) in visit_list:
                    tmp_sum = tmp_sum + val
                tmp_sum = tmp_sum // len(visit_list)
                for (x,y,val) in visit_list:
                    graph[x][y] = tmp_sum
    if flag==1:
        ans = ans + 1
    else:
        print(ans)
        # for i in range(n):
        #     for j in range(n):
        #         print(graph[i][j], end=' ')
        #     print()
        exit()
    


                




