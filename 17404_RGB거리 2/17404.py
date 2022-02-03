n = int(input())
# R, G, B
cost_list = list([None])
for _ in range(n):
    cost = list(map(int,input().split()))
    cost_list.append(cost)

# dp[i][j][k]: 'i'색깔로 시작하고, 'j'번째 위치에서, 'k'색깔을 가질때 최솟값
dp = [ [ [float('inf')]*3 for _ in range(n+1) ] for _ in range(3) ]
# 1번째가 r시작
dp[0][1][0] = cost_list[1][0]

# 1번째가 g시작
dp[1][1][1] = cost_list[1][1]

# 1번째가 b시작
dp[2][1][2] = cost_list[1][2]
for i in range(2, n+1):
    r,g,b = cost_list[i][0], cost_list[i][1], cost_list[i][2]
    for start in range(3):
        dp[start][i][0] = min(dp[start][i-1][1]+r, dp[start][i-1][2]+r)
        dp[start][i][1] = min(dp[start][i-1][0]+g, dp[start][i-1][2]+g)
        dp[start][i][2] = min(dp[start][i-1][0]+b, dp[start][i-1][1]+b)

# 1번째와 n번째가 다른 6개 중에서 비교한다
ans = min(dp[0][n][1], dp[0][n][2])
ans = min(ans, dp[1][n][0], dp[1][n][2])
ans = min(ans, dp[2][n][0], dp[2][n][1])
print(ans)