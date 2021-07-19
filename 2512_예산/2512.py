# -*- coding:utf-8 -*-
import sys
import os


n = int(input())
budget = list(map(int, input().split()))
target = int(input())


# 범위에 주의하자
# right에 +1을 안하면 left+1 < right조건이 바로 실행되서 오답이 나올수있다.
#
# 3
# 1 1 1
# 3
# 인 경우 left = 0, right = 1이기뚜맨에 while문에 진입을 못하고 print(0)이 나오고 오답이 나옴
# max(budget)+1을 해주면, left =0, right = 2이기 때문에 while문에 진입가능하고 정답도출가능
left = 0
right = max(budget)

while (left+1 < right):
    mid = (left+right)//2
    total = 0
    for i in budget:
        if i >= mid:
            total = total + mid
        else:
            total = total + i
    if total <= target:
        left = mid
    else:
        right = mid
print(left)


# while (left <= right):
#     mid = (left+right)//2
#     total = 0
#     for i in budget:
#         if i >= mid:
#             total = total + mid
#         else:
#             total = total + i
#     if total <= target:
#         left = mid+1
#     else:
#         right = mid-1
# print(right)
