from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())

visited = [0] * 100001

# 핵심.
# prev[n] 에는 n에 도달하기 전에 왔던 숫자가 들어온다
# 예) 10 -> 20 으로 움직였다면, prev[20] 에는 10이 들어감.
prev = [0] * 100001

Q = deque()
Q.append((n,0))
visited[n] = 1
prev[n] = n

def PrintRec():
    global m
    ans = list()
    while prev[m] != m:
        ans.append(m)
        m = prev[m]
    ans.append(m)
    for i in reversed(ans):
        print(i, end=' ')
        
while Q:
    n, dist = Q.popleft()
    #print(n)
    if n==m:
        print(dist)
        # prev 를 이용해서 route 출력을 빠르게 할수있다.
        PrintRec()
        exit()

    if n*2>=0 and n*2 <=100000 and visited[2*n]==0:
        visited[2*n] = 1
        prev[2*n] = n
        Q.append((n*2, dist+1))
    if n+1>=0 and n+1 <=100000 and visited[n+1]==0:
        visited[n+1] = 1
        prev[n+1] = n
        Q.append((n+1, dist+1))
    if n-1>=0 and n-1 <=100000 and visited[n-1]==0:
        visited[n-1]=1
        prev[n-1] = n
        Q.append((n-1, dist+1))

    

    
