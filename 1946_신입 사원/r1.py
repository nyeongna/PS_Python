from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    cand = list()
    for _ in range(n):
        a, b = map(int, stdin.readline().strip().split())
        cand.append((a,b))
    cand = sorted(cand, key=lambda x:x[0])
    # 서류심사 1등은 무조건 합격이다
    target = cand[0][1]
    cnt = 1
    # 서류심사 순으로 정렬했으므로 면접시험도 그보다 낮다면 탈락
    # 따라서 면접시험 성적이 올라가는 횟수(?)만 찾으면 된다.
    for a,b in cand[1:]:
        if b < target:
            target = b
            cnt = cnt + 1
    print(cnt)
