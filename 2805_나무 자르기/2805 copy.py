# -*- coding:utf-8 -*-
import sys
import os

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_h = max(tree)

left = 0
right = max_h

#      ������ �̷��� �س�����
# right�� ������ ���� ū ���� �ǰ�
# left��  ������ �ƴ� ���� ���� �������� ��.
while (left <= right):
    mid = (left+right) // 2
    total = 0
    for i in tree:
        if mid <= i:
            total += i-mid
    if total >= m:
        left = mid+1
    else:
        right = mid-1
print(right)
