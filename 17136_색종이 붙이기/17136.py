import sys

graph = [ list(map(int,input().split())) for _ in range(10) ]
zeros=[]
for i in range(10):
    for j in range(10):
        if graph[i][j]==1:
            zeros.append([i,j])
            

num = [0, 5, 5, 5, 5, 5]
ans = 1e10

def DFS(cnt, paper):
    

    if cnt==len(zeros):
        global ans
        ans = min(ans, paper)
        return
    
    x, y = zeros[cnt]
    if graph[x][y] != 1:
        DFS(cnt+1, paper)
        return
    # 5x5
    if num[5] and x <= 5 and y <= 5:
        flag=1
        for i in range(5):
            for j in range(5):
                if graph[x+i][y+j] != 1:
                    flag=0
                    break
            if flag==0:
                break
        if flag==1:
            num[5] = num[5] - 1
            for i in range(5):
                for j in range(5):
                    graph[x+i][y+j] = 5
            #print(f'{x}, {y}, 5 done, move to DFS {cnt+1},{paper+1}')
            DFS(cnt+1, paper+1)
            num[5] = num[5] + 1
            for i in range(5):
                for j in range(5):
                    graph[x+i][y+j] = 1
    
    # 4x4

    if num[4] and x <= 6 and y <= 6:
        flag=1
        for i in range(4):
            for j in range(4):
                if graph[x+i][y+j] != 1:
                    flag=0
                    break
            if flag==0:
                break
        if flag==1:
            num[4] = num[4] - 1
            for i in range(4):
                for j in range(4):
                    graph[x+i][y+j] = 4
            DFS(cnt+1, paper+1)
            num[4] = num[4] + 1
            for i in range(4):
                for j in range(4):
                    graph[x+i][y+j] = 1
    # 3x3
    if num[3] and x <= 7 and y <= 7:
        flag=1
        for i in range(3):
            for j in range(3):
                if graph[x+i][y+j] != 1:
                    flag=0
                    break
            if flag==0:
                break
        if flag==1:
            num[3] = num[3] - 1
            for i in range(3):
                for j in range(3):
                    graph[x+i][y+j] = 3
            DFS(cnt+1, paper+1)
            num[3] = num[3] + 1
            for i in range(3):
                for j in range(3):
                    graph[x+i][y+j] = 1
    # 2x2
    if num[2] and x <= 8 and y <= 8:
        flag=1
        for i in range(2):
            for j in range(2):
                if graph[x+i][y+j] != 1:
                    flag=0
                    break
            if flag==0:
                break
        if flag==1:
            num[2] = num[2] - 1
            for i in range(2):
                for j in range(2):
                    graph[x+i][y+j] = 2
            DFS(cnt+1, paper+1)
            num[2] = num[2] + 1
            for i in range(2):
                for j in range(2):
                    graph[x+i][y+j] = 1
    # 1x1
    if num[1] and x <= 9 and y <= 9:
        flag=1
        for i in range(1):
            for j in range(1):
                if graph[x+i][y+j] != 1:
                    flag=0
                    break
            if flag==0:
                break
        if flag==1:
            num[1] = num[1] - 1
            for i in range(1):
                for j in range(1):
                    graph[x+i][y+j] = 6
            DFS(cnt+1, paper+1)
            num[1] = num[1] + 1
            for i in range(1):
                for j in range(1):
                    graph[x+i][y+j] = 1

DFS(0, 0)
if ans != 1e10:
    print(ans)
else:
    print(-1)
