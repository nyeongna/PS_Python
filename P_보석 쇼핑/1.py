def solution(gems):
    num_of_type = len(set(gems))
    gem_dict = dict()
    start, end = 0, 0
    left, right, ans = 0,0,float('inf')
    while start < len(gems) and end < len(gems):
        target = gems[end]
        if target not in gem_dict:
            gem_dict[target] = 1
        else:
            gem_dict[target] += 1
        end = end + 1
        if len(gem_dict) == num_of_type:
            while start < end:
                if gem_dict[gems[start]] == 1:
                    if end-start < ans:
                        ans, left, right = end-start, start, end-1
                    break
                else:
                    gem_dict[gems[start]] -= 1
                    start += 1
    return [left+1, right+1]


gems = ['A','A','B', 'B','C','C','C']
print(solution(gems))