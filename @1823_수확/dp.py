import sys
sys.setrecursionlimit(90000)

n = int(input())
rice = list()
for _ in range(n):
    rice.append(int(input()))

'''
첫 벼의 범위가 (0 ~ n-1) 일때
dp[i][j]: 벼의 시작 지점이 i, 끝 지점이 j 일때, 가질 수 있는 최고의 이익 (시간을 고려한 최대이익임)

- dp[3][3] 이라면, 3번째 위치의 벼를 수확할때 시간이 n임을 가정해야함.
- 아래식을 이용하면 자동으로 위를 가정하고의 풀이임. 
'''
dp = [ [0]*n for _ in range(n) ]

def F(first, last, level):
    # base case
    if first > last:
        return 0
    if dp[first][last] != 0:
        return dp[first][last]
    
    dp[first][last] = max( F(first+1, last, level+1) + rice[first]*level, F(first, last-1, level+1) + rice[last]*level )
    return dp[first][last]
F(0, n-1, 1)

print(dp[0][n-1])
for i in range(n):
    for j in range(n):
        print(f'{i},{j} : {dp[i][j]}')