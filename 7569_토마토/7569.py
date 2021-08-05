from collections import deque

'''
시간 복잡도
O(r * c * h) = O(1,000,000) 통과
'''
c, r, h = map(int, input().split())
graph = [ [list(map(int, input().split())) for _ in range(r) ]  for _ in range(h) ]

cnt = 0
tomato_Q = deque()
visited = [ [ [0]*c for _ in range(r)] for _ in range(h)]
for k in range(h):
    for i in range(r):
        for j in range(c):
            if graph[k][i][j]==0:
                cnt = cnt + 1
            elif graph[k][i][j]==1:
                tomato_Q.append((k,i,j,0))
                visited[k][i][j]=1

# 모두 익어있는 상태라면 0 출력 후 종료
if cnt == 0:
    print(0)
    exit()
ans = float('-inf')
x_dir = [-1,0,1,0,0,0]
y_dir = [0,1,0,-1,0,0]
z_dir = [0,0,0,0,1,-1]

# BFS
while len(tomato_Q) > 0:
    z,x,y,time = tomato_Q.popleft()
    ans = max(ans, time)
    for i in range(6):
        dx, dy, dz = x + x_dir[i], y + y_dir[i], z + z_dir[i]
        if 0<=dx<r and 0<=dy<c and 0<=dz<h and visited[dz][dx][dy] == 0 and graph[dz][dx][dy]==0:
            cnt = cnt - 1
            visited[dz][dx][dy]=time+1
            tomato_Q.append((dz,dx,dy,time+1))
# 모두 다 익었다면
if cnt == 0:
    print(ans)
# 덜 익은 토마토 존재한다면
else:
    print(-1)







