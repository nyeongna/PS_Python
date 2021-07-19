from sys import stdin
import sys
from typing import AnyStr
sys.setrecursionlimit(30000)

n = int(input())
ans = 0
ans_list = []

def H(num, fromm, to, via):
    if num==1:
        ans_list.append((fromm,to))
        return
    H(num-1, fromm, via, to)
    ans_list.append((fromm, to))
    H(num-1, via, to, fromm)

H(3, 1, 3, 2)
print(len(ans_list))
for i in ans_list:
    print(i[0], i[1])