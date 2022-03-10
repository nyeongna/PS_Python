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
    
def dfs(idx, dir, NS_check, arrow):
    if idx==0 or idx==t+1:
        return
    left, right = wheel_list[idx][6], wheel_list[idx][2]
    if arrow=='left' and right!=NS_check:
        if dir==1:
            wheel_list[idx].append(wheel_list[idx].popleft())
        elif dir==-1:
            wheel_list[idx].appendleft(wheel_list[idx].pop())
        dfs(idx-1, dir*-1, left, 'left')
    elif arrow=='right' and left!=NS_check:
        if dir==1:
            wheel_list[idx].append(wheel_list[idx].popleft())
        elif dir==-1:
            wheel_list[idx].appendleft(wheel_list[idx].pop())
        dfs(idx+1, dir*-1, right, 'right')

for _ in range(int(input())):
    idx, dir = map(int, input().split())
    left, right = wheel_list[idx][6], wheel_list[idx][2]
    # 시계방향 회전
    if dir==1:
        wheel_list[idx].appendleft(wheel_list[idx].pop())
    # 반시계방향 회전
    elif dir==-1:
        wheel_list[idx].append(wheel_list[idx].popleft())

    # idx 바퀴의 왼쪽으로 dfs 진행
    dfs(idx-1, dir, left, 'left')
    # idx 바퀴의 오른쪽으로 dfs 진행
    dfs(idx+1, dir, right, 'right')

cnt=0
for i in range(1,t+1):
    cnt = cnt + wheel_list[i][0]
print(cnt)
