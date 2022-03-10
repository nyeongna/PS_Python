n, start = map(str, input().split())
n=int(n)
word_dict = dict()
word_list = list()
for _ in range(n):
    word = input()
    word_dict[word]=1
    word_list.append(word)
word_list.sort(key=len)
visited = dict()

max_word = start
max_len = len(start)
visited[start]=1


'''
1번 방법
dfs: 1000번 돌음
단어비교: 80번
dfs 단어비교 최대 1000번

2번 방법
-길이순으로 정렬한다음에, 처음부터 iterate 하고
- i번째 자리를 뺸 단어가 dict에 들어있으면 가능하단 뜻이므로 dict에 넣어주는 방식
'''

def dfs(word):
    #print(word + " visited'"
    global max_len, max_word
    if len(word) > max_len:
        max_word = word
        max_len = len(word)
    for (key, val) in word_dict.items():
        if key in visited:
            continue
        if len(key) != len(word)+1:
            continue
        # 문자열+1 이 문자열이 되는지 비교를 어떻게 빨리하나..??
        # 투포인터 활용
        # coal
        # cal
        idx1, idx2, skip, flag = 0, 0, 0, 0
        for _ in range(len(word)):
            # 틀린 글자로 1번은 봐준다
            if key[idx1] != word[idx2] and skip==1:
                flag=1
                break
            elif key[idx1] != word[idx2] and skip==0:
                idx1 += 1
                skip=1
            # 글자 맞는지 비교
            if key[idx1] != word[idx2]:
                flag=1
                break
            idx1, idx2 = idx1+1, idx2+1
        if flag==0:
            visited[key]=1
            dfs(key)

dfs(start)
print(max_word)
