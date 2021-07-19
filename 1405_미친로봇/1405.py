import sys

n, E, W, S, N = map(int, input().split())
E = E / 100
W = W / 100
S = S / 100
N = N / 100

visited = [ [0]*35 for _ in range(35) ] 
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

ans = 0
def DFS(x,y,dist,prob):
    if dist==n:
        global ans
        ans = ans + prob
        return
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if visited[dx][dy]==0:
            visited[dx][dy]=1
            if i==0:
                DFS(dx,dy,dist+1,prob*N)
            elif i==1:
                DFS(dx,dy,dist+1,prob*E)
            elif i==2:
                DFS(dx,dy,dist+1,prob*S)
            else:
                DFS(dx,dy,dist+1,prob*W)
            visited[dx][dy]=0
visited[15][15] = 1
DFS(15,15,0,1)
print(ans)
