n=int(input())
r = n//5
s = list(map(str,input()))
ss=list()
for i in range(0, n, r):
    ss.append(s[i:i+r])
# for i in ss:
#     print(i)

'''
8 -> 6 -> 9 -> 0
5 -> 3 -> 2 -> 4
7 -> 1
제일 공간을 많이 차지하는 것부터 확인한다
8은 0을 포함하기 때문에 0먼저 검사하면 안된다
'''
ans=list()
visited=[0]*r
for i in range(r):
    if visited[i]==0:
        # 0, 2-9 숫자가 들어갈 여유가 있는지
        if i+2 <= r-1:
            #print(i)
            if ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
               ss[1][i]=='#' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
               ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
               ss[3][i]=='#' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
               ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
               ans.append('8')
               for j in range(3):
                   visited[i+j]=1
               continue
            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='#' and ss[1][i+1]=='.' and ss[1][i+2]=='.' and \
                 ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
                 ss[3][i]=='#' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
                 ans.append('6')
                 for j in range(3):
                     visited[i+j]=1
                 continue
            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='#' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
                 ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
                 ss[3][i]=='.' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
                 ans.append('9')
                 for j in range(3):
                     visited[i+j]=1
                 continue
            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='#' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
                 ss[2][i]=='#' and ss[2][i+1]=='.' and ss[2][i+2]=='#' and \
                 ss[3][i]=='#' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
                 ans.append('0')
                 for j in range(3):
                     visited[i+j]=1
                 continue

            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='#' and ss[1][i+1]=='.' and ss[1][i+2]=='.' and \
                 ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
                 ss[3][i]=='.' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
                 ans.append('5')
                 for j in range(3):
                     visited[i+j]=1
                 continue
            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='.' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
                 ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
                 ss[3][i]=='.' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
                 ans.append('3')
                 for j in range(3):
                     visited[i+j]=1
                 continue
            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='.' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
                 ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
                 ss[3][i]=='#' and ss[3][i+1]=='.' and ss[3][i+2]=='.' and \
                 ss[4][i]=='#' and ss[4][i+1]=='#' and ss[4][i+2]=='#':
                 ans.append('2')
                 for j in range(3):
                     visited[i+j]=1
                 continue
            elif ss[0][i]=='#' and ss[0][i+1]=='.' and ss[0][i+2]=='#' and \
                 ss[1][i]=='#' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
                 ss[2][i]=='#' and ss[2][i+1]=='#' and ss[2][i+2]=='#' and \
                 ss[3][i]=='.' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='.' and ss[4][i+1]=='.' and ss[4][i+2]=='#':
                 ans.append('4')
                 for j in range(3):
                     visited[i+j]=1
                 continue
            elif ss[0][i]=='#' and ss[0][i+1]=='#' and ss[0][i+2]=='#' and \
                 ss[1][i]=='.' and ss[1][i+1]=='.' and ss[1][i+2]=='#' and \
                 ss[2][i]=='.' and ss[2][i+1]=='.' and ss[2][i+2]=='#' and \
                 ss[3][i]=='.' and ss[3][i+1]=='.' and ss[3][i+2]=='#' and \
                 ss[4][i]=='.' and ss[4][i+1]=='.' and ss[4][i+2]=='#':
                 ans.append('7')
                 for j in range(3):
                     visited[i+j]=1
                 continue

        if ss[0][i]=='#' and \
           ss[1][i]=='#' and \
           ss[2][i]=='#' and \
           ss[3][i]=='#' and \
           ss[4][i]=='#':
           ans.append('1')
           visited[i]=1


print(''.join(ans))