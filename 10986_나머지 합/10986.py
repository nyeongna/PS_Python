import sys

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

psum = [0] * (n+1)
remain = [0] * (m+1)

for idx, n in enumerate(num_list):
    psum[idx+1] = psum[idx] + n
    remain[psum[idx+1] % m] += 1
ans = 0
ans = ans + remain[0]
for i in remain:
    if i != 0:
        ans = ans + (i * (i-1)) / 2
print(int(ans))
