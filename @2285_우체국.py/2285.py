n = int(input())

village_list = list()
for _ in range(n):
    loc, ppl = map(int, input().split())
    village_list.append((loc,ppl))

village_list = sorted(village_list)
left = int(-1e9-1)
right = int(1e9+1)
ans = float('inf')
#####################################################################################
'''
삼분탐색 (tertiary)
# x = (-1e9 ~ 1e9) 사이의 점
# get_dist(x): 우체국이 x에 있을때 사람들의 거리의 합이라면
# get_dist(x)는 최솟점을 갖는 이차함수이다 (아래로 볼록)
'''

# 우체국이 idx에 위치해 있을때 모든 사람들의 거리의 합
def get_dist(idx):
    cur_sum=0
    for i in village_list:
        cur_sum += abs(idx-i[0])*i[1]
    return cur_sum

# 범위가 대충 3정도로 추려졌을떄 멈춤
while right - left >= 3:
    p = (left*2 + right) // 3
    q = (left + right*2) // 3
    # get_dist(p) 가 get_dist(q) 보다 높다는 것은
    # 최솟점이 left와 p 사이에 존재할 수 없음
    # 따라서 left와 p 사이 범위는 무시해도되므로 left=p 로 치환
    if get_dist(p) >= get_dist(q):
        left = p
    # get_dist(p)가 get_dist(q) 보다 낮다면
    # 최솟점이 q와 right 사이에 존재할 수 없음
    # right=q 로 치환함으로써 --> q와 right 사이의 범위 무시
    else:
        right = q

# p=10 q=12
ans_idx = 0
for i in range(left, right+1, 1):
    if get_dist(i) < ans:
        ans = get_dist(i)
        ans_idx = i
print(ans_idx)

'''
Nlog3M
N=십만
M=20억
'''