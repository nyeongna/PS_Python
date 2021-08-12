'''
핵심 알고리즘
1. BFS를 이용해서 4개 이상은 다 터뜨린다.
2. 다 터지고 중간중간 빈칸은 queue를 이용한다. 열 기준으로 빈칸제외 puyo가 있는 칸을 다 queue에 넣고
   새로운 map에다가 각 열마다 queue pop을 해서 차례대로 쌓으면 완성!
'''

'''

.    Y      .     .     .  .
.    .      .     .     .  .
.    .      .     .     .  .
.    Y      .     .     .  .
.    .      .     .     
     Y      .     .     .  .
.    Y      .     .     .  .
.    Y      .     .     .  .
.    Y      .     .     .  .
.    Y      G     .     .  .
.    .      Y     G     .  .
.    .      Y     G     G  .

[] [YYYYYY] [YYG] [GG] [G] []


......
......
.....
......
....
......
.Y....
.Y....
.Y....
.YG...
.YYG..
.YYGG.

'''
from collections import deque
r, c, = 12, 6
graph = [ list(map(str, input())) for _ in range(r)]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

ans = 0
while True:
    # BFS로 다 돌고 터뜨리기
    Q = deque()
    visited=[ [0]*c for _ in range(r)]
    boom = 0

    for i in range(r):
        for j in range(c):
            if graph[i][j] != '.' and visited[i][j]==0:
                puyo_list = [(i,j)]
                visited[i][j]=1
                Q.append((i,j,graph[i][j],0))
                # (i,j) 위치의 puyo가 터질수있는지 확인
                while len(Q) > 0:
                    x, y, color, cnt = Q.popleft()
                    for k in range(4):
                        dx, dy = x + x_dir[k], y + y_dir[k]
                        if 0<=dx<r and 0<=dy<c and visited[dx][dy]==0 and graph[dx][dy]==color:
                            visited[dx][dy]=1
                            Q.append((dx,dy,color,cnt+1))
                            puyo_list.append((dx,dy))

                # 4이상 연결되어 있으면 터뜨린다.
                if len(puyo_list) >= 4:
                    boom = 1
                    for x,y in puyo_list:
                        graph[x][y] = '.'
    # 터진것이 있다면 ans += 1
    if boom == 1:
        ans += 1
    # 터진것이 없다면 이제 안터지므로 ans 출력 후 종료
    else:
        print(ans)
        exit()
    # stack에서 다 넣고 맵 새로 그린다
    stack_list = [ deque() for _ in range(c) ]
    for col in range(c):
        for row in range(r-1, -1, -1):
            if graph[row][col] != '.':
                stack_list[col].append(graph[row][col])

    graph_tmp = [ ['.' for _ in range(c)] for _ in range(r) ]
    for idx, stack in enumerate(stack_list):
        row = r - 1
        while stack:
            graph_tmp[row][idx] = stack.popleft()
            row -= 1
    graph = graph_tmp




