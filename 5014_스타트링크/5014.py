import sys
from collections import deque

f, s, g, u, d = map(int, input().split())

graph = [ 0 for _ in range(f+3) ]

Q = deque()
Q.append([s, 0])
graph[s]=1

while len(Q)>0:
    cur = Q[0][0]
    dist = Q[0][1]
    Q.popleft()

    if cur == g:
        print(dist)
        exit()

    if cur+u >= 1 and cur+u <= f and graph[cur+u]==0:
        graph[cur+u]=1
        Q.append([cur+u, dist+1])
    if cur-d >= 1 and cur-d <= f and graph[cur-d]==0:
        graph[cur-d]=1
        Q.append([cur-d, dist+1])
    
print("use the stairs")
