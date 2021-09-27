from collections import deque


############# INPUT
n = int(input())
k = int(input())
graph = [ [0]*(n+1) for _ in range(n+1) ]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 2
l = int(input())
turn_list = deque()
for _ in range(l):
    turn_list.append(input().split())
#############################################3

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
snake = deque([(1,1)])
snake_x, snake_y, snake_d = 1, 1, 1
graph[snake_x][snake_y] = 1

time = 0
while True:
    # 현재 방향으로 진행
    x, y = snake[-1][0], snake[-1][1]
    dx, dy = x+x_dir[snake_d], y+y_dir[snake_d]
    # "다음 진행 방향"이 graph를 벗어나거나, 현재 뱀 부분이면 GAME OVER
    if  1 > dx or n < dx or 1 > dy or n < dy or graph[dx][dy]==1:
        print(time+1)
        exit()
    # 뱀을 한칸 전진
    snake.append((dx,dy))
    #사과가 없다면, 뱀 꼬리부분 자름
    if graph[dx][dy]==0:
        # snake의 진행사항을 deque으로 관리해서 pop이 O(1)걸리게끔한다.
        # 사과를 다 먹으면 몸통 길이가 100이고 전체 graph크기가 10,000 이고 turn을 계속하면 무한대로 돌수도(?)있다.
        px, py = snake.popleft()
        graph[px][py]=0
    graph[dx][dy]=1

    time = time + 1
    # 아직 turn 할게 있다면 snake의 방향을 바꿔준다
    if turn_list and (str(time) == turn_list[0][0]):
        t, dir = turn_list.popleft()
        if dir == 'D':
            snake_d = (snake_d + 1) % 4
        elif dir == 'L':
            snake_d = (snake_d - 1) % 4



