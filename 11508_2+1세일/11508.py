from sys import stdin

#입력 받기
n = int(input())
# 내림차순 정렬
list = sorted(  [ int(input()) for _ in range(n) ], reverse=True)

ans = 0
# 그리디 방식으로 최대한 비싼 것을 적게 넣는 방식으로 넣다보면 최적의 해가 구해짐
# 0, 1번째는 값을 지불, 2번째는 공짜 ...계속
for idx in range(n):
    if idx%3 == 0 or idx%3 == 1:
        ans = ans + list[idx]
print(ans)

# 시간복잡도
# Sort = O(nlogn)
# for문 = O(n)
# 최종 O(nlogn)