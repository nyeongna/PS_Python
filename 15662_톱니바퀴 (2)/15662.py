t = int(input())
from collections import deque

wheel_list = list()
wheel_list.append(None)
for _ in range(t):
    # wheel[2]: 오른쪽면
    # wheel[6]: 왼쪽면 
    wheel = deque(list(map(int, input())))
    wheel_list.append(wheel)
# a=int(input())
# for i in wheel_list:
#     print(i)

def dfs(idx, dir, side, arrow, start):

    if idx==0 or idx==t+1:
        return

    left, right = wheel_list[idx][6], wheel_list[idx][2]
    if start==0: 
        # 시계방향 회전
        if dir==1:
            wheel_list[idx].appendleft(wheel_list[idx].pop())
        # 반시계방향 회전
        elif dir==-1:
            wheel_list[idx].append(wheel_list[idx].popleft())
        dfs(idx-1, dir, left, 'left', None)
        dfs(idx+1, dir, right, 'right', None)

    else:
        # idx 기준 오른쪽에 있는 톱니바퀴가 비교해서
        print(idx, dir, side, arrow, start)
        print(wheel_list[idx][2])
        if arrow=='left' and wheel_list[idx][2] != side:
            # 오른쪽에 있는 톱니바퀴가 시계방향(1) 로 회전했다면
            # idx 톱니바퀴는 반시계방향으로 외전
            print('left에 들어옴')
            print(idx, dir, side, arrow, start)
            print(wheel_list[idx][2])
            if dir == 1:
                wheel_list[idx].append(wheel_list[idx].popleft())
                dfs(idx-1, -1, left, 'left', None)
            # idx 톱니바퀴는 시계방향으로 회전
            elif dir== -1:
                wheel_list[idx].appendleft(wheel_list[idx].pop())
                dfs(idx-1, 1, right, 'left', None)

        elif arrow=='right' and wheel_list[idx][6] != side:
            print('right에 들어옴')
            print(idx, dir, side, arrow, start)
            print(wheel_list[idx][6])
            # 왼쪽쪽에 있는 톱니바퀴가 시계방향(1) 로 회전했다면
            # idx 톱니바퀴는 반시계방향으로 외전
            if dir == 1:
                wheel_list[idx].append(wheel_list[idx].popleft())
                dfs(idx+1, -1, right, 'right', None)
            # idx 톱니바퀴는 시계방향으로 회전
            elif dir == -1:
                wheel_list[idx].appendleft(wheel_list[idx].pop())
                dfs(idx+1, 1, left, 'right', None)
    
for _ in range(int(input())):
    idx, dir = map(int, input().split())
    # idx 바퀴의 왼쪽으로 dfs 진행
    dfs(idx, dir, wheel_list[idx][6], 'left', 0)
    # idx 바퀴의 오른쪽으로 dfs 진행
    dfs(idx, dir, wheel_list[idx][2], 'right', 0)

    print('----------')
    print(idx)
    for i in wheel_list:
        print(i)
    print()
