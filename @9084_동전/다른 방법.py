
import sys
sys.setrecursionlimit(30000)
t = int(input())
    
for _ in range(t):
    n = int(input())
    coin_list = list(map(int, input().split()))
    target = int(input())


    # dp[i] 를 'i원'을 만들수있는 동전 경우의 수
    dp = [0]*(target+1)
    # dp[0] 은 1로 초기화한다. (3원으로 3원을 만드는 경우의 수, 6원으로 6원을 만드는 경우의 수 등등... 1개로 만들때를 대비해서)
    dp[0]=1
    for coin in coin_list:
        for idx in range(coin, target+1, 1):
            dp[idx] = dp[idx] + dp[idx-coin]
    print(dp[target])

    
