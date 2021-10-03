import sys
sys.setrecursionlimit(30000)


######################################## input
n=int(input())
graph= list()
for _ in range(n):
    graph.append(input())

######################################## initialization
normal, blind = 0, 0
visit = [ [0]*n for _ in range(n)]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
#######################################
def DFS(x, y, color,status):
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]

        # 정상이라면
        if 0<=dx<n and 0<=dy<n and status=='normal' and graph[dx][dy]==color and visit[dx][dy]==0:
            visit[dx][dy]=1
            DFS(dx,dy,color,status)
        # 적록색약이라면
        elif 0<=dx<n and 0<=dy<n and status=='blind' and visit[dx][dy]==0:
            # 'R' ,'G' 라면
            if (color=='R' or color=='G') and (graph[dx][dy]=='R' or graph[dx][dy]=='G'):
                visit[dx][dy]=1
                DFS(dx,dy,color,status)
            # 'B' 라면
            elif color=='B' and graph[dx][dy]=='B':
                visit[dx][dy]=1
                DFS(dx,dy,color,status)

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            normal += 1
            visit[i][j]=1
            DFS(i,j,graph[i][j],'normal')

visit = [ [0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            blind += 1
            visit[i][j]=1
            DFS(i,j,graph[i][j],'blind')

print(normal, blind)