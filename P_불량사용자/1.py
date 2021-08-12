from itertools import permutations, combinations

'''
완전탐색을 이용한 8p8 * 8 = 최대
'''
def solution(user_id, banned_id):
    n = len(user_id)
    r = len(banned_id)
    ans = 0
    # user_id 는 중복 카운트를 허락하지 않음
    for comb in combinations(user_id, r):
        if comb == ('frodo', 'fradi', 'abc123', 'frodoc'):
            print(comb)
        # 모든 banned_id 순열 중에서
        for perm in permutations(banned_id, r):
            flag=1
            for idx in range(r):
                # 길이가 안맞으면 break
                if len(comb[idx]) != len(perm[idx]):
                    flag=0
                    break
                # 글자 하나하나 맞는지 비교한다
                for pos,ch in enumerate(comb[idx]):
                    if comb[idx][pos] != perm[idx][pos] and perm[idx][pos] != '*':
                        flag=0
                        break
                if flag==0:
                    break
            # 순열 1개라도 식이 완성되면 ans += 1
            # 하고 break 해서 다음 조합을 테스트한다
            if flag==1:
                ans = ans + 1
                break
    print(ans)
    return ans

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])