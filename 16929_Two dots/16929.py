n, m = map(int, input().split())
graph = list()
for _ in range(n):
    row = list(map(str, input()))
    graph.append(row)

visited = [ [0]*(m) for _ in range(n) ]
finished = [ [0]*(m) for _ in range(n) ]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
possible_dir = {
    -1:[0,1,2,3],
    0:[0,1,3],
    1:[0,1,2],
    2:[1,2,3],
    3:[0,2,3]
}
def DFS(x, y, cnt, color, dir):
    global visited, finished
    visited[x][y] = 1
    for i in range(4):
        if i not in possible_dir[dir]:
            continue
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<n and 0<=dy<m and visited[dx][dy]==0 and graph[dx][dy]==color:
            DFS(dx,dy,cnt+1,color,i)
        elif 0<=dx<n and 0<=dy<m and finished[dx][dy] == 0 and graph[dx][dy]==color and cnt>=4:
            print('Yes')
            exit()
    finished[x][y]=1

for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            DFS(i, j, 1, graph[i][j], -1)
print('No')