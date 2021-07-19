from sys import stdin
from collections import deque

n = int(input())
k = int(input())
sensor_list = list(map(int, input().split()))

# k가 n 이상이면 모든 센서 위치 위에 집중국을 세울 수 있기 때문에 0초
if k>=n:
    print(0)
    exit()

# 센서들의 중복 위치를 없애고 오름차순 정렬 -> O(NlogN)
sensor_list = sorted(list(set(sensor_list)))

# 센서들 사이의 거리를 오름차순으로 정렬
sensor_dist_list=[]
for idx in range(len(sensor_list)-1):
    sensor_dist_list.append((sensor_list[idx+1] - sensor_list[idx]))
sensor_dist_list.sort()
#print(sensor_dist_list)

'''
k=1이면, 어차피 센서들 사이의 모든 거리를 다 더해야함
k=2이면, 센서들 사이의 거리중 '제일 긴 거리'를 스킵하고 나머지만 커버하면됨
k=3이면, 센서들 사이의 거리중 '게징 긴 2개의 거리'를 스킵하고 나머지만 커버하면됨...
    -즉 N=5, k=3 이면 총 센서들 사이의 거리가 4개가 나오고 여기서 2개를 스킵할 수 있으므로 가장 짧은 거리 2개만 커버하면됨
    -N=5, k=1 0개 스킵, 4개 거리 더함
    -N=5, k=2 1개 스킵, 3개 거리 더함
    -N=5, k=3 2개 스킵, 2개 거리 더함
    -N=5, k=4 3개 스킵, 1개 거리 더함
    -패턴: N-k번 더하면됨 (제일 작은 거리부터)
'''

ans = 0
# 실제로는 n 대신 len(sensor_list) 사용. 왜냐하면, n에서 받은 것중에는 중복되는 좌표가 있기때문
for idx in range(len(sensor_list)-k):
    ans = ans + sensor_dist_list[idx]

print(ans)


'''
시간 복잡도
O(NlogN(정렬) + N + N)  => O (NlogN)
N이 최대 10,000이므로 가능
'''