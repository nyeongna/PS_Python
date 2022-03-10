
n, m, k = map(int, input().split())
# graph에는 [상어번호] 저장 (0일시 빈칸)
graph = [ list(map(int, input().split())) for _ in range(n) ]

# smell_graph 에는 [상어번호, 냄새시간] 기록
smell_graph = [ [[0,0]]*(n+1) for _ in range(n+1)]
init_direct = [None] + list(map(int,input().split()))

# 1: 위, 2:아래, 3:왼, 4:오른
x_dir = [None,-1,1, 0, 0]
y_dir = [None,0, 0,-1, 1]

# dir_dict[2][3]: '2'번째 상어가 '왼쪽'을 바라볼때 우선순위
dir_dict = dict()
for i in range(1,m+1):
    dir_dict[i]=dict()

# sq_dict에 상어정보 [x좌표, y좌표, 방향] 기록
sq_dict = dict()

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            sq_idx = graph[i][j]
            smell_graph[i][j] = [sq_idx, k]
            sq_dict[sq_idx] = [i, j, init_direct[sq_idx]]

# 각 상어의 방향 별 우선순위 방향을 기록
for i in range(1, m+1):
    for j in range(1, 5):
        dir_dict[i][j] = list(map(int,input().split()))

for time in range(1, 1001):
    # 모든 상어에 대해서 iterate
    for idx,val in sq_dict.items():
        # 죽어있는 상어면 pass
        if val == None:
            continue
        x, y, d = val[0], val[1], val[2]
        
        #빈칸으로 움직일수 없으면 flag=0
        flag=0
        for dir in dir_dict[idx][d]:
            dx = x + x_dir[dir]
            dy = y + y_dir[dir]

            # 1 아무 냄새가 없었던 칸인경우
            if 0<=dx<n and 0<=dy<n and smell_graph[dx][dy][1]==0:
                # 1.1 이동하려는 칸에 상어가 있는경우 O
                if graph[dx][dy] != 0:
                    enemy_idx = graph[dx][dy]
                    # 현재 이동하려는 상어가 더 셈
                    if enemy_idx > idx:
                        graph[x][y]=0
                        graph[dx][dy]=idx
                        sq_dict[idx] = [dx,dy,dir]
                        sq_dict[enemy_idx] = None
                        flag=1
                        break
                    # 원래 있던 상어가 더 셈
                    else:
                        # 이동하려는 상어번호 죽임
                        graph[x][y]=0
                        sq_dict[idx]=None
                        flag=1
                        break
                # 1.2 이동하려는 칸에 상어가 없는경우 X
                else:
                    graph[x][y]=0
                    graph[dx][dy]=idx
                    sq_dict[idx] = [dx,dy,dir]
                    flag=1
                    break

        # 2 자신 냄새가 있던 곳으로 되돌아감
        if flag==0:
            for dir in dir_dict[idx][d]:
                dx = x + x_dir[dir]
                dy = y + y_dir[dir]
                # 2.1 우선순위에 의거해 자신냄새가 있는 쪽으로 바로이동
                if 0<=dx<n and 0<=dy<n and smell_graph[dx][dy][0]==idx:
                    # 다음위치로 이동
                    graph[dx][dy] = idx
                    # 상어정보 dict에 업데이트
                    sq_dict[idx] = [dx, dy, dir]
                    # 이동 전 위치 초기화
                    graph[x][y] = 0
                    break
    # 새롭게 바뀐 상어정보에 기반해서 smell_graph 업데이트
    for key,val in sq_dict.items():
        if val==None:
            continue
        x, y, d = val[0], val[1], val[2]
        smell_graph[x][y] = [key, k]
    # 상어가 위치한 곳 빼고 나머지 자리에서 냄새 -1초
    for i in range(n):
        for j in range(n):
            # 상어나, 냄새가 있던 자리면
            if graph[i][j] == 0 and smell_graph[i][j][1] > 0:
                smell_graph[i][j][1] -= 1
                if smell_graph[i][j][1] == 0:
                    smell_graph[i][j][0] = 0
    # 몇마리 상어 살아있나 확인
    sq_num=0
    for kk, v in sq_dict.items():
        if v != None:
            sq_num += 1
    if sq_num == 1:
        print(time)
        exit()

print(-1)


        
            
