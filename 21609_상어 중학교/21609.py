from collections import deque
import heapq
n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
def BFS(x,y, color,visited):
    tmp_group = list([(x,y)])
    rb_visited = [ [0]*(n+1) for _ in range(n+1) ]
    Q = deque()
    Q.append((x,y))
    rb_cnt, mb_x, mb_y = 0, x, y

    while len(Q) > 0:
        x, y = Q.popleft()
        for i in range(4):
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            # 일반 블록이고 색깔 같을때
            if 0<=dx<n and 0<=dy<n and visited[dx][dy]==0 and graph[dx][dy]==color:
                visited[dx][dy]=1
                Q.append((dx,dy))
                tmp_group.append((dx, dy))
                mb_x, mb_y = min(mb_x, dx), min(mb_y, dy)
            # 무지개 블록일때
            elif 0<=dx<n and 0<=dy<n and rb_visited[dx][dy]==0 and graph[dx][dy]==0:
                rb_visited[dx][dy]=1
                Q.append((dx,dy))
                tmp_group.append((dx,dy))
                rb_cnt += 1
    # 그룹 size, 무지개블록 size, 기준블록 행, 기준블록 열
    if len(tmp_group) >= 2:
        return (-len(tmp_group), -rb_cnt, -mb_x, -mb_y, tmp_group)
    else:
        return [float('-inf')]
    
ans = 0
cnt=0

while True:
    visited = [ [0]*(n+1) for _ in range(n+1)]
    group_list = list()
    #print(f'현재 단계: {cnt}')
    for i in range(n):
        for j in range(n):
            # 한번도 방문하지 않았고, 일반블록일 경우(그룹에는 적어도 1개 이상의 일반 블록이 있어야함)
            if visited[i][j]==0 and 1<=graph[i][j]<=m:
                visited[i][j]=1
                group = BFS(i,j, graph[i][j],visited)
                if group[0] != float('-inf'):
                    group_list.append(group)
    # 블록그룹이 생성 안됐다면 게임 끝
    if len(group_list) == 0:
        print(ans)
        exit()

    # 지울 블록을 찾는다
    heapq.heapify(group_list)
    target_group = heapq.heappop(group_list)[4]

##################################
    # # 가장 큰 블록 그룹
    # print(f'가장 큰 블록그룹')
    # for kk in target_group:
    #     print(kk)
    # print()
#################################

    # 정해진 블록그룹 없애기 (-10은 빈공간)
    for x, y in target_group:
        graph[x][y] = -10

    # 점수 획득
    ans = ans + len(target_group)*len(target_group)
    
    # 중력 작용
    for j in range(n):
        floor = n
        for i in range(n-1,-1,-1):
            if 0<=graph[i][j]<=m:
                block = graph[i][j]
                graph[i][j] = -10
                graph[floor-1][j] = block
                floor=floor-1
            elif graph[i][j]==-1:
                floor = i

##################################
    # # 중력 작용 1번째 후
    # print(f'중력 작용 1번째 후')
    # for i in graph:
    #     print(i)
    # print()
#################################
    

    # 90도 반시계 회전
    graph = list(map(list, zip(*graph)))[::-1]

##################################
    # # 중력 작용 1번째 후
    # print(f'반시계 회전후')
    # for i in graph:
    #     print(i)
    # print()
#################################

    # 중력 작용
    for j in range(n):
        floor = n
        for i in range(n-1,-1,-1):
            if 0<=graph[i][j]<=m:
                block = graph[i][j]
                graph[i][j] = -10
                graph[floor-1][j] = block
                floor=floor-1
            elif graph[i][j]==-1:
                floor = i

##################################
    # 중력 작용 2번째 후
    # print(f'중력 작용 2번째 후')
    # for i in graph:
    #     print(i)
    # print()
#################################

    cnt=cnt+1
    