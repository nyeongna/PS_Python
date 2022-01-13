p, t = map(int, input().split())
degree_list = list(map(int, input().split()))
test_list = list(map(int, input().split()))

# 만들 수 있는 모든 각도를 cand_dict에 저장
cand_dict = dict()

# q에는 만들 수 있는 모든 각도들을 차례차례 찾아간다
q = [0]
while len(q) > 0:
    cur = q.pop()
    # 현재까지 만들 수 있는 각도에 input으로 주어진 각도들을 더하고(+) 빼가면서(-)
    # 계속해서 새롭게 만들 수 있는 각도를 찾아간다
    for degree in degree_list:
        sum1 = (cur + degree) % 360
        minus1 = abs(cur-degree) % 360
        if sum1 not in cand_dict:
            q.append(sum1)
            cand_dict[sum1]=1
        if minus1 not in cand_dict:
            q.append(minus1)
            cand_dict[minus1]=1

for t in test_list:
    if t in cand_dict:
        print('YES')
    else:
        print('NO')

