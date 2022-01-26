n, m, k = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
ops_list= list(map(int,input().split()))
import copy
def ops_1():
    global graph
    graph = graph[::-1]
def ops_2():
    global graph
    for idx,row in enumerate(graph):
        graph[idx] = row[::-1]
def ops_3():
    global graph
    graph = list(map(list,zip(*graph[::-1])))
def ops_4():
    global graph
    graph = list(map(list,zip(*graph)))[::-1]

# 5, 6 연산 이후에는 n,m이 바뀌기 때문에 새롭게 업데이트 해야한다
def ops_5():
    global graph
    a, b, c, d = list(), list(), list(), list()
    n = len(graph)
    m = len(graph[0])
    for idx, row in enumerate(graph):
        if idx < n//2:
            a.append(row[:m//2])
            b.append(row[m//2:])
        else:
            c.append(row[:m//2])
            d.append(row[m//2:])
    tmp_graph=  [ [a,b],
                  [c,d] ]
    tmp_graph = list(map(list,zip(*tmp_graph[::-1])))
    for i in range(2):
        for j in range(2):
            for x in range(len(tmp_graph[i][j])):
                for y in range(len(tmp_graph[i][j][0])):
                    graph[x+i*(n//2)][y+j*(m//2)] = tmp_graph[i][j][x][y]
# 5, 6 연산 이후에는 n,m이 바뀌기 때문에 새롭게 업데이트 해야한다
def ops_6():
    global graph
    a, b, c, d = list(), list(), list(), list()
    n,m = len(graph), len(graph[0])
    for idx, row in enumerate(graph):
        if idx < n//2:
            a.append(row[:m//2])
            b.append(row[m//2:])
        else:
            c.append(row[:m//2])
            d.append(row[m//2:])
    tmp_graph=  [ [a,b],
                  [c,d] ]
    tmp_graph = list(map(list,zip(*tmp_graph)))[::-1]
    for i in range(2):
        for j in range(2):
            for x in range(len(tmp_graph[i][j])):
                for y in range(len(tmp_graph[i][j][0])):
                    graph[x+i*(n//2)][y+j*(m//2)] = tmp_graph[i][j][x][y]



for ops in ops_list:
    if ops==1:
        ops_1()
    elif ops==2:
        ops_2()
    elif ops==3:
        ops_3()
    elif ops==4:
        ops_4()
    elif ops==5:
        ops_5()
        # res=calc5(graph)
        # graph=copy.deepcopy(res)
    else:
        ops_6()
        # res=calc6(graph)
        # graph=copy.deepcopy(res)
for i in range(len(graph)):
    for j in range(len(graph[0])):
        print(graph[i][j], end= ' ')
    print()

    
