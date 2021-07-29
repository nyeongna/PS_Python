
n, l = map(int, input().split())

for num in range(l, 101):
    pivot = n // num - 1
    total = 0
    for i in range(pivot, pivot+num):
        total += i
    if total == n:
        for i in range(pivot, pivot+num):
            print(i, end=' ')
        exit()
print(-1)