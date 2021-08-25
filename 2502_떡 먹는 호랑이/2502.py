'''
D = 1 --> a
D = 2 --> b
D = 3 --> a + b
D = 4 --> a + 2b
D = 5 --> 2a + 3b
D = 6 --> 3a + 5b
...
'''

d, k = map(int, input().split())

# dp[i][0]: i번째날 줘야하는 떡 갯수의 a의 계수 (a는 1일에 줘야하는 떡의 갯수)
# dp[i][1]: i번째날 줘야하는 떡 갯수의 b의 계수 (b는 2일에 줘야하는 떡의 갯수)
dp = [ [0,0] for _ in range(50) ] 
dp[1][0], dp[1][1] = 1, 0
dp[2][0], dp[2][1] = 0, 1

for i in range(3, d+1, 1):
    dp[i][0] = dp[i-2][0] + dp[i-1][0]
    dp[i][1] = dp[i-2][1] + dp[i-1][1]

# dp[d][0] 에는 a의 계수,
# dp[d][1] 에는 b의 계수가 저장되어있음.
# 즉 3a + 5b = 41 같은 미지수가 2개인 일차방정식을 풀면됨.
# 이중 for문으로 완전탐색으로 구한다.
for i in range(1, k//dp[d][0]):
    for j in range(1, k//dp[d][1]):
        if i*dp[d][0] + j*dp[d][1] == k:
            print(i)
            print(j)
            exit()