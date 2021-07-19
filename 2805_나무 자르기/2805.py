import sys
import os

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_h = max(tree)

left = 0
right = max_h

#      ������ �̷��� �س����� left���� ���� �Ǵ� �� �߿��� ���� ū ��
#                           right���� ���� �ȵǴ� ���߿��� ���� ���� ���� ���´�
#                           [15, 16] �̰� 15�� left, 16�� right�� ����Ű�� ���������� ����Ƿ� while loop ����
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
