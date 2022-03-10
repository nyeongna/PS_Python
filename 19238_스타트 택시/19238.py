'''
-현재 택시 위치에서 최단거리 손님의 위치를 찾을때
 모든 손님의 위치를 먼저 다 bfs로 훑고, <거리, 행, 열> 순으로 우선순위 큐에서 꺼냄
-출발지에서 목적지까지의 거리 x2가 충전됨
 현재 택시에서 출발지까지 가는 거리는 충전거리에 포함 안됨
-손님의 출발지와 목적지가 같을 수 없음
-각 손님의 출발지는 모두 다르다
'''
from collections import deque
import heapq
from re import X
n, m, fuel = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
tx, ty = map(int, input().split())
tx, ty = tx-1, ty-1
customer_dict = dict()
round=0
for _ in range(m):
    sx, sy, gx, gy = map(int, input().split())
    sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1
    graph[sx][sy] = 2
    customer_dict[(sx,sy)] = (gx,gy)

class customer:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        
    def __lt__(self, other):
        if self.d == other.d:
            if self.x == other.x:
                return self.y < other.y
            else:
                return self.x < other.x
        else:
            return self.d < other.d
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
while True:
    Q = deque()
    Q.append((tx,ty,0))
    visited=[ [0]*(n+1) for _ in range(n+1) ]
    visited[tx][ty]=1
    customer_hq = list()
    # 최단거리 손님 찾기
    while len(Q) > 0:
        x, y, dist = Q.popleft()
        if graph[x][y]==2:
            heapq.heappush(customer_hq, customer(x,y,dist) )
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if 0<=dx<n and 0<=dy<n and graph[dx][dy]!=1 and visited[dx][dy]==0:
                visited[dx][dy]=1
                Q.append((dx,dy,dist+1))

    # 현재 택시 위치에서 더이상 태울 손님을 못찾음
    if len(customer_hq)==0:
        # 아직 태워야할 손님이 있을경우: -1
        if round < m:
            print(-1)
        # 태워야할 손님 다 태웠을 경우: fuel
        elif round >= m:
            print(fuel)
        exit()

    # 최단거리 손님
    c = heapq.heappop(customer_hq)
    # 손님을 태우러갈 연료가 모자르면 끗
    if c.d > fuel:
        print(-1)
        exit()
    # 안모자르면 태우러 간다
    fuel = fuel - c.d

    # 출발지에서 목적지까지 연료가 남아있으면 간다
    Q = deque()
    Q.append((c.x, c.y, 0))
    visited[c.x][c.y]=1
    visited=[ [0]*(n+1) for _ in range(n+1)]
    gx, gy = customer_dict[(c.x, c.y)]
    can_reach=0
    while len(Q) > 0:
        x, y, dist = Q.popleft()
        if x==gx and y==gy:
            # 출발지에서 목적지까지 갈 연료 남아있음
            if dist <= fuel:
                fuel += dist
                can_reach=1
                break
            # 출발지에서 목적지까지 갈 연료가 남아있지않으면 끗
            else:
                print(-1)
                exit()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if 0<=dx<n and 0<=dy<n and graph[dx][dy]!=1 and visited[dx][dy]==0:
                visited[dx][dy]=1
                Q.append((dx,dy,dist+1))
    # 출발지에서 도착지로 갈 수 없는 경우 겜끝
    if can_reach==0:
        print(-1)
        exit()
    # 여기까지 도달했으면 손님을 목적지까지 데려다 줬다는 뜻
    # 1. 태워줬던 손님을 지도상에서 지우고
    # 2. 택시는 목적지 위치로 옮긴다
    # 3. 태워준 손님 수 +1
    graph[c.x][c.y] = 0
    tx, ty = gx, gy
    round += 1

        

    

            

