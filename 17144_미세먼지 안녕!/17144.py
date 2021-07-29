from sys import stdin
import copy

r, c, t = map(int, stdin.readline().strip().split())
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range(r) ]
cx1, cx2, cy = None, None, None
for i in range(r):
    for j in range(c):
        if graph[i][j]== -1:
            cx1, cx2, cy = i-1, i, j
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

def spread():
    global graph, r, c
    graph_tmp = [ [0]*c for _ in range(r) ]

    for i in range(r):
        for j in range(c):
            if graph[i][j] >= 5:
                cnt = 0
                d = graph[i][j]//5
                for k in range(4):
                    dx, dy = i + x_dir[k], j + y_dir[k]
                    if 0<=dx<r and 0<=dy<c and graph[dx][dy] != -1:
                        graph_tmp[dx][dy] += d
                        cnt += 1
                graph_tmp[i][j] -= d * cnt
    for i in range(r):
        for j in range(c):
            graph[i][j] += graph_tmp[i][j]

def clean_bottom():
    global r, c, cx2, cx2
    # 왼쪽
    for row in range(cx2+2, r, 1):
        graph[row-1][0] = graph[row][0]
    # 밑쪽
    for col in range(1, c, 1):
        graph[r-1][col-1] = graph[r-1][col]
    # 오른쪽
    for row in range(r-2, cx2-1, -1):
        graph[row+1][c-1] = graph[row][c-1]
    # 위쪽
    for col in range(c-2, 0, -1):
        graph[cx2][col+1] = graph[cx2][col]
    graph[cx2][1]=0

def clean_up():
    global r, c, cx1
    #왼쪽
    for row in range(cx1-2, -1, -1):
        graph[row+1][0] = graph[row][0]
    #위쪽
    for col in range(1, c, 1):
        graph[0][col-1] = graph[0][col]
    #오른쪽
    for row in range(1, cx1+1, 1):
        graph[row-1][c-1] = graph[row][c-1]
    #밑쪽
    for col in range(c-2, 0, -1):
        graph[cx1][col+1] = graph[cx1][col]
    graph[cx1][1]=0
    
for time in range(t):
    spread()
    clean_bottom()
    clean_up()

ans = 0
for i in range(r):
    for j in range(c):
        ans = ans + graph[i][j]
print(ans+2)
