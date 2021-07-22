import sys
import heapq

n = int(input())

class_list = []
for _ in range(n):
    idx, start, end = map(int, input().split())
    class_list.append((start,end))

class_list = sorted(class_list, key=lambda x: (x[0], x[1]))

# n은 1 이상이므로 강의실 1개 만들고 첫번째 수업을 진행
# heap에는 끝나는 시간만 기록한다. 젤 빨리 비워지는 강의실에 다음 강의를 넣어야하기 때문
class_num = 1
heap = [class_list[0][1]]

for lecture in class_list[1:]:
    # 현재 빈 강의실이 없으면 강의실 추가
    if heap[0] > lecture[0]:
        class_num += 1
        heapq.heappush(heap, lecture[1])
    # 현재 빈 강의실이 있으면 강의실 추가 없이 다음 수업 진행
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lecture[1])
print(class_num)
'''
시간복잡도
class_list 정렬: NlogN
for문: N(class_list 길이만큼 돌고) * logN (돌때마다 heappush)
최종: NlogN + NlogN = NlogN
'''
