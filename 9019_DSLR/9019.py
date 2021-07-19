import sys
from collections import deque

t = int(input())


def D(num):
    return num * 2 % 10000


def S(num):
    return 9999 if num == 0 else num-1


def L(num):
    # a = num // 1000
    # b = num % 1000
    # L = b * 10 + a
    # return L
    num = str(num).zfill(4)
    first = num[0]
    return int(num[1:] + first)


def R(num):
    # a = num % 10
    # b = num // 10
    # R = a * 1000 + b
    # return R
    num = str(num).zfill(4)
    last = num[-1]
    return int(last+num[:-1])


for _ in range(t):
    A, B = map(int, input().split())

    visited = [0] * 10001
    visited[A] = 1
    Q = deque()
    Q.append([A, ""])

    while len(Q) > 0:
        x, rec = Q.popleft()
        if x == B:
            print(rec)
            break
        if visited[D(x)] == 0:
            visited[D(x)] = 1
            Q.append([D(x), rec+"D"])

        if visited[S(x)] == 0:
            visited[S(x)] = 1
            Q.append([S(x), rec+"S"])

        if visited[L(x)] == 0:
            visited[L(x)] = 1
            Q.append([L(x), rec+"L"])

        if visited[R(x)] == 0:
            visited[R(x)] = 1
            Q.append([R(x), rec+"R"])
