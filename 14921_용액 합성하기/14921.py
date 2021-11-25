n = int(input())
'''
1. N개의 용액들의 특성값은 모두 서로 다르고,
2. 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.
'''
s = list(map(int, input().split()))
min_ans = float('inf')
min_nums = None

first = 0
last = len(s)-1

while first < last:
    # two pointer 사용해서 가장왼쪽에 위치한 값과 오른쪽에 위치한 값 합
    sum = s[first] + s[last]
    # 이 합의 절대값이 현재 기록한 합의 절대값과 비교
    if abs(sum) < abs(min_ans):
        min_ans = abs(sum)
        min_nums = [s[first], s[last]]
    # 현재 합이 0이상이면 값을 낮춰야 하므로 last idx 1개 줄임
    if sum >= 0:
        last -= 1
    # 현재 합이 0 미만이면 값을 올려야 하므로 first idx 1개 올림
    elif sum < 0:
        first += 1
# 구한 두 용액의 특성값을 더한다
print(min_nums[0]+min_nums[1])