n, m = map(int, input().split())
'''
1. 플로이드-와샬 O(n^3)을 통해
    모든 node 끼리의 길을 뚫어준다
    a= i node로 올 수 있는 node와
    b= i node로 부터 갈 수 있는 node에는 'inf'가 없을것이다
2. a+b를 합친 것이 n-1개이면 해당 node는 자신의 등수를 알 수 있음

3. n=500 이므로 500 * 500 * 500 = 1.25억이지만 캐싱을 통해 플로이드는 빠르다

'''
graph = [ [float('inf')]*(n+1) for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min( graph[i][k] + graph[k][j], graph[i][j])

ans = 0
for k in range(1, n+1):
    cnt=0
    for i in range(1, n+1):
        if graph[k][i] != float('inf'):
            cnt += 1
        if graph[i][k] != float('inf'):
            cnt += 1
    if cnt==n-1:
        ans += 1
print(ans)
