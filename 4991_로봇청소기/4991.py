from sys import stdin
from collections import deque
from itertools import permutations


x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while True:
    m, n = map(int, stdin.readline().rstrip().split())
    if m == 0 and n == 0:
        exit()
    graph = [ list(map(str, stdin.readline().rstrip())) for _ in range (n) ]

    dirty_list = []
    # 시작 위치 먼저 찾기. (dirty_list의 0번째 idx가 시작 위치가 되도록)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                dirty_list.append((i,j))
    # 더러운 곳 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='*':
                dirty_list.append((i,j))
    dirty_list_dist = [ [0]*len(dirty_list) for _ in range(len(dirty_list)) ]

    flag=0

    # 원점과 더러운곳 사이들의 위치를 구한다.
    for idx, (x,y) in enumerate(dirty_list):
        Q = deque()
        Q.append((x,y,0))
        visited = [ [0]*m for _ in range(n) ]
        visited[x][y]=1
        
        cnt=0
        while len(Q) > 0:
            xx,yy,dist = Q.popleft()
            if (xx,yy) in dirty_list:
                dirty_list_dist[idx][dirty_list.index((xx,yy))] = dist
                cnt=cnt+1
            for i in range(4):
                dx = xx + x_dir[i]
                dy = yy + y_dir[i]
                if dx>=0 and dx<n and dy>=0 and dy<m and visited[dx][dy]==0 and graph[dx][dy] != 'x':
                    visited[dx][dy]=1
                    Q.append((dx,dy,dist+1))
        #print(cnt, len(dirty_list))
        if cnt != len(dirty_list):
            flag=1
            break
    if flag==1:
        print(-1)
        continue
    # 모든 순열에 대해 계산해서 최소 거리를 찾아낸다
    ans = float('inf')
    permu_list = [ x for x in range(1, len(dirty_list), 1) ]
    for permu in permutations(permu_list, len(permu_list)):
        dist = dirty_list_dist[0][permu[0]]
        for idx,num in enumerate(permu[:-1]):
            dist = dist + dirty_list_dist[permu[idx]][permu[idx+1]]
        ans = min(ans, dist)
    print(ans)

        
