import heapq
from collections import deque
tx,ty = 5, 4
n=6
aaa = list()

class customer:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        print(self.x, self.y, self.d)
        
    def __lt__(self, other):
        if self.d == other.d:
            if self.x == other.x:
                return self.y < other.y
            else:
                return self.x < other.x
        else:
            return self.d < other.d

Q = deque()
Q.append((tx,ty,0))
visited=[ [0]*(n+1) for _ in range(n+1) ]
visited[tx][ty]=1
customer_hq = list()
# 최단거리 손님 찾기
while len(Q) > 0:
    x, y, dist = Q.popleft()
    if graph[x][y]==2:
        print(x,y,dist)
        heapq.heappush(customer_hq, customer(x,y,dist))
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if 0<=dx<n and 0<=dy<n and graph[dx][dy]!=1 and visited[dx][dy]==0:
            visited[dx][dy]=1
            Q.append((dx,dy,dist+1))
            if graph[dx][dy]==2:
                customer_hq.append((dx,dy,dist+1))

a = heapq.heappop(aaa)
print(a.x, a.y, a.d)