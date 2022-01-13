n = int(input())
graph =  [ [0]*(n+1) for _ in range(n+1) ]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        graph[i+1][j+1] = row[j]


'''
    0
1       2
    3
'''
def check(x, y, d1, d2):
    graph_tmp = [ [0]*(n+1) for _ in range(n+1) ]
    # 0, 1, 2, 3 꼭짓점 각각의 (x,y)좌표
    x_0, y_0 = x, y
    x_1, y_1 = x+d1, y-d1
    x_2, y_2 = x+d2, y+d2
    x_3, y_3 = x+d1+d2, y-d1+d2

    # 1번구역의 행은 1 <= x < 1번꼭짓점의 x좌표
    #         열은 1 <= y < 0번꼭짓점의 y좌표
    # 행의 값이 0번 꼭짓점의 x좌표 이상이면 y좌표의 끝범위를 +1
    cnt=0
    for i in range(1, x_1):
        if i >= x_0:
            cnt += 1
        for j in range(1, y_0-cnt+1):
            graph_tmp[i][j] = 1

    # 2번구역의 행은 1 <= x <= 2번꼭짓점의 x좌표
    #         열은 1 <= y <= n
    # 행의 값이 0번 꼭짓점의 x좌표 초과면 y좌표의 시작범위를 +1
    cnt=0
    for i in range(1, x_2+1):
        if i > x_0:
            cnt+=1
        for j in range(y_0+cnt+1, n+1):
            graph_tmp[i][j] = 2

    # 3번구역의 행은 n >= x > 1번꼭짓점의 x좌표-1
    #         열은 1 <= y < 3번꼭짓점의 y좌표
    # 행의 값이 3번 꼭짓점의 x좌표 미만이면 y좌표의 끝범위를 -1
    cnt=0
    for i in range(n, x_1-1, -1):
        if i < x_3:
            cnt+=1
        for j in range(1, y_3-cnt):
            graph_tmp[i][j] = 3

    # 4번구역의 행은 n >= x > 2번꼭짓점의 x좌표
    #         열은 n >= y > 3번꼭짓점의 y좌표
    # 행의 값이 3번 꼭짓점의 x좌표 이하이면 y좌표의 시작범위를 +1
    cnt=0
    for i in range(n, x_2, -1):
        if i <= x_3:
            cnt+=1
        for j in range(y_3+cnt, n+1):
            graph_tmp[i][j]= 4

    num_cnt = [0]*5
    for i in range(1, n+1):
        for j in range(1, n+1):
            num_cnt[graph_tmp[i][j]] += graph[i][j]

    if 1 in num_cnt:
        return float('inf')
    return max(num_cnt) - min(num_cnt)

ans = float('inf')
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if (x+d1+d2 > n) or (1 > y-d1) or (y+d2 > n):
                    continue
                num = check(x, y, d1, d2)
                ans = min(ans, num)

print(ans)