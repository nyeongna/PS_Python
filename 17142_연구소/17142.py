from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().strip().split())
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range(n) ]

virus_list = []
nums_to_fill = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_list.append((i,j))
        if graph[i][j]==0:
            nums_to_fill += 1


x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

ans = float('inf')

for comb in combinations(virus_list, m):
    Q = deque()
    visited=[ [0]*n for _ in range(n) ]
    for x, y in comb:
        Q.append((x,y,0))
        visited[x][y]= -1

    cnt = 0
    total_time = 0
    while len(Q) > 0:
        x, y, dist = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if dx>=0 and dx<n and dy>=0 and dy<n and (graph[dx][dy]==0 or graph[dx][dy]==2) and visited[dx][dy]==0:
                visited[dx][dy]=dist+1
                Q.append((dx,dy,dist+1))
                if graph[dx][dy]==0:
                    total_time = max(total_time, dist+1)
                    cnt += 1

    if cnt == nums_to_fill:
        ans = min(ans, total_time)

if ans == float('inf'):
    print(-1)
else:
    print(ans)


