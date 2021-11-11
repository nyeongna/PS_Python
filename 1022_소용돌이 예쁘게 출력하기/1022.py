r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1+5000, c1+5000, r2+5000, c2+5000

#graph = [ [0]*(10002) for _ in range(10002) ]

max_dist=float('-inf')

dir = [
    (0,-1), # ⬅️  왼쪽
    (-1,0), # ⬆️ 위쪽
    (0,1),  # 👉 오른쪽
    (1,0)   # ⤵️ 밑쪽
]
x, y = 10000, 10000
num, d, d_cnt = 100020001, 0, 
while num != 0:
    if num%10000000 == 0:
        print(x, y, num)
    #graph[x][y] = num
    num -= 1
    dx,dy= x+dir[d][0], y+dir[d][1]
    if dx < 0 or dx > 10000 or dy < 0 or dy > 10000 or graph[dx][dy] != 0:
        d = (d+1)%4
    x, y = x + dir[d][0], y + dir[d][1]

x_boundary = r2-r1+1
y_boundary = c2-c1+1
for i in range(r1, r2+1, 1):
    for j in range(c1, c2+1, 1):
        print(graph[i][j], end=' ')
        max_dist = max(max_dist, len(str(graph[i][j])))
    print()
print()

for i in range(r1, r2+1, 1):
    for j in range(c1, c2+1, 1):
        print(str(graph[i][j]).rjust(max_dist, " "), end=' ')
    print()
