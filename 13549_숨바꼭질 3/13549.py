n, k = map(int, input().split())
from collections import deque
Q = deque()
Q.append((n,0))
visited=[0]*(100000+1)
visited[n]=1

while len(Q) > 0:
    cur, dist = Q.popleft()
    if cur == k:
        print(dist)
        exit()
    # *2로 갈 수 있는 곳을 먼저 다 미리 추가함
    cur2 = cur*2
    while cur2 <= 100000 and cur2!=0:
        if visited[cur2]==0:
            visited[cur2]=1
            Q.append((cur2, dist))
        cur2 = cur2*2
    if 0<=cur-1<=100000 and visited[cur-1]==0:
        visited[cur-1]=1
        Q.append((cur-1, dist+1))
    if 0<=cur+1<=100000 and visited[cur+1]==0:
        visited[cur+1]=1
        Q.append((cur+1, dist+1))

'''
시간복잡도:
*2씩 커지므로 숫자 1 기준으로 17번 *2 해주면 10만을 초과하므로
모든 숫자 100,000에 대해 17번만 확인하면 모든 경우 확인가능
=1,700,000 정도면 통과가능
'''