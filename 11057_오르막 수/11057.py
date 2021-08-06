'''
dp 문제.
dp[i][j] = i 길이에서 첫번째 숫자가 j 일때의 오르막 개수
dp[i][j] = dp[i][j-1] - dp[i-1][j-1] 이라는 패턴을 발견할 수 있다 (그려보면...발견하기쉽다)
'''
n = int(input())
dp = [ [0]*10 for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        sum = 0
        if j==0:
            for k in range(10):
                sum = sum + dp[i-1][k]
            dp[i][j] = sum%10007
        else:
            dp[i][j] = (dp[i][j-1] - dp[i-1][j-1])%10007

ans = 0
for i in range(10):
    ans = ans + dp[n][i]
print(ans%10007)