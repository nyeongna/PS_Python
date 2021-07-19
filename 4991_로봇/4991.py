from sys import stdin
from collections import deque
from itertools import permutations

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while True:
    m, n = map(int, stdin.readline().rstrip().split())
    if n == 0 and m ==0:
        exit()
    graph = [ list(map(str, stdin.readline().rstrip())) for _ in range(n) ]
    rx, ry = 0, 0
    
    cand_list = []
    # 로봇의 위치부터 cand_list에 추가
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                rx, ry = i, j
                cand_list.append((i,j))
    # 더러운곳 위치를 cand_list에 로봇 위치 다음에 순차적으로 추가
    for i in range(n):
        for j in range(m):
            if graph[i][j] =='*':
                cand_list.append((i,j))


    cand_dist_list = [ [0]*len(cand_list) for _ in range(len(cand_list)) ]
    # 총 방문해야할 더러운곳의 갯수
    dirty_num = len(cand_list)
    flag=0
    # 로봇과 더러운곳 사이의 최단거리를 BFS를 통해 다 미리 구해서 2차원 배열(cand_dist_list)에 저장
    for idx, (x, y) in enumerate(cand_list):
        dirty_cnt = len(cand_list)
        Q = deque()
        visited = [[0]*m for _ in range(n)]
        Q.append((x,y,0))
        visited[x][y]=1
        while len(Q) > 0:
            xx, yy, dist= Q.popleft()
            if (xx,yy) in cand_list:
                cand_dist_list[idx][cand_list.index((xx,yy))] = dist
                dirty_cnt -= 1
                if dirty_cnt == 0:
                    break
            for i in range(4):
                dx = xx + x_dir[i]
                dy = yy + y_dir[i]
                if dx>=0 and dx<n and dy>=0 and dy<m and visited[dx][dy]==0 and graph[dx][dy] != 'x':
                    visited[dx][dy] = 1
                    Q.append((dx,dy,dist+1))
        # 모든 더러운 곳을 방문하지 못했다면 -1 출력
        if dirty_cnt != 0:
            flag=1
            break
    if flag==1:
        print(-1)
        continue
                    
    # 모든 더러운곳의 순열을 만들어서 각각 거리를 빠르게 구해서 (상수시간, 2차원배열로 미리 구했음)
    # 젤 빠른 거리의 합을 print
    ans = float('inf')
    num_list = [ i+1 for i in range(len(cand_list)-1) ]
    for comb in permutations(num_list, len(num_list)):
        dist = cand_dist_list[0][comb[0]]
        for idx in range(len(comb)-1):
            dist += cand_dist_list[comb[idx]][comb[idx+1]]
        ans = min(ans, dist)
    print(ans)
    



    


