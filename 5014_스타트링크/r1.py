import sys
from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * 1000001
Q = deque()

Q.append([S, 0])
while len(Q) > 0:
    cur, dist = Q.popleft()
    if cur == G:
        print(dist)
        exit()
    up = cur + U if cur + U <= F else cur
    if visited[up] == 0:
        visited[up] = 1
        Q.append([up, dist+1])
    down = cur - D if cur - D >= 1 else cur
    if visited[down] == 0:
        visited[down] = 1
        Q.append([down, dist+1])
print('use the stairs')
