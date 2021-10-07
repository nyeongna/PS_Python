t = int(input())
for _ in range(t):
    n = int(input())
    coin_list = list(map(int, input().split()))
    target = int(input())
    coin_list.insert(0,0)
    dp = [ [0]*(target+1) for _ in range(len(coin_list)) ]
    for i in range(len(coin_list)):
        dp[i][0] = 1
    dp[0][0]=1
    for i in range(1, n+1):
        coin = coin_list[i]
        for j in range(1, target+1):
            # i-1 행을 i행에 미리 복사를 하거나
            # j-coin < 0 인 부분만 복사를 한다.
            if j-coin >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin]
            else:
                dp[i][j] = dp[i-1][j]
    # for i in range(n+1):
    #     for j in range(target+1):
    #         print(dp[i][j], end= ' ')
    #     print()
    print(dp[n][target])