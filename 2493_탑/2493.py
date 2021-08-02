from collections import deque

n = int(input())
towers = list(map(int, input().split()))
Q = deque()


for idx, h in enumerate(towers):
    if len(Q) == 0:
        print(0, end=' ')
        Q.append((h,idx))
    else:
        while len(Q) > 0:
            if Q[-1][0] < h:
                Q.pop()
            else: break
        if len(Q) == 0:
            print(0, end=' ')
        else:
            print(Q[-1][1]+1, end=' ')
        Q.append((h, idx))

'''
시간복잡도 O(n)
'''