from itertools import combinations

n = int(input())
string_list = list()
for _ in range(n):
    string_list.append(input())

ans = 0
ans_list = list()
for comb in combinations(string_list, 2):
    s1, s2 = comb[0], comb[1]

    # s1, s2 길이가 다르면 불가능
    if len(s1) != len(s2):
        continue
    ch_dict = dict()
    ch_dict2 = dict()
    for idx in range(len(s1)):
        if s1[idx] not in ch_dict:
            ch_dict[s1[idx]] = list([idx])
        else:
            ch_dict[s1[idx]].append(idx)

        if s2[idx] not in ch_dict2:
            ch_dict2[s2[idx]] = list([idx])
        else:
            ch_dict2[s2[idx]].append(idx)

    flag = 0
    # s1의 같은 알파벳의 위치가 s2의 같은 알파벳의 위치와 같으면
    # s1의 a의 위치가 1,2,4 면 s2의 1,2,4 위치는 같은 알파벳이어야함
    # s1
    # a b b a c
    # 0 1 2 3 4
    # visit1=[1,1,1,0,...0]
    for key, value in ch_dict.items():
        target = s2[value[0]]
        for idx in value:
            if s2[idx] != target:
                flag = 1
                break
        if flag==1:
            break
    # s2의 같은 알파벳의 위치가 s1의 같은 아파벳의 위치와 같으면
    # s2의 a의 위치가 1,2,5 면 s1의 1,2,5 위치는 같은 알파벳이어야함
    # s2
    # x y y x d
    # 0 1 2 3 4
    # visit2=[0,0,0,1,...,1,1,0]
    for key, value in ch_dict2.items():
        target = s1[value[0]]
        for idx in value:
            if s1[idx] != target:
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        ans = ans + 1
        ans_list.append((s1,s2))
        
            
#print(ans_list)
print(ans)
        

