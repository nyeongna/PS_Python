# -*- coding:utf-8 -*-
import sys
import os

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_h = max(tree)

left = 0
right = max_h

#      범위를 이렇게 해놓으면
# right가 정답중 가장 큰 수가 되고
# left가  정답이 아닌 수중 가장 작은수가 됨.
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
