import sys
from collections import deque

n, k = map(int, input().split())
visited = [0]*100001

Q = deque()
Q.append([n, 0])
while len(Q) > 0:
    cur, dist = Q.popleft()
    if cur==k:
        print(dist)
        exit()
    if cur-1 >= 0 and cur-1 <=100000 and visited[cur-1]==0:
        visited[cur-1]=1
        Q.append([cur-1, dist+1])
    if cur+1 >=0 and cur +1 <=100000 and visited[cur+1]==0:
        visited[cur+1]=1
        Q.append([cur+1, dist+1])
    if cur*2 >= 0 and cur*2 <=100000 and visited[cur*2]==0:
        visited[cur*2]=1
        Q.append([cur*2,dist+1])

