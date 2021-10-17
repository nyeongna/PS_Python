from collections import deque

n, m = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append((list(map(str,input()))))


for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            rx, ry = i, j
        if graph[i][j]=='B':
            bx, by = i, j
        if graph[i][j]=='O':
            gx, gy = i, j
x_dir = (-1, 0, 1, 0)
y_dir = (0, 1, 0, -1)

def move(x, y, dir):

    move_cnt = 0    
    while 0 <= x + x_dir[dir] < n and 0 <= y + y_dir[dir] < m and graph[x+x_dir[dir]][y+y_dir[dir]] != '#':
        #print(f'{x+x_dir[dir]} {y+y_dir[dir]}')
        x = x + x_dir[dir]
        y = y + y_dir[dir]
        move_cnt += 1
        # 골에 빠졌다면
        if x==gx and y==gy:
            return (x, y, move_cnt, 1)
    #print(f'최종: {x},{y}')
    return (x, y, move_cnt, 0)

Q = deque()
Q.append((rx,ry,bx,by,0))
visited=dict()
visited[(rx,ry,bx,by)]=1

while len(Q) > 0:
    rx, ry, bx, by, dist = Q.popleft()
    
    if dist > 10:
        print(-1)
        exit()
    for i in range(4):

        nRx, nRy, Rmove, Rgoal = move(rx, ry, i)
        nBx, nBy, Bmove, Bgoal = move(bx, by, i)
        
        # 파란구슬이 빠졌다면 continue
        if  Bgoal==1:
            continue

        # 파란구슬 안빠지고 빨간구슬이 빠졌다면 성공
        if  Rgoal==1 and dist+1 <=10 :
            print(dist+1)
            exit()

        # 두 구슬이 같은 장소에 도달했다면, 많이 움직인 구슬을 한칸 움직인 반대방향으로 옮김.
        if nRx == nBx and nRy == nBy:
            if Rmove > Bmove:
                nRx = nRx + x_dir[i]*-1
                nRy = nRy + y_dir[i]*-1
                Rmove -= 1
            if Rmove < Bmove:
                nBx = nBx + x_dir[i]*-1
                nBy = nBy + y_dir[i]*-1
                Bmove -= 1
        # 둘다 안움직였을때 pass
        if  Rmove == 0 and Bmove == 0:
            visited[(nRx,nRy,nBx,nBy)]=1
            continue
        # 이미 방문했으면 pass
        if (nRx, nRy,nBx,nBy) in visited:
            continue
        # 방문 표시하고 deque에 추가
        visited[(nRx,nRy,nBx,nBy)]=1
        Q.append((nRx,nRy,nBx,nBy, dist+1))

print(-1)
    
