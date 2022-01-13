R, C, K = map(int, input().split())
graph = [ [0]*C for _ in range(R) ]

def check(i,j,sticker):
    for r in range(len(sticker)):
        for c in range(len(sticker[0])):
            # 범위 벗어났으면, return -1
            if r+i >= R or c+j >= C:
                return -1
            # 이미 graph에 칠해져 있으면, return -1
            if sticker[r][c]==1 and graph[r+i][c+j]==1:
                return -1
    # 여기 도착했으면 (i,j)에 붙힐 수 있음
    for r in range(len(sticker)):
        for c in range(len(sticker[0])):
            if sticker[r][c]==1:
                graph[r+i][c+j]=1
    return 1

for _ in range(K):
    r, c = map(int, input().split())
    sticker = [ list(map(int, input().split())) for _ in range(r) ]
    flag=0
    for k in range(4):
        for i in range(R):
            for j in range(C):
                res = check(i,j,sticker)
                # 1 이면 붙힌것이므로, 다음 sticker로 넘어감
                if res==1:
                    flag=1
                    break
            if flag==1:
                break
        # graph 전부 다 안되면 90도 회전한 후 다시 graph 탐색
        if flag==0:
            sticker=list(zip(*sticker[::-1]))
        if flag==1:
            break
ans=0
for i in graph:
    for j in i:
        if j==1:
            ans+=1
print(ans)



            