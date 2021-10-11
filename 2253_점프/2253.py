
n, m = map(int, input().split())
dp = [ [ float('inf') for _ in range(200)] for _ in range(n+1) ]
X_list = dict()
for _ in range(m):
    X_list[int(input())]=1
if 2 in X_list:
    print(-1)
    exit()
dp[1][0] = 0
dp[2][1] = 1
for i in range(2, n+1):
    # i번째 돌은 너무 작다면 continue
    if i in X_list:
        continue
    # n이 최대 10000이므로 최대 점프 크기는 200 이하이다. (n^2 + n - 20000 = 0)
    for j in range(200):
        # 'i'번째 돌에 j번째 점프로 도착한 기록이 있다면
        if dp[i][j] != float('inf'):
            # 큰 돌이고 n범위를 벗어나지 않는다면, 'i+j-1' 위치를 'j-1' 점프크기로 도달 (i는 현재 돌 위치)
            if j>=2 and i+j-1 not in X_list and i+j-1 <= n:
                dp[i+j-1][j-1]  = min(dp[i+j-1][j-1], dp[i][j]+1)
            # 큰 돌이고 n범위를 벗어나지 않는다면, 'i+j' 위치를 'j' 점프크기로 도달
            if i+j not in X_list and i+j <= n:
                dp[i+j  ][j  ]  = min(dp[i+j][j], dp[i][j]+1)
            # 큰 돌이고 n범위를 벗어나지 않는다면, 'i+j+1' 위츠를 'j+1' 점프크기로 도달
            if i+j+1 not in X_list and i+j+1 <= n:
                dp[i+j+1][j+1]  = min(dp[i+j+1][j+1],dp[i][j]+1)

ans=float('inf')
for i in range(200):
    ans = min(ans, dp[n][i])
if ans == float('inf'):
    print(-1)
else:
    print(ans)



