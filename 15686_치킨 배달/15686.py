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

# chicken, home 위치를 미리 다 저장
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

# 폐점 안시킬 위치를 조합으로 알아냄
for comb in combinations(chicken_list, m):
    total_dist = 0
    # 각 집에서 가장 가까운 치킨거리 찾아냄
    for home in home_list:
        min_dist = float('inf')
        for chicken in comb:
            min_dist = min(min_dist, abs(home[0]-chicken[0])+abs(home[1]-chicken[1]))
        total_dist += min_dist
    # 가장 가까운 치킨거리 합을 업데이트
    ans = min(ans, total_dist)
print(ans)


