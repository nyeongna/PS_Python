from collections import deque

n, m = map(int, input().split())
books = list(map(int, input().split()))
pos, neg = deque(), deque()

# pos, neg 리스트에 각자 원소를 넣는다
for num in books:
    if num < 0:
        neg.append(num*-1)
    else:
        pos.append(num)
# pos, neg 리스트를 내림차순 정렬 한다 (젤 긴 것부터 묶어야한다...)
pos, neg = sorted(pos, reverse=True), sorted(neg, reverse=True)

# 가장 큰 수를 찾는다. 가장 큰 수는 편도로만 가도된다 (마지막에 가면 되기 때문)
largest = float('-inf')
if len(pos) > 0:
    largest = max(largest, pos[0])
if len(neg) > 0:
    largest = max(largest, neg[0])

# 가는 거리를 계산한다
dist = 0
for idx,num in enumerate(pos):
    if idx%m == 0:
        dist = dist + num

for idx,num in enumerate(neg):
    if idx%m==0:
        dist = dist + num

print(dist*2-largest)
    

