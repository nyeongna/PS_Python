from sys import stdin
from collections import deque
t = int(input())
for _ in range(t):
    p = stdin.readline().strip()
    n = int(stdin.readline().strip())
    ary = deque(stdin.readline().strip()[1:-1].split(','))
    flag=1
    for order in p:
        if order=='D':
            if len(ary) <= 0 or ary[0]=='':
                print('error')
                flag=0
                break
            if flag==1:
                ary.popleft()
            elif flag==-1:
                ary.pop()
        elif order=='R':
            flag = flag * -1
    if flag == -1:
        ary = '[' + ','.join(list(ary)[::-1]) + ']'
        print(ary)
    elif flag == 1:
        ary = '[' + ','.join(list(ary)) + ']'
        print(ary)

