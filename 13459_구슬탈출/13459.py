from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [ list(map(str,stdin.readline().strip())) for _ in range(n) ]

rx, ry = 0, 0
bx, by = 0, 0
hx, hy = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j
        if graph[i][j] == 'O':
            hx, hy = i, j

visited = [ [ [ [0]*11 for _ in range(11) ] for _ in range(11) ] for _ in range(11) ]

Q = deque()
Q.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = 1

def Rollup(rx, ry, bx, by):
    red_flag=0
    blue_flag=0
    higher = 'red'

    # 초기에 어디가 더 높은 위치에 있는지 확인
    if ry==by:
        if rx > bx:
            higher = 'blue'
    # red 위로 굴린다
    while rx-1 >= 0 and rx-1 < n and graph[rx-1][ry] != '#':
        rx = rx - 1
        if graph[rx][ry] == 'O':
            red_flag = 1
    # blue 위로 굴린다
    while bx-1 >= 0 and bx-1 < n and graph[bx-1][by] != '#':
        bx = bx - 1
        if graph[bx][by] == 'O':
            blue_flag = 1
    # 둘이 같은 곳에 떨어지고 처음에 red가 더 위에였다면, blue 위치를 한 칸 내린다
    if rx==bx and ry==by and higher=='red':
        bx = bx + 1
    # 둘이 같은 곳에 떨어지고 blue가 더 위에였다면, red 위치를 한 칸 내린다
    if rx==bx and ry==by and higher=='blue':
        rx = rx + 1
    
    success = 0
    # red, blue 안떨어짐 - 계속 진행
    if red_flag == 0 and blue_flag == 0:
        success = 0
    # red, blue 둘다 떨어짐 - 실패
    elif red_flag == 1 and blue_flag == 1:
        success = 2
    # red 떨어지고, blue 안떨어짐 - 성공
    elif red_flag == 1 and blue_flag == 0:
        success = 1
    # red 안떨어지고, blue 떨어짐 - 실패
    elif red_flag== 0 and blue_flag==1:
        success = 2
    
    return rx, ry, bx, by, success

def Rolldown(rx, ry, bx, by):
    red_flag=0
    blue_flag=0
    higher = 'red'

    # 초기에 어디가 더 높은 위치에 있는지 확인
    if ry==by:
        if rx > bx:
            higher = 'blue'
    # red 위로 굴린다
    while rx+1 >= 0 and rx+1 < n and graph[rx+1][ry] != '#':
        rx = rx + 1
        if graph[rx][ry] == 'O':
            red_flag = 1
    # blue 위로 굴린다
    while bx+1 >= 0 and bx+1 < n and graph[bx+1][by] != '#':
        bx = bx + 1
        if graph[bx][by] == 'O':
            blue_flag = 1
    # 둘이 같은 곳에 떨어지고 처음에 red가 더 위에였다면, red 위치를 한 칸 올린다
    if rx==bx and ry==by and higher=='red':
        rx = rx - 1
    # 둘이 같은 곳에 떨어지고 blue가 더 위에였다면, blue 위치를 한 칸 올린다
    if rx==bx and ry==by and higher=='blue':
        bx = bx - 1
    
    success = 0
    # red, blue 안떨어짐 - 계속 진행
    if red_flag == 0 and blue_flag == 0:
        success = 0
    # red, blue 둘다 떨어짐 - 실패
    elif red_flag == 1 and blue_flag == 1:
        success = 2
    # red 떨어지고, blue 안떨어짐 - 성공
    elif red_flag == 1 and blue_flag == 0:
        success = 1
    # red 안떨어지고, blue 떨어짐 - 실패
    elif red_flag== 0 and blue_flag==1:
        success = 2
    
    return rx, ry, bx, by, success

def Rollleft(rx, ry, bx, by):
    red_flag=0
    blue_flag=0
    left = 'red'

    # 초기에 어디가 왼쪽에 있는지 확인
    if rx==bx:
        if ry > by:
            left = 'blue'
    # red 왼쪽으로 굴린다
    while ry-1 >= 0 and ry-1 < m and graph[rx][ry-1] != '#':
        ry = ry - 1
        if graph[rx][ry] == 'O':
            red_flag = 1
    # blue 왼쪽로 굴린다
    while by-1 >= 0 and by-1 < m and graph[bx][by-1] != '#':
        by = by - 1
        if graph[bx][by] == 'O':
            blue_flag = 1
    # 둘이 같은 곳에 떨어지고 처음에 red가 더 왼쪽이였다면, blue 위치를 오르쪽으로 한 칸
    if rx==bx and ry==by and left=='red':
        by = by + 1
    # 둘이 같은 곳에 떨어지고 blue가 더 왼쪽이였다면, red 위치를 오른쪽으로 한 칸
    if rx==bx and ry==by and left=='blue':
        ry = ry + 1
    
    success = 0
    # red, blue 안떨어짐 - 계속 진행
    if red_flag == 0 and blue_flag == 0:
        success = 0
    # red, blue 둘다 떨어짐 - 실패
    elif red_flag == 1 and blue_flag == 1:
        success = 2
    # red 떨어지고, blue 안떨어짐 - 성공
    elif red_flag == 1 and blue_flag == 0:
        success = 1
    # red 안떨어지고, blue 떨어짐 - 실패
    elif red_flag== 0 and blue_flag==1:
        success = 2
    
    return rx, ry, bx, by, success
    
