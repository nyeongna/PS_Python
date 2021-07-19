from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().rstrip().split())
graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range(n) ]

virus_list = []

numsToFilled=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            virus_list.append((i,j))
        if graph[i][j]==0 or graph[i][j]==2:
            numsToFilled +=1
numsToFilled -= m
        


ans = float('inf')

for combi in combinations(virus_list, m):
    Q = deque()
    visited = [ [0]*n for _ in range(n) ]
    for x,y in combi:
        visited[x][y] = 1
        Q.append((x,y,0))

    total_time = 0
    cnt = 0
    while len(Q) > 0:
        x, y, dist = Q.popleft()
        for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
           dx = x + i
           dy = y + j
           if dx>=0 and dx<n and dy>=0 and dy<n and (graph[dx][dy]==0 or graph[dx][dy]==2) and visited[dx][dy]==0:
               visited[dx][dy] = 1
               Q.append((dx,dy,dist+1))
               total_time = max(total_time, dist+1)
               cnt += 1
    
    # flag=1
    # for i in range(n):
    #     for j in range(n):
    #         if graph[i][j]==0 and visited[i][j]==0:
    #             flag=0
    #         if graph[i][j]==2 and visited[i][j]==0:
    #             flag=0
    if cnt==numsToFilled:
        ans = min(ans, total_time)
    
if ans == float('inf'):
    print(-1)
else:
    print(ans)