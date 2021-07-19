from sys import stdin
from collections import deque

n, m = map(int, input().split())
graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range(n) ]

x_dir = [-1, 0, 1, 0]
y_dir = [0, 1, 0, -1]

def melt():
    x, y = 0, 0
    Q = deque()
    visit = [ [0]*m for _ in range(n) ]
    Q.append((x,y))
    visit[x][y] = 1

    # Find Chesse boundary
    while len(Q) > 0:
        x, y = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 1:
                graph[dx][dy] = 2
            elif 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0 and visit[dx][dy]==0:
                visit[dx][dy]=1
                Q.append((dx,dy))

    # Melting cheese
    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                graph[i][j]=0
    
def countCheese():
    visited = [ [0]* m for _ in range(n) ]
    block_cnt = 0
    cheese_cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==0:
                block_cnt = block_cnt + 1
                #cheese_cnt = cheese_cnt + 1
                visited[i][j]=1
                Q = deque()
                Q.append((i,j))
                while len(Q) > 0 :
                    x, y, = Q.popleft()
                    for i in range(4):
                        dx = x + x_dir[i]
                        dy = y + y_dir[i]
                        if 0<=dx<n and 0<=dy<m and graph[dx][dy]==1 and visited[dx][dy]==0:
                            #cheese_cnt = cheese_cnt + 1
                            visited[dx][dy]=1
                            Q.append((dx,dy))
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                cheese_cnt += 1

    return block_cnt, cheese_cnt

def printGraph(time):
    for i in graph:
        print(i)
    print()

# cheese counting
sec_before = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            sec_before += 1

# main fucnction
for time in range(1, 10000, 1):
    melt()
    block_cnt, cheese_cnt = countCheese()
    #
    # print(f'time : {time}')
    # printGraph(time)
    # print(block_cnt)
    # print()
    #
    if block_cnt==0:
        print(time)
        print(sec_before)
        exit()
        
    sec_before = cheese_cnt
    
