import sys
from collections import deque

n, t, g = map(int, input().split())

# A: increase 'n' by 1
# B: double 'n' and decrease the highest value position by 1 (except 0)

Q = deque()
visited = [0] * 100000
visited[n] = 1
Q.append([n, 0])

found=False
while len(Q) > 0:
    cur, dist = Q.popleft()

    if cur==g:
        found=True
        break

    # A button
    if cur+1 <= 99999 and visited[cur+1]==0:
        visited[cur+1]=1
        Q.append([cur+1, dist+1])
    
    # B button
    
    if cur*2 <= 99999:
        bval = cur * 2
        cbval = list(map(int,str(bval)))
        digit = len(str(bval))
        for i in range(digit):
            if cbval[i] != 0:
                cbval[i] = cbval[i]-1
                break
        val = list(map(str, cbval))
        val = int(''.join(val))
        if visited[val]==0:
            visited[val]=1
            Q.append([val,dist+1])
    
if found and dist <= t:
    print(dist)
else:
    print('ANG')

    
