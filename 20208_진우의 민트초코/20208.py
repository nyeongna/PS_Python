from itertools import permutations

n, m, h = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

mint_list = list()
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            mint_list.append((i,j))
        elif graph[i][j]==1:
            sx, sy = i, j

'''
완전탐색
모든 경로를 순열을 이용하여 만들어내고 갈 수 있는지 검사한다.
nPn + nPn-1 + nPn-2 + ... + nP1
n=10이라서 통과가능
'''
ans = 0
# n개의 민트를 먹을 수 있을 때
for mint_num in range(len(mint_list), 0, -1):
    # n개의 민트를 먹는 순열(민트 먹는 순서)
    for perm in permutations(mint_list, mint_num):
        x, y, cur_hp, flag = sx, sy, m, 1
        for nx, ny in perm:
            dist = abs(nx-x) + abs(ny-y)
            if dist <= cur_hp:
                cur_hp = cur_hp - dist + h
                x = nx
                y = ny
            else:
                flag=0
                break
        if flag==1:
            last_to_home = abs(nx-sx) + abs(ny-sy)
            # 만약 마지막 위치에서 집까지 갈 수 있으면
            # 최대 민트를 먹을 수 있는 개수 발견
            if last_to_home <= cur_hp:
                print(mint_num)
                exit()
print(0)
