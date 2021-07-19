from sys import stdin

# r, c, n 입력받기
r, c, n = map(int, stdin.readline().rstrip().split())
graph = [ list(map(str, stdin.readline().rstrip())) for _ in range(r) ]

# 빈칸은 0, 폭탄은 4
for i in range(r):
    for j in range(c):
        if graph[i][j]=='.':
            graph[i][j]=0
        elif graph[i][j]=='O':
            graph[i][j]=4

# 모든 폭탄 1초 카운트
def updateGraph():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0:
                graph[i][j] = graph[i][j] - 1

#빈칸에 폭탄 설치, 폭탄은 1초 카운트
def Install():
    for i in range(r):
        for j in range(c):
            if graph[i][j]==0:
                graph[i][j]=4
            else:
                graph[i][j] = graph[i][j] - 1

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

# 1초 카운트 후 터지는 폭탄들 전부 리스트에 저장 후
# 마지막에 몰아서 터뜨림.
  # 미리미리 터뜨리면, 터져야 할 곳도 0으로 바꿔서 다 안터질 수 있음.
def Explode():
    candidate = []
    for i in range(r):
        for j in range(c):
            # 폭탄 1초 카운트
            if graph[i][j] > 0:
                graph[i][j]  = graph[i][j] - 1

            # 폭탄 터지면 리스트에 저장
            if graph[i][j]==1:
                candidate.append((i,j))

    # 몰아서 터뜨리기
    for (x,y) in candidate:
        graph[x][y]=0
        for k in range(4):
            dx = x + x_dir[k]
            dy = y + y_dir[k]
            if dx>=0 and dx<r and dy>=0 and dy<c:
                graph[dx][dy]=0
    
                

# 맨 처음 설치 0초
cnt = 0
# 맨 처음 설치 후 1초는 아무것도 하지 않음. 폭탄들의 시간만 흐름
cnt = cnt + 1
updateGraph()

# cnt가 짝수면 '설치', 홀수면 '폭발'
while cnt != n:
    cnt = cnt+1
    # cnt 짝수면 '설치'
    if cnt%2 == 0:
        Install()
    # cnt 홀수면 '폭발'
    else:
        Explode()

# 정답 print
for i in range(r):
    for j in range(c):
        if graph[i][j]==0:
            print('.',end='')
        else:
            print('O', end='')
    print()

# ----------------------------------------------
# 또다른 풀이
# 2차원 배열 2개를 만들어서 tmp, graph로 설정
# tmp는 1초 전, graph는 폭탄설치후로 해놓고, 어차피 폭탄은 번갈아가며 터지므로
# tmp 기반으로 폭탄 터뜨리면서 graph를 바꿔주고, 바뀐 graph를 통해 tmp 업데이트
# 폭발 후에는 graph 기반으로 다시 graph 빈칸에 폭탄 설치
# tmp 기반으로 폭탄 터뜨리면서 graph를 바꿔주고, 바뀐 graph를 통해 tmp 업데이트..... 반복
