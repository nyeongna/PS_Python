from collections import deque
import math

m, n = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))


x_dir = [1, 0, -1, 0]
y_dir = [0, 1, 0, -1]
visited = [ [0]*m for _ in range(n) ]
room_cnt=0
max_room_size=float('-inf')
###########################################################################
'''
완전 탐색
O (50 * 50 * 4 * 50 * 50) = 2천 500만 = 통과
O (m * n * 4 * m * n)
'''
# 방 몇칸 인지 셈
def BFS(x, y, val, visited):
    global max_room_size
    Q = deque()
    Q.append((x,y))
    cnt=1
    while len(Q) > 0:
        x, y = Q.popleft()
        # '0000' 형식의 이진법으로 나타내서 0 이면 갈 수 있는 방향 1이면 벽 방향
        # 왼쪽부터 <<< 서, 북, 동, 남 >>>  순서
        bin_val = bin(graph[x][y])[2:].zfill(4)
        for i in range(4):
            # bin_val[i]가 0이어야지 뚫린 방향이다
            if bin_val[i]=='0':
                dx = x + x_dir[i]
                dy = y + y_dir[i]
                if 0<=dx<n and 0<=dy<m and visited[dx][dy]==0:
                    visited[dx][dy]=1
                    cnt += 1
                    Q.append((dx,dy))
    return cnt
    
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            room_cnt += 1
            visited[i][j]=1
            size = BFS(i,j, graph[i][j], visited)
            # 최대 방크기 계산
            max_room_size = max(max_room_size, size)

print(room_cnt)
print(max_room_size)

for i in range(n):
    for j in range(m):
        bin_val = bin(graph[i][j])[2:].zfill(4)
        # 각 칸 (50x5) 마다 벽이 있는 곳을 한 개씩 없애보고
        # 그 칸에 대해서만 BFS 실행
        # 못 가는 칸은 이미 최대 방을 구했으므로 또 다시 돌 필요가 없음
        for k in range(4):
            if bin_val[k]=='1':
                visited= [ [0]*m for _ in range(n) ]
                # 벽 허물고
                graph[i][j] -= int(math.pow(2, 3-k))
                visited[i][j]=1
                # 벽 허물고 몇 칸 늘어났는지 검사
                size=BFS(i, j, graph[i][j], visited)
                max_room_size = max(max_room_size, size)
                # 벽 다시 채우고
                graph[i][j] += int(math.pow(2,3-k))
print(max_room_size)

