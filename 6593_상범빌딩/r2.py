from collections import deque


x_dir = [-1,0,1,0,0,0]
y_dir = [0,1,0,-1,0,0]
z_dir = [0,0,0,0,1,-1]
while True:
    l, r, c = map(int, input().split())
    if l==0 and r==0 and c==0:
        exit()
    graph = list()
    for _ in range(l):
        floor = list()
        for _ in range(r):
            col = list(map(str, input()))
            floor.append(col)
        throw = input()
        graph.append(floor)
    
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if graph[k][i][j] == 'S':
                    sz, sx, sy = k, i, j
                if graph[k][i][j] == 'E':
                    gz, gx, gy = k, i, j
    #print(gz, gx, gy)
    Q = deque()
    Q.append((sz, sx, sy, 0))
    visited = [ [ [ 0 for _ in range(c) ] for _ in range(r) ] for _ in range(l) ]
    visited[sz][sx][sy] = 1

    while len(Q) > 0:
        z, x, y, dist = Q.popleft()
        if z == gz and x == gx and y == gy:
            print(f'Escaped in {dist} minute(s).')
            break
        for i in range(6):
            dz, dx, dy = z + z_dir[i], x + x_dir[i], y + y_dir[i]
            if 0<=dx<r and 0<=dy<c and 0<=dz<l and visited[dz][dx][dy]==0 and (graph[dz][dx][dy]=='.' or graph[dz][dx][dy]=='E'):
                visited[dz][dx][dy]=1
                Q.append((dz, dx, dy, dist+1))
                #print(f'dz, dx, dy {dz, dx, dy} added')
    if not (z == gz and x == gx and y == gy):
        print('Trapped!')