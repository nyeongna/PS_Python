from sys import stdin

# 입력받기
graph = [ list(map(int, stdin.readline().strip().split())) for _ in range(9) ]

#
zero_list = []
row_dict = [ dict() for _ in range(9) ]
col_dict = [ dict() for _ in range(9) ]
quad_dict = [ dict() for _ in range(9) ]

# 각 숫자들의 위치에 해당하는 row, col, quad에 이미 숫자가 있다고 표시하기 (dict에 표시)
for i in range(9):
    for j in range(9):
        num = graph[i][j]
        if num==0:
            zero_list.append((i,j))
        else:
            row_dict[i][num] = 1
            col_dict[j][num] = 1
            quad_dict[i//3*3 + j//3][num] = 1

# 0 위치의 갯수
zero_num = len(zero_list)

# 그래프 출력
def PrintGraph():
    for i in range(9):
        for j in range(9):
            print(graph[i][j], end=' ')
        print()
# (x,y) 위치에 num을 넣을 수 있는지 체크
def checkNum(x,y,num):
    if num in row_dict[x]:
        return 0
    if num in col_dict[y]:
        return 0
    if num in quad_dict[x//3*3 + y//3]:
        return 0
    return 1
# (x,y) 위치에 num이 있다고 표기
def markNum(x,y,num):
    row_dict[x][num]=1
    col_dict[y][num]=1
    quad_dict[x//3*3 + y//3][num]=1    
# (x,y) 위치에서 num이 있다는 기록을 제거
def deleteNum(x,y,num):
    row_dict[x].pop(num)
    col_dict[y].pop(num)
    quad_dict[x//3*3 + y//3].pop(num)

def DFS(level):
    if level==zero_num:
        PrintGraph()
        exit()
    # 채워야할 자리의 level(idx) 정보를 뽑아내고
    x, y = zero_list[level]
    # 1~10 중 되는 숫자를 시도해본다.
    for try_num in range(1,10,1):
        if checkNum(x, y, try_num) == 1:
            markNum(x, y, try_num)
            graph[x][y] = try_num
            DFS(level+1)
            deleteNum(x, y, try_num)

DFS(0)

'''
시간 복잡도
10^빈 자리의 갯수이지만...."baekjoon의 백트래킹 알고리즘으로 풀 수 있는 입력만 주어진다. 다음은 그 알고리즘의 수행 시간이다" 조건이 있으므로 풀리는듯?
'''