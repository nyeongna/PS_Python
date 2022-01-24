from itertools import combinations

n, m = map(int, input().split())
# wok_list에 한번 요리 당 <1개, 2개 wok 조합>으로 만들 수 있는 모든 경우의 수 추가
wok_list = list(map(int, input().split()))
for comb in combinations(wok_list, 2):
    if comb[0] + comb[1] <= n:
        wok_list.append(comb[0]+comb[1])

# list(set())를 통해 중복제거 --> 시간복잡도 최소화
wok_list=list(set(wok_list))

# dp[i]: 'i'개의 짜장면을 만들때 필요한 최소 요리 횟수
dp = [0]*(n+1)
for i in range(1, n+1, 1):
    min_num = float('inf')
    for wok in wok_list:
        if (i - wok) >= 0:
            min_num = min(min_num, dp[i-wok])
    dp[i] = min_num + 1

if dp[n]>=float('inf'):
    print(-1)
else:
    print(dp[n])
