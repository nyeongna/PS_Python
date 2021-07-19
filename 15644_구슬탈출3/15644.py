from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [ list(map(str,stdin.readline().strip())) for _ in range(n) ]

rx, ry = 0, 0
bx, by = 0, 0
hx, hy = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j
        if graph[i][j] == 'O':
            hx, hy = i, j

visited = [ [ [ [0]*11 for _ in range(11) ] for _ in range(11) ] for _ in range(11) ]

Q = deque()
Q.append((rx, ry, bx, by, 0, ""))
visited[rx][ry][bx][by] = 1
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
z_dir = ['U','R','D','L']

def move(_x, _y, dx, dy):
    cnt=0
    while _x+dx >= 0 and _x+dx < n and _y+dy>=0 and _y+dy<m and graph[_x+dx][_y+dy] != '#':
        _x += dx
        _y += dy
        cnt += 1
        if graph[_x][_y] == 'O':
            return (0,0,0,0)
    return (_x, _y, cnt, 1)

while len(Q) > 0:
    rx, ry, bx, by, dist, route = Q.popleft()
    for i in range(4):
        nrx, nry, rmove, rResult = move(rx, ry, x_dir[i], y_dir[i])
        nbx, nby, bmove, bResult = move(bx, by, x_dir[i], y_dir[i])
        # blue 
        if bResult == 0:
            continue
        # red 
        if rResult == 0 and dist+1 <= 10:
            print(dist+1)
            print(route+z_dir[i])
            exit()
        # red, blue 
        if nrx==nbx and nry==nby:
            # Red
            if rmove > bmove:
                nrx = nrx - x_dir[i]
                nry = nry - y_dir[i]
            # blue
            elif rmove < bmove:
                nbx = nbx - x_dir[i]
                nby = nby - y_dir[i]
        
        if visited[nrx][nry][nbx][nby] == 0 and dist+1 <= 9:
            visited[nrx][nry][nbx][nby] = 1
            Q.append((nrx, nry, nbx, nby, dist+1, route+z_dir[i]))
        
print(-1)

            


