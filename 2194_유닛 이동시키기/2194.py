from collections import deque

n, m, a, b, k = map(int, input().split())
graph = [ [0]*(m+1) for _ in range(n+1) ] 
for _ in range(k):
    x, y, = map(int, input().split())
    graph[x-1][y-1] = 1
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
gx, gy = map(int, input().split())
gx, gy = gx-1, gy-1

############## BFS 이용 최단거리
Q = deque()
Q.append((sx,sy,0))
visited = [ [0]* (m+1) for _ in range(n+1) ]
visited[sx][sy]=1

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while len(Q) > 0:
    x, y, dist = Q.popleft()
    if x==gx and y==gy:
        print(dist)
        exit()
    # 4방향 동서남북 체크
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        flag=1
        # 맨왼쪽위 좌표만 이용해서 방문여부 체크
        if 0<=dx<n and 0<=dy<m and visited[dx][dy]==1:
            continue
        # 안가본 좌표면, 유닛 전체 크기가 움직일 수 있는지 체크
        for xx in range(a):
            for yy in range(b):
                if 0 > dx+xx or dx+xx >= n or 0 > dy+yy or dy+yy >= m or graph[dx+xx][dy+yy] == 1:
                    flag=0
                    break
            if flag==0:
                break
        # 유닛이 움직일 수 있다면 bfs deque에 추가
        if flag==1:
            visited[dx][dy]=1
            Q.append((dx,dy,dist+1))

print(-1)