# -*- coding:utf-8 -*-
import sys
import os


n = int(input())
budget = list(map(int, input().split()))
target = int(input())


# ������ ��������
# right�� +1�� ���ϸ� left+1 < right������ �ٷ� ����Ǽ� ������ ���ü��ִ�.
#
# 3
# 1 1 1
# 3
# �� ��� left = 0, right = 1�̱�Ѹǿ� while���� ������ ���ϰ� print(0)�� ������ ������ ����
# max(budget)+1�� ���ָ�, left =0, right = 2�̱� ������ while���� ���԰����ϰ� ���䵵�Ⱑ��
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
