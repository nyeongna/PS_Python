import sys
import os

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_h = max(tree)

left = 0
right = max_h

#      범위를 이렇게 해놓으면 left에는 답이 되는 수 중에서 가장 큰 수
#                           right에는 답이 안되는 수중에서 가장 작은 수가 나온다
#                           [15, 16] 이고 15가 left, 16이 right를 가르키면 범위조건을 벗어나므로 while loop 종료
while (left+1 < right):
    mid = (left+right) // 2
    total = 0
    for i in tree:
        if mid <= i:
            total += i-mid
    if total >= m:
        left = mid
    else:
        right = mid
print(left)
