'''
시간 복잡도
nCr = 100
집최대갯수 2*n = 100
집당 bfs = 2500
2500 x 100 x 100 = 2천500만 통과
'''
from itertools import combinations

n, m = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

chicken_list = list()
home_list = list()
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken_list.append((i,j))
            graph[i][j]=0
        elif graph[i][j]==1:
            home_list.append((i,j))

ans = float('inf')
for comb in combinations(chicken_list, m):
    for x,y in comb:
        graph[x][y]=2
    total_dist = 0
    for home in home_list:
        min_dist = float('inf')
        for chicken in comb:
            min_dist = min(min_dist, abs(home[0]-chicken[0])+abs(home[1]-chicken[1]))
        total_dist += min_dist
    ans = min(ans, total_dist)
    
print(ans)