def Rollright(rx, ry, bx, by):
    red_flag=0
    blue_flag=0
    left = 'red'

    # 초기에 어디가 왼쪽에 있는지 확인
    if rx==bx:
        if ry > by:
            left = 'blue'
    # red 오른쪽으로 굴린다
    while ry+1 >= 0 and ry+1 < m and graph[rx][ry+1] != '#':
        ry = ry + 1
        if graph[rx][ry] == 'O':
            red_flag = 1
    # blue 오른쪽로 굴린다
    while by+1 >= 0 and by+1 < m and graph[bx][by+1] != '#':
        by = by + 1
        if graph[bx][by] == 'O':
            blue_flag = 1
    # 둘이 같은 곳에 떨어지고 처음에 red가 더 왼쪽이였다면, red 위치를 왼쪽으로 한 칸
    if rx==bx and ry==by and left=='red':
        ry = ry - 1
    # 둘이 같은 곳에 떨어지고 blue가 더 왼쪽이였다면, blue 위치를 왼쪽으로 한 칸
    if rx==bx and ry==by and left=='blue':
        by = by - 1
    
    success = 0
    # red, blue 안떨어짐 - 계속 진행
    if red_flag == 0 and blue_flag == 0:
        success = 0
    # red, blue 둘다 떨어짐 - 실패
    elif red_flag == 1 and blue_flag == 1:
        success = 2
    # red 떨어지고, blue 안떨어짐 - 성공
    elif red_flag == 1 and blue_flag == 0:
        success = 1
    # red 안떨어지고, blue 떨어짐 - 실패
    elif red_flag== 0 and blue_flag==1:
        success = 2
    
    return rx, ry, bx, by, success

def printGraph(rx,ry,bx,by):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                graph[i][j] = '.'
            if graph[i][j] == 'B':
                graph[i][j] ='.'
    graph[rx][ry] = 'R'
    graph[bx][by] = 'B'
    for i in graph:
        print(''.join(i))

while len(Q) > 0:
    rx, ry, bx, by, dist = Q.popleft()
    #print(f'초기단계: {rx}, {ry}, {bx}, {by}')
    #printGraph(rx,ry,bx,by)

    rrx, rry, bbx, bby, success = Rollup(rx, ry, bx, by)
    #print(f'Up-\t{rrx},{rry},{bbx},{bby}, {dist+1}, {success}')
    if success == 0 and visited[rrx][rry][bbx][bby]==0:
        visited[rrx][rry][bbx][bby] = 1
        Q.append((rrx, rry, bbx, bby, dist+1))
                
    elif success == 1 and dist+1 <= 10:
        print(1)
        #print('dist: ' + str(dist+1))
        exit()
    
    rrx, rry, bbx, bby, success = Rolldown(rx, ry, bx, by)
    #print(f'Down-\t{rrx},{rry},{bbx},{bby}, {dist+1}, {success}')
    if success == 0 and visited[rrx][rry][bbx][bby]==0:
        visited[rrx][rry][bbx][bby] = 1
        Q.append((rrx, rry, bbx, bby, dist+1))
        
    elif success == 1 and dist+1 <= 10:
        print(1)
        #print('dist: ' + str(dist+1))
        exit()
    
    rrx, rry, bbx, bby, success = Rollleft(rx, ry, bx, by)
    #print(f'Left-\t{rrx},{rry},{bbx},{bby}, {dist+1}, {success}')
    if success == 0 and visited[rrx][rry][bbx][bby]==0:
        visited[rrx][rry][bbx][bby] = 1
        Q.append((rrx, rry, bbx, bby, dist+1))
        
    elif success == 1 and dist+1 <= 10:
        print(1)
        #print('dist: ' + str(dist+1))
        exit()

    rrx, rry, bbx, bby, success = Rollright(rx, ry, bx, by)
    #print(f'Right-\t{rrx},{rry},{bbx},{bby}, {dist+1}, {success}')
    if success == 0 and visited[rrx][rry][bbx][bby]==0:
        visited[rrx][rry][bbx][bby] = 1
        Q.append((rrx, rry, bbx, bby, dist+1))
        
    elif success == 1 and dist+1 <= 10:
        print(1)
        #print('dist: ' + str(dist+1))
        exit()

    #print()
    
print(0)