# 플로이드 와샬로도 가능 O(n^3)이지만!

n = int(input())
m = int(input())
dist = [ [0]*(n+1) for _ in range(n+1) ]
for i in range(n):
    for j in range(n):
        if i!=j:
            dist[i][j]=float('inf')
        # 출발점과 도착점이 같으면 여행가능이라고 표시해야함
        elif i==j:
            dist[i][j]=1
graph = [ list(map(int, input().split())) for _ in range(n) ]

for i in range(n):
    for j in range(n):
        if i==j: continue
        if graph[i][j] > 0:
            dist[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

order_list = list(map(int, input().split()))
ans=0
for i in range(m-1):
    a, b = order_list[i], order_list[i+1]
    ans += dist[a-1][b-1]

if ans==float('inf'):
    print("NO")
else:
    print("YES") 
