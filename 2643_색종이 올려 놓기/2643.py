n = int(input())
paper_list = list()
for _ in range(n):
    paper = sorted(list(map(int, input().split())), reverse=True)
    paper_list.append(paper)
paper_list = sorted(paper_list)
dp = [0]*(n+1)


# LIS (Longest Increasing Subseqence) 이용
# 조건1: 색종이 크기가 점점 작아지거나 같아야함
# 조건2: 변들이 평행 = 밑 종이의  큰 변이 윗 종이의   큰 변보다 크거나 같고
            #    = 밑 종이의 작은 변이 윗 종이의 작은 변보다 크거나 같아야함
# 따라서 각각의 색종이의 (큰변, 작은변을) 내림차순 정렬
# 이렇게 모아진 색종이들을 오름차순 정렬
'''
ex) [[2, 1], [8, 7], [12, 11], [14, 12], [15, 12], [20, 10], [20, 20]]
큰 변(왼쪽)은 오름차순 정렬 되었으므로 걱정하지 않고
작은변 (오른쪽) 값만 비교하면서 '가장 긴 증가 부분수열' 을 찾으면 된다.
시간복잡도: O(n^2). nlogn 도 가능하긴 함
'''
for i in range(n):
    max_num = 0
    for j in range(i):
        if paper_list[i][1] >= paper_list[j][1]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num + 1

print(max(dp))