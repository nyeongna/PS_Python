import sys
import os

t = int(input())

while t > 0:
    t = t-1
    n = int(input())
    num = list(map(int, input().split()))
    psum = 0
    ans = float('-inf')
    for n in num:
        psum = max(psum, 0) + n
        ans = max(ans, psum)
    print(ans)
