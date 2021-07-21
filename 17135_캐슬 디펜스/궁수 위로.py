from collections import deque
from itertools import combinations
from sys import stdin
import copy

n, m, shooting_range = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
graph.append( [0]*m )
position = [ i for i in range(m) ]

def BFS(tmp_graph, round, comb):
    killed = set()
    for pos in comb:
        Q = deque()
        visited=[ [0]*m for _ in range(round) ]
        Q.append((round, pos, 0))
        while len(Q) > 0:
            x, y, dist = Q.popleft()
            if dist > shooting_range: break
            if dist <= shooting_range and tmp_graph[x][y]==1:
                killed.add((x,y))
                break
            for x_dir, y_dir in (0,-1), (-1,0), (0,1):
                dx, dy = x + x_dir, y + y_dir
                if 0<=dx<=round-1 and 0<=dy<m and visited[dx][dy]==0:
                    visited[dx][dy]=1
                    Q.append((dx,dy,dist+1))
    for (x,y) in killed:
        tmp_graph[x][y]=0
    return len(killed)
    

ans = 0
# 궁수 위치 조합
for comb in combinations(position, 3):
    # 라운드
    tmp_graph = copy.deepcopy(graph)
    total_kill = 0
    for round in range(n, 0, -1):
        kill = BFS(tmp_graph, round, comb)
        total_kill = total_kill + kill
    ans = max(ans, total_kill)
print(ans)
    
'''
시간 복잡도
궁수 위치 조합 -> mC3 = 455
총 라운드 -> n
각 라운드 별 bfs -> d^2

= mc3 * n * d^2

ㅅ'''