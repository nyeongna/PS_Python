######################################################################## INPUT
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

import heapq
from collections import deque

sx, sy, ss, s_eat, ans_time = None, None, 2, 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            sx, sy = i, j
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
'''
시간복잡도:
물고기를 찾을 때 마다 O(N^2 * logN)
총 물고기 O(N^2)

==> O(N^4 * logN), N=20이므로 가능
'''
######################################################################## 알고리즘
while True:
    #1. 현재 위치에서 갈 수 있는 물고기 전체 위치를 파악 (BFS)
    Q = deque()
    Q.append((sx,sy,0))
    visited = [ [0]*n for _ in range(n) ]
    visited[sx][sy]=1

    ## 상어로부터 가장 가까운 물고기 위치 저장하는 min_heap
    ### Min_heap 말고 bfs를 도는데 위에 왼쪽 부터 찾는 순으로 구현해도 됨
    fish_list = list()

    while len(Q) > 0:
        x, y, dist = Q.popleft()
        for i in range(4):
            dx, dy = x + x_dir[i], y + y_dir[i]
            if 0<=dx<n and 0<=dy<n and visited[dx][dy]==0 and graph[dx][dy] <= ss:
                if graph[dx][dy] != 0 and graph[dx][dy] < ss:
                    heapq.heappush(fish_list, (dist+1, dx, dy))
                visited[dx][dy]=1
                Q.append((dx,dy,dist+1))
    
    #2. 가장 가까운 물고기 위치로 간다 (min heap)
    ## 더 이상 먹을 수 있는 물고기가 없으면 종료
    if len(fish_list) == 0:
        print(ans_time)
        exit()
    # 가장 가까운 물고기 위치 뽑고, 현재 물고기 위치를 0으로 치환
    ndist, nx, ny = heapq.heappop(fish_list)
    graph[sx][sy]=0
    # 해당 위치로 옮겨주고, 성장하고, 다 컸으면 size up, 시간초도 ndist 만큼 up
    sx, sy, s_eat, ans_time = nx, ny, s_eat+1, ans_time + ndist
    graph[sx][sy]=9
    if ss == s_eat:
        ss += 1
        s_eat = 0
