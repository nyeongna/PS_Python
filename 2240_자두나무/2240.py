t, w = map(int, input().split())

dp = [ [ [0]*(w+1) for _ in range(t+1) ] for _ in range(3) ]
dp[1][0][0]=0
b4tree = [0, 2, 1]
# k자리 i초 j번움직임
for time in range(1, t+1):
    tree = int(input())
    for m in range(w+1):
        if tree==1:
            if m == 0:
                dp[1][time][0] = dp[1][time-1][0]+1
            else:
                dp[1][time][m] = max(dp[1][time-1][m]+1, dp[2][time-1][m-1]+1)
                dp[2][time][m] = max(dp[1][time-1][m-1], dp[2][time-1][m])
        else:
            if m == 0:
                dp[1][time][0] = dp[1][time-1][0]
            else:
                dp[1][time][m] = max(dp[1][time-1][m], dp[2][time-1][m-1])
                dp[2][time][m] = max(dp[1][time-1][m-1]+1, dp[2][time-1][m]+1)

# for i in range(1, t+1):
#     for j in range(w+1):
#         print('time:'+str(i)+' move:'+str(j) +' '+ str(dp[1][i][j]), str(dp[2][i][j]))
# print()
ans=float('-inf')
for i in range(w+1):
    ans=max(ans,dp[1][t][i],dp[2][t][i])
print(ans)