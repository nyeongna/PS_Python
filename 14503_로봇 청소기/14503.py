from sys import stdin
import sys

n, m = map(int, input().split())
rx, ry, direction = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
visited = [ [0]*m for _ in range(n) ]

# 다음 방향 좌표 및 방향을 알려준다
def nextDir(d, idx, x, y):
    nd = (d+idx)%4
    if nd==0:
        return (-1+x, 0+y,nd)
    elif nd==1:
        return (0+x, 1+y,nd)
    elif nd==2:
        return (1+x, 0+y,nd)
    elif nd==3:
        return (0+x, -1+y,nd)

# 후진 방향 좌표를 알려준다
def backDir(x, y, d):
    if d==0:
        return (x+1, y)
    elif d==1:
        return (x, y-1)
    elif d==2:
        return (x-1, y)
    elif d==3:
        return (x, y+1)

ans = 1
while True:
    visited[rx][ry] = 1
    flag=0
    # 4방향 탐색
    for i in range(3, -1, -1):
        dx, dy, dd = nextDir(direction, i, rx, ry)
        # 청소가 가능한 방향이면 청소를 하고 표시를 한다(flag=1) 그리고 청소칸 + 1
        if dx>=0 and dx<n and dy>=0 and dy<m and visited[dx][dy]==0 and graph[dx][dy]==0:
            visited[dx][dy]=1
            rx, ry, direction = dx, dy, dd
            ans = ans + 1
            flag=1
            break
    # 청소할 곳이 있다면 1번으로 돌아감
    if flag==1:
        continue
    # 뒤에가 벽이라서 후진이 불가하면 exit
    bx, by = backDir(rx, ry, direction)
    if graph[bx][by]==1:
        print(ans)
        exit()
    # 후진 가능 하면 후진하고 continue
    rx, ry = bx, by

'''
시간 복잡도
O (N x M)
'''