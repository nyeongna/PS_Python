'''
1,2,3,4...
1,2,3,4...단계가 반복됨
다 반복될떄마다 cnt++ 해서 마지막에 *4 해주면 --> 몇 단계인지 구할 수 있음
'''

'''
3 2
1 2 1 2 1 2
0 1 2 3 4 5
시작점: 0
내리는점: n-1

0
1 2 1 2 1 2
0 1 2 3 4 5

0 0 0
0 1 2 

1
2 1 2 1 2 1
5 0 1 2 3 4

0 0 0
2 0 1 

'''
from collections import deque
n, k = map(int, input().split())
hp_list = deque(list(map(int, input().split())))
# 어차피 n-1 번째에 도달하면 무조건 로봇을 내리므로 처음 n개의 위치만 추적하면됨
robot_list = deque([0]*n)

ans, cnt = 1, 0
while True:
    # 벨트회전
    # 벨트&로봇 같이 회전하므로 hp 깎일일이 없다
    hp_list.appendleft(hp_list.pop())
    robot_list.appendleft(robot_list.pop())
    if robot_list[-1]==1:
        robot_list[-1]=0
    # 로봇이동
    # 이동하려는 칸에 로봇이 없고 & 내구도 1이상
    for i in range(len(robot_list)-2, -1, -1):
        if robot_list[i]==1 and robot_list[i+1] == 0 and hp_list[i+1] >= 1:
            robot_list[i+1]=1
            robot_list[i]=0
            hp_list[i+1] -= 1
            if hp_list[i+1] == 0:
                cnt += 1
        if robot_list[-1]==1:
            robot_list[-1]=0
    # 로봇 올리기
    # 젤 첫번째 벨트 내구도 1 이상이면 로봇 올림
    if hp_list[0] >= 1:
        hp_list[0] -= 1
        robot_list[0] = 1
        if hp_list[0] == 0:
            cnt += 1
    # 내구도 0인 칸이 K개 이상이면 멈춤, 아니면 다시동작
    if cnt >= k:
        print(ans)
        exit()
    ans += 1
