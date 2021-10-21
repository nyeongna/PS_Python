

# dp[i][j] 는 큰거 i개, 작은거 j개 일때 먹을 수 있는 경우의 수
dp = [ [0]*(30+1) for _ in range(30+1) ]



def f(big, small):
    # big이 0개면 small만 먹는 수밖에 없으므로 경우의 수 1
    if big==0:
        return 1
    # small 갯수가 마이너스면 말이 안되므로 return 0
    if small < 0:
        return 0
    # 가지치기
    if dp[big][small] != 0:
        return dp[big][small]
    # big이 i개 small이 j개 일때 경우의 수는 big을 먹어서 i-1개 small이 j+1개 되는 수 (i-1, j+1) +
    #                                    small 먹어서 (i, j-1)
    dp[big][small] = f(big-1, small+1) + f(big, small-1)

    return dp[big][small]

while True:
    n = int(input())
    if n==0:
        exit()
    print(f(n,0))
    