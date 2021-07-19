from sys import stdin

n = int(stdin.readline().rstrip())
graph = [ list(map(int, stdin.readline().rstrip().split())) for _ in range (n) ]
ans = [0,0,0,0]

def Check(x,y, size):
    standard = graph[x][y]
    for i in range(x, x+size, 1):
        for j in range(y, y+size, 1):
            if graph[i][j] != standard:
                return 0
    return standard+2

def Divide(x, y, size):
    flag = Check(x,y, size)
    if flag != 0:
        ans[flag] = ans[flag] + 1
        return
    
    m = size//3
    for i in range(3):
        for j in range(3):
            Divide(x+i*m,y+j*m,m)
    # Divide(x, y, m)
    # Divide(x, y+m, m)
    # Divide(x, y+2*m,m)

    # Divide(x+m,y,m)
    # Divide(x+m,y+m,m)
    # Divide(x+m,y+2*m,m)

    # Divide(x+2*m,y,m)
    # Divide(x+2*m,y+m,m)
    # Divide(x+2*m,y+2*m,m)

Divide(0, 0, n)
for i in ans[1:]:
    print(i)