from collections import deque

ans = int(input())
Q = deque()
#        화면, 클립보드, dist
Q.append((1,0,0))
visited=dict()
visited[(1,0)]=1
while len(Q) > 0:
    screen, clip, dist = Q.popleft()
    if screen==ans:
        print(dist)
        exit()
    # 화면 -> 클립보드 저장
    f1 = (screen, screen, dist+1)
    if f1 not in visited:
        visited[f1]=1
        Q.append(f1)
    # 클립보드 -> 화면 붙여넣기
    f2 = (screen+clip, clip, dist+1)
    if clip > 0 and f2 not in visited:
        visited[f2]=1
        Q.append(f2)
    # 화면에 있는 이모티콘 1개 삭제
    f3 = (screen-1, clip, dist+1)
    if screen > 0 and f3 not in visited:
        visited[f3]=1
        Q.append(f3)
    

    