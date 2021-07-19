from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().strip().split())

visited = [0] * 100001
cnt = [0] * 100001

Q = deque()
Q.append((n, 0))
visited[n] = 1
found = 0
cnt = 0
while len(Q) > 0:
    n, dist = Q.popleft()
    
    if found and dist > found:
        continue
    if n==m:
        found = dist
        cnt += 1
        continue

    if n-1>=0 and n-1<=100000 and visited[n-1] == 0:
        # 이렇게 visited[n]=1 을 먼저 해버리면 +1, *2 등 다른방법으로는 시도를 하지 않아서 정답에 갈수없다.
        if n-1 != m:
            visited[n-1] = 1
        Q.append((n-1,dist+1))
    if n+1>=0 and n+1<=100000 and visited[n+1] == 0:
        if n+1 != m:
            visited[n+1] = 1
        Q.append((n+1, dist+1))
    if n*2 >= 0 and n*2 <= 100000 and visited[n*2] == 0:
        if n*2 != m:
            visited[n*2] = 1
        Q.append((n*2, dist+1))
    
print(found)
print(cnt)