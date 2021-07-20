import sys
import heapq

n = int(input())

class_list = []
for _ in range(n):
    idx, start, end = map(int, input().split())
    class_list.append((idx,start,end))

class_list = sorted(class_list, key=lambda x: (x[1], x[2]))

# n은 1이상이므로 강의실 1개 만들고 첫번째 수업을 진행
class_num = 1
heap = [class_list[0][2]]

for lecture in class_list[1:]:
    # 현재 빈 강의실이 없으면 강의실 추가
    if heap[0] > lecture[1]:
        class_num += 1
        heapq.heappush(heap, lecture[2])
    # 현재 빈 강의실이 있으면 강의실 추가 없이 다음 수업 진행
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lecture[2])

print(class_num)
    
