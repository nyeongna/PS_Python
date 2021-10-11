from sys import stdin

n = int(input())
work_list = list()
for _ in range(n):
    day, pay = map(int, stdin.readline().rstrip().split())
    work_list.append((day,pay))

dp = [0]*(n+2)

# dp[i]: 'i'번째 날에 얻을 수 있는 최대이익
for i, (day, profit) in enumerate(work_list):
    # 현재날짜(i) + 일처리필요일수(day)에 최댓값을 누적
    if i+day<=n:
        dp[i+day] = max(dp[i+day], dp[i]+profit)
    # 현재 일(i)을 처리 안하고 다음날로 넘어감
    if i+1 <=n:
        dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])
