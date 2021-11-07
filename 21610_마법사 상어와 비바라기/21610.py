n, m = map(int , input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,input().split())))

cloud_list = [ (n-1,0), (n-1,1), (n-2,0), (n-2, 1) ] 

dir_list = [
    (None, None),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1)
]

for _ in range(m):
    dir, dist = map(int, input().split())
    n_cloud_list = dict()

    # 구름 이동
    for cloud in cloud_list:
        x, y = cloud[0], cloud[1]
        x_dir, y_dir = dir_list[dir][0], dir_list[dir][1]
        for _ in range(dist):
            # (x,y) 좌표로 관리하지말고 x좌표, y좌표 따로 관리한다
            # x가 범위를 벗어나면 다시 조절해주고, y가 범위를 벗어나면 다시 조절해준다
            x, y = x+x_dir, y+y_dir
            if x == -1:
                x=n-1
            elif x == n:
                x=0
            if y == -1:
                y=n-1
            elif y == n:
                y=0
        n_cloud_list[(x,y)]=1
    
    # 각 구름에서 비가 내려 바구니 +1
    for cloud in n_cloud_list:
        x, y = cloud[0], cloud[1]
        graph[x][y] += 1
    
    # +1 된 바구니에서 대각선에 1이상 바구니만큼 A[x][y] 증가
    cnt_list = list()
    for (x,y) in n_cloud_list.keys():
        cnt=0
        for ddir in [2,4,6,8]:
            x_dir,y_dir = dir_list[ddir][0], dir_list[ddir][1]
            dx, dy = x+x_dir, y+y_dir
            if 0<=dx<n and 0<=dy<n and graph[dx][dy]:
                cnt+=1
        cnt_list.append((x,y,cnt))
    for x,y,cnt in cnt_list:
        graph[x][y] += cnt
        

    # 바구니 물 2이상 AND 구름이 사라진 칸이 아니라면, 여기에 구름 생성
    cloud_list.clear()
    for i in range(n):
        for j in range(n):
            if (i,j) not in n_cloud_list and graph[i][j] >= 2:
                cloud_list.append((i,j))
                graph[i][j] -= 2

ans=0
for i in range(n):
    for j in range(n):
        ans += graph[i][j]
print(ans)


    
    

        
    


            


