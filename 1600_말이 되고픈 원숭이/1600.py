k = int(input())
c, r = map(int, input().split())
graph = [ list(map(int,input().split())) for _ in range(r) ]
from collections import deque
'''
-k번 동안 나이트처럼 움직일 수 있음. (장애물을 뛰어넘을 수 있음!)
--장애물에 도착할 수는 없음
-k번을 다 쓴 이후에는 동서남북으로만 이동가능 (장애물쪽으로 이동 불가능)
 [시작->도착] 하는 최소 이동 횟수는 ? => BFS

-200 * 200 * 30 배열을 만든다
visited[k][i][j]: k 횟수가 남아있을때 <i,j> 칸에 도달할 수 있는 최소이동횟수
'''
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
hx_dir = [-1, -2, -2, -1, 1, 2, 2, 1]
hy_dir = [-2, -1, 1, 2, 2, 1, -1, -2]
visited = [ [ [0]*c for _ in range(r) ] for _ in range(k+1) ]
Q = deque()
# x, y, dist, 남은이동횟수
Q.append((0,0,0,k))
visited[k][0][0]=1
ans = float('inf')

while len(Q) > 0:
    x, y, dist, kk = Q.popleft()
    if x==r-1 and y==c-1:
        ans = min(ans, dist)
        continue
    # 나이트 이동방향이 1이상 남아있으면 시도해본다
    if kk > 0:
        for i in range(8):
            dx = x + hx_dir[i]
            dy = y + hy_dir[i]
            # 가려는 방향을 남은횟수가 똑같은 상태에서 이미 가봤다면 pass
            # 나이트 무빙 체크
            if 0<=dx<r and 0<=dy<c and graph[dx][dy]==0 and visited[kk-1][dx][dy]==0:
                visited[kk-1][dx][dy]=dist+1
                Q.append((dx,dy,dist+1,kk-1))
    # 동서남북 체크
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<r and 0<=dy<c and graph[dx][dy]==0 and visited[kk][dx][dy]==0:
            visited[kk][dx][dy]=dist+1
            Q.append((dx,dy,dist+1,kk))
if ans==float('inf'):
    print(-1)
else:
    print(ans)

        





