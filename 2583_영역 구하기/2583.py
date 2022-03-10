# 예제에서랑 다르게 r,c를 뒤바꿔서 저장한다
c, r, k = map(int, input().split())
graph = [ [0]*c for _ in range(r)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())

    # 에제의 그래프를 90도 시계방향으로 돌린 그래프에 칠한다
    # 돌려도 어차피 동일한 결과를 나타냄
    for i in range(lx, rx):
        for j in range(ly, ry):
            graph[i][j]=1
visited = [ [0]*c for _ in range(r) ]
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

from collections import deque
def bfs(x,y):
    Q = deque()
    Q.append((x,y))
    cnt=1
    while len(Q) > 0:
        x, y = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if 0<=dx<r and 0<=dy<c and graph[dx][dy]==0 and visited[dx][dy]==0:
                visited[dx][dy]=1
                cnt+=1
                Q.append((dx,dy))
    return cnt
ans=0
ans_list=list()
for i in range(r):
    for j in range(c):
        if graph[i][j]==0 and visited[i][j]==0:
            visited[i][j]=1
            cnt=bfs(i,j)
            ans_list.append(cnt)
            ans+=1
ans_list.sort()
print(ans)
print(*ans_list)