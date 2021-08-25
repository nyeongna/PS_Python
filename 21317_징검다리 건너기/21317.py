n = int(input())

# energy[i][0]: i번째에서 i+1번째 돌로 짧은 점프 에너지
# energy[i][1]: i번째에서 i+2번째 돌로   긴 점프 에너지
energy = [ [0,0] for _ in range(100)]
for idx in range(n-1):
    s, l = map(int, input().split())
    energy[idx] = (s,l)
k = int(input())

# dp[i][0] i번째 돌까지 매우 큰 점프 안하고 최소로 필요한 에너지
# dp[i][1] i번째 돌까지 매우 큰 점프   하고 최소로 필요한 에너지
dp = [ [0,0] for _ in range(51) ]
dp[0][0], dp[0][1] = 0, 0
dp[1][0], dp[1][1] = energy[0][0], energy[0][0]

for pos in range(2, n, 1):
    # 매우 큰 점프 안하고 도착
    dp[pos][0] = min(dp[pos-1][0]+energy[pos-1][0], dp[pos-2][0]+energy[pos-2][1])

    # 매우 큰 점프 하고 도착
    dp[pos][1] = min(dp[pos-1][1]+energy[pos-1][0], dp[pos-2][1]+energy[pos-2][1])
    if pos >= 3:
        dp[pos][1] = min(dp[pos][1], dp[pos-3][0]+k)
        
# for i in range(1, n):
#     print(dp[i][0], dp[i][1])
print(min(dp[n-1][0], dp[n-1][1]))
    


