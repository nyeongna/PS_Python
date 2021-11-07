from sys import stdin

n, m = map(int, stdin.readline().strip().split())
dist = [ [0]*(n+1) for _ in range(n+1) ]
for i in range(n+1):
    for j in range(n+1):
        if i!=j:
            dist[i][j] = float('inf')
for _ in range(m):
    f, s, d = map(int, stdin.readline().strip().split())
    dist[f][s]=d
    dist[s][f]=d
a, b = map(int, stdin.readline().strip().split())

# O(n^3) 이어서 n=1000 이지만
# 캐싱떄문에 1초안에 돌아간다.
# 파이썬의 입력 시간 문제때문에 터지는듯
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j: continue
            dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

ans = min(dist[1][a] + dist[a][b] + dist[b][n], dist[1][b] + dist[b][a] + dist[a][n])
if ans == float('inf'):
    print(-1)
else:
    print(ans)

