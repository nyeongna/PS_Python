r1, c1, r2, c2 = map(int, input().split())

map = [ [0]*(6) for _ in range(51) ]

max_dist=float('-inf')

dir = [
    (0,1),  # 👉 오른쪽
    (-1,0), # ⬆️ 위쪽
    (0,-1), # ⬅️  왼쪽
    (1,0)   # ⤵️ 밑쪽
]

# num: 1부터 시작
# x, y는 (0,0) 좌표에서 시작한다고 가정
# d는 방향
x, y, d, num = 0, 0, 0, 1
# step은 현재 방향으로 몇 칸 갔는지 나타냄
# 현재 방향으로 max_step 만큼 갈 수 있음
# 방향이 2번 바뀔때마다 (정확히 말하면 오른쪽으로 갈 차례거나 왼쪽으로 갈 차례면) max_step + 1 해줌
step, max_step = 0, 1

# map 배열(최대 50x5)가 얼마나 채워졌는지 확인함
# cnt가 total_cnt가 되었다면, 다 채워진것이므로 while문에서 break
cnt, total_cnt= 0, (r2-r1+1) * (c2-c1+1)
max_num = float('-inf')
while True:
    # 현재 iterate하고 있는 (x,y)좌표가 <r1,r2> , <c1,c2> 범위안에 있다면 map을 update
    if r1 <= x <= r2 and c1 <= y <= c2:
        max_num = max(max_num, num)
        # x-r1 하는 이유는 r1이 음수일수도 있어서 r1만큼을 빼주면 (x-r1)은 0부터 시작하고 양수를 보장
        map[x-r1][y-c1] = num
        cnt += 1
        # cnt가 totla_cnt 되었다면 , break
        if cnt == total_cnt:
            break
    # d방향으로 1칸 전진
    x = x + dir[d][0]
    y = y + dir[d][1]
    step += 1
    num += 1

    # 방향 갱신 (앞에 벽)
    if step==max_step:
        step=0
        d = (d+1)%4
        if d==0 or d==2:
            max_step += 1

max_num = len(str(max_num))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(map[i][j]).rjust(max_num, " "), end= ' ')
    print()



