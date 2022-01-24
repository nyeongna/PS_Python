n, m, k = map(int, input().split())

# dp[i][j]: 'j'번쨰 도시에서 'i'번째 횟수로 왔을 때 최고 기내식 점수
dp = [ [-1]*(n+1) for _ in range(m+1) ]
flight_list = list()
for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        flight_list.append((a,b,c))
flight_list.sort()

# 1 부터 N 까지는 무조건 보장이므로 dp[1][1]은 무조건 flight_list에 포함
# 출발점이므로 0 으로 초기화
dp[1][1]=0
for a,b,c in flight_list:
    # m 미만까지만 봐야한다. b 도시로 도착하는 것도 포함시켜야 하므로
    for i in range(1, m):
        # 현재 a번째 도시까지 오는 길이 m 미만으로 있을 때 다음 도시로 넘어갈 수 있음
        if dp[i][a] != -1:
            dp[i+1][b] = max(dp[i+1][b], dp[i][a]+c)
# dp[i][n] (i=1~m) 즉, n번째 도시에 m이하로 올 수 있는 방법중
# 가장 기내식 점수가 높은 것을 도출.
ans=-1
for i in range(1,m+1):
    ans = max(ans, dp[i][n])
print(ans)

'''
시간 복잡도
O(k * m) = 100000 * 300 = 30,000,000 => 통과
'''