'''
목표: 격자 밖으로 나간 모래의 양의 합
회전: 벽을 만날때마다 방향을 바꾼다
-왼, 밑, 오른, 위 (왼쪽이랑 오른쪽으로 갈 땐 step+1 해줌)
'''
import copy


n = int(input())
graph = [ list(map(int,input().split())) for _ in range(n) ]
gg = [ [0]*n for _ in range(n) ]
size = n**2
x, y = n//2, n//2
gg[x][y] = 0
x_dir = [0, 1, 0, -1]
y_dir = [-1,0, 1,  0]
step = 0
dir = 0
cnt = 1

# sp_# 은 # 방향에 해당하는 이차원배열 비율표
sp_0 = [
    [0,    0,  0.02,    0,  0],
    [0,   0.1, 0.07, 0.01,  0],
    [0.05, -1,    0,    0,  0],
    [0,   0.1, 0.07, 0.01,  0],
    [0,     0, 0.02,    0,  0]
]
sp_3 = copy.deepcopy(sp_0)
sp_3 = list(zip(*sp_3[::-1]))
sp_2 = copy.deepcopy(sp_3)
sp_2 = list(zip(*sp_2[::-1]))
sp_1 = copy.deepcopy(sp_2)
sp_1 = list(zip(*sp_1[::-1]))

sp_dict={
    0: sp_0,
    1: sp_1,
    2: sp_2,
    3: sp_3
}

ans = 0
# 토네이도 발생지점에서 방향에 해당하는 곳에 모래 흩뿌림
def spread(x,y,dir):
    global ans
    sand = graph[x][y]
    spread_sum = 0
    ax, ay = None, None
    for i in range(5):
        for j in range(5):
            dx = x+i-2
            dy = y+j-2
            fly_sand = int(sand*sp_dict[dir][i][j])
            if sp_dict[dir][i][j] == -1:
                ax, ay = x+i-2, y+j-2
            # %로 퍼질때- 그래프 내에서 퍼질때
            if sp_dict[dir][i][j] > 0 and 0 <= dx < n and 0 <= dy < n:
                spread_sum += fly_sand
                graph[dx][dy] += fly_sand
            # #로 퍼질때- 그래프 밖으로 퍼질때
            elif sp_dict[dir][i][j] > 0 and (0 > dx or dx >= n or 0 > dy or dy >= n):
                spread_sum += fly_sand
                ans += fly_sand
    # 알파로 퍼뜨리기
    if 0 <= ax < n and 0 <= ay < n:
        graph[ax][ay] += sand - spread_sum
    else:
        ans += sand - spread_sum
    # 토네이도가 친 장소는 이제 모래가 없음 (x,y)
    graph[x][y] = 0

while cnt != n**2:
    cur = 0
    if dir==0 or dir==2:
        step += 1
    for _ in range(step):
        x = x + x_dir[dir]
        y = y + y_dir[dir]
        # 토네이도 이동
        gg[x][y] = cnt
        
        # 토네이도 좌표와 방향을 줌
        spread(x, y, dir)
        cnt += 1
        if cnt==n**2:
            break
    dir = (dir+1) % 4

print(ans)








