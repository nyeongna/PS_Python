'''
짝수열 기준
왼쪽   (x-1, y)에 있으면 -1
오른쪽  (x+1, y)에 있으면 -1
왼쪽밑 (x-1, y+1)
오른쪽밑 (x, y+1)
왼쪽위 (x-1, y-1)
오른쪽위 (x, y-1)

홀수열 기준
왼 (x-1, y)
오른 (x+1, y)
왼쪽밑 (x, y+1)
오른쪽밑 (x+1, y+1)
왼쪽위 (x, y-1)
오른쪽위 (x+1, y-1)
'''

c, r = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(r) ]
visited= [ [0]*c for _ in range(r) ]

def check(i,j):
    if i%2==0:
        for (x,y) in [(-1,0), (1, 0), (0, 1), (1, 1), (0, -1), (1, -1)]:
            dx = i+y
            dy = j+x
            if 0<=dx<r and 0<=dy<c and graph[dx][dy]==0:
                print(f'{dx}, {dy} 벽존재')

for i in range(r):
    for j in range(c):
        if (i==0 or i==r-1 or j==0 or j==c-1) and graph[i][j]==0:
            if i%2==0:
                check(i,j)
                for (x,y) in [(-1,0), (1, 0), (0, 1), (1, 1), (0, -1), (1, -1)]:
                    dx = i+y
                    dy = j+x
                    if 0<=dx<r and 0<=dy<c and graph[dx][dy]==1:
                        print(f'{dx}, {dy} 벽존재')

ans = 0
for i in range(r):
    for j in range(c):
        if graph[i][j]==1:
            print(f'**현재위치 i:{i}, j:{j}')
            ans += 6
            # 홀수열
            if i%2==0:
                print("홀수열")
                for (x,y) in [(-1,0), (1, 0), (0, 1), (1, 1), (0, -1), (1, -1)]:
                    dx = i+y
                    dy = j+x
                    if 0<=dx<r and 0<=dy<c and graph[dx][dy]==1:
                        print(f'{dx}, {dy} 벽존재')
                        ans -= 1
            # 짝수열
            elif i%2==1:
                print("짝수열")
                #i:1, j:1
                for (x,y) in [(-1, 0), (1, 0), (-1, 1), (0, 1), (-1,-1), (0, -1)]:
                    dx = i+y
                    dy = j+x
                    if 0<=dx<r and 0<=dy<c and graph[dx][dy]==1:
                        print(f'{dx}, {dy} 벽존재')
                        ans -=1
            print()
print(ans)

'''
짝수열 기준
왼쪽   (x-1, y)에 있으면 -1
오른쪽  (x+1, y)에 있으면 -1
왼쪽밑 (x-1, y+1)
오른쪽밑 (x, y+1)
왼쪽위 (x-1, y-1)
오른쪽위 (x, y-1)
'''