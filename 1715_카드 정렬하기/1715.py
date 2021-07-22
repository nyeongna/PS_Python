import sys
import heapq

# 입력 받기
n = int(input())
card_list = [ int(input()) for _ in range(n) ]

# priority_queue 생성
heapq.heapify(card_list)

ans = 0
# heap에 1개가 남았다는 것은 모든 카드를 합쳤다는 뜻
while len(card_list) != 1:
    f = heapq.heappop(card_list)
    s = heapq.heappop(card_list)
    ans = ans + f + s
    heapq.heappush(card_list, f+s)

print(ans)

'''
시간 복잡도
Priority_queue 생성: O(N)
while 문: N(while 문) * LogN(while문 돌아갈때마다 f+s heappush)

최종: N*LogN
'''