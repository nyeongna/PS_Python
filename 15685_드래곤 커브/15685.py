n = int(input())
# n개의 드래곤커브를 저장할 리스트
dc_list = list()
'''
문제에서 나왔듯이 4방향 존재
0: 오른쪽
1: 위쪽
2: 왼쪽
3: 밑쪽
'''

# 각 방향에 맞게 더해줘야할 x,y의 방향
dir_list = {
    0: (0, 1),
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0)
}
# 0 -> 1
# 1 -> 2
# 2 -> 3
# 3 -> 0
new_dir = [1,2,3,0]

'''
x 세대에서 x+1 세대로 넘어갈 때
이전 x세대의 드래곤커브 선분들을 역순으로 참조해서 x+1세대의 드래곤커브들이 차례차례 완성됨
'''
for _ in range(n):
    y, x, d, level = map(int, input().split())
    dc = [(x,y,d)]
    for _ in range(level):
        sx, sy, sz = dc[-1]
        for idx in range(len(dc)-1, -1, -1):
            nx, ny = dir_list[sz]
            sx = sx + nx
            sy = sy + ny
            sz = new_dir[dc[idx][2]]
            dc.append((sx,sy,sz))
    dc_list.append(dc)

graph = [ [0]*105 for _ in range(105) ]

# 구한 모든 드래곤커브를 색칠한다
for dc in dc_list:
    x, y, z = dc[0]
    graph[x][y] = 1
    for xx, yy, zz in dc:
        nx, ny = dir_list[zz]
        xx = xx + nx
        yy = yy + ny
        graph[xx][yy] = 1
ans = 0
# (i,j) 좌표 기준 (i+1,j) (i,j+1), (i+1,j+1), (i,j) 모두 표시가 되어있으면 정사각형 완성이라고 간주
for i in range(101):
    for j in range(101):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            ans += 1
print(ans)

        


    

    