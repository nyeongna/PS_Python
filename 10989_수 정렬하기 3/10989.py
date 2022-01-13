n= int(input())
num_cnt = [0]*10001
for _ in range(n):
    n = int(input())
    num_cnt[n] += 1
for i in range(1, 10001):
    for j in range(num_cnt[i]):
        print(i)
