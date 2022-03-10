from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().strip().split())

visited = [0] * 100002
cnt = [0] * 100002

Q = deque()
Q.append((n, 0))
visited[n] = 1
found = 0
cnt = 0
while len(Q) > 0:
    n, dist = Q.popleft()

    # 핵심.
    # pop 되고 visited[n]=1을 체크해준다.
    visited[n] = 1
    if found and dist>found:
        continue
    # 처음에 딱 발견했으면, 현재 Q에 들어있는 값들에 대해서만 비교를 해주고
    # bfs 확장은 멈춰도된다
    if n==m:
        found=dist
        cnt += 1
        continue

    if n-1 >=0 and n-1 <=100000 and visited[n-1] == 0:
        # 여기서 visitedpn[n]=1을 체크하면 n-1 말고, n+1, n*2 로 가는 방법이 막히게 된다.
        # 예를들어, 1에서 2를 갈때 +1로 가는 방법 1개, *2로 가는 방법 1개 해서 총 2가지 방법이 있다(가는 시간은 같다 = 1초)
        # 하지만 여기서 visited[n]=1을 걸어버리면, *2로 1에서 2로 가는 방법이 시도하지 않게된다!!!!!!!!
        Q.append((n-1,dist+1))

    if n+1 >=0 and n+1 <=100000 and visited[n+1] == 0:
        Q.append((n+1, dist+1))

    if n*2 >= 0 and n*2 <= 100000 and visited[n*2] == 0:
        Q.append((n*2, dist+1))
    
print(found)
print(cnt)