n, m = map(int, input().split())
graph = dict()
import sys
sys.setrecursionlimit(3000)
'''
Trie 자료구조
-폴더 안에 같은 파일이 들어올 수는 없음
-graph dict 안에 특정 폴더의 하위구조를 모두 저장한다 (1계층으로)
-
'''
'''
{
    main: {FA-dict,
           FB-dict},
    FA: {file1-int,
         file2-int},
    FB: {FC-dict,
         file1-int,
         file3-int},
    FC:
}
'''
for _ in range(n+m):
    parent, sub, type = input().split()
    # sub가 폴더일경우 value 값 1
    if type=='1':
        if parent not in graph:
            graph[parent] = {
                sub: 1
            }
        else:
            graph[parent][sub] = 1
    # sub가 파일일경우 value 값 0
    else:
        if parent not in graph:
            graph[parent] = {
                sub: 0
            }
        else:
            graph[parent][sub] = 0

def dfs(q, q_dict):
    if q not in graph:
        return
    for key,value in graph[q].items():
        # 폴더 하위 파일이-파일
        if graph[q][key]==0:
            if key not in q_dict:
                q_dict[key]=1
            else:
                q_dict[key] += 1
        # 폴더 하위 파일이-폴더
        else:
            dfs(key, q_dict)
            
def count(q_dict):
    type, cnt = 0, 0
    for k,v in q_dict.items():
        cnt += v
        type += 1
    print(type, cnt)
    return type, cnt

for _ in range(int(input())):
    q = input().split('/')[-1]
    # q_dict안에 쿼리값에 대한 파일 정보를 담음 (key 갯수가 파일종류
    #                                    val 총합이 파일총합)
    q_dict = dict()
    dfs(q, q_dict)
    count(q_dict)

            



