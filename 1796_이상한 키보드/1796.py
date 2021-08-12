'''
핵심 알고리즘: 완전탐색 '재귀'
1. 화면 밖으로는 못 움직이므로 알파벳 'a'를 다 가려면 왼쪽 끝에 있는 'a'와 오른쪽 끝에 있는 'a'에 위치만 알면 (오른쪽 위치 - 왼쪽 위치)가
   모든 알파벳 'a'에 도달하기 위해 필요한 최소 횟수이다.
2. 하지만 왼쪽 -> 오른쪽으로 갈지, 오른쪽 -> 왼쪽으로 갈지는 다음 알파벳의 위치에 따라 달라진다.
3. 따라서 1. 왼쪽 -> 오른쪽 /// 오른쪽 -> 왼쪽 둘다 해보고 다음 알파벳으로 넘어가면서 모든 경우를 탐색해본다.
'''
'''
a askjdaosijdaoi a
'''
s = list(map(str, input()))
max_idx = [-1]*(ord('z')+1)
min_idx = [-1]*(ord('z')+1)

ans = float('inf')
        #현재 알파벳, 현재 idx 위치, 현재까지 움직인 횟수
def DFS(alpha, cur, total_move):
    global ans
    # 현재까지 움직인 횟수가 전에 움직여서 한것보다 크면 바로 return
    if total_move >= ans:
        return
    # a~z 까지 다 돌은 경우 total_move를 비교해본다
    if alpha > ord('z'):
        ans = min(ans, total_move)
        return
    
    # 현재의 알파벳이 1개인 경우
    if max_idx[alpha] == min_idx[alpha]:
        DFS(alpha+1, max_idx[alpha], abs(max_idx[alpha]-cur) + max_idx[alpha]-min_idx[alpha] + total_move)

    #현재 알파벳이 2개 이상 존재하는 경우
    elif max_idx[alpha] != float('-inf'):
        # 현재 알파벳에서 오른쪽으로 가고, 오른쪽 -> 왼쪽으로 가서, 왼쪽에 있는 alpha의 위치(idx)에서 시작하는 경우
        DFS(alpha+1, min_idx[alpha], abs(max_idx[alpha]-cur) + max_idx[alpha]-min_idx[alpha] + total_move)

        # 현재 알파벳에서 왼쪽으로 가고, 왼쪽 -> 오른쪽으로 가서, 오른쪽에 있는 alpha의 위치(idx)부터 시작하는 경우
        DFS(alpha+1, max_idx[alpha], abs(min_idx[alpha]-cur) + max_idx[alpha]-min_idx[alpha] + total_move)

    #현재 알파벳이 존재하지 않는 경우 스킵
    else:
        DFS(alpha+1, cur, total_move)


for i in range(ord('a'), ord('z')+1, 1):
    max_pos, min_pos = float('-inf'), float('inf')
    for idx, char in enumerate(s):
        if ord(char) == i:
            max_pos, min_pos = max(max_pos, idx), min(min_pos, idx)
    max_idx[i] = max_pos
    min_idx[i] = min_pos

DFS(ord('a'), 0, 0)
ans = ans + len(s)
print(ans)

