'''
바이러스를 놓을 수 있는 공간 최대 10곳
바이러스 개수 M: 10
그래프 크기 N: 50

바이러스 위치 조합: 최대 10C5=252
그래프: 2500
시간복잡도: 252*2500 = 630,000 통과
'''
from collections import deque
from itertools import combinations
import copy

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

n, m = map(int, input().split())
graph = [ list(map(int,input().split())) for _ in range(n) ]

virus_cand,empty_list = list(), list()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_cand.append((i,j))
        if graph[i][j] != 1:
            empty_list.append((i,j))
            
ans = float('inf')
for comb in combinations(virus_cand, m):
    Q = deque()
    visited=[ [0]*n for _ in range(n) ]
    for x,y in comb:
        Q.append((x,y,0))
        visited[x][y]=1
    cnt, required_dist = len(Q), 0
    while len(Q) > 0:
        x,y,dist = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            # 벽이 아니면 채워넣는다
            if 0<=dx<n and 0<=dy<n and (graph[dx][dy]==0 or graph[dx][dy]==2) and visited[dx][dy]==0:
                visited[dx][dy]=1
                Q.append((dx,dy,dist+1))
                # 다 채우는데 필요한 시간초
                required_dist = max(required_dist, dist+1)
                cnt += 1
    # 만약 모든 칸을 채울 수 있다면, 최소 시간을 구한다
    # 벽(1)이 아닌 곳은 다 채워야함 (바이러스 후보 위치도 채워야함)
    if cnt == len(empty_list):
        ans = min(ans, required_dist)

if ans==float('inf'):
    print(-1)
else:
    print(ans)


        
        

    


