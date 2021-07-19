from sys import stdin
from collections import deque


ans_r, ans_c, k = map(int, input().split())
ans_r, ans_c = ans_r-1, ans_c-1

graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range(3) ]

def R_Operation():
    max_length = float('-inf')
    for idx, row in enumerate(graph):
        dic = dict()
        for num in row:
            if num==0:
                continue
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        r = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        rr = []
        for f, s, in r:
            rr.append(f)
            rr.append(s)
        max_length = max(max_length, len(rr))
        graph[idx] = rr
    for row in graph:
        for i in range(max_length - len(row)):
            row.append(0)
    
def C_Operation():
    global graph
    max_length = float('-inf')
    graph_tmp = []

    for col in range(len(graph[0])):
        dic = dict()
        for row in range(len(graph)):
            num = graph[row][col]
            if num==0:
                continue
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        c = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        cc = []
        for f, s, in c:
            cc.append(f)
            cc.append(s)
        max_length = max(max_length, len(cc))
        graph_tmp.append(cc)

    graph_tmp2 = [ [0]*len(graph[0]) for _ in range(max_length) ]
    for ridx, row in enumerate(graph_tmp):
        for cidx, col in enumerate(row):
            graph_tmp2[cidx][ridx] = row[cidx]
    graph = graph_tmp2

if ans_r >= 0 and ans_r < len(graph) and ans_c >= 0 and ans_c < len(graph[0]) and graph[ans_r][ans_c]==k:
    print(0)
    exit()
for time in range(100):
    row_num = len(graph)
    col_num = len(graph[0])

    # 행 개수 >= 열 개수: R연산
    if row_num >= col_num:
        R_Operation()
    # 행 개수 < 열 개수: C연산
    else:
        C_Operation()

    if ans_r >= 0 and ans_r < len(graph) and ans_c >=0 and ans_c < len(graph[0]) and graph[ans_r][ans_c] == k:
        print(time+1)
        exit()
print(-1)
exit()