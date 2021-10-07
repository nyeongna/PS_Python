n = int(input())
graph = [input() for _ in range(n)]
visited = [ [ 0 for _ in range(n) ] for _ in range(n) ]

ans_list = list()
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
def DFS(x, y):
    global graph

    cnt = 1
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<n and 0<=dy<n and visited[dx][dy]==0 and graph[dx][dy]=='1':
            visited[dx][dy]=1
            cnt = cnt + DFS(dx,dy)
    return cnt
for i in range(n):
    for j in range(n):
        if graph[i][j]=='1' and visited[i][j]==0:
            visited[i][j]=1
            cnt = DFS(i,j)
            ans_list.append(cnt)
ans_list = sorted(ans_list)
print(len(ans_list))
for i in ans_list:
    print(i)