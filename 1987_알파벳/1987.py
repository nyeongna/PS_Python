r, c = map(int, input().split())

graph = [ input() for _ in range(r) ]

alpha = [0] * 26
ans = 1
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

def DFS(x, y, dist):
    global ans
    ans = max(ans, dist)
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx>=0 and dx < r and dy>=0 and dy < c and alpha[ord(graph[dx][dy])-ord('A')]==0:
            alpha[ord(graph[dx][dy])-ord('A')]=1
            DFS(dx,dy,dist+1)
            alpha[ord(graph[dx][dy])-ord('A')]=0

alpha[ord(graph[0][0])-ord('A')]=1
DFS(0,0,1)
print(ans)
