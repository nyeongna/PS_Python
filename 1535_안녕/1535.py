n = int(input())
neg_list = list(map(int, input().split()))
pos_list = list(map(int, input().split()))
neg_list.insert(0,0)
pos_list.insert(0,0)

# dp[i][j]: 'i'번째 사람을 만났을 때 'j'의 체력으로 만들 수 있는 최대 행복
## dp[i] 처럼 1차원 dp배열로는 만들 수 없다. 사람을 1명씩만 만날 수 있기 때문.
## 1차원 dp배열로 만들면 각 사람을 '무한히' 만날 수 있음을 가정하는 것이다.
dp = [ [ 0 for _ in range(101) ] for _ in range(n+1) ]

for i in range(1, n+1):
    for j in range(101):
        dp[i][j] = dp[i-1][j]
        if j-neg_list[i] > 0:
            dp[i][j] = max( dp[i-1][j], dp[i-1][j-neg_list[i]] + pos_list[i])

print(dp[n][100])
