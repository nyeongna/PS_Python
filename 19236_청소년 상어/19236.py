import copy
'''
물고기 이동
-1번부터 -> 16번 순으로 이동함
-1칸만 이동 가능
-이동가능한 곳: 빈칸, 다른 물고기 칸 (반시계 45도 움직여서 탐색)
 -반시계 45도 돌면서 탐색함
-이동불가능X : 상어칸, 경계밖칸

상어 이동
-여러 칸 이동 가능 (지나가는 곳은 무시함)
-이동가능한 곳: 물고기가 무조건 존재해야 함
-이동불가능X : 빈칸, 경게밖칸
 -이동 불가능 하면 끝
 -최대값 계산

상어,물고기 이동 시 자리를 교환하는 식으로 이동함 (순간이동 설정)

각 칸에서 나올 수 있는 경우의 수 3
모든 칸 16
3^16 = 4천만
-물고기이동: 3*16=48
-상어이동: 3

설계
- dfs 완전탐색 -> base 조건을 상어가 못움직이는 경우 점수를 구하고 return
- dfs에서 return 되면 상어와 물고기 위치를 되돌려줌
- 물고기 위치를 관리하는 dict
- 격자를 관리하는 list graph
'''
x_dir = [None, -1, -1, 0, 1, 1, 1, 0, -1]
y_dir = [None, 0, -1, -1, -1, 0, 1, 1, 1]
graph = [ [0]*(4) for _ in range(4) ]
fish_dict = dict()
for row_num in range(4):
    row = list(map(int, input().split()))
    for col_num in range(4):
        j=col_num*2
        fish_idx, fish_dir = row[j], row[j+1]
        fish_dict[fish_idx] = (row_num, col_num, fish_dir)
        graph[row_num][col_num] = [fish_idx, fish_dir, 'fish']

# for i in graph:
#     print(i)
# for k,v in fish_dict.items():
#     print(k,v)

# 시작할때 (0,0) 물고기 자리에 상어를 둔다
first_fish_idx, first_fish_dir = graph[0][0][0], graph[0][0][1]
# 해당 인덱스의 물고기를 지워준다
del fish_dict[first_fish_idx]
graph[0][0] = [0, first_fish_dir, 'shark']
# 상어 위치, 방향 파악
sx, sy, sd = 0, 0, first_fish_dir
# 시작 점수
score = first_fish_idx
max_score = score

def dfs(sx, sy, sd, score, graph, fish_dict):
    global max_score
    # global sx, sy, sd, score, max_score
    # 물고기 이동함
    for fish_idx in range(1, 17, 1):
        # 1~16 번순으로 없는 물고기면 continue
        if fish_idx not in fish_dict:
            continue
        fish_x, fish_y, fish_dir = fish_dict[fish_idx]
        for _ in range(8):
            dx = fish_x + x_dir[fish_dir]
            dy = fish_y + y_dir[fish_dir]
            # 물고기가 가려는 방향이 경계 안이고
            if 0<=dx<4 and 0<=dy<4:
                dest_idx, dest_dir, dest_status = graph[dx][dy]
                # 가려는 곳이 물고기면
                if dest_status == 'fish':
                    # graph, fish_dict 업데이트
                    graph[fish_x][fish_y][1] = fish_dir
                    graph[fish_x][fish_y], graph[dx][dy] = graph[dx][dy], graph[fish_x][fish_y]
                    fish_dict[fish_idx] = (dx, dy, fish_dir)
                    fish_dict[dest_idx] = (fish_x, fish_y, dest_dir)
                    break
                # 가려는 곳이 빈칸이면
                elif dest_status == 'empty':
                    graph[fish_x][fish_y][1] = fish_dir
                    graph[fish_x][fish_y], graph[dx][dy] = graph[dx][dy], graph[fish_x][fish_y]
                    fish_dict[fish_idx] = (dx, dy, fish_dir)
                    break
            fish_dir += 1
            if fish_dir == 9:
                fish_dir = 1

    # 상어가 갈 수 있는 후보리스트
    tmp_sx, tmp_sy, tmp_sd = sx, sy, sd
    flag = 0
    for i in range(1,4,1):
        dx = tmp_sx + x_dir[tmp_sd] * i
        dy = tmp_sy + y_dir[tmp_sd] * i
        if 0<=dx<4 and 0<=dy<4 and graph[dx][dy][2] == 'fish':
            tmp_f_idx, tmp_f_dir, tmp_f_status = graph[dx][dy]
            # 상어위치를 graph에 업데이트
            graph[dx][dy] = [0, tmp_f_dir, 'shark']
            graph[tmp_sx][tmp_sy] = [-1, -1, 'empty']
            # 상어 변수를 물고기 x,y,d로 업데이트
            sx, sy, sd = dx, dy, tmp_f_dir
            # fish_dict 에서 먹힌 물고기 정보 지우기
            del fish_dict[tmp_f_idx]
            score += tmp_f_idx
            dfs(sx, sy, sd, score, copy.deepcopy(graph), copy.deepcopy(fish_dict))

            # 다시 되돌리기
            score -= tmp_f_idx
            fish_dict[tmp_f_idx] = (dx, dy, tmp_f_dir)
            sx, sy, sd = tmp_sx, tmp_sy, tmp_sd
            graph[tmp_sx][tmp_sy] = [0, tmp_sd, 'shark']
            graph[dx][dy] = [tmp_f_idx, tmp_f_dir, tmp_f_status]
            flag=1

    # 상어가 못 움직였으면 집에 간다는 뜻 = 점수 업데이트
    if flag==0:
        #print(eat_list)
        max_score = max(max_score, score)
        
dfs(sx, sy, sd, score, graph, fish_dict)
print(max_score)

