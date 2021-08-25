from itertools import combinations
from typing import AnyStr

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0

for cnt in range(1,n+1):
    for comb in combinations(num_list, cnt):
        if sum(list(comb)) == s:
            #print(comb, type(comb))
            ans = ans + 1
print(ans)

''' 시간복잡도
경우의수 O(2^(n+1)*n) 약 4천만 통과
'''