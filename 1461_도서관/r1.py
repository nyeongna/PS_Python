import heapq

n, m = map(int, input().split())
books = list(map(int, input().split()))
pos, neg = [], []

for num in books:
    if num < 0:
        heapq.heappush(neg, num)
    else:
        heapq.heappush(pos, num*-1)
dist=0

largest = float('-inf')
if len(pos) > 0:
    largest = max(largest, pos[0]*-1)
if len(neg) > 0:
    largest = max(largest, neg[0]*-1)
idx=0
while len(pos) > 0:
    if idx==0:
        a = -1*heapq.heappop(pos)
        dist += a
    else: heapq.heappop(pos)
    idx = idx + 1
    if idx==m: idx = 0
    

idx=0
while len(neg) > 0:
    if idx==0:
        a = -1*heapq.heappop(neg)
        dist += a
    else: heapq.heappop(neg)
    idx = idx + 1
    if idx==m: idx = 0
    

print(largest)
print(dist*2 - largest)