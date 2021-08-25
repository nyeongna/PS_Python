from sys import stdin
from collections import deque
import copy

n, mm, k = map(int, stdin.readline().strip().split())
graph = [ [list() for _ in range(n)] for _ in range(n) ]
for _ in range(mm):
    r, c, m, s, d = map(int, stdin.readline().strip().split())
    graph[r-1][c-1].append((m,s,d))

direction_dict = {
    0 : (-1, 0),
    1 : (-1, 1),
    2 : (0, 1),
    3 : (1, 1),
    4 : (1, 0),
    5 : (1, -1),
    6 : (0, -1),
    7 : (-1, -1)
}
for _ in range(k):
    tmp_graph = [ [list() for _ in range(n)] for _ in range(n) ]
    two_fire = set()
    for i in range(n):
        for j in range(n):
            for (mass, speed, dir) in graph[i][j]:
                dx, dy, x_dir, y_dir = i, j, direction_dict[dir][0], direction_dict[dir][1]
                # 격자를 벗어나서 움직일 수 있으므로 % n 해주면된다.
                dx = (dx + x_dir*speed) % n
                dy = (dy + y_dir*speed) % n
                # while dspeed:
                #     dx = dx + x_dir
                #     dy = dy + y_dir
                #     dspeed = dspeed - 1
                # # dx, dy가 (-) 값이 될수도 있으므로 다시 %n 해준다
                #dx, dy = dx%n, dy%n
                tmp_graph[dx][dy].append((mass,speed,dir))
                if len(tmp_graph[dx][dy])>=2:
                    two_fire.add((dx,dy))

    # 파이어볼이 2개 이상인 곳만 돌린다.
    for (x,y) in list(two_fire):
        m_sum, s_sum = 0, 0
        even_flag, odd_flag = 0, 0
        for idx in range(len(tmp_graph[x][y])):
            m_sum += tmp_graph[x][y][idx][0]
            s_sum += tmp_graph[x][y][idx][1]
            if tmp_graph[x][y][idx][2] % 2 == 0:
                even_flag = 1
            else:
                odd_flag = 1
        mm = m_sum // 5
        ss = s_sum // len(tmp_graph[x][y])
        tmp_graph[x][y].clear()
        if mm > 0:
            if even_flag == 1 and odd_flag == 1:
                tmp_graph[x][y].extend( [(mm, ss, 1), (mm, ss, 3), (mm, ss, 5), (mm, ss, 7) ] )
            else:
                tmp_graph[x][y].extend( [(mm, ss, 0), (mm, ss, 2), (mm, ss, 4), (mm, ss, 6) ] )
    
    graph = tmp_graph

ans = 0
for i in range(n):
    for j in range(n):
        for (m,s,d) in graph[i][j]:
            ans = ans + m
print(ans)