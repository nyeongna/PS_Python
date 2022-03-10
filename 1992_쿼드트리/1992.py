'''
-모두 0/1 이 아니면 '(' 을 추가하고 재귀를 시작함
-재귀가 끝나면 ')'로 끝냄
-N은 2의 제곱이므로 바운더리 걱정 X
'''
n = int(input())
graph = [ list(map(int, input())) for _ in range(n) ]

ans=""
def divide(i, j, k):
    global ans
    # 4개로 쪼갠다
    zero, one = 0, 0
    for ii in range(k):
        for jj in range(k):
            if graph[ii+i][jj+j]==0:
                zero = 1
            elif graph[ii+i][jj+j]==1:
                one = 1
    if zero==1 and one==1:
        size = k//2
        ans += '('
        divide(i, j, size)
        divide(i, j+size, size)
        divide(i+size, j, size)
        divide(i+size, j+size, size)
        ans += ')'
    elif zero==1 and one==0:
        ans += '0'
    elif zero==0 and one==1:
        ans += '1'
    
divide(0, 0, n)
print(ans)
