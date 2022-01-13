x, k = map(int, input().split())
x = list(map(str, '0'*100+bin(x)[2:]))
'''
(x + y) 와 (x | y) 의 성질을 알아야함
-성립이 되려면 x와 y의 같은 자릿수에 대해서 1과1이 동시에 오면 안됨. 더해지면(+) 0이 되고 OR(|) 에서는 1이 되기때문
-따라서 0/1, 1/0, 0/0 인 조합은 모두 가능하다
'''
# 이진수 x에 대해서 '1'을 가지는 자릿값을 모두 기록
zero_dict = dict()
for i in range(len(x)):
    if x[i]=='1':
        zero_dict[i]=1

k = bin(k)[2:]
cnt = len(k)-1
x=['0']*len(x)
# 모두 0으로 초기화한 x길이를 가지는 x 이진수를 새로 만듦
for i in range(len(x)-1, -1, -1):
    # 원래의 x 이진수 값에서 1인 자리는 skip
    # 왜냐하면 1인 자리에는 무조건 0이 와야함
    # 원래의 x 이진수 값에서 0인 자리는 0 or 1 아무거나 와도 됨
    # 따라서 원래 0인 자리에 k 이진수 값을 그대로 복사
    if i not in zero_dict:
        x[i]=k[cnt]
        cnt-=1
    if cnt == -1:
        break

print(int('0b'+''.join(x), 2))