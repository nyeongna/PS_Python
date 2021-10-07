########################################### init
n = int(input())
graph = [input() for _ in range(n)]
visited = [ [ 0 for _ in range(n) ] for _ in range(n) ]

ans_list = list()
###########################################
# DFS 들어왔을때 범위 검사를 함 
def DFS(x, y):
    if 0 > x or x >= n or 0 > y or y >= n or visited[x][y]==1 or graph[x][y]=='0':
        return 0
    visited[x][y]=1
    # DFS 들어오기 전에 범위 검사 X
    return 1 + DFS(x-1, y) + DFS(x, y+1) + DFS(x+1, y) + DFS(x, y-1)

for i in range(n):
    for j in range(n):
        if graph[i][j]=='1' and visited[i][j]==0:
            ans_list.append(DFS(i,j))

############################################ Sorting in ascending order
ans_list = sorted(ans_list)

############################################ 정답 출력
print(len(ans_list))
for i in ans_list:
    print(i)