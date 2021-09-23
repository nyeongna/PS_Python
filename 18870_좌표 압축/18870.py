import sys
from sys import stdin

n = int(input())
s_list = list(map(int, stdin.readline().strip().split()))

ans_dict = dict()

# 정렬한다
sorted_list = sorted(s_list)

for i in range(len(sorted_list)):
    # 현재까지 dict의 len가 현재 num보다 작은 숫자들의 갯수
    num = sorted_list[i]
    if num not in ans_dict:
        ans_dict[num] = len(ans_dict)

for num in s_list:
    print(ans_dict[num], end=' ')



