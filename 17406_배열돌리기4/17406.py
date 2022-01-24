from itertools import permutations
import copy

n, m, k = map(int, input().split())
graph = [ [0]*(m+2) for _ in range(n+2) ]
input_graph = [ list(map(int, input().split())) for _ in range(n) ]
for i in range(n):
    for j in range(m):
        graph[i+1][j+1] = input_graph[i][j]

rotation_list = [ list(map(int, input().split())) for _ in range(k) ]

def rotate(tmp_graph, r, c, kk):

    for round in range(1,kk+1):
        t_graph_size = (round*2)+1
        nn = round+1
        # 0단계: 'n'round 에서는 (n*2)+1+1 t_graph 생성
        t_graph = [ [0]*(t_graph_size+1) for _ in range(t_graph_size+1) ]
        # 1단계:
        for i in range(round*2):
            t_graph[nn-round][nn-round+i+1] = tmp_graph[r-round][c-round+i]
        # 2단계:
        for i in range(round*2):
            t_graph[nn-round+i+1][nn+round] = tmp_graph[r-round+i][c+round]
        # 3단계:
        for i in range(round*2):
            t_graph[nn+round][nn+round-i-1] = tmp_graph[r+round][c+round-i]
        # 4단계:
        for i in range(round*2):
            t_graph[nn+round-i-1][nn-round] = tmp_graph[r+round-i][c-round]
        # print('tmp_graph')
        # for i in tmp_graph:
        #     print(i)
        # print('t_graph_')
        # for i in t_graph:
        #     print(i)
        # print()
        for i in range(1, t_graph_size+1):
            for j in range(1, t_graph_size+1):
                if i!=1 and i!=t_graph_size and j!=1 and j!=t_graph_size:
                    continue
                tmp_graph[r-round-1+i][c-round-1+j] = t_graph[i][j]

        # print('tmp_graph after t_graph')
        # for i in tmp_graph:
        #     print(i)
        # print()

ans_min = float('inf')
cnt=1
for comb in permutations(rotation_list, k):
    tmp_graph = copy.deepcopy(graph)
    for (r, c, kk) in comb:
        rotate(tmp_graph, r, c, kk)
    comb_min = float('inf')
    for row in range(1, n+1):
        sum_row = sum(tmp_graph[row])
        comb_min = min(comb_min, sum_row)
    ans_min = min(ans_min, comb_min)
    # print('final tmp_graph: ' + str(cnt))
    # cnt+=1
    # for i in tmp_graph:
    #     print(i)
    # print()
print(ans_min)
    
