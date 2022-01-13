import copy
n, r = map(int, input().split())
graph=list()
for _ in range(pow(2,n)):
    a=list(map(int, input().split()))
    graph.append(a)

tmp_graph = [ [0]*pow(2,n) for _ in range(pow(2,n))]

def operation(i,j,l,order):
    if order==1:
        for x in range(l//2):
            for y in range(l):
                graph[i+x][j+y], graph[i+l-1-x][j+y] = graph[i+l-1-x][j+y], graph[i+x][j+y]
    elif order==2:
        for x in range(l//2):
            for y in range(l):
                graph[i+y][j+x], graph[i+y][j+l-1-x] = graph[i+y][j+l-1-x], graph[i+y][j+x]
    elif order==3:
        b_list=list()
        for x in range(l):
            s_list=list()
            for y in range(l):
                s_list.append(graph[i+x][j+y])
            b_list.append(s_list)
            
        b_list=list(zip(*b_list[::-1]))
        for x in range(l):
            for y in range(l):
                graph[i+x][j+y] = b_list[x][y]
    elif order==4:
        b_list=list()
        for x in range(l):
            s_list=list()
            for y in range(l):
                s_list.append(graph[i+x][j+y])
            b_list.append(s_list)
        b_list=list(zip(*b_list))[::-1]
        for x in range(l):
            for y in range(l):
                graph[i+x][j+y] = b_list[x][y]           
for _ in range(r):
    order, l = map(int, input().split())
    if 1<=order<=4:
        for i in range(0, pow(2,n), pow(2,l)): # 0 2 4 6
            for j in range(0, pow(2,n), pow(2,l)):
                operation(i,j,pow(2,l),order)
    elif order==5:
        b_list=list()
        for i in range(0, pow(2,n), pow(2,l)):
            s_list=list()
            for j in range(0, pow(2,n), pow(2,l)):
                s_list.append((i,j))
            b_list.append(s_list)
        b_list=b_list[::-1]
        for kk in range(len(b_list)):
            for zz in range(len(b_list[0])):
                x, y = b_list[kk][zz][0], b_list[kk][zz][1]
                for i in range(0, pow(2,l)):
                    for j in range(0, pow(2,l)):
                        tmp_graph[i+kk*pow(2,l)][j+zz*pow(2,l)] = graph[x+i][y+j]
        graph=copy.deepcopy(tmp_graph)

    elif order==6:
        b_list=list()
        for i in range(0, pow(2,n), pow(2,l)):
            s_list=list()
            for j in range(0, pow(2,n), pow(2,l)):
                s_list.append((j,i))
            b_list.append(s_list)
        b_list=b_list[::-1]

        for kk in range(len(b_list)):
            for zz in range(len(b_list[0])):
                x, y = b_list[zz][kk][0], b_list[zz][kk][1]
                for i in range(0, pow(2,l)):
                    for j in range(0, pow(2,l)):
                        tmp_graph[i+kk*pow(2,l)][j+zz*pow(2,l)] = graph[x+i][y+j]
        graph=copy.deepcopy(tmp_graph)
    
    elif order==7:
        b_list=list()
        for i in range(0, pow(2,n), pow(2,l)):
            s_list=list()
            for j in range(0, pow(2,n), pow(2,l)):
                s_list.append((i,j))
            b_list.append(s_list)
        b_list=list(zip(*b_list[::-1]))
        for kk in range(len(b_list)):
            for zz in range(len(b_list[0])):
                x, y = b_list[kk][zz][0], b_list[kk][zz][1]
                for i in range(0, pow(2,l)):
                    for j in range(0, pow(2,l)):
                        tmp_graph[i+kk*pow(2,l)][j+zz*pow(2,l)] = graph[x+i][y+j]
        graph=copy.deepcopy(tmp_graph)
    
    elif order==8:
        b_list=list()
        for i in range(0, pow(2,n), pow(2,l)):
            s_list=list()
            for j in range(0, pow(2,n), pow(2,l)):
                s_list.append((i,j))
            b_list.append(s_list)
        b_list=list(zip(*b_list))[::-1]

        for kk in range(len(b_list)):
            for zz in range(len(b_list[0])):
                x, y = b_list[kk][zz][0], b_list[kk][zz][1]
                for i in range(0, pow(2,l)):
                    for j in range(0, pow(2,l)):
                        tmp_graph[i+kk*pow(2,l)][j+zz*pow(2,l)] = graph[x+i][y+j]
        graph=copy.deepcopy(tmp_graph)

        
for i in range(pow(2,n)):
    for j in range(pow(2,n)):
        print(graph[i][j], end=' ')
    print()