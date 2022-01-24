import copy
n, m = map(int, input().split())
'''
완전탐색
-모든 CCTV를 4방향 다 검사한다
-최대 CCTV 갯수는 8개
-바꿀 수 있는 방향 4개
--> 4^8 * (nm) = 400만
'''

graph = [ list(map(int,input().split())) for _ in range(n) ]
cctv_list = list() # (x좌표, y좌표, cctv 종류)
wall_list = list() # (x좌표, y좌표)
rec = [0]*10
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 6:
            wall_list.append((i,j))
        elif 1<=graph[i][j]<=5:
            cctv_list.append((i,j,graph[i][j]))
cctv_dir = {
    1: [ [(-1,0)],        [(0,1)],        [(1,0)],         [(0,-1)] ],
    2: [ [(-1,0), (1,0)], [(0,1), (0,-1)], [(-1,0), (1,0)], [(0,1), (0,-1)] ],
    3: [ [(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(0,-1), (-1,0)] ],
    4: [ [(0,-1),(-1,0),(0,1)], [(-1,0),(0,1),(1,0)], [(0,1), (1,0), (0,-1)], [(1,0), (0,-1), (-1,0)] ],
    5: [ [(-1,0),(0,1), (1,0), (0,-1)], [(-1,0),(0,1), (1,0), (0,-1)], [(-1,0),(0,1), (1,0), (0,-1)], [(-1,0),(0,1), (1,0), (0,-1)] ]
}
def see(dc, cctv, tmp_graph):
    x, y, c = cctv[0], cctv[1], cctv[2]
    for dir in cctv_dir[c][dc]:
        dx = x + dir[0]
        dy = y + dir[1]
        while 0<=dx<n and 0<=dy<m and graph[dx][dy] != 6:
            tmp_graph[dx][dy] = '#'
            dx = dx + dir[0]
            dy = dy + dir[1]
            
ans = float('inf')
def dfs(level):
    global ans
    if level==len(cctv_list):
        tmp_graph = copy.deepcopy(graph)
        for idx,cctv in enumerate(cctv_list):
            see(rec[idx],cctv,tmp_graph)
        blind=0
        for i in range(n):
            for j in range(m):
                if tmp_graph[i][j]==0:
                    blind += 1
        ans = min(ans, blind)
        return
    for i in range(4):
        rec[level]=i
        dfs(level+1)
dfs(0)
print(ans)