import sys


dp = [ [ 0 for _ in range(10) ] for _ in range(66) ]

for i in range(10):
    dp[1][i] = 1

for i in range(2, 66):
    for j in range(10):
        # dp[3][0] = dp[2][0] ~ dp[2][9]
        # dp[3][1] = dp[2][1] ~ dp[2][9]
        # dp[3][2] = dp[2][2] ~ dp[2][9]
        # dp[3][3] = dp[2][3] ~ dp[2][9]
        # ...
        # dp[3][9] = dp[2][9] + dp[2][9]
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    for i in range(10):
        sum += dp[n][i]
    print(sum)
