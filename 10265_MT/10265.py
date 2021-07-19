import sys
from collections import deque

t = int(input())

while t>0:
    t=t-1
    start, target = map(int, input().split())
    visited = [0] * 10000
    visited[start]=1
    Q = deque()
    Q.append([start, ""])
    
    while len(Q) > 0:
        cur, d = Q.popleft()

        if cur == target:
            print(d)
            break
        D = cur*2 % 10000
        if visited[D] == 0:
            visited[D] = 1
            Q.append([D, d+"D"])
        S = 9999 if cur==0 else cur-1
        if visited[S] == 0:
            visited[S] = 1
            Q.append([S, d+"S"])
        
        a = cur // 1000
        b = cur % 1000
        L = b * 10 + a
        if visited[L] == 0:
            visited[L]=1
            Q.append([L, d+"L"])
        
        a = cur % 10
        b = cur // 10
        R = a * 1000 + b
        if visited[R] == 0:
            visited[R] =1
            Q.append([R, d+"R"])
        
        