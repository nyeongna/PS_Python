a, b = map(int, input().split())
from collections import deque
Q = deque()
Q.append((a,1))

# *2랑 오른쪽에 1 붙히면 어차피 10억까지 금방 도달함
# visited 배열 추가를 해서 최적화 할 필요 X
while len(Q) > 0:
    num,dist = Q.popleft()
    if num==b:
        print(dist)
        exit()
    if 1<=num*2<=10e9:
        Q.append((num*2, dist+1))
    if 1<=num*10+1<=10e9:
        Q.append((num*10+1, dist+1))
print(-1)