'''
Longest Common Subsequence (LCS, 최대 공통 부분수열)
'''

A = input()
B = input()

# dp[i][j] = A의 [1..i] 와 B의 [1..j] 까지의 최대 공통 부분수열
dp = [ [0]*(len(B)+1) for _ in range(len(A)+1) ]

for i in range(len(A)+1):
    for j in range(len(B)+1):
        if i==0 or j==0:
            continue
        # dp[i][j]는 언제나 A[0..i-1] 와 B[0..j-1] 까지의 최대 공통 부분수열을 가지고 있다
        # 따라서 A[0..i-2] 와 B[0..j-2] 까지의 최대 공통 부분수열에서 +1 (A[i-1]==B[j-1] 이므로 공통되므로 +1 해줌)
        elif A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # A[i-1]와 B[j-1]이 다를 경우
        #  A[0..i-2]와 B[0..j-1] 의 최대 공통 부분수열인 dp[i-1][j],
        #  A[0,,i-1]과 B[0..j-2] 의 최대 공통 부분수열인 dp[i][j-1]을 비교한다.
        # 즉 현재 i, j 부분을 비교하는 과정 이전의 LCS는 유지된다.
        # "현재 i, j 부분 비교 과정 이전"이 "dp[i-1][j] 와 dp[i][j-1] 비교"이다
        elif A[i-1] != B[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])

'''

'''