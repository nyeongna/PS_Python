target = int(input())
k = int(input())
coin_list = list()
for _ in range(k):
    coin, num = map(int, input().split())
    coin_list.append((coin, num))


# dp[i] = i원을 만들 수 있는 경우의 수
dp = [0]*(target+1)

# "0원을 만드는 것도 1가지 경우의 수로 친다면" --> dp[0]=1
dp[0]=1
for i in range(k):
    coin = coin_list[i][0]
    coin_num = coin_list[i][1]
    # target 부터 거꾸로 채워넣어서 현재 coin을 중복으로 세지 않게 함.
    # 거꾸로 채워넣으면서 현재 coin이 k개 만큼 안들어갔을때 coin*k원을 뺸 상태에서를 더해준다.
        # j-coin*k 원을 만들 수 있는 경우의 수만큼 j원을 만들 수 있기 때문

# 먄악 target j=12원,
#     j=8원 일때 2가지,
#     j=4원 일때 2가지,
#     j=0원 일때 1가지, 경우의 수를 구해놨다고 치고 현재 4원 2개를 가지고 있고 추가하고 싶다면
#         j=8원 일때 경우의 수 2가지에 4원을 각각 더하면 12원이 되므로 2가지 경우의수
#         j=4원 일때 경우의 수 2가지에 4*2원을 각각 더하면 12원이 되므로 2가지 경우의수
#         j=0원 일때 경우의 수 1가지는 4원이 2개밖에 없으므로 만족하지 못하므로 pass
#         따라서 dp[12] = dp[12] + dp[12 - 4*1] + dp[12 - 4*2] = 4가지가 됨

    for j in range(target, -1, -1):
        # 현재 coin을 1~k번까지 빼가면서 경우의 수를 채워넣는다
        for k in range(1, coin_num+1):
            if j-coin*k >= 0:
                dp[j] = dp[j] + dp[j-coin*k]
print(dp[target])
# print(dp)
    