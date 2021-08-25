from sys import stdin

n, m = map(int, stdin.readline().strip().split())
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range(n) ]

ans_list = []
for _ in range(m):
    ans_list.append(list(map(int, stdin.readline().strip().split())))

# dp[i][j] = (1,1) - (i,j) 까지의 합
dp = [ [0]*(n+1) for _ in range(n+1) ]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

# (x1, y1) - (x2, y2) 까지의 거리는
# dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] 로 구할 수 있음.
for x1, y1, x2, y2 in ans_list:
    print( dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] )

'''
시간 복잡도
O(n^2 + m) --> dp[i][j] 처음에 계산할 때 필요
'''

