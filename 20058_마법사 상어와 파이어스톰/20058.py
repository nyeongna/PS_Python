'''
1. 회전한다
2. 2개 이하로 연결된 곳의 얼음 -1
3. 1~2번 반복
'''
from collections import deque
n, q = map(int, input().split())
graph = [ list(map(int,input().split())) for _ in range(2**n) ]
level_list = list(map(int, input().split()))
nn = 2**n
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

def bfs(x,y,visited):
    Q = deque()
    Q.append((x,y,0))
    visited_list = list([x,y])
    visited[x][y]=1
    cnt, total_ice = 1, graph[x][y]
    while len(Q) > 0:
        x, y, dist = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if 0<=dx<nn and 0<=dy<nn and visited[dx][dy]==0 and graph[dx][dy]>0:
                Q.append((dx,dy,dist+1))
                visited_list.append((dx,dy))
                visited[dx][dy]=1
                cnt+=1
                total_ice += graph[dx][dy]
    return cnt, total_ice

def meltIce(x,y, melt_ice_list):
    cnt=0
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<nn and 0<=dy<nn and graph[dx][dy] > 0:
            cnt+=1
    if cnt < 3:
        melt_ice_list.append((x,y))

# q만큼 돌린다
for level in level_list:
    size = 2**level
    # 2^level 크기로 구역 나누기
    # x, y 는 구역의 첫번째 구역
    for x in range(0, nn, size):
        for y in range(0, nn, size):
            tmp_graph = list()
            for i in range(size):
                row=list()
                for j in range(size):
                    row.append(graph[x+i][y+j])
                tmp_graph.append(row)
            tmp_graph=list(zip(*tmp_graph[::-1]))

            for i in range(size):
                for j in range(size):
                    graph[x+i][y+j] = tmp_graph[i][j]

    # 얼음 -1 하기
    melt_ice_list = list()
    for i in range(nn):
        for j in range(nn):
            if graph[i][j] > 0:
                meltIce(i,j, melt_ice_list)
    for xx,yy in melt_ice_list:
        graph[xx][yy] -= 1

    # 남아있는 얼음 합
    # 가장 큰 덩어리 크기
    visited=[ [0]*(nn+1) for _ in range(nn+1) ]
    total_ice_size = 0
    max_ice_cnt = 0
    for i in range(nn):
        for j in range(nn):
            if graph[i][j] > 0 and visited[i][j]==0:
                ice_cnt, ice_size = bfs(i,j,visited)
                max_ice_cnt = max(max_ice_cnt, ice_cnt)
                total_ice_size += ice_size
    
print(total_ice_size)
print(max_ice_cnt)
