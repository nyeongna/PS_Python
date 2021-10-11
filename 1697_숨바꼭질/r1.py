from collections import deque

n, k = map(int, input().split())
Q = deque([ (n,0) ])
visited = [0] * (100001)
visited[n] = 1

while len(Q) > 0:
    idx, dist = Q.popleft()
    if idx==k:
        print(dist)
        exit()
    if 0 <= idx*2 <=100000 and visited[idx*2]==0:
        visited[idx*2]=1
        Q.append((idx*2, dist+1))
    if 0 <= idx+1 <=100000 and visited[idx+1]==0:
        visited[idx+1]=1
        Q.append((idx+1, dist+1))
    if 0<=idx-1 <=100000 and visited[idx-1]==0:
        visited[idx-1]=1
        Q.append((idx-1, dist+1))

