
'''
시간복잡도
O( c * (r * c) * r) = O (100 * 100 * 100 * 100) = 1억번 애매?
'''

from sys import stdin

r, c, m = map(int, input().split())
graph = [ [(0,0,0)]*(c+1) for _ in range(r+1) ]

# 상어 정보 입력받아서 graph에 입력
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    if d==1:
        d = 0
    elif d==2:
        d = 2
    elif d==3:
        d = 1
    elif d==4:
        d = 3
    graph[x][y] = (s, d, z)

# 북, 동, 남, 서
direction = [
    [-1, 0, 0],
    [0, 1, 1],
    [1, 0, 2],
    [0, -1, 3]
]

def move(x, y, speed, dir, size):
    # 왼쪽 오른쪽 방향이라면 (c*2-2)
    if dir == 1 or dir == 3:
        count = speed % (c*2-2)
    # 위 아래 방향이라면 % (r*2-2)
    elif dir== 0 or dir == 2:
        count = speed % (r*2-2)
    x_dir, y_dir, dir = direction[dir]
    # 상어 현재 방향으로 count 만큼만 움직이면 된다.
    # s의 최대인 1000까지 안돌고 r*2-2 OR c*2-2 번만 돌면 된다. 시간단축 핵심!
    for _ in range(count):
        if (x==1 and dir==0) or (x==r and dir==2) or (y==1 and dir==3) or (y==c and dir==1):
            x_dir, y_dir, dir = direction[(dir+2)%4]
        x = x + x_dir
        y = y + y_dir
    return x, y, dir
        
    
ans = 0
fisher_pos = 0

while fisher_pos < c:
    # 1. 낚시왕 오른쪽으로 한칸 이동
    fisher_pos = fisher_pos + 1
    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다
    for row in range(1, r+1):
        # 해당 열에서 물고기 발견하면, 없앤다. (z 크기가 0이 아니면 물고기가 있음)
        if graph[row][fisher_pos][2] != 0:
            ans = ans + graph[row][fisher_pos][2]
            graph[row][fisher_pos] = (0,0,0)
            break
    # 3. 상어가 이동한다
    # 이미 움직인 물고기는 또 움직이면 안되므로 tmp에 따로 저장해놓고 나중에 graph = tmp로 치환
    tmp = [ [(0,0,0)]*(c+1) for _ in range(r+1) ]
    for i in range(1, r+1):
        for j in range(1, c+1):
            if graph[i][j][2] != 0:
                speed, dir, size = graph[i][j][0], graph[i][j][1], graph[i][j][2]
                nx, ny, nd = move(i, j, speed, dir, size)
                if tmp[nx][ny][2] < size:
                    tmp[nx][ny] = (speed, nd, size)
    graph = tmp
    
print(ans)
    




