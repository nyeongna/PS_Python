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
        # 사진틀에 없는 후보면 추가해준다 (추천수1, 등록된 시간)
        if target not in candidate:
            candidate[target] = [1, time]
        # 이미 사진틀에 있는 후보면 추천수만 +1
        else:
            candidate[target][0] += 1
    # 사진틀이 꽉차 있으면 추천수가 가장 적고 오래된 사진을 지운다
    else:
        #이미 사진틀에 있으면 추천수만 +1
        if target in candidate:
            candidate[target][0] += 1
        # 추천수가 가장 적고 가장 오래  된 사진을 지운다
        else:
            #지워야할 후보를 뽑아낸다
            deleted = sorted([ [key, value[0], value[1] ] for key, value in candidate.items() ], key=lambda x: (x[1], x[2]) )[0][0]
            # 사진틀에서 삭제
            candidate.pop(deleted)
            # 새로운 후보 추가
            candidate[target] = [1, time]
            
# 마지막에 사진첩에 있는 후보들을 오름차순으로 출력
for last_candidate in sorted( [ key for key, value in candidate.items() ] ):
    print(last_candidate, end=' ')

'''
시간 복잡도: M x NlogN, where M = 추천 수, N = 사진틀의 갯수
'''
        