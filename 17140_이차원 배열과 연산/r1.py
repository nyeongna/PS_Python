from sys import stdin
from collections import deque

r, c, k = map(int, input().split())
r, c = r-1, c-1

graph = [ list(map(int, input().split())) for _ in range(3) ]

if r>=0 and r < 3 and c >=0 and c < 3 and graph[r][c]==k:
    print(0)
    exit()

def R_operation():
    max_col_length = float('-inf')
    for idx, row in enumerate(graph):
        dic = dict()
        for num in row:
            if num == 0:
                continue
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] = dic[num] + 1
        num_cnt_list = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        r = []
        for f, s in num_cnt_list:
            r.append(f)
            r.append(s)
        max_col_length = max(max_col_length, len(r))
        graph[idx] = r
    for row in graph:
        for num in range(max_col_length-len(row)):
            row.append(0)

        
def C_operation():
    global graph
    max_row_length = float('-inf')
    graph_tmp = []
    for col_idx in range(len(graph[0])):
        dic = dict()
        for row_idx in range(len(graph)):
            num = graph[row_idx][col_idx]
            if num == 0:
                continue
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        num_cnt_list = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        c = []
        for f,s in num_cnt_list:
            c.append(f)
            c.append(s)
        graph_tmp.append(c)
        max_row_length = max(max_row_length, len(c))
    
    for row in graph_tmp:
        for num in range(max_row_length - len(row)):
            row.append(0)

    graph_tmp2 = [ [0]*len(graph[0]) for _ in range(max_row_length) ]
    
    for row_idx in range(len(graph[0])):
        for col_idx in range(max_row_length):
            graph_tmp2[col_idx][row_idx] = graph_tmp[row_idx][col_idx]

    graph = graph_tmp2



for time in range(100):
    row_num = len(graph)
    col_num = len(graph[0])

    if row_num >= col_num:
        R_operation()
    else:
        C_operation()

    if r>=0 and r < len(graph) and c >= 0 and c < len(graph[0]) and graph[r][c]==k:
        print(time+1)
        exit()
print(-1)
