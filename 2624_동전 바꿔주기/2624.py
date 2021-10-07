target = int(input())
k = int(input())
coin_list = list()
for _ in range(k):
    coin, num = map(int, input().split())
    coin_list.append((coin, num))

