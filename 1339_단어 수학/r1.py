from itertools import permutations
import copy
n = int(input())
alpha_list = list()
for _ in range(n):
    alpha = list(map(str, input()))
    alpha_list.append(alpha)


'''
모든 알파벳 25개
쓰여진 알파벳 종류 갯수는 최대 10개
알파벳 길이는 최대 8

ACDEB
FFAAB
 DCDC
 CDCD
  ABC
각 자릿수에서 후보를 뽑는다

'''
used_alpha = set()
for i in range(n):
    for ch in alpha_list[i]:
        used_alpha.add(ch)
used_alpha = list(used_alpha)
num_list = [ i for i in range(10) ]
for _ in range(10-len(used_alpha)):
    num_list.pop(0)

ans = float('-inf')
nn = len(used_alpha)
alpha_ord = [0]*300
num_dict = dict()
for perm in permutations(num_list, len(used_alpha)):
    '''일차원배열 visited이용해서 알파벳에 해당하는 숫자찾기
    3552 ms
    '''
    for i in range(nn):
         alpha_ord[ord(used_alpha[i])] = perm[i]
    '''dict 이용해서 알파벳에 해당하는 숫자찾기
    7984 ms
    '''
    #for i in range(nn):
    #    num_dict[used_alpha[i]] = perm[i]

    num=0
    for i in alpha_list:
        numm=0
        for j in i:
            numm = numm * 10 + alpha_ord[ord(j)]
            #numm = numm*10 + num_dict[j]
        num += numm
    ans = max(ans, num)
print(ans)
        
    
    