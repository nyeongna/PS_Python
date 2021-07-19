# -*- coding:utf-8 -*-
import sys
import os

n, m = map(int, input().split())
song = list(map(int, input().split()))

left = 0
right = sum(song)+1


def Check(length):
    total = 0
    cnt = 1
    for one in song:
        if total + one <= length:
            total = total + one
        else:
            cnt += 1
            total = one
    if cnt <= m:
        return 1
    else:
        return 0


# while left+1 < right:
#     mid = (left + right) // 2
#     chk = Check(mid)
#     #print(mid, chk)
#     if chk and mid >= max(song):
#         right = mid
#     else:
#         left = mid
# print(right)


while left <= right:
    mid = (left + right) // 2
    chk = Check(mid)
    #print(mid, chk)
    if chk and mid >= max(song):
        right = mid-1
    else:
        left = mid+1
print(left)
