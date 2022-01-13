n = int(input())
dp=[0]*(101)

for i in range(1,n+1):
    if i<=3:
        dp[i]=i
    else:
        for j in range(3, i):
            dp[i] = max(dp[i-j]*(j-1), dp[i])
        dp[i] = max(dp[i], dp[i-1]+1)

print(dp[n])
