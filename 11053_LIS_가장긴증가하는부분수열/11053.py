n = int(input())
num_list = list(map(int, input().split()))

dp = [0]*(n+1)
for i in range(n):
    max_num = 0
    for j in range(i):
        if num_list[i] > num_list[j]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num + 1

print(max(dp))
        