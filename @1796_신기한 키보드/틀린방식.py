'''
잘못된 접근..
그리디로 접근하면 안된다 caabcd 같은경우 17이 나와야하는데 그리디로 하면 19로 나온다 오답
'''
from collections import deque
import heapq
import copy

s = list(map(str, input()))
target_list = copy.deepcopy(s)
heapq.heapify(target_list)
length = len(s)

ans = 0
Q = deque()
Q.append((0,0))
visited=[0]*(length+1)
visited[0]=1

timed=0
while len(Q) > 0 and len(target_list) > 0:
    pos, dist = Q.popleft()
    if s[pos] == target_list[0]:
        ans = ans + dist + 1 # enter
        s[pos] = '' # 빈칸으로 만들기
        heapq.heappop(target_list)
        Q.clear()
        Q.append((pos, 0))
        visited=[0]*(length+1)
        continue
    for x in (-1, 1):
        dx = pos + x
        if 0<=dx<length and visited[dx]==0:
            visited[dx]=1
            Q.append((dx, dist+1))
print(ans)



