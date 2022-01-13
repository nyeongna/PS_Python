# dfs
def dfs(level, exp, n):
    if level==n:
        # 빈칸은 없애고 eval을 한다
        if eval(exp.replace(' ', '')) == 0:
            print(exp)
        return
    # ASCI 순서대로 ' ', '+' , '-'
    dfs(level+1, exp+' '+str(level+1), n)
    dfs(level+1, exp+'+'+str(level+1), n)
    dfs(level+1, exp+'-'+str(level+1), n)

# test case 만큼 실행
for _ in range(int(input())):
    n = int(input())
    dfs(1, '1', n)
    print()
