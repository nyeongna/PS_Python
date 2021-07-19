from sys import stdin
from collections import deque

def newDir(dir):
    if dir==1:
        return 1
    if dir==3:
        return 2
    if dir==2:
        return 3
    if dir==4:
        return 0

n, m = map(int, stdin.readline().rstrip().split())
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range (n) ]
sx, sy, sd = map(int, stdin.readline().rstrip().split())
gx, gy, gd = map(int, stdin.readline().rstrip().split())
sx -=1
sy -=1
gx -=1
gy -=1
sd = newDir(sd)
gd = newDir(gd)

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

Q = deque()
Q.append((sx, sy, sd, 0))
visited = [ [[0]*m for _ in range(n)] for _ in range(5) ]
visited[sd][sx][sy] = 1
dir_dict = {
    0: (-1, 0),
    1: (0, 1),
    2: (1,0),
    3: (0,-1)
}
def newDirection(dir, i):
    new_dir = (dir+i) % 4
    turnCnt = 0
    if i==0:
        turnCnt = 0
    elif i==1 or i==3:
        turnCnt = 1
    else:
        turnCnt = 2
    return dir_dict[new_dir][0], dir_dict[new_dir][1], new_dir, turnCnt

def changedDir(dir, i):
    new_dir = (dir+i)%4
    turnCnt=0
    if i==1 or i==3:
        turnCnt = 1
    if i==2:
        turnCnt=2
    return new_dir, turnCnt

while len(Q) > 0:
    x, y, dir, dist = Q.popleft()
    #print(f'--popped: x:{x}, y:{y}, dir:{dir}, dist:{dist}')
    if x==gx and y==gy and dir == gd:
        print(dist)
        exit()
    # 1, 2, 3 칸 전진
    for num in range(1,4,1):
        dx, dy = dir_dict[dir][0], dir_dict[dir][1]
        nx = x + dx*num
        ny = y + dy*num

        # 범위 벗어나면 break
        if nx < 0 or nx >= n or ny < 0 or ny >=m: break
        # 벽 만나면 더 이상 진행 불가이므로 break
        if graph[nx][ny] == 1: break
        # 이미 방문된 곳이라면, continue를 통해 +2, +3칸은 체크해본다
        if visited[dir][nx][ny]==1: continue

        visited[dir][nx][ny]=1
        #print(f'pushed- x:{nx}, y:{ny}, dir:{dir}, dist:{dist+1} 전진')
        Q.append((nx,ny,dir,dist+1))

    # 방향 전환
    for i in range(4):
        new_dir, turnCnt = changedDir(dir, i)
        if visited[new_dir][x][y] == 0:
            visited[new_dir][x][y] = 1
            #print(f'pushed- x:{x}, y:{y}, dir:{new_dir}, dist:{dist+turnCnt} 방향')
            Q.append((x,y,new_dir,dist+turnCnt))