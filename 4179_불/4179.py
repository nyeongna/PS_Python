from collections import deque
r, c = map(int, input().split())
graph = [ list(map(str,input())) for _ in range(r) ]
sx, sy, fire_list = None, None, list()
for i in range(r):
    for j in range(c):
        if graph[i][j]=='J':
            sx, sy = i, j
        elif graph[i][j] == 'F':
            fire_list.append((i,j))
Q, visited = deque(), [ [0]*(c+1) for _ in range(r+1) ]
for x,y in fire_list:
    Q.append((x,y,0,'F'))
    visited[x][y]=1
Q.append((sx,sy,0,'J'))
visited[sx][sy]=1
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while len(Q) > 0:
    x, y, dist, status = Q.popleft()
    if status=='J' and ((x==0 and 0<=y<c) or (x==r-1 and 0<=y<c) or (y==0 and 0<=x<r) or (y==c-1 and 0<=x<r)):
        print(dist+1)
        exit()
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<r and 0<=dy<c and visited[dx][dy]==0 and graph[dx][dy]=='.':
            visited[dx][dy]=1
            Q.append((dx,dy,dist+1,status))
print('IMPOSSIBLE')



'''
불이 이동할 공간에 똑같이 지훈이가 이동하면 지훈이는 타죽으므로,
불이 이동할 공간으로는 지훈이가 이동할 수 없다.
-> 불을 먼저 q에 넣으면 지훈이의 이동을 막을 수 있다
'''
