from sys import stdin
from collections import deque

# 바퀴 상태 입력 받기
wheel_list = []
for _ in range(4):
    wheel_list.append(deque(list(map(int, stdin.readline().strip()))))

k = int(input())
for _ in range(k):
    wheel, direction = map(int, input().split())
    wheel -= 1
    # 각 바퀴 돌리는 방향 1: 시계, -1: 반시계, 0: 안움직임
    rotate = [0, 0, 0, 0]
    rotate[wheel] = direction

    # check which wheel should be rotating
    # 바로 돌리지 말고 각 바퀴가 돌아가는지 안돌아가는지 체크한다
    # 오른쪽 방향
    for idx in range(wheel, 0, -1):
        if wheel_list[idx][6] != wheel_list[idx-1][2]:
            rotate[idx-1] = -rotate[idx]
    # 왼쪽 방향
    for idx in range(wheel, 3, 1):
        if wheel_list[idx][2] != wheel_list[idx+1][6]:
            rotate[idx+1] = -rotate[idx]

    # rotate the wheels
    for idx, dir in enumerate(rotate):
        if dir == 1:
            wheel_list[idx].appendleft(wheel_list[idx].pop())
        elif dir == -1:
            wheel_list[idx].append(wheel_list[idx].popleft())
ans = 0
for idx in range(4):
    ans = ans + wheel_list[idx][0] * 2**idx
print(ans)

'''
시간 복잡도: k
'''
