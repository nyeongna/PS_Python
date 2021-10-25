import sys
sys.setrecursionlimit(62600)
n, m = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

ans=0
x_dir=[-1,0,1,0,-1,1,1,-1]
y_dir=[0,1,0,-1,1,1,-1,-1]

visited=[ [0]*(m+1) for _ in range(n+1) ]
def dfs(x, y):
    cnt = 1
    for i in range(8):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<n and 0<=dy<m and graph[dx][dy]==1 and visited[dx][dy]==0:
            visited[dx][dy]=1
            graph[dx][dy]=0
            cnt += dfs(dx,dy)
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            #print(i,j)
            visited[i][j]=1
            graph[i][j]=0
            ans+=1
            dfs(i,j)
print(ans)