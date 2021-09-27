n = int(input())
num_list = list()
for _ in range(n):
    num_list.extend( [int(input())] )

dp = [0 for _ in range(n) ]
dp[0] = 1

# dp[i] 는 'i'번째 요소를 끝으로 갖는 배열이 갖는 LIS(최대증가부분수열)
'''
3 7 5 2 6 1 4
'''
for i in range(1,n):
    max_num = 1
    for j in range(i-1, -1, -1):
        if num_list[j] < num_list[i]:
            max_num = max(max_num, dp[j]+1)
    dp[i] = max_num

max_LIS = max(dp)
ans = n - max_LIS
print(ans)
'''
3 7 5 2 6 1 4
'''