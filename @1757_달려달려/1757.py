n, m = map(int, input().split())
dist=[int(input()) for _ in range(n) ]
dist.insert(0,None)

dp = [ [ [0]*(502) for _ in range(10002) ] for _ in range(2) ]

'''
dp[k][i][j]: k가 0이면 쉬는중, 1이면 달리는 상태
             i는 분을 뜻함
             j는 지침지수를 뜻함
'''
for i in range(1, n+1):
    for j in range(m+1):
        # 지침이 0일때 (i에서 달리는 상태일수없다)
        if j==0:
            # i-1에서 쉬고, j+1 지침 가지고 있을때
            # i-1에서 달리고 j+1 지침 가지고 있을때
            # i-1에서 쉬고, 0 지침 가지고 있을때
            dp[0][i][0] = max(dp[0][i-1][1], dp[1][i-1][1], dp[0][i-1][0])
        # 지침이 1일때
        elif j==1:
            # i에서 쉴때는 i-1에서 쉬고 2지침 vs i-1에서 뛰었고 2지침
            dp[0][i][1] = max(dp[0][i-1][j+1], dp[1][i-1][j+1])
            # i에서 뛸때는 i-1에서 쉬고 0지침 vs i-1에서 뛰었고 0지침. i-1에서 쉬었어도, 0지침이므로 i에서는 뛰어도됨.
            dp[1][i][1] = max(dp[0][i-1][j-1], dp[1][i-1][j-1])+dist[i]
        # 지침이 2이상일때
        elif j>=2:
            # i에서 쉬려면, i-1에서 뛰거나 쉰 상태 상관없음
            dp[0][i][j] = max(dp[0][i-1][j+1], dp[1][i-1][j+1])
            # i에서 뛰려면 i-1에서 뛴 상태여야함. 고로 i-1에서 쉰 상태는 고려안함
            dp[1][i][j] = dp[1][i-1][j-1]+dist[i]

# n번째에서 쉰 상태를 출력
print(dp[0][n][0])