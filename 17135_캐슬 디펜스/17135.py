from collections import deque
from sys import stdin
from itertools import combinations

n, m, archer_range = map(int, input().split())
graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range (n) ]
graph.append([0]*m)

positions = [ num for num in range(m) ]

max_kill = float('-inf')

# 궁수의 위치 조합
for comb in combinations(positions, 3):
    fx, fy = n, comb[0]
    sx, sy = n, comb[1]
    tx, ty = n, comb[2]

    # 이번 조합으로 죽일 수 있는 적의 수
    total_kill = 0

    # 처음 적 위치 기록
    enemy_list = set()
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                enemy_list.add((i, j))

    # 적이 없을 때까지 라운드 진행
    for round in range(m+100):
        # 1번째 궁수
        f_list = []
        for (x,y) in enemy_list:
            d = abs(fx-x) + abs(fy-y)
            if d <= archer_range:
                f_list.append((x,y,d))
        f_list = sorted(f_list, key=lambda x: (x[2], x[1]))
        if f_list:
            f_target = f_list[0][:2]
        else:
            f_target = None

        # 2번째 궁수
        s_list = []
        for (x, y) in enemy_list:
            d = abs(sx-x) + abs(sy-y)
            if d <= archer_range:
                s_list.append((x,y,d))
        s_list = sorted(s_list, key=lambda x: (x[2], x[1]))
        if s_list:
            s_target = s_list[0][:2]
        else:
            s_target = None

        # 3번째 궁수
        t_list = []
        for (x, y) in enemy_list:
            d = abs(tx-x) + abs(ty-y)
            if d <= archer_range:
                t_list.append((x,y,d))
        t_list = sorted(t_list, key=lambda x: (x[2], x[1]))
        if t_list:
            t_target = t_list[0][:2]
        else:
            t_target = None

        killed_enemy = {f_target, s_target, t_target}
        # 처음 적 리스트
        #print('이번 라운드 적 리스트')
        #print(enemy_list)
        enemy_list = enemy_list - killed_enemy
        # 죽여야할 적 리스트
        #print('죽여야 할 적 리스트')
        #print(killed_enemy)
        for targett in killed_enemy:
            if targett is not None:
                total_kill += 1
        #total_kill += len(killed_enemy)
        #print('현재까지 죽인 적')
        #print(total_kill)

        # 죽이고 난 후 적 리스트
        #print('죽이고 난 후 적 리스트')
        #print(enemy_list)
        # 화살 발사 후 적들 한칸 내려오기
        # 성에 도달한 적들
        arrive_castle = set()
        others = set()
        for ex,ey in enemy_list:
            if ex + 1 == n:
                arrive_castle.add((ex,ey))
            else:
                others.add((ex+1, ey))
        # enemy_list 재설치
        enemy_list = others

        #print('적들 내려오고 enemy list')
        #print(enemy_list)
        if len(enemy_list)==0:
            break

    max_kill = max(max_kill, total_kill)
print(max_kill)
exit()



