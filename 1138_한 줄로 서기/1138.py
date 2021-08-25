n = int(input())

left_list = list(map(int, input().split()))
ans = [0]*(n)

# idx는 i번째 작은 키, target은 i번째 왼쪽에 몇명이 있는가
for idx,target in enumerate(left_list):
    # cnt는 왼쪽에서부터 큰 사람을 몇명 거쳐왔는가
    # idx2는 i번쨰 키를 놓을 자리를 찾는 변수
    cnt, idx2 = 0, 0
    while idx2 < n:
        # i번째 키에 해당하는 왼쪽 큰 수 조건을 만족하고, 현재 idx2 위치가 아직 업데이트가 안되었다면 업데이트함
        if cnt == target and ans[idx2]==0:
            break
        if ans[idx2]==0:
            cnt = cnt + 1
        idx2 += 1
    ans[idx2] = idx+1

print(*ans)

    

