from collections import deque
from itertools import combinations
from sys import stdin

n, m = map(int, stdin.readline().strip().split())
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range(n) ]

zero_list, virus_list = [], []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_list.append((i,j))
        elif graph[i][j]==2:
            virus_list.append((i,j))

ans, x_dir, y_dir = 0, [-1,0,1,0], [0,1,0,-1]
for comb in combinations(zero_list, 3):
    # 3개 벽 세우기
    for (x,y) in comb:
        graph[x][y] = 1
    # 바이러스 퍼뜨리기
    cnt = 0
    Q = deque(virus_list)
    visited = [ [0]*m for _ in range(n) ]
    while len(Q) > 0:
        x, y = Q.popleft()
        for i in range(4):
            dx, dy = x + x_dir[i], y + y_dir[i]
            if 0<=dx<n and 0<=dy<m and graph[dx][dy]==0 and visited[dx][dy]==0:
                visited[dx][dy]=1
                Q.append((dx,dy))
    # 안전영역 카운트
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0 and visited[i][j]==0:
                cnt = cnt+1
    # 최대 안전영역 비교
    ans = max(ans, cnt)
    # 3개 벽 풀기
    for (x,y) in comb:
        graph[x][y] = 0
print(ans)
 
'''
시간 복잡도
0 <= N, M <= 8 이므로 벽을 세울 수 있는 경우의 수 64C3 = 40,000
BFS 한번 당 N, M = 64
64C3 * N * M = 2,560,000 통과 가능
'''

    
    
