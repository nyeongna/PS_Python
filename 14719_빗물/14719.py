h, w = map(int, input().split())
graph = list(map(int, input().split()))

cur_height, cur_idx, sum, left_to_right = 0,0,0,0
for idx, height in enumerate(graph):
    # 동일 혹은 커져가는 높이에서만 빗물을 구한다 왼->오
    if height >= cur_height:
        left_to_right += cur_height * (idx - cur_idx - 1) - sum
        cur_height = height
        cur_idx = idx
        sum = 0
    else:
        sum += height

cur_height, cur_idx, sum, right_to_left = 0,0,0,0
for idx, height in enumerate(graph[::-1]):
    # 동일 높이에서 [왼->오] 와 [오->왼] 의 고인빗물 겹치는걸 피하기 위해 커져가는 높이에서만 빗물을 구한다 오->왼
    if height > cur_height:
        # 오->왼 쌓인 빗물 누적
        right_to_left += cur_height * (idx - cur_idx - 1) - sum
        cur_height = height
        cur_idx = idx
        sum = 0
    # 현재 높이보다 작은 높이들은 더해놓고 나중에 빼준다. 이 높이들만큼 빗물이 안차기 때문
    else:
        sum += height

print(left_to_right + right_to_left)
