from collections import deque
import sys
import heapq

n = int(input())
like_num = int(input())
like = list(map(int, input().split()))

candidate = dict()

for time,target in enumerate(like):

    # 아직 사진틀에 여유가 있다면
    if len(candidate) < n:
        if target not in candidate:
            candidate[target] = [1, time]
        else:
            candidate[target][0] += 1
    # 사진틀이 꽉차 있으면 추천수가 가장 적고 오래된 사진을 지운다
    else:
        if target in candidate:
            candidate[target][0] += 1
        else:
            deleted = sorted([ [key, value[0], value[1] ] for key, value in candidate.items() ], key=lambda x: (x[1], x[2]) )[0][0]
            candidate.pop(deleted)
            candidate[target] = [1, time]

for last_candidate in sorted( [ key for key, value in candidate.items() ] ):
    print(last_candidate, end=' ')

'''
시간 복잡도: M x NlogN, where M = 추천 수, N = 사진틀의 갯수
'''
        