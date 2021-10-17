from collections import deque
n, k = map(int, input().split())

'''
BFS 이용.
단, dequeue 된 시점에서 visited[k]를 해준다. 그래야 모든 경우의 수를 체크가능
  - 1 에서 +1 해서 2
  - 1 에서 *2 해서 2     => 2가지 모두 다른 경우의 수
왜? 다른 x점에서 k로 못들어오기 때문..
'''

Q=deque()
Q.append((n,0))
visited=[0]*(200001)
min_dist, cnt = float('inf'), 0

while len(Q) > 0:
    x, dist = Q.popleft()
    visited[x]=1
    # 처음로 min_dist 발견하면 break
    if x==k:
        cnt += 1
        min_dist = dist
        break
    if 0 <= x-1 <= 100000 and visited[ x-1 ]==0:
        Q.append((x-1, dist+1))

    if 0 <= x+1 <= 100000 and visited[ x+1 ]==0:
        Q.append((x+1, dist+1))

    if 0 <= x*2 <= 100000 and visited[ x*2 ]==0:
        Q.append((x*2, dist+1))

# 현재 deque에 있는 요소 중 min_dist와 동일한 dist를 가진 갯수만 더해준다.
while len(Q) > 0:
    x, dist = Q.popleft()
    if x==k and dist == min_dist:
        cnt += 1
print(min_dist)
print(cnt)