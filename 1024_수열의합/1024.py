
n, l = map(int, input().split())

for length in range(l, 101, 1):
    k = n - (length*(length-1)//2)
    # k가 0보다 작다면 애초에 length 크기의 연속된 숫자로 n을 만들 수 없다.
    if k<0:
        print(-1)
        exit()
    # k % length == 0 이란것은 length 크기의 연속된 숫자로 n을 만들 수 있다는 얘기
    if k % length==0:
        # idx는 length 크기의 연속된 각 숫자에 idx만큼 더한 숫자들의 합이 n이 된다는 뜻
        idx = k // length
        ans = [ num+idx for num in range(length)]
        for num in ans:
            print(num, end=' ')
        exit()
print(-1)
