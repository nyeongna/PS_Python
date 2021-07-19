import sys

r, c, k = map(int, input().split())
graph = [ list(map(str, input())) for _ in range(r) ]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

start = [r-1, 0 ]
end = [0, c-1]

visited = [ [0]*c for _ in range(r) ]
ans = 0
def DFS(x, y, dist):
    if x==end[0] and y == end[1] and dist == k:
        global ans
        ans = ans + 1
        return
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if (0 <= dx < r) and (0 <= dy < c) and graph[dx][dy] == '.' and visited[dx][dy] == 0:
            visited[dx][dy]=1
            DFS(dx, dy, dist+1)
            visited[dx][dy]=0

visited[start[0]][start[1]] = 1
DFS(start[0], start[1], 1)
print(ans)