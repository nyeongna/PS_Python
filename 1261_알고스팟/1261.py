from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().rstrip().split())
graph = [ list(map(int, stdin.readline().rstrip())) for _ in range(n) ]

wall_num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            wall_num = wall_num + 1

left = 0
right = wall_num
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

ans = wall_num

while left <= right:
    mid = (left + right) // 2
    #print(f'mid: {mid}')
    flag=0
    Q = deque()
    Q.append((0,0,mid))
    visited = [ [-1]*m for _ in range(n) ]
    visited[0][0] = mid

    while len(Q) > 0:
        x,y,breaking = Q.popleft()
        #print(f'popped: {x} {y}')
        if x==n-1 and y==m-1:
            #print(f'{mid}으로 성공')
            ans = min(ans, mid)
            flag=1
            break
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if dx >= 0 and dx < n and dy >= 0 and dy < m and visited[dx][dy] <= breaking:
                # 가려는 곳이 벽이라면
                if graph[dx][dy] == 1 and breaking > 0 and visited[dx][dy] < breaking-1:
                    visited[dx][dy] = breaking-1
                    Q.append((dx,dy,breaking-1))
                # 가려는 곳이 빈 칸이라면
                elif graph[dx][dy] == 0 and visited[dx][dy] < breaking:
                    visited[dx][dy] = breaking
                    Q.append((dx,dy,breaking))
    # for i in visited:
    #     print(i)
    if flag==1:
        right = mid-1
    else:
        left = mid+1
print(ans)

