c, r = map(int, input().split())

str_to_int={
    'N':0,
    'E':1,
    'S':2,
    'W':3
}
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
n, m = map(int, input().split())
# 로봇의 정보는 robot_dict로 관리
# 로봇의 그래프 위치는 graph를 통해 관리
robot_dict=dict()
graph = [ [0]*(c+1) for _ in range(r+1) ]

for idx in range(n):
    y, x, d = map(str, input().split())
    x, y, d = r-int(x)+1, int(y), str_to_int[d]

    # 로봇의 정보는 robot_dict에 저장
    # 로봇의 위치는 graph에 저장
    robot_dict[idx+1] = (x, y, d)
    graph[x][y] = (x, y, d, idx+1)

for _ in range(m):
    idx, ops, cnt = map(str,input().split())
    idx, ops, cnt = int(idx), ops, int(cnt)
    rx, ry, rd = robot_dict[idx]
    # L, R이면 방향만 바꿔서 다시 robot_dict, graph 업데이트
    if ops == 'L':
        new_rd = (rd-cnt)%4
        robot_dict[idx] = (rx, ry, new_rd)
        graph[rx][ry] = (rx,ry,new_rd,idx)
    # R, R이면 방향만 바꿔서 다시 robot_dict, graph 업데이트
    elif ops == 'R':
        new_rd = (rd+cnt)%4
        robot_dict[idx] = (rx, ry, new_rd)
        graph[rx][ry] = (rx,ry,new_rd,idx)
    # F 이면 방향대로 한칸씩 전진하면서 불가능하면 오류 print하고 종료
    elif ops == 'F':
        dx, dy = rx, ry
        for step in range(cnt):
            dx = dx + x_dir[rd]
            dy = dy + y_dir[rd]
            if dx < 1 or dx > r or dy < 1 or dy > c:
                print(f"Robot {idx} crashes into the wall")
                exit()
            elif graph[dx][dy] != 0:
                print(f"Robot {idx} crashes into robot {graph[dx][dy][3]}")
                exit()
        # cnt만큼 F를 통과했으므로, 마지막위치와 시작위치 업데이트해줌
        robot_dict[idx] = (dx,dy,rd)
        graph[dx][dy] = (dx, dy, rd, idx)
        graph[rx][ry] = 0

# 여기까지 왔으면 모든 임무 완수 가능
print('OK')
        

        
    