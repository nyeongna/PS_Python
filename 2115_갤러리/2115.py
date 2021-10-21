n, m = map(int, input().split())

graph=list()
for _ in range(n):
    graph.append(input())

visited = [ [ [0]*4 for _ in range(m)] for _ in range(n) ]

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
empty_box = {0:(0,1), 1:(1,0), 2:(0,1), 3:(1,0)}
ans=0
ans_list=list()

'''
그리디 완전탐색(구현)
(i,j) 빈칸 기준 윗벽     +  오른쪽 빈 칸   + 오른쪽 빈 칸의 위쪽,
               오른쪽벽  +  밑쪽 빈칸     + 밑쪽빈칸의 오른쪽벽,
               밑쪽벽   +  오른쪽 빈칸    + 오른쪽 빈칸의 밑쪽벽,
               왼쪽벽   +  밑쪽 빈칸      + 밑쪽 빈칸의 왼쪽벽
만 검사해서 조건 충족되면 ans+1 (그리디)하게 접근.
-그리디하게 접근해도 최대가 보장안되는 경우를 못찾겠음...
'''
for i in range(n):
    for j in range(m):
        if graph[i][j]=='.':
            for k in range(4):
                if visited[i][j][k]==1:
                    continue
                # i, j는 현재 빈칸의 위치
                # dx, dy는 (i,j)기준 k 위치의 벽
                dx = i + x_dir[k]
                dy = j + y_dir[k]
                # empty_x, empty_y는 이어질 빈 칸 위치
                empty_x, empty_y = i + empty_box[k][0], j + empty_box[k][1]
                # edx, edy 는 (empty_x, empty_y) 기준 k위치의 벽
                edx, edy = empty_x + x_dir[k], empty_y + y_dir[k]
                # 모든 기준을 통과하면 그림 전시 가능
                if 0<=dx<n and 0<=dy<m and 0<=edx<n and 0<=edy<m and graph[dx][dy]=='X' and graph[edx][edy]=='X' and graph[empty_x][empty_y]=='.' and visited[empty_x][empty_y][k]==0:
                    visited[i][j][k]=1
                    visited[empty_x][empty_y][k]=1
                    ans += 1
                    ans_list.append((i,j,empty_x,empty_y, k))

print(ans)
                

