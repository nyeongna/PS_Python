n, m = map(int, input().split())
num_list = [ int(input()) for _ in range(n) ]
num_list.insert(0, 0)

'''
dp[i][j]: 'i'번째 idx까지 숫자가 있을때, 'j'개의 구간을 가질 떄 가질 수 있는 최대값
dp[i][j] 에서 'i'번째 미포함하면 -> dp[i-1][j] 와 동일
             'i'번쨰 포함면 -> dp[k-2][j-1] + sum[i]-sum[k-1] (2<= k <= i)
'''

'''
dp[4][2]
     k i
 1 2 3 4 5  6
-1 3 1 2 4 -1
'''
sum_list = [0]*(n+1)
for i in range(1, n+1):
    sum_list[i] = sum_list[i-1]+num_list[i]
print(num_list)
print(sum_list)

dp = [ [0]*(m+1) for _ in range(n+1) ]
for i in range(m+1):
    dp[0][i] = float('-inf')

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, i+1):
            if k>=2:
                dp[i][j] = max(dp[i][j], dp[k-2][j-1]+sum_list[i]-sum_list[k-1])
            elif k==1 and j==1:
                dp[i][j] = max(dp[i][j], sum_list[i])
                

for i in range(n+1):
    for j in range(m+1):
        print(dp[i][j], end= ' ')
    print()