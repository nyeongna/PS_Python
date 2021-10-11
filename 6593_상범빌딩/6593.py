import sys
from collections import deque


x_dir = [-1,0,1,0,0,0]
y_dir = [0,1,0,-1,0,0]
z_dir = [0,0,0,0,1,-1]

while True:
    l, r, c = map(int, input().split())
    if l==0 and r == 0 and c == 0:
        break
    start=0
    goal=0
    graph = [ [ [0]*c for _ in range(r) ] for _ in range(l) ]
    
    for k in range(l):
        for i in range(r):
            line = list(map(str, input()))
            for idx,char in enumerate(line):
                if char=='S':
                    start = [k,i,idx]
                if char=='E':
                    goal = [k, i, idx]
                graph[k][i][idx] = char
        input()

    Q = deque()
    start.append(0)
    Q.append(start)
    graph[start[0]][start[1]][start[2]] = '#'
    
    #print(start, goal)
    found=False
    while len(Q) > 0:
        ll, rr, cc, dist = Q.popleft()
        if ll==goal[0] and rr == goal[1] and cc == goal[2]:
            found=True
            break            
        for idx in range(6):
            dx = rr + x_dir[idx]
            dy = cc + y_dir[idx]
            dz = ll + z_dir[idx]
            if (dx >= 0 and dx < r and dy >= 0 and dy < c and dz >= 0 and dz < l and (graph[dz][dx][dy]=='.' or graph[dz][dx][dy]=='E')):
                graph[dz][dx][dy] = '#'
                Q.append([dz, dx, dy, dist+1])
    if found:
        print(f'Escaped in {dist} minute(s).')
    else:
        print('Trapped!')
                

    